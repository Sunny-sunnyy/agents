# 81. Day 4 - Playwright Integration with LangGraph - Creating Web-Browsing AI Agents

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng trực tiếp từ `G:\Agent2026Win\agents\4_langgraph\3_lab3.ipynb`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript 81 khớp trực tiếp với các cell đầu của `3_lab3.ipynb`, đặc biệt ở phần async mode, `TypedDict` state, push tool, Playwright toolkit và notebook-specific setup.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này mở đầu Day 4 bằng cách đưa `Playwright - framework tự động hóa trình duyệt` vào hệ LangGraph để tạo agent có thể duyệt web thật.
- Bài học nhắc lại `super-step - siêu bước`, `reducers - bộ hợp nhất cập nhật`, và `checkpointing - chụp điểm khôi phục trạng thái` như nền của graph runtime trước khi thêm browser automation.
- Điểm mới quan trọng là chạy `LangGraph` ở `async mode - chế độ bất đồng bộ`, dùng `await tool.arun(...)` và `await graph.ainvoke(...)`.
- State vẫn tối giản với `messages: Annotated[list, add_messages]`, cho thấy reducer message history vẫn là trục dữ liệu chính của graph.
- Một custom tool cũ được reuse là `push notification - gửi thông báo đẩy`, sau đó kết hợp với bộ Playwright tools để chuẩn bị cho project sidekick.
- `PlayWrightBrowserToolkit` cung cấp nhiều low-level browser tools như navigate, click, extract text, extract hyperlinks và inspect current page.
- Notebook cũng nhấn mạnh đây là môi trường notebook nên phải xử lý async loop cẩn thận bằng `nest_asyncio`, và có lưu ý riêng cho Windows khi Playwright có thể va chạm event loop policy.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu Playwright được thêm vào LangGraph như một tập tools để agent tương tác với browser thật.
  - Hiểu sự khác nhau giữa sync và async invocation trong LangGraph.
  - Hiểu vì sao notebook environment cần xử lý event loop đặc biệt khi dùng browser automation async.
- Practical goals - mục tiêu thực hành:
  - Có thể khởi tạo Playwright browser async và lấy ra toolkit tools.
  - Có thể khai báo graph state tối thiểu và chuẩn bị toolset cho lesson kế tiếp.
  - Biết chỗ nào trong notebook cần `nest_asyncio` và chỗ nào cần cảnh giác với Windows.
- What learner should be able to explain - người học cần giải thích được:
  - `await graph.ainvoke(...)` khác gì `graph.invoke(...)`.
  - Vì sao Playwright tools là một bước nhảy lớn so với các tools nội bộ trước đó.
  - Tại sao `nest_asyncio` chỉ là workaround cho notebook, không phải ý tưởng runtime cốt lõi của graph.

## 4. Previous Context - Liên hệ với bài trước
Lesson này nối trực tiếp từ Day 3, đặc biệt là các bài về `tool calling - gọi công cụ`, `conditional edges - cạnh có điều kiện`, và `checkpointing`. Nếu Day 3 cho thấy graph có thể quyết định dùng tool và giữ memory giữa các invocations, thì lesson 81 mở rộng phạm vi “tool” từ search/push đơn giản sang browser control thật. Nó cũng tái sử dụng mental model `super-step + checkpointing` từ lesson 76, 79, 80 để chuẩn bị cho agent web-browsing phức tạp hơn.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Playwright - framework tự động hóa trình duyệt
  - Meaning - nghĩa: Công cụ cho phép mở browser thật, render JavaScript, đọc trang, click phần tử và điều hướng như người dùng thật.
  - Why it matters - vì sao quan trọng: Đây là nền để agent truy cập web động thay vì chỉ gọi API hay request HTML tĩnh.
  - Relationship - liên hệ với khái niệm khác: Được đóng gói thành tools để LangGraph node hoặc ToolNode gọi.
- Term - thuật ngữ: async mode - chế độ bất đồng bộ
  - Meaning - nghĩa: Cách chạy tools và graph bằng `await`, cho phép IO-bound work như browser automation hoạt động đúng luồng.
  - Why it matters - vì sao quan trọng: Browser actions và web extraction thường là tác vụ chờ IO, rất hợp với async execution.
  - Relationship - liên hệ với khái niệm khác: Kết hợp với `nest_asyncio` trong notebook và `graph.ainvoke(...)` ở runtime.
- Term - thuật ngữ: PlayWrightBrowserToolkit - bộ công cụ trình duyệt Playwright
  - Meaning - nghĩa: Tập tool wrappers từ LangChain Community để thao tác với Playwright browser.
  - Why it matters - vì sao quan trọng: Giúp agent có sẵn capability browser mà không phải tự viết thủ công từng wrapper.
  - Relationship - liên hệ với khái niệm khác: Cung cấp tools như `navigate_browser`, `extract_text`, rồi sau đó được ghép chung với custom push tool.
- Term - thuật ngữ: headful mode - chế độ hiện cửa sổ trình duyệt
  - Meaning - nghĩa: Browser được mở ra có giao diện nhìn thấy được.
  - Why it matters - vì sao quan trọng: Dễ debug hành vi agent hơn khi đang học.
  - Relationship - liên hệ với khái niệm khác: Đối lập với `headless mode - chế độ không hiện cửa sổ`.
- Term - thuật ngữ: nest_asyncio - thư viện vá event loop lồng nhau
  - Meaning - nghĩa: Patch cho `asyncio` để cho phép notebook chạy nested event loop.
  - Why it matters - vì sao quan trọng: Tránh lỗi khi vừa có notebook event loop, vừa muốn chạy async browser/tool invocations.
  - Relationship - liên hệ với khái niệm khác: Đây là workaround môi trường notebook, không phải bản chất của LangGraph.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - Notebook environment.
   - Environment variables đã được load.
   - Browser automation requirement cho project sidekick.
2. Processing steps:
   - Khởi tạo state `messages` với reducer `add_messages`.
   - Reuse custom `push` tool từ bài trước.
   - Patch notebook event loop bằng `nest_asyncio`.
   - Tạo async browser bằng `create_async_playwright_browser(headless=False)`.
   - Dựng `PlayWrightBrowserToolkit` và lấy danh sách tools.
3. Output:
   - Một tập browser tools sẵn sàng để test thủ công và để đưa vào graph lesson kế tiếp.
4. Control flow / data flow:
   - Notebook setup -> async patch -> browser creation -> toolkit -> tools list.
   - State model và tool definitions được chuẩn bị trước khi xây graph hoàn chỉnh.
5. Decision points:
   - Chọn sync hay async graph/tool execution.
   - Chọn headful hay headless browser.
   - Có cần notebook workaround cho event loop hay không.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Async graph execution - thực thi graph bất đồng bộ
  - Purpose - mục đích: Cho phép graph điều phối các browser/tool actions IO-bound hiệu quả hơn.
  - When to use - dùng khi nào: Khi tool hoặc browser client có API async.
  - Trade-off - đánh đổi: Cần hiểu event loop và debug async stack khó hơn code sync.
  - Common mistake - lỗi dễ gặp: Gọi tool async như tool sync hoặc quên `await`.
- Technique - kỹ thuật: Toolkit-first browser integration - tích hợp browser qua toolkit có sẵn
  - Purpose - mục đích: Tận dụng tập tool cộng đồng thay vì tự viết browser wrappers.
  - When to use - dùng khi nào: Khi cần browser automation nhanh để học hoặc prototype.
  - Trade-off - đánh đổi: Abstraction tiện nhưng phải hiểu tool names/capabilities thật sự có gì.
  - Common mistake - lỗi dễ gặp: Tưởng toolkit là “agent hoàn chỉnh” thay vì chỉ là capability layer.
- Technique - kỹ thuật: Notebook async patching - vá async cho notebook
  - Purpose - mục đích: Giúp môi trường notebook chịu được nested event loop.
  - When to use - dùng khi nào: Khi chạy async browser automation trong notebook.
  - Trade-off - đánh đổi: Đây là workaround hơi “hacky”, không nên nhầm với production architecture.
  - Common mistake - lỗi dễ gặp: Mang nguyên workaround này sang Python module như một requirement bắt buộc.

## 8. Code Walkthrough - Phân tích code nếu có
- File / block: state và async primer trong `3_lab3.ipynb`
  - Purpose - mục đích: Thiết lập state tối thiểu và chuyển mental model từ sync sang async.
  - Key logic - logic chính: `State` chỉ có `messages` với reducer `add_messages`; markdown giải thích `tool.arun` và `graph.ainvoke`.
  - Important lines / functions:
    - `class State(TypedDict):`
    - `messages: Annotated[list, add_messages]`
    - `graph_builder = StateGraph(State)`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - State vẫn tối giản vì lesson này ưu tiên thêm browser capability trước, chưa tăng độ phức tạp business state.
    - Async mode ở đây là thay execution model, không thay data model.
