# === IMPORT THƯ VIỆN ===
from typing import Annotated
from typing_extensions import TypedDict

# LangGraph: framework để xây dựng agentic workflow với graph
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver  # Lưu trữ lịch sử hội thoại
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from typing import List, Any, Optional, Dict
from pydantic import BaseModel, Field
from sidekick_tools import playwright_tools, other_tools
import uuid
import asyncio
from datetime import datetime

load_dotenv(override=True)


# === ĐỊNH NGHĨA STATE CỦA GRAPH ===
class State(TypedDict):
    """
    State chứa toàn bộ thông tin trong quá trình xử lý:
    - messages: Lịch sử hội thoại giữa user và AI
    - success_criteria: Tiêu chí để đánh giá kết quả có thành công không
    - feedback_on_work: Phản hồi từ Evaluator nếu chưa đạt yêu cầu
    - success_criteria_met: Đã hoàn thành success criteria chưa?
    - user_input_needed: Cần user trả lời câu hỏi không?
    """
    messages: Annotated[List[Any], add_messages]
    success_criteria: str
    feedback_on_work: Optional[str]
    success_criteria_met: bool
    user_input_needed: bool


# === OUTPUT CỦA EVALUATOR ===
class EvaluatorOutput(BaseModel):
    """
    Evaluator sẽ trả về Structured Output gồm 3 field:
    - feedback: Nhận xét về kết quả của Worker
    - success_criteria_met: Đã đạt tiêu chí thành công chưa?
    - user_input_needed: Cần user trả lời/clarify không?
    """
    feedback: str = Field(description="Feedback on the assistant's response")
    success_criteria_met: bool = Field(description="Whether the success criteria have been met")
    user_input_needed: bool = Field(
        description="True if more input is needed from the user, or clarifications, or the assistant is stuck"
    )