- File / block: push tool và Playwright toolkit setup trong `3_lab3.ipynb`
  - Purpose - mục đích: Ghép custom tool cũ với browser tools mới.
  - Key logic - logic chính: Reuse `push`, tạo async browser, lấy `toolkit.get_tools()`.
  - Important lines / functions:
    - `def push(text: str):`
    - `tool_push = Tool(...)`
    - `async_browser = create_async_playwright_browser(headless=False)`
    - `toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)`
    - `tools = toolkit.get_tools()`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - `headless=False` giúp nhìn được browser đang bị agent điều khiển.
    - Toolkit trả về nhiều tools nhỏ thay vì một tool “browse web” duy nhất.
- File / block: notebook-specific async workaround
  - Purpose - mục đích: Tránh va chạm event loop trong notebook.
  - Key logic - logic chính: `import nest_asyncio` rồi `nest_asyncio.apply()`, kèm hướng dẫn Windows workaround trong markdown.
  - Important lines / functions:
    - `import nest_asyncio`
    - `nest_asyncio.apply()`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Đây là phần phụ trợ môi trường chạy, không phải business logic của sidekick.
    - Lesson có nhắc rõ Day 5 chuyển sang Python module thì nhu cầu này giảm đi.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Sync tool execution
  - Pros: Dễ hiểu hơn cho người mới.
  - Cons: Không hợp bằng với browser automation IO-bound và khó map sang notebook demo hiện tại.
  - When to choose: Khi tools đơn giản hoặc không có browser async APIs.
- Option: Async tool execution
  - Pros: Phù hợp Playwright, mở đường cho graph có browser operations thực tế.
  - Cons: Tăng độ khó về event loop, especially trong notebook.
  - When to choose: Đây là lựa chọn đúng cho lesson này.
- Option: Tự viết browser wrapper
  - Pros: Kiểm soát tối đa interface và behavior.
  - Cons: Chậm, nhiều việc lặp, không cần thiết cho giai đoạn học.
  - When to choose: Khi toolkit có sẵn không đủ capability hoặc cần guardrails đặc thù.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Tưởng Playwright chỉ là web scraping tool
  - Root cause: Quen với request/BeautifulSoup hơn browser automation.
  - Symptom: Đánh giá thấp khả năng render JavaScript, click, navigate thật của toolset.
  - Fix / prevention: Nhớ rằng Playwright là browser runtime đầy đủ, không chỉ là HTML fetcher.
- Failure mode: Quên `await` khi chạy tool hoặc graph async
  - Root cause: Chuyển từ sync examples cũ sang async lesson mới.
  - Symptom: Lỗi coroutine chưa được await hoặc graph không chạy đúng.
  - Fix / prevention: Kiểm tra mọi điểm gọi tool/browser/graph trong lesson này đều theo API async.
- Failure mode: Nhầm notebook workaround với production requirement
  - Root cause: Thấy `nest_asyncio` và tưởng đó là phần cốt lõi của app.
  - Symptom: Kiến trúc module sau này bị cồng kềnh không cần thiết.
  - Fix / prevention: Tách bạch environment workaround với orchestration logic.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: `Browser automation agent - tác tử tự động hóa trình duyệt` là nền gần với các sản phẩm “computer use” hoặc “operator-like agents”, nơi model điều phối browser thay vì chỉ trả lời text.
- Mở rộng: Trong hệ production, browser tools thường cần thêm guardrails như domain allowlist, timeout budgets, screenshot logging và rate limiting vì browser là tool có side effects mạnh.
- Mở rộng: Chuyển từ notebook async hacks sang service/module thực sự thường giúp debugging dễ hơn rất nhiều, nhất là với Playwright và long-running agent loops.

## 12. Study Pack - Gói ôn tập
### Must remember
- Day 4 mở đầu bằng Playwright integration cho LangGraph.
- Lesson này giới thiệu `async mode` cho tools và graph.
- State vẫn tối giản với `messages` + `add_messages`.
- `PlayWrightBrowserToolkit` cung cấp nhiều browser tools granular.
- `nest_asyncio` là workaround cho notebook.
- Browser automation là capability mới quan trọng để build sidekick.

### Self-check questions
- Vì sao lesson này cần chuyển sang `graph.ainvoke(...)`?
- `PlayWrightBrowserToolkit` cung cấp loại capability gì?
- `nest_asyncio` giải quyết vấn đề môi trường nào?
- Tại sao state trong lesson này vẫn giữ rất đơn giản?
- Vì sao browser automation mạnh hơn cách chỉ request HTML tĩnh?

### Flashcards
- Q: `await graph.ainvoke(state)` dùng khi nào?
  A: Khi graph được chạy ở async mode, thường để phối hợp với tools IO-bound như Playwright.
- Q: `PlayWrightBrowserToolkit` trả về gì?
  A: Một tập browser tools như navigate, click, extract text, extract hyperlinks và các thao tác trang khác.
- Q: `nest_asyncio` có phải là phần bản chất của LangGraph không?
  A: Không, nó là workaround cho notebook event loop.

### Interview Q&A nếu phù hợp
- Q: Tại sao browser automation là bước tiến lớn trong agent systems?
  A: Vì nó cho phép agent thao tác web động và giao diện thật, thay vì chỉ trả lời text hoặc gọi API đóng gói sẵn.
- Q: Khi nào bạn chọn async orchestration cho agent?
  A: Khi tools và external interactions chủ yếu là IO-bound, như browser control, web calls, hay concurrent service interactions.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide Day 4 để đối chiếu sơ đồ hoặc bullet chính thức của lesson.
- Không có trace/log riêng cho lesson 81 ngoài transcript và notebook.
- Chưa cần scan thêm file/folder khác vì transcript và notebook đã đủ để map trực tiếp lesson này.

# 82. Day 4 - Create AI Web Assistants - Playwright, LangChain & Gradio Implementation

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng trực tiếp từ `G:\Agent2026Win\agents\4_langgraph\3_lab3.ipynb`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript 82 khớp trực tiếp với nửa sau `3_lab3.ipynb`, đặc biệt ở các cell dictionary comprehension, test navigate/extract, bind tools, graph build, `MemorySaver`, và `gr.ChatInterface`.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này chuyển Playwright tools từ capability thô thành một `web assistant - trợ lý web` thật sự có LLM đứng giữa để quyết định khi nào dùng tool nào.
- Instructor test toolkit trước bằng cách gọi trực tiếp `navigate_browser` và `extract_text` để chứng minh browser tools hoạt động độc lập với LLM.
- Tất cả browser tools được ghép với custom `push` tool thành `all_tools`, rồi bind vào `ChatOpenAI(model="gpt-4o-mini")`.
- Node `chatbot` trở thành một LLM-backed node trả về `messages`, còn `ToolNode` thực thi tool calls khi LLM yêu cầu.
- Graph pattern của lesson là một vòng lặp một-agent: `START -> chatbot -> tools -> chatbot`, với `conditional edge - cạnh có điều kiện` từ chatbot sang tools.
- `MemorySaver` và `thread_id` được dùng để giữ memory giữa các super-steps; Gradio callback không tự quản lý history logic, mà dựa chủ yếu vào checkpointing.
- Lesson kết thúc bằng web assistant có thể mở CNN, lấy headline, tra tỷ giá USD/GBP và gửi push notification, đồng thời trace được đầy đủ trong LangSmith.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách biến tập tools thành một agent loop hoàn chỉnh trong LangGraph.
  - Hiểu vai trò của `ToolNode`, `tools_condition`, và conditional edge trong tool-calling flow.
  - Hiểu checkpointing được dùng cho conversation continuity thay vì dựa vào history của Gradio.
- Practical goals - mục tiêu thực hành:
  - Có thể test browser tools trực tiếp trước khi bind vào LLM.
  - Có thể build graph web assistant tối thiểu và nối nó với Gradio UI.
  - Có thể đọc trace LangSmith để xem agent đã dùng tool nào theo thứ tự nào.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao graph của lesson này chỉ là “một agent với tool loop”, chưa phải multi-agent.
  - `tools_condition` hoạt động như một if-statement backend ra sao.
  - Vì sao Gradio history được bỏ qua một phần và checkpointing được chọn làm memory source chính.

## 4. Previous Context - Liên hệ với bài trước
Lesson này là bước triển khai trực tiếp của lesson 81. Nếu lesson 81 mới thêm Playwright toolkit vào hệ toolset, thì lesson 82 dùng chính toolset đó để xây một web assistant chạy được. Nó cũng kéo dài chuỗi tư tưởng từ Day 3 về `tool calling`, `conditional edges`, và `MemorySaver` để cho thấy một graph chatbot có thể được nâng thành browser-using assistant mà không phải đổi mental model cơ bản.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: ToolNode - node thực thi tools
  - Meaning - nghĩa: Node dựng sẵn của LangGraph để xử lý tool calls do model phát ra.
  - Why it matters - vì sao quan trọng: Tách hẳn phần “LLM quyết định” khỏi phần “tool thực thi”.
  - Relationship - liên hệ với khái niệm khác: Đi cùng `llm.bind_tools(...)` và `tools_condition`.
- Term - thuật ngữ: tools_condition - điều kiện gọi tools
  - Meaning - nghĩa: Hàm điều kiện dựng sẵn để route từ chatbot node sang ToolNode khi output của model chứa tool call.
  - Why it matters - vì sao quan trọng: Giúp graph lặp qua tool-use mà không phải tự viết parser route thủ công.
  - Relationship - liên hệ với khái niệm khác: Nằm ở `conditional edge` từ chatbot sang tools.
- Term - thuật ngữ: bind_tools - gắn tools vào model
  - Meaning - nghĩa: Tạo model wrapper biết schema của các tools và có thể trả structured tool calls.
  - Why it matters - vì sao quan trọng: Cho phép LLM lựa chọn tool dựa trên prompt và conversation state.
  - Relationship - liên hệ với khái niệm khác: Là cầu nối giữa tool definitions và `ToolNode`.
- Term - thuật ngữ: one-agent tool loop - vòng lặp một agent với tools
  - Meaning - nghĩa: Một graph có duy nhất một LLM node nhưng có thể lặp giữa reasoning và tool execution.
  - Why it matters - vì sao quan trọng: Đây là pattern cơ bản trước khi học multi-agent worker/evaluator ở lab kế tiếp.
  - Relationship - liên hệ với khái niệm khác: Cấu trúc `chatbot -> tools -> chatbot`.
- Term - thuật ngữ: checkpoint-backed chat memory - bộ nhớ chat dựa trên checkpoint
  - Meaning - nghĩa: Memory giữa các lượt chat được giữ bằng checkpointer, không chỉ bằng UI history.
  - Why it matters - vì sao quan trọng: Tách UI layer khỏi graph memory semantics.
  - Relationship - liên hệ với khái niệm khác: Dùng `MemorySaver` và `configurable.thread_id`.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - User prompt từ Gradio.
   - Browser tools + push tool đã được bind vào model.
   - Thread config cho checkpointer.
2. Processing steps:
   - Test thủ công Playwright tools bằng `navigate_browser` và `extract_text`.
   - Ghép `all_tools = tools + [tool_push]`.
   - Tạo `llm_with_tools = llm.bind_tools(all_tools)`.
   - Node `chatbot` gọi model với `state["messages"]`.
   - Nếu model phát tool call thì graph route sang `ToolNode`.
   - ToolNode chạy tools rồi quay lại `chatbot`.
   - Graph được compile với `MemorySaver`.
   - Gradio callback dùng `await graph.ainvoke(...)`.
3. Output:
   - Final assistant reply hoặc side effect như push notification sau khi agent duyệt web.
4. Control flow / data flow:
   - User input -> chatbot -> optional tools -> chatbot -> final reply.
   - Message state được reducer cộng dồn và checkpoint lưu giữa các super-steps.
5. Decision points:
   - Model có cần tool call không.
   - Tool nào trong `all_tools` nên được chọn.
   - Có dùng history UI hay tin vào checkpointing làm memory backbone.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Direct tool smoke test - kiểm tra tools trực tiếp trước khi đưa vào agent
  - Purpose - mục đích: Tách lỗi capability của tool khỏi lỗi reasoning của LLM.
  - When to use - dùng khi nào: Khi tích hợp tool phức tạp như browser automation.
  - Trade-off - đánh đổi: Tốn thêm bước, nhưng giảm đáng kể thời gian debug.
  - Common mistake - lỗi dễ gặp: Bind tool vào LLM ngay rồi không biết lỗi nằm ở tool hay prompt.
- Technique - kỹ thuật: One-agent with tool loop - một agent lặp với tools
  - Purpose - mục đích: Xây baseline web assistant đơn giản trước khi chuyển sang multi-agent.
  - When to use - dùng khi nào: Khi bài toán chỉ cần một reasoning node với external actions.
  - Trade-off - đánh đổi: Chưa có quality-control layer riêng như evaluator.
  - Common mistake - lỗi dễ gặp: Gọi đây là multi-agent dù thực tế chỉ có một LLM node.
- Technique - kỹ thuật: Checkpoint-first session memory - memory phiên dựa trên checkpoint
  - Purpose - mục đích: Để graph giữ state giữa các lượt chat mà không phụ thuộc vào frontend history.
  - When to use - dùng khi nào: Khi dùng LangGraph chat loops nhiều lượt.
  - Trade-off - đánh đổi: Phải quản lý `thread_id` rõ ràng.
  - Common mistake - lỗi dễ gặp: Truyền `history` của Gradio nhưng không hiểu nó không phải source of truth chính.

## 8. Code Walkthrough - Phân tích code nếu có
- File / block: smoke test Playwright tools trong `3_lab3.ipynb`
  - Purpose - mục đích: Chứng minh browser tools hoạt động trước khi giao cho agent.
  - Key logic - logic chính: Tạo `tool_dict`, rút `navigate_browser` và `extract_text`, rồi gọi async trực tiếp trên CNN.
  - Important lines / functions:
    - `tool_dict = {tool.name: tool for tool in tools}`
    - `navigate_tool = tool_dict.get("navigate_browser")`
    - `extract_text_tool = tool_dict.get("extract_text")`
    - `await navigate_tool.arun({"url": "https://www.cnn.com"})`
    - `text = await extract_text_tool.arun({})`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Đây là bước bóc tách “tool works” khỏi “agent reasons correctly”.
    - Dictionary comprehension giúp truy cập tool theo tên, tránh mò theo index.
- File / block: chatbot node + bind tools
  - Purpose - mục đích: Biến LLM thành reasoning node biết gọi browser tools và push tool.
  - Key logic - logic chính: `llm.bind_tools(all_tools)` rồi node `chatbot` trả về message do model sinh ra.
  - Important lines / functions:
    - `all_tools = tools + [tool_push]`
    - `llm = ChatOpenAI(model="gpt-4o-mini")`
    - `llm_with_tools = llm.bind_tools(all_tools)`
    - `def chatbot(state: State):`
    - `return {"messages": [llm_with_tools.invoke(state["messages"])]}`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Node này không trực tiếp chạy tool; nó chỉ phát ra tool calls hoặc final reply.
    - Reducer `add_messages` sẽ gắn output mới vào conversation state cũ.
- File / block: graph + ToolNode + Gradio callback
  - Purpose - mục đích: Đóng gói web assistant thành graph chat chạy được.
  - Key logic - logic chính: Dựng `ToolNode`, thêm conditional edge, compile với memory, rồi dùng `graph.ainvoke` trong callback.
  - Important lines / functions:
    - `graph_builder.add_node("chatbot", chatbot)`
    - `graph_builder.add_node("tools", ToolNode(tools=all_tools))`
    - `graph_builder.add_conditional_edges("chatbot", tools_condition, "tools")`
    - `graph_builder.add_edge("tools", "chatbot")`
    - `memory = MemorySaver()`
    - `result = await graph.ainvoke({...}, config=config)`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - `tools_condition` đóng vai trò if-statement xem model có phát tool call không.
    - Callback bỏ qua `history` làm memory backbone và tin vào checkpointing qua `thread_id`.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Test tool trực tiếp trước rồi mới bind vào LLM
  - Pros: Debug sạch hơn, biết chắc capability có chạy.
  - Cons: Thêm bước thủ công.
  - When to choose: Nên chọn khi tool phức tạp như browser.
- Option: Một agent + tool loop
  - Pros: Đơn giản, rõ control flow, đủ mạnh cho nhiều tác vụ web.
  - Cons: Chưa có layer đánh giá chất lượng output.
  - When to choose: Khi mới build baseline assistant.
- Option: Multi-agent ngay từ đầu
  - Pros: Có thể thêm evaluator, planner, reviewer sớm.
  - Cons: Khó debug hơn và quá nặng cho bước đầu browser integration.
  - When to choose: Khi baseline one-agent đã ổn và cần quality loop rõ ràng hơn.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Gọi graph này là multi-agent
  - Root cause: Thấy có tools, routing và loop nên nghĩ đã có nhiều agents.
  - Symptom: Hiểu sai ranh giới giữa “agent + tools” và “nhiều agent nodes”.
  - Fix / prevention: Nhớ lesson 82 chỉ có một LLM node là `chatbot`.
- Failure mode: Dùng frontend history làm memory source chính
  - Root cause: Quen tư duy Gradio chat apps.
  - Symptom: Memory semantics lệch với checkpoint semantics của graph.
  - Fix / prevention: Coi checkpointing là source of truth cho graph state continuity.
- Failure mode: Tool trả về side effect nhưng không có structured success response tốt
  - Root cause: Custom tool như push notification trả `null` hoặc response nghèo nàn.
  - Symptom: Trace khó đọc, agent feedback về tool result không mạch lạc.
  - Fix / prevention: Cho tool trả metadata thành công/thất bại nhất quán hơn.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: Pattern `LLM node + ToolNode + conditional edge` là một trong những shape phổ biến nhất cho production tool-using agents vì tách reasoning và execution khá sạch.
- Mở rộng: Browser-using assistants trong thực tế thường cần thêm step xác thực nguồn, retry policy và tool-result summarization để tránh model đọc nhầm nội dung web thô.
- Mở rộng: Trace observability như LangSmith rất quan trọng vì browser agents thường phát sinh chuỗi tool calls dài, khó hiểu nếu chỉ nhìn kết quả cuối.