# === CLASS SIDEKICK - AI ASSISTANT CHÍNH ===
class Sidekick:
    """
    Sidekick là AI assistant sử dụng LangGraph workflow gồm:
    - Worker: AI làm việc, dùng tools (browser, search, file...)
    - Evaluator: AI đánh giá kết quả có đạt yêu cầu không
    - Tools: Các công cụ hỗ trợ (browser, search, wikipedia, python...)
    """
    def __init__(self):
        self.worker_llm_with_tools = None  # LLM Worker bind với tools
        self.evaluator_llm_with_output = None  # LLM Evaluator với structured output
        self.tools = None  # Danh sách tools
        self.llm_with_tools = None
        self.graph = None  # LangGraph workflow
        self.sidekick_id = str(uuid.uuid4())  # ID duy nhất cho session
        self.memory = MemorySaver()  # Lưu lịch sử hội thoại
        self.browser = None  # Browser instance
        self.playwright = None  # Playwright instance

    async def setup(self):
        """
        Khởi tạo Sidekick:
        1. Tạo playwright tools (browser automation)
        2. Tạo các tools khác (search, file, wikipedia, python)
        3. Bind tools với Worker LLM (GPT-4o-mini)
        4. Setup Evaluator LLM với structured output
        5. Xây dựng LangGraph workflow
        """
        self.tools, self.browser, self.playwright = await playwright_tools()
        self.tools += await other_tools()
        worker_llm = ChatOpenAI(model="gpt-5-nano")
        self.worker_llm_with_tools = worker_llm.bind_tools(self.tools)
        evaluator_llm = ChatOpenAI(model="gpt-5-nano")
        self.evaluator_llm_with_output = evaluator_llm.with_structured_output(EvaluatorOutput)
        await self.build_graph()

    def worker(self, state: State) -> Dict[str, Any]:
        """
        Worker node - AI làm việc chính:
        - Nhận task từ user và success criteria
        - Dùng tools (browser, search...) để giải quyết
        - Nếu có feedback từ Evaluator, sửa lại theo feedback
        - Trả về kết quả hoặc câu hỏi cho user
        """
        system_message = f"""You are a helpful assistant that can use tools to complete tasks.
    You keep working on a task until either you have a question or clarification for the user, or the success criteria is met.
    You have many tools to help you, including tools to browse the internet, navigating and retrieving web pages.
    You have a tool to run python code, but note that you would need to include a print() statement if you wanted to receive output.
    The current date and time is {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    This is the success criteria:
    {state["success_criteria"]}
    You should reply either with a question for the user about this assignment, or with your final response.
    If you have a question for the user, you need to reply by clearly stating your question. An example might be:

    Question: please clarify whether you want a summary or a detailed answer

    If you've finished, reply with the final answer, and don't ask a question; simply reply with the answer.
    """

        # Nếu có feedback từ Evaluator (bị reject lần trước), thêm vào system message
        if state.get("feedback_on_work"):
            system_message += f"""
    Previously you thought you completed the assignment, but your reply was rejected because the success criteria was not met.
    Here is the feedback on why this was rejected:
    {state["feedback_on_work"]}
    With this feedback, please continue the assignment, ensuring that you meet the success criteria or have a question for the user."""

        # Thêm/cập nhật system message vào messages
        found_system_message = False
        messages = state["messages"]
        for message in messages:
            if isinstance(message, SystemMessage):
                message.content = system_message
                found_system_message = True

        if not found_system_message:
            messages = [SystemMessage(content=system_message)] + messages

        # Gọi LLM với tools để xử lý
        response = self.worker_llm_with_tools.invoke(messages)

        # Trả về response cập nhật state
        return {
            "messages": [response],
        }

    def worker_router(self, state: State) -> str:
        """
        Router sau Worker node:
        - Nếu Worker gọi tools (tool_calls) -> chuyển tới "tools" node
        - Nếu không -> chuyển tới "evaluator" node để kiểm tra kết quả
        """
        last_message = state["messages"][-1]

        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        else:
            return "evaluator"

    def format_conversation(self, messages: List[Any]) -> str:
        """Format lại lịch sử hội thoại thành text dễ đọc cho Evaluator"""
        conversation = "Conversation history:\n\n"
        for message in messages:
            if isinstance(message, HumanMessage):
                conversation += f"User: {message.content}\n"
            elif isinstance(message, AIMessage):
                text = message.content or "[Tools use]"
                conversation += f"Assistant: {text}\n"
        return conversation

    def evaluator(self, state: State) -> State:
        """
        Evaluator node - AI đánh giá kết quả:
        - Kiểm tra xem Worker đã hoàn thành success criteria chưa
        - Đánh giá chất lượng của kết quả
        - Xác định có cần user input không (câu hỏi, clarification...)
        - Trả về feedback để Worker tiếp tục hoặc kết thúc
        """
        last_response = state["messages"][-1].content

        system_message = """You are an evaluator that determines if a task has been completed successfully by an Assistant.
    Assess the Assistant's last response based on the given criteria. Respond with your feedback, and with your decision on whether the success criteria has been met,
    and whether more input is needed from the user."""

        user_message = f"""You are evaluating a conversation between the User and Assistant. You decide what action to take based on the last response from the Assistant.

    The entire conversation with the assistant, with the user's original request and all replies, is:
    {self.format_conversation(state["messages"])}

    The success criteria for this assignment is:
    {state["success_criteria"]}

    And the final response from the Assistant that you are evaluating is:
    {last_response}

    Respond with your feedback, and decide if the success criteria is met by this response.
    Also, decide if more user input is required, either because the assistant has a question, needs clarification, or seems to be stuck and unable to answer without help.

    The Assistant has access to a tool to write files. If the Assistant says they have written a file, then you can assume they have done so.
    Overall you should give the Assistant the benefit of the doubt if they say they've done something. But you should reject if you feel that more work should go into this.

    """
        # Nếu đã có feedback trước đó (Worker bị reject nhiều lần), cân nhắc yêu cầu user input
        if state["feedback_on_work"]:
            user_message += f"Also, note that in a prior attempt from the Assistant, you provided this feedback: {state['feedback_on_work']}\n"
            user_message += "If you're seeing the Assistant repeating the same mistakes, then consider responding that user input is required."

        evaluator_messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=user_message),
        ]

        # Gọi Evaluator LLM để nhận structured output
        eval_result = self.evaluator_llm_with_output.invoke(evaluator_messages)
        new_state = {
            "messages": [
                {
                    "role": "assistant",
                    "content": f"Evaluator Feedback on this answer: {eval_result.feedback}",
                }
            ],
            "feedback_on_work": eval_result.feedback,
            "success_criteria_met": eval_result.success_criteria_met,
            "user_input_needed": eval_result.user_input_needed,
        }
        return new_state

    def route_based_on_evaluation(self, state: State) -> str:
        """
        Router sau Evaluator node:
        - Nếu đã đạt success criteria HOẶC cần user input -> END (dừng)
        - Nếu chưa đạt và không cần user -> quay lại "worker" để làm tiếp
        """
        if state["success_criteria_met"] or state["user_input_needed"]:
            return "END"
        else:
            return "worker"

    async def build_graph(self):
        """
        Xây dựng LangGraph workflow:
        
        Flow: START -> worker -> [tools hoặc evaluator]
        - Nếu worker gọi tools -> tools node -> quay lại worker
        - Nếu worker không gọi tools -> evaluator đánh giá
        - Evaluator quyết định: END (xong) hoặc quay lại worker (làm tiếp)
        
        Graph sử dụng MemorySaver để lưu lịch sử hội thoại
        """
        # Khởi tạo StateGraph với State schema
        graph_builder = StateGraph(State)

        # Thêm các nodes
        graph_builder.add_node("worker", self.worker)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_node("evaluator", self.evaluator)

        # Thêm edges (kết nối giữa các nodes)
        graph_builder.add_conditional_edges(
            "worker", self.worker_router, {"tools": "tools", "evaluator": "evaluator"}
        )
        graph_builder.add_edge("tools", "worker")
        graph_builder.add_conditional_edges(
            "evaluator", self.route_based_on_evaluation, {"worker": "worker", "END": END}
        )
        graph_builder.add_edge(START, "worker")

        # Compile graph với memory checkpointer
        self.graph = graph_builder.compile(checkpointer=self.memory)

    async def run_superstep(self, message, success_criteria, history):
        """
        Chạy một "superstep" - một vòng lặp xử lý hoàn chỉnh:
        - Nhận message từ user và success criteria
        - Chạy graph cho đến khi END (hoàn thành hoặc cần user input)
        - Trả về lịch sử chat đầy đủ: user message + AI reply + evaluator feedback
        """
        config = {"configurable": {"thread_id": self.sidekick_id}}

        state = {
            "messages": message,
            "success_criteria": success_criteria or "The answer should be clear and accurate",
            "feedback_on_work": None,
            "success_criteria_met": False,
            "user_input_needed": False,
        }
        result = await self.graph.ainvoke(state, config=config)
        user = {"role": "user", "content": message}
        reply = {"role": "assistant", "content": result["messages"][-2].content}
        feedback = {"role": "assistant", "content": result["messages"][-1].content}
        return history + [user, reply, feedback]

    def cleanup(self):
        """
        Giải phóng tài nguyên khi đóng app:
        - Đóng browser (Playwright)
        - Dừng Playwright instance
        - Xử lý cả trường hợp có asyncio loop hoặc không
        """
        if self.browser:
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(self.browser.close())
                if self.playwright:
                    loop.create_task(self.playwright.stop())
            except RuntimeError:
                # Nếu không có running loop, chạy trực tiếp
                asyncio.run(self.browser.close())
                if self.playwright:
                    asyncio.run(self.playwright.stop())