## 12. Study Pack - Gói ôn tập
### Must remember
- Lesson 82 biến Playwright tools thành web assistant hoàn chỉnh.
- Có bước smoke test tools trước khi bind vào model.
- Graph pattern là `START -> chatbot -> tools -> chatbot`.
- `ToolNode` chạy tools; `chatbot` node quyết định có dùng tools hay không.
- Memory của graph dựa trên `MemorySaver` và `thread_id`.
- Đây vẫn là one-agent flow, chưa phải worker-evaluator multi-agent.

### Self-check questions
- Vì sao nên test `navigate_browser` và `extract_text` trực tiếp trước?
- `tools_condition` giải quyết việc gì trong graph?
- Vì sao lesson này vẫn là một agent?
- `thread_id` đóng vai trò gì với Gradio chat app này?
- Vì sao push tool side effect cần response nhất quán hơn?

### Flashcards
- Q: `ToolNode` làm gì?
  A: Nó thực thi tool calls mà model đã phát ra.
- Q: `tools_condition` thường được dùng ở đâu?
  A: Ở conditional edge từ LLM node sang ToolNode.
- Q: Web assistant lesson 82 có bao nhiêu LLM agent node?
  A: Một node chính là `chatbot`.

### Interview Q&A nếu phù hợp
- Q: Tại sao nên tách “tool smoke test” khỏi “LLM tool use” khi tích hợp tool mới?
  A: Vì như vậy có thể debug capability layer và reasoning layer độc lập, giảm thời gian xác định root cause.
- Q: Tại sao checkpointing tốt hơn việc chỉ giữ chat history ở frontend?
  A: Vì checkpointing gắn trực tiếp với graph runtime và có thể tái sử dụng ngoài UI, phù hợp hơn với stateful agent workflows.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide Day 4 cho lesson này.
- Không có export trace LangSmith riêng, nên phần tracing dựa trên transcript mô tả và logic notebook.
- Chưa cần scan thêm file/folder khác vì transcript và notebook đã khớp trực tiếp.

# 83. Day 4 - LLM Evaluator Agents - Creating Feedback Loops with Structured Outputs

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng trực tiếp từ `G:\Agent2026Win\agents\4_langgraph\4_lab4.ipynb`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript 83 khớp trực tiếp với phần đầu `4_lab4.ipynb`, nhất là ở `EvaluatorOutput`, state giàu hơn, `worker_llm`, `evaluator_llm.with_structured_output(...)`, và system prompt của worker.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này mở lab 4 bằng việc giới thiệu `structured outputs - đầu ra có cấu trúc` và `evaluator agent - tác tử đánh giá`.
- `EvaluatorOutput` được định nghĩa bằng `Pydantic BaseModel` với ba trường chính: `feedback`, `success_criteria_met`, và `user_input_needed`.
- State của graph được mở rộng mạnh: ngoài `messages` còn có `success_criteria`, `feedback_on_work`, `success_criteria_met`, và `user_input_needed`.
- Worker và evaluator dùng hai LLM instances riêng: worker được `bind_tools`, còn evaluator dùng `with_structured_output(EvaluatorOutput)`.
- Lesson nhấn mạnh reducer chỉ được gán cho `messages`; các field khác khi node trả về sẽ overwrite state cũ, không phải cộng dồn.
- Prompt của worker được thiết kế để giữ agent tiếp tục làm việc cho tới khi hoặc đạt success criteria, hoặc cần hỏi lại user.
- Đây là bước dịch chuyển từ “tool-using assistant” sang “assistant có quality-control loop”.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu structured outputs khác gì prompt-to-JSON thủ công.
  - Hiểu evaluator là một LLM node riêng với schema đầu ra rõ ràng.
  - Hiểu state giàu hơn có thể chứa cả control flags cho graph routing.
- Practical goals - mục tiêu thực hành:
  - Có thể định nghĩa `Pydantic` schema cho evaluator output.
  - Có thể mở rộng state để mang cả success criteria và feedback loop metadata.
  - Có thể cấu hình hai LLMs với hai vai trò runtime khác nhau.
- What learner should be able to explain - người học cần giải thích được:
  - `with_structured_output(EvaluatorOutput)` đang làm gì phía sau abstraction.
  - Vì sao `messages` cần reducer nhưng `success_criteria_met` thì không.
  - Tại sao worker prompt phải ép model phân biệt “final answer” với “question for user”.

## 4. Previous Context - Liên hệ với bài trước
Lesson 83 kế thừa trực tiếp lesson 82 nhưng thay vì chỉ có một agent tự quyết định tool calls, nó bổ sung một lớp đánh giá riêng. Nó cũng mở rộng tinh thần từ Day 2 về `state design - thiết kế trạng thái`: nếu Day 2 dạy cách state có thể chứa messages và reducers, thì ở đây state trở thành nơi chứa cả business criteria và routing flags. Đồng thời, nó chuẩn bị cho lesson 84 nơi evaluator node và routing loop sẽ thực sự hoàn chỉnh.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: structured outputs - đầu ra có cấu trúc
  - Meaning - nghĩa: Cách yêu cầu model trả kết quả theo schema rõ ràng, thường ánh xạ thành object typed trong code.
  - Why it matters - vì sao quan trọng: Giảm ambiguity so với parse text tự do, đặc biệt hữu ích cho routing decisions.
  - Relationship - liên hệ với khái niệm khác: Ở lesson này nó được dùng cho evaluator, không dùng cho worker.
- Term - thuật ngữ: EvaluatorOutput - schema đầu ra của evaluator
  - Meaning - nghĩa: Pydantic object mô tả feedback, success flag và yêu cầu hỏi thêm user hay không.
  - Why it matters - vì sao quan trọng: Biến đánh giá chất lượng thành dữ liệu machine-readable thay vì chỉ là lời văn.
  - Relationship - liên hệ với khái niệm khác: Là output contract cho evaluator LLM.
- Term - thuật ngữ: success criteria - tiêu chí thành công
  - Meaning - nghĩa: Điều kiện người dùng đưa vào ngay từ đầu để evaluator quyết định câu trả lời đã đủ chưa.
  - Why it matters - vì sao quan trọng: Làm rõ definition of done cho agent.
  - Relationship - liên hệ với khái niệm khác: Được lưu trong state và được cả worker lẫn evaluator dùng.
- Term - thuật ngữ: feedback_on_work - phản hồi về phần việc đã làm
  - Meaning - nghĩa: Phản hồi evaluator gửi lại để worker sửa câu trả lời ở vòng sau.
  - Why it matters - vì sao quan trọng: Tạo feedback loop thay vì chỉ pass/fail một lần.
  - Relationship - liên hệ với khái niệm khác: Được worker prompt đọc ở các lượt retry.
- Term - thuật ngữ: overwrite fields - cập nhật kiểu ghi đè
  - Meaning - nghĩa: Các field không có reducer sẽ lấy giá trị mới do node trả về để thay state cũ.
  - Why it matters - vì sao quan trọng: Cần hiểu để tránh nhầm mọi state field đều được accumulate như messages.
  - Relationship - liên hệ với khái niệm khác: Đối lập với `messages` là field có reducer `add_messages`.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - User request.
   - Success criteria do user xác định.
   - Browser tools từ lesson trước.
2. Processing steps:
   - Định nghĩa `EvaluatorOutput`.
   - Mở rộng `State` với flags và feedback fields.
   - Khởi tạo `worker_llm` có tools.
   - Khởi tạo `evaluator_llm_with_output`.
   - Viết worker node với system prompt nhấn mạnh success criteria và rule khi nào phải hỏi lại user.
3. Output:
   - Một worker node và một evaluator contract sẵn sàng để ghép thành feedback loop.
4. Control flow / data flow:
   - `success_criteria` đi vào state từ đầu, được worker và evaluator cùng đọc.
   - `messages` tích lũy qua reducer; `feedback_on_work`, `success_criteria_met`, `user_input_needed` được cập nhật theo từng node output.
5. Decision points:
   - Dùng structured outputs native hay prompt-to-JSON thủ công.
   - Khi nào worker nên trả final answer, khi nào nên hỏi lại user.
   - Field nào cần reducer, field nào chỉ cần overwrite.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Schema-first evaluator design - thiết kế evaluator từ schema trước
  - Purpose - mục đích: Biến feedback loop thành luồng có cấu trúc và dễ route.
  - When to use - dùng khi nào: Khi cần LLM đánh giá đầu ra của LLM khác hoặc của chính nó.
  - Trade-off - đánh đổi: Cần model hỗ trợ structured output tốt hoặc phải có fallback parse JSON thủ công.
  - Common mistake - lỗi dễ gặp: Chỉ yêu cầu evaluator “nói xem có tốt không” mà không ép schema cụ thể.
- Technique - kỹ thuật: Criteria-in-state - đưa tiêu chí thành công vào state
  - Purpose - mục đích: Giúp cả worker và evaluator truy cập chung definition of done.
  - When to use - dùng khi nào: Khi workflow có nhiều node cùng cần một objective chung.
  - Trade-off - đánh đổi: State phức tạp hơn, cần quản lý rõ semantics từng field.
  - Common mistake - lỗi dễ gặp: Để success criteria ở UI layer nhưng không đưa vào graph state.
- Technique - kỹ thuật: Prompt guardrails cho worker
  - Purpose - mục đích: Ép worker phân biệt rõ “cần hỏi lại user” với “đã hoàn thành”.
  - When to use - dùng khi nào: Khi có evaluator đứng sau và cần behavior ổn định hơn.
  - Trade-off - đánh đổi: Prompt dài hơn và phải tuning thực nghiệm.
  - Common mistake - lỗi dễ gặp: Để worker trả lời mơ hồ kiểu “can I help with anything else?” làm evaluator khó route.

## 8. Code Walkthrough - Phân tích code nếu có
- File / block: `EvaluatorOutput` và state mở rộng trong `4_lab4.ipynb`
  - Purpose - mục đích: Xây data contracts cho feedback loop.
  - Key logic - logic chính: `EvaluatorOutput` mô tả output evaluator; `State` chứa cả messages lẫn control fields.
  - Important lines / functions:
    - `class EvaluatorOutput(BaseModel):`
    - `feedback: str`
    - `success_criteria_met: bool`
    - `user_input_needed: bool`
    - `class State(TypedDict):`
    - `messages: Annotated[List[Any], add_messages]`
    - `success_criteria: str`
    - `feedback_on_work: Optional[str]`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Đây là lần đầu state của Day 4 mang logic điều phối thật, không chỉ conversation messages.
    - Chỉ `messages` dùng reducer; các field control còn lại được hiểu là “giá trị hiện hành”.
- File / block: khởi tạo worker LLM và evaluator LLM
  - Purpose - mục đích: Tách hai vai trò reasoning và judging thành hai runtime clients khác nhau.
  - Key logic - logic chính: Worker bind tools, evaluator bind schema output.
  - Important lines / functions:
    - `worker_llm_with_tools = worker_llm.bind_tools(tools)`
    - `evaluator_llm_with_output = evaluator_llm.with_structured_output(EvaluatorOutput)`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Cùng có thể là `gpt-4o-mini`, nhưng runtime contract của hai node là khác nhau hoàn toàn.
    - Worker phát tool calls hoặc answer; evaluator phát structured decision object.
- File / block: worker prompt logic
  - Purpose - mục đích: Buộc worker tiếp tục làm việc đến khi đạt tiêu chí hoặc cần hỏi user.
  - Key logic - logic chính: Prompt chèn `success_criteria`, nếu có `feedback_on_work` thì bổ sung phần sửa lỗi vòng trước.
  - Important lines / functions:
    - `def worker(state: State) -> Dict[str, Any]:`
    - `This is the success criteria: {state['success_criteria']}`
    - `if state.get("feedback_on_work"):`
    - `response = worker_llm_with_tools.invoke(messages)`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - `feedback_on_work` biến evaluator feedback thành context cho lượt reasoning tiếp theo.
    - Node trả về `messages` mới, để reducer append vào hội thoại.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Structured outputs native
  - Pros: Machine-readable rõ ràng, code sạch hơn.
  - Cons: Phụ thuộc model support và abstraction layer.
  - When to choose: Khi cần routing/data contracts chắc chắn.
- Option: Prompt model trả JSON thủ công
  - Pros: Linh hoạt, dùng được với nhiều model hơn.
  - Cons: Tự parse, dễ lỗi format, tốn guardrails hơn.
  - When to choose: Khi model không support structured outputs native.
- Option: Một LLM tự đánh giá chính mình trong cùng node
  - Pros: Đơn giản hơn về graph shape.
  - Cons: Kém tách bạch và khó quan sát feedback loop.
  - When to choose: Chỉ khi cần MVP rất nhanh và không cần graph rõ.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Tưởng structured outputs là “ma thuật khác hẳn JSON”
  - Root cause: Dùng abstraction mà quên cơ chế bên dưới.
  - Symptom: Khó fallback khi model không hỗ trợ.
  - Fix / prevention: Nhớ bản chất vẫn là model được bias trả JSON đúng schema rồi được parse vào object.
- Failure mode: Gắn reducer cho mọi field hoặc ngược lại quên reducer cho messages
  - Root cause: Không phân biệt field nào là append-only history, field nào là current status.
  - Symptom: State semantics rối, routing flags không ổn định.
  - Fix / prevention: Chỉ reducer cho field thật sự cần accumulate như `messages`.
- Failure mode: Prompt worker quá mơ hồ
  - Root cause: Không ép rõ khi nào được hỏi lại user và khi nào phải ra final answer.
  - Symptom: Evaluator khó quyết định `user_input_needed`.
  - Fix / prevention: Cho rule rõ và ví dụ cụ thể trong prompt.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: `LLM-as-judge - dùng LLM làm bộ giám khảo` là pattern rất mạnh nhưng thường cần tiêu chí rõ và observability tốt, nếu không sẽ dễ thành loop “tự khen/tự chê” mơ hồ.
- Mở rộng: State-rich workflows như lesson này gần hơn nhiều với real agent systems, vì chúng mang cả objective, progress flags và review metadata, không chỉ message history.
- Mở rộng: Structured outputs đặc biệt mạnh khi đầu ra của model sẽ được machine dùng tiếp, ví dụ route graph, gọi API, ghi DB, hay xác định escalation paths.

## 12. Study Pack - Gói ôn tập
### Must remember
- Lesson 83 giới thiệu structured outputs và evaluator agent.
- `EvaluatorOutput` có `feedback`, `success_criteria_met`, `user_input_needed`.
- State được mở rộng với business/control fields.
- Worker và evaluator là hai LLM clients với contracts khác nhau.
- Chỉ `messages` dùng reducer `add_messages`.
- Worker prompt phải rạch ròi giữa hỏi user và trả final answer.

### Self-check questions
- `with_structured_output(EvaluatorOutput)` giúp ích gì cho routing?
- Vì sao `success_criteria` cần được lưu trong state?
- Tại sao `feedback_on_work` quan trọng trong retry loop?
- Vì sao không nên để mọi field trong state dùng reducer?
- Nếu model không hỗ trợ structured outputs native thì fallback là gì?

### Flashcards
- Q: `EvaluatorOutput` chứa những gì?
  A: Feedback, cờ đạt tiêu chí thành công, và cờ cần hỏi thêm user.
- Q: Field nào trong state lesson 83 có reducer?
  A: `messages`.
- Q: Worker đọc `feedback_on_work` để làm gì?
  A: Để sửa câu trả lời ở vòng sau nếu evaluator đã reject vòng trước.

### Interview Q&A nếu phù hợp
- Q: Tại sao nên tách worker và evaluator thành hai nodes riêng?
  A: Vì như vậy feedback loop rõ hơn, routing rõ hơn, và observability tốt hơn so với nhét mọi thứ vào một prompt duy nhất.
- Q: Khi nào structured outputs đáng dùng hơn plain text outputs?
  A: Khi output sẽ được machine tiêu thụ tiếp để route, validate hoặc cập nhật state.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide Day 4 cho lesson này.
- Không có benchmark so sánh structured output native với parse-JSON manual.
- Chưa cần scan thêm file/folder khác vì transcript và notebook đã đủ ngữ cảnh trực tiếp.

# 84. Day 4- Creating LLM Feedback Loops - Worker-Evaluator Implementation in LangGraph

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng trực tiếp từ `G:\Agent2026Win\agents\4_langgraph\4_lab4.ipynb`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript 84 khớp trực tiếp với các cell `worker_router`, `format_conversation`, `evaluator`, `route_based_on_evaluation`, và graph builder của `4_lab4.ipynb`.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này hoàn chỉnh `worker-evaluator loop - vòng lặp worker-evaluator` trong LangGraph.
- `worker_router` kiểm tra message cuối: nếu là tool call thì route sang `tools`, nếu không thì sang `evaluator`.
- `format_conversation` chuyển message objects thành transcript text đơn giản kiểu `User:` và `Assistant:` để evaluator đọc dễ hơn.
- Node `evaluator` dùng system prompt + user prompt + `success_criteria` + conversation history + final answer để đánh giá câu trả lời mới nhất của worker.
- Evaluator output không chỉ là lời phê bình, mà còn cập nhật ba phần state: feedback text, `success_criteria_met`, và `user_input_needed`.
- `route_based_on_evaluation` quyết định: nếu đã đạt tiêu chí hoặc cần thêm input từ user thì kết thúc super-step; nếu chưa và chưa cần user, quay lại worker để thử tiếp.
- Kết quả là một graph có loop thực sự, gần hơn với `agent pattern - mẫu tác tử` của Anthropic/OpenAI hơn so với chatbot tool loop tuyến tính đơn giản.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu evaluator loop hoạt động như một control system cho worker.
  - Hiểu routing logic dựa trên state flags, không chỉ dựa trên tool calls.
  - Hiểu prompt engineering trong evaluator là phần rất thực nghiệm, không có công thức cứng.
- Practical goals - mục tiêu thực hành:
  - Có thể viết router cho worker và router cho evaluator.
  - Có thể format conversation thành input ổn định cho evaluator.
  - Có thể build graph multi-node với cả tool loop và review loop.
- What learner should be able to explain - người học cần giải thích được:
  - Worker chuyển sang evaluator ở điều kiện nào.
  - Evaluator dựa vào đâu để quyết định quay lại worker hay kết thúc.
  - Vì sao phần feedback-history trong prompt evaluator giúp giảm vòng lặp lặp lại lỗi cũ.

## 4. Previous Context - Liên hệ với bài trước
Lesson 84 là phần “runtime implementation” của lesson 83. Nếu lesson 83 mới dựng state, schema và worker prompt, thì lesson 84 biến các thành phần đó thành graph feedback loop thật sự. Nó cũng là bước nâng cấp rõ ràng từ lesson 82: thay vì agent trả output cuối ngay sau khi dùng tools xong, nay output phải đi qua một evaluator node trước khi được coi là xong việc.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: worker router - bộ định tuyến của worker
  - Meaning - nghĩa: Hàm xác định sau worker node thì graph nên đi sang tools hay sang evaluator.
  - Why it matters - vì sao quan trọng: Tách nhánh “cần thao tác thêm” khỏi nhánh “đã có câu trả lời để đánh giá”.
  - Relationship - liên hệ với khái niệm khác: Dựa vào `tool_calls` trên message cuối.
- Term - thuật ngữ: evaluator node - node đánh giá
  - Meaning - nghĩa: Node LLM dùng structured output để chấm chất lượng câu trả lời hiện tại của worker.
  - Why it matters - vì sao quan trọng: Tạo quality gate nội bộ thay vì trả output ra user ngay.
  - Relationship - liên hệ với khái niệm khác: Đọc `success_criteria`, `messages`, `feedback_on_work` từ state.
- Term - thuật ngữ: route_based_on_evaluation - định tuyến dựa trên đánh giá
  - Meaning - nghĩa: Hàm route từ evaluator sang `END` hoặc quay lại `worker`.
  - Why it matters - vì sao quan trọng: Đây là nơi feedback loop được hiện thực hóa thành control flow thật.
  - Relationship - liên hệ với khái niệm khác: Dùng flags `success_criteria_met` và `user_input_needed`.
- Term - thuật ngữ: formatted conversation context - ngữ cảnh hội thoại đã chuẩn hóa
  - Meaning - nghĩa: Chuỗi text đơn giản hóa từ message objects để evaluator dễ đọc toàn cục.
  - Why it matters - vì sao quan trọng: Giảm độ rối khi đưa full message object semantics vào evaluator prompt.
  - Relationship - liên hệ với khái niệm khác: Do utility `format_conversation` tạo ra.
- Term - thuật ngữ: feedback loop - vòng lặp phản hồi
  - Meaning - nghĩa: Quá trình worker tạo output, evaluator chấm, rồi worker sửa tiếp dựa trên feedback.
  - Why it matters - vì sao quan trọng: Là nền để agent tự hiệu chỉnh trước khi trả lời user.
  - Relationship - liên hệ với khái niệm khác: Đây là pattern trung tâm của lesson 84.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - State chứa conversation, success criteria, feedback cũ nếu có.
2. Processing steps:
   - Worker chạy.
   - `worker_router` kiểm tra message cuối.
   - Nếu có tool call: route sang tools rồi quay lại worker.
   - Nếu không có tool call: route sang evaluator.
   - Evaluator đọc conversation, success criteria, final response và feedback cũ.
   - Evaluator trả structured decision object và update state flags.
   - `route_based_on_evaluation` quyết định `END` hay quay lại worker.
3. Output:
   - Hoặc final state đủ tốt để trả về user.
   - Hoặc worker nhận feedback mới để sửa tiếp.
4. Control flow / data flow:
   - `worker -> tools -> worker` cho action loop.
   - `worker -> evaluator -> worker/END` cho review loop.
   - Feedback và flags đi qua state, không đi qua biến cục bộ tạm.
5. Decision points:
   - Message cuối có tool call hay không.
   - Success criteria đã đạt chưa.
   - Worker có đang lặp lại lỗi cũ đến mức cần hỏi lại user hay không.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Two-stage routing - định tuyến hai tầng
  - Purpose - mục đích: Tách nhánh hành động bằng tool khỏi nhánh kiểm định chất lượng.
  - When to use - dùng khi nào: Khi agent vừa cần dùng tools vừa cần self-review.
  - Trade-off - đánh đổi: Graph phức tạp hơn và có thể loop nhiều vòng.
  - Common mistake - lỗi dễ gặp: Trộn logic tool routing và evaluation routing vào cùng một if block mơ hồ.
- Technique - kỹ thuật: Repetition in evaluator prompting - lặp lại chỉ dẫn trong prompt evaluator
  - Purpose - mục đích: Tăng xác suất model hiểu đúng điều gì phải đánh giá và khi nào cần user input.
  - When to use - dùng khi nào: Khi evaluator decisions còn không ổn định.
  - Trade-off - đánh đổi: Prompt dài hơn, token nhiều hơn.
  - Common mistake - lỗi dễ gặp: Cố viết prompt ngắn quá dù behavior còn không ổn định.
- Technique - kỹ thuật: Prior-feedback carryover - mang feedback cũ sang vòng sau
  - Purpose - mục đích: Giảm việc evaluator và worker lặp lại cùng một lỗi nhiều vòng.
  - When to use - dùng khi nào: Khi workflow có thể quay lại worker nhiều lần.
  - Trade-off - đánh đổi: Prompt phức tạp hơn và cần quản lý feedback semantics rõ.
  - Common mistake - lỗi dễ gặp: Không đưa feedback cũ vào prompt, khiến loop quay vòng vô ích.

## 8. Code Walkthrough - Phân tích code nếu có
- File / block: `worker_router` trong `4_lab4.ipynb`
  - Purpose - mục đích: Xác định worker cần thực thi tools hay chuyển sang evaluation.
  - Key logic - logic chính: Dựa vào `last_message.tool_calls`.
  - Important lines / functions:
    - `def worker_router(state: State) -> str:`
    - `last_message = state["messages"][-1]`
    - `if hasattr(last_message, "tool_calls") and last_message.tool_calls:`
    - `return "tools"`
    - `return "evaluator"`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Nếu message cuối là tool call thì chưa có câu trả lời cuối để chấm.
    - Router này là cầu nối giữa action loop và review loop.
- File / block: `format_conversation` + `evaluator`
  - Purpose - mục đích: Chuẩn hóa conversation và biến evaluator thành node chấm điểm có cấu trúc.
  - Key logic - logic chính: Build system/user prompts, invoke evaluator LLM with structured output, rồi update state.
  - Important lines / functions:
    - `def format_conversation(messages: List[Any]) -> str:`
    - `def evaluator(state: State) -> State:`
    - `eval_result = evaluator_llm_with_output.invoke(evaluator_messages)`
    - `"feedback_on_work": eval_result.feedback`
    - `"success_criteria_met": eval_result.success_criteria_met`
    - `"user_input_needed": eval_result.user_input_needed`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Evaluator chỉ chấm `last_response`, nhưng vẫn nhìn toàn bộ conversation để hiểu bối cảnh.
    - Structured output làm state update dễ route hơn rất nhiều so với parse plain text.
- File / block: graph builder với worker/tools/evaluator loop
  - Purpose - mục đích: Hiện thực hóa multi-step feedback loop bằng graph edges.
  - Key logic - logic chính: Worker conditional edge sang tools/evaluator, tools quay lại worker, evaluator conditional edge sang worker/END.
  - Important lines / functions:
    - `graph_builder.add_node("worker", worker)`
    - `graph_builder.add_node("tools", ToolNode(tools=tools))`
    - `graph_builder.add_node("evaluator", evaluator)`
    - `graph_builder.add_conditional_edges("worker", worker_router, ...)`
    - `graph_builder.add_conditional_edges("evaluator", route_based_on_evaluation, ...)`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Đây là lúc graph chuyển từ one-agent tool loop sang true feedback loop pattern.
    - `END` chỉ xảy ra khi đã ổn hoặc cần user quay lại hỗ trợ.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Worker trả lời xong là kết thúc
  - Pros: Nhanh, ít token, graph đơn giản.
  - Cons: Không có internal quality control.
  - When to choose: Khi task đơn giản hoặc cost rất nhạy.
- Option: Worker + evaluator feedback loop
  - Pros: Tăng chất lượng, có cơ hội sửa sai trước khi trả user.
  - Cons: Tốn token hơn, prompt engineering khó hơn, có nguy cơ loop dài.
  - When to choose: Khi output chất lượng quan trọng hơn latency cực thấp.
- Option: Yêu cầu user đánh giá thủ công thay vì evaluator tự động
  - Pros: Độ tin cậy cao hơn ở tác vụ mơ hồ.
  - Cons: Mất tính tự động và làm user mệt.
  - When to choose: Khi domain quá khó để evaluator tự judge ổn định.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Evaluator chê cùng một lỗi nhiều lần nhưng vẫn không escalate
  - Root cause: Prompt evaluator thiếu hướng dẫn khi lỗi bị lặp lại.
  - Symptom: Worker-evaluator loop kéo dài vô ích.
  - Fix / prevention: Mang `feedback_on_work` cũ vào prompt và cho rule “nếu lặp lại thì yêu cầu user input”.
- Failure mode: Evaluator chấm toàn bộ conversation thay vì chấm response cuối
  - Root cause: Prompt không tách rõ “conversation context” và “final response under evaluation”.
  - Symptom: Decision mơ hồ hoặc đánh giá sai trọng tâm.
  - Fix / prevention: Chỉ rõ final response cần chấm dù vẫn cung cấp full context.
- Failure mode: Route logic kết thúc quá sớm hoặc không bao giờ kết thúc
  - Root cause: Flags trong state không được set/overwrite đúng.
  - Symptom: Graph dừng oan hoặc loop vô hạn.
  - Fix / prevention: Theo dõi kỹ state updates của evaluator và route function.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: `Worker-reviewer loops - vòng lặp người làm và người duyệt` là một trong những pattern cốt lõi của agentic workflows, nhất là khi cần tăng reliability mà không phải fine-tune model.
- Mở rộng: Trong production, evaluator thường cần thêm fail-safe như max iteration count, cost budget, hoặc escalation-to-human để tránh loop vô hạn.
- Mở rộng: Prompting evaluator thực chất là một bài toán đánh đổi giữa độ chính xác, độ nhất quán và chi phí; nhiều hệ thống thực tế dùng rule-based checks kết hợp evaluator LLM thay vì chỉ LLM thuần.

## 12. Study Pack - Gói ôn tập
### Must remember
- `worker_router` route sang `tools` hoặc `evaluator`.
- `format_conversation` biến message objects thành text dễ đọc cho evaluator.
- Evaluator chấm response cuối dựa trên success criteria và full context.
- Evaluator update `feedback_on_work`, `success_criteria_met`, `user_input_needed`.
- `route_based_on_evaluation` quyết định quay lại worker hay kết thúc.
- Đây là feedback loop thực sự của Day 4.

### Self-check questions
- Điều gì khiến graph đi sang `tools` thay vì `evaluator`?
- Evaluator cần thấy cả conversation history để làm gì?
- Vì sao evaluator vẫn được nhắc lại cùng một rule ở nhiều chỗ trong prompt?
- Khi nào graph kết thúc dù câu trả lời chưa đạt?
- `feedback_on_work` ảnh hưởng thế nào đến vòng lặp sau?

### Flashcards
- Q: `worker_router` kiểm tra gì?
  A: Nó kiểm tra message cuối có chứa `tool_calls` hay không.
- Q: `route_based_on_evaluation` cho ra những nhánh nào?
  A: `worker` hoặc `END`.
- Q: Khi nào `user_input_needed` nên là `True`?
  A: Khi assistant cần clarification hoặc đang mắc kẹt, không thể tiếp tục tốt nếu thiếu thêm input từ user.

### Interview Q&A nếu phù hợp
- Q: Tại sao feedback loop giúp agent đáng tin hơn?
  A: Vì nó thêm một bước kiểm định nội bộ, cho phép sửa sai trước khi user thấy output cuối.
- Q: Rủi ro lớn nhất của worker-evaluator pattern là gì?
  A: Loop kéo dài hoặc tự lặp vô ích nếu prompts và stopping conditions không được thiết kế kỹ.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide cho lesson này.
- Không có max-iteration guard hay benchmark loop-length trong nguồn được cung cấp.
- Chưa cần scan thêm file/folder khác vì transcript và notebook đã đủ trực tiếp.

# 85. Day 4 - Building an AI Sidekick Using LangGraph, Gradio & Browser Automation

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng trực tiếp từ `G:\Agent2026Win\agents\4_langgraph\4_lab4.ipynb`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript 85 khớp trực tiếp với phần Gradio UI và callback logic của `4_lab4.ipynb`, cộng với diễn giải trace LangSmith của lần chạy sidekick.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson 85 đóng gói worker-evaluator graph thành ứng dụng `Sidekick - trợ lý đồng nghiệp cá nhân` với Gradio UI.
- Mỗi phiên Gradio được gán `thread_id` ngẫu nhiên để tách memory giữa các người dùng hoặc các lần mở app khác nhau.
- Callback `process_message` tạo `config` từ thread, dựng initial state từ `message` và `success_criteria`, rồi gọi `await graph.ainvoke(...)`.
- UI hiển thị không chỉ câu trả lời của worker mà còn cả `Evaluator Feedback`, giúp người học nhìn thấy feedback loop ngay trên giao diện.
- Transcript thừa nhận có một điểm chưa thật elegant: app đang kết hợp `Gradio history` với memory của LangGraph, thay vì render lại toàn bộ history trực tiếp từ graph state.
- Demo sidekick dùng browser để tra tỷ giá USD/GBP, rồi evaluator xác nhận/nhận xét mức độ đáp ứng success criteria.
- LangSmith trace cho thấy đầy đủ chuỗi `worker -> tools -> evaluator`, minh họa đây không còn là demo chatbot đơn giản mà là agentic app có browser automation và kiểm tra chất lượng nội bộ.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách bọc graph thành một ứng dụng UI dùng được.
  - Hiểu vai trò của `thread_id` trong multi-session isolation.
  - Hiểu ranh giới và chỗ “chưa đẹp” giữa frontend history và graph memory.
- Practical goals - mục tiêu thực hành:
  - Có thể viết callback nhận user input và success criteria rồi invoke graph.
  - Có thể hiển thị cả worker response lẫn evaluator feedback trong UI.
  - Có thể reset session và tạo thread mới cho user mới.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao mỗi Gradio session cần thread riêng.
  - `process_message` chuyển dữ liệu UI thành graph state như thế nào.
  - Vì sao app hiện tại hoạt động được dù phần history rendering chưa phải thiết kế tối ưu nhất.

## 4. Previous Context - Liên hệ với bài trước
Lesson 85 là lớp ứng dụng hóa của lesson 83-84. Nếu lesson 84 hoàn thành feedback loop trong graph, thì lesson 85 gắn graph đó vào một Gradio app có session isolation và demo thực tế. Nó cũng kéo dài bài học từ Day 3 về `thread_id` và checkpointing: memory không chỉ là khái niệm backend nữa, mà trở thành cách phân tách conversation giữa nhiều người dùng UI.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: thread_id - định danh luồng hội thoại
  - Meaning - nghĩa: Khóa logic để checkpointer biết state nào thuộc về phiên nào.
  - Why it matters - vì sao quan trọng: Cho phép nhiều session độc lập cùng chạy sidekick mà không lẫn memory.
  - Relationship - liên hệ với khái niệm khác: Nằm trong `configurable.thread_id` khi invoke graph.
- Term - thuật ngữ: process_message - callback xử lý tin nhắn
  - Meaning - nghĩa: Hàm trung gian giữa UI và graph runtime.
  - Why it matters - vì sao quan trọng: Đây là điểm biến user interaction thành graph state invocation thực tế.
  - Relationship - liên hệ với khái niệm khác: Dùng `graph.ainvoke(state, config=config)`.
- Term - thuật ngữ: session isolation - cô lập phiên
  - Meaning - nghĩa: Mỗi người dùng hoặc mỗi lần mở app có memory và checkpoints riêng.
  - Why it matters - vì sao quan trọng: Tránh contamination giữa conversations.
  - Relationship - liên hệ với khái niệm khác: Được hiện thực bằng `make_thread_id()` và Gradio `State`.
- Term - thuật ngữ: UI-visible evaluator feedback - phản hồi evaluator hiển thị trên giao diện
  - Meaning - nghĩa: Quyết định hiển thị cả feedback review, không chỉ answer cuối.
  - Why it matters - vì sao quan trọng: Tăng tính minh bạch khi học workflow agentic.
  - Relationship - liên hệ với khái niệm khác: Lấy `result["messages"][-2]` và `result["messages"][-1]` để render.
- Term - thuật ngữ: frontend history vs graph memory - lịch sử frontend so với bộ nhớ graph
  - Meaning - nghĩa: Hai nguồn “history” khác nhau, một để render UI và một để duy trì runtime state.
  - Why it matters - vì sao quan trọng: Nếu trộn chúng không cẩn thận thì app vẫn chạy nhưng kiến trúc chưa sạch.
  - Relationship - liên hệ với khái niệm khác: Instructor thừa nhận đây là phần có thể làm elegant hơn sau.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - User request.
   - Success criteria từ user.
   - Thread id của session hiện tại.
2. Processing steps:
   - `make_thread_id()` tạo UUID cho session mới.
   - `process_message(...)` tạo `config = {"configurable": {"thread_id": thread}}`.
   - Callback dựng initial state với message, success criteria và các flags mặc định.
   - `await graph.ainvoke(state, config=config)` chạy whole graph super-step.
   - Callback rút assistant reply và evaluator feedback từ state trả về.
   - Ghép chúng vào Gradio history để render ra UI.
   - `reset()` xóa UI fields và sinh thread mới.
3. Output:
   - Sidekick UI hiển thị user message, assistant answer, evaluator feedback.
4. Control flow / data flow:
   - UI input -> callback -> graph state -> worker/tools/evaluator -> result state -> UI history render.
   - Thread id đi cùng config để checkpointer tách session memories.
5. Decision points:
   - Có hiển thị evaluator feedback cho user hay không.
   - Có dùng state làm source of truth duy nhất cho UI history hay không.
   - Khi reset thì có giữ thread cũ hay tạo thread mới.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Session-scoped thread ids - thread theo phạm vi phiên
  - Purpose - mục đích: Cô lập memory giữa các user sessions.
  - When to use - dùng khi nào: Với mọi stateful LangGraph app có nhiều người dùng hoặc nhiều cuộc hội thoại.
  - Trade-off - đánh đổi: Cần quản lý identity/session mapping rõ nếu app lớn hơn.
  - Common mistake - lỗi dễ gặp: Dùng một thread chung cho mọi session rồi memory bị lẫn.
- Technique - kỹ thuật: UI transparency bằng evaluator feedback
  - Purpose - mục đích: Giúp người học thấy feedback loop thay vì chỉ thấy câu trả lời cuối.
  - When to use - dùng khi nào: Demos, debug, teaching, agent observability.
  - Trade-off - đánh đổi: UI có thể ồn hơn với end user thông thường.
  - Common mistake - lỗi dễ gặp: Ẩn toàn bộ feedback rồi khó hiểu tại sao graph dừng hay retry.
- Technique - kỹ thuật: Thin callback over graph runtime - callback mỏng phủ lên graph
  - Purpose - mục đích: Giữ business orchestration trong graph, không nhét vào UI code.
  - When to use - dùng khi nào: Khi muốn app dễ mở rộng và dễ debug.
  - Trade-off - đánh đổi: UI vẫn cần hiểu một chút cấu trúc result state để render đúng.
  - Common mistake - lỗi dễ gặp: Cho callback tự quản lý business state song song với graph state.

## 8. Code Walkthrough - Phân tích code nếu có
- File / block: `make_thread_id` và `process_message` trong `4_lab4.ipynb`
  - Purpose - mục đích: Tạo session-isolated graph invocations từ UI.
  - Key logic - logic chính: Sinh UUID, dựng config, dựng initial state, invoke graph, bóc result để render.
  - Important lines / functions:
    - `def make_thread_id() -> str:`
    - `config = {"configurable": {"thread_id": thread}}`
    - `state = {...}`
    - `result = await graph.ainvoke(state, config=config)`
    - `reply = {"role": "assistant", "content": result["messages"][-2].content}`
    - `feedback = {"role": "assistant", "content": result["messages"][-1].content}`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - `thread_id` là chìa khóa để memory không “dây sang” các lần mở app khác.
    - Callback giả định hai message cuối lần lượt là worker answer và evaluator feedback.
- File / block: Gradio UI layout cho Sidekick
  - Purpose - mục đích: Tạo giao diện nhập request và success criteria cho graph.
  - Key logic - logic chính: Dùng `gr.Blocks`, `gr.Chatbot`, hai `Textbox`, nút `Go!` và `Reset`.
  - Important lines / functions:
    - `with gr.Blocks(theme=gr.themes.Default(primary_hue="emerald")) as demo:`
    - `thread = gr.State(make_thread_id())`
    - `chatbot = gr.Chatbot(label="Sidekick", height=300, type="messages")`
    - `go_button.click(process_message, ...)`
    - `reset_button.click(reset, [], [message, success_criteria, chatbot, thread])`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Success criteria được lấy trực tiếp từ UI, không hard-code trong backend.
    - `gr.State` giữ thread hiện tại cho phiên frontend đó.
- File / block: reset flow và phần “chưa elegant”
  - Purpose - mục đích: Quản lý session lifecycle cơ bản.
  - Key logic - logic chính: `reset()` trả về textbox rỗng, chatbot rỗng và thread mới; transcript cũng thừa nhận history hiện được ghép nửa từ UI, nửa từ graph.
  - Important lines / functions:
    - `async def reset():`
    - `return "", "", None, make_thread_id()`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Reset không chỉ xóa UI mà còn đổi thread để graph memory bắt đầu sạch.
    - Đây là chỗ app đang ưu tiên đơn giản hóa demo hơn là purity kiến trúc.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Hiển thị cả evaluator feedback trong UI
  - Pros: Minh bạch, hữu ích cho học tập và debug.
  - Cons: Có thể nhiều thông tin với user phổ thông.
  - When to choose: Demos, internal tools, prototyping.
- Option: Chỉ hiển thị answer cuối
  - Pros: UI gọn hơn, giống sản phẩm tiêu dùng hơn.
  - Cons: Mất khả năng quan sát feedback loop.
  - When to choose: Khi muốn UX đơn giản cho end user.
- Option: Render history từ Gradio + graph pha trộn
  - Pros: Code nhanh, dễ dựng demo.
  - Cons: Kiến trúc chưa sạch và có khả năng lệch lịch sử.
  - When to choose: MVP hoặc tutorial nhanh.
- Option: Render history hoàn toàn từ graph state
  - Pros: Đồng nhất source of truth.
  - Cons: Cần code kỹ hơn để unpack history từ checkpoints/state.
  - When to choose: Khi muốn app production-like hơn.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Mọi user dùng chung một thread id
  - Root cause: Không gắn thread theo session UI.
  - Symptom: Sidekick nhớ nhầm dữ liệu của user khác.
  - Fix / prevention: Sinh thread mới cho mỗi session hoặc mỗi conversation logical.
- Failure mode: UI history và graph memory lệch nhau
  - Root cause: Trộn hai nguồn state mà không có source of truth rõ.
  - Symptom: UI hiển thị khác những gì graph thực sự đang nhớ.
  - Fix / prevention: Dần chuyển sang render history từ graph state hoặc checkpoint snapshots.
- Failure mode: Giả định quá cứng về vị trí messages cuối
  - Root cause: Callback tin chắc `[-2]` là worker reply và `[-1]` là evaluator feedback.
  - Symptom: Nếu graph shape đổi, UI render sai.
  - Fix / prevention: Chuẩn hóa output contract hoặc tag messages rõ hơn.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: `Session isolation - cô lập phiên` là một yêu cầu bắt buộc khi đưa stateful agents lên web apps; nếu không làm tốt, bug memory contamination sẽ rất khó phát hiện và rất nguy hiểm.
- Mở rộng: Khi app lớn hơn, phần callback/UI thường nên mỏng dần và chuyển sang API/backend layer riêng, còn Gradio hoặc frontend chỉ gọi backend đó.
- Mở rộng: Việc hiển thị evaluator feedback trực tiếp là một dạng lightweight observability cho user; trong sản phẩm thật có thể chuyển nó thành debug mode thay vì luôn hiển thị.

## 12. Study Pack - Gói ôn tập
### Must remember
- Lesson 85 đóng gói graph thành app Sidekick bằng Gradio.
- Mỗi session dùng thread id riêng để tách memory.
- `process_message` biến UI inputs thành initial graph state.
- App hiển thị cả worker answer lẫn evaluator feedback.
- `reset()` xóa UI và tạo thread mới.
- Transcript thừa nhận phần history hiện tại là demo-friendly hơn là kiến trúc tối ưu.

### Self-check questions
- Vì sao mỗi session cần thread riêng?
- `process_message` lấy những gì từ UI để tạo state?
- Vì sao reset phải sinh thread mới?
- Hạn chế chính của cách render history hiện tại là gì?
- Khi nào nên ẩn evaluator feedback khỏi UI?

### Flashcards
- Q: `thread_id` trong lesson 85 dùng để làm gì?
  A: Để gắn memory/checkpoints của graph với đúng session conversation.
- Q: `process_message` trả gì cho UI?
  A: Lịch sử chat mới có user message, worker reply và evaluator feedback.
- Q: Vì sao lesson này vẫn nói phần history chưa thật elegant?
  A: Vì nó đang pha trộn Gradio history với memory của LangGraph thay vì dùng một source of truth duy nhất.

### Interview Q&A nếu phù hợp
- Q: Làm sao bạn tránh lẫn memory giữa nhiều người dùng trong một agent web app?
  A: Tôi sẽ gắn mỗi session hoặc conversation với một `thread_id` riêng và bảo đảm backend memory/checkpointing luôn key theo id đó.
- Q: Khi nào nên render history từ graph state thay vì từ frontend state?
  A: Khi muốn tính nhất quán cao hơn, đặc biệt với stateful/multi-step agents có nhiều message nội bộ và checkpoint semantics phức tạp.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide Day 4 cho lesson này.
- Không có file app/module tách riêng ngoài notebook để so sánh cách đóng gói production hơn.
- Chưa cần scan thêm file/folder khác vì transcript và notebook đã đủ để tổng hợp lesson này.
