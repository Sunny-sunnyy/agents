# Day 3 - Multi-Model Integration, Structured Outputs, and Guardrails in Agent SDK

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

---

# 40. Day 3- Multi-Model Integration - Using Gemini, DeepSeek & Groq with OpenAI Agents

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([3_lab3.ipynb](file:///G:/Agent2026Win/agents/3_lab3.ipynb#L19-L262))
- Summary lịch sử: đã dùng ([day1_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day1_summary.md), [day2_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day2_summary.md) - bối cảnh về hệ thống phân cấp SDR)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học thực hành tích hợp các mô hình ngôn ngữ lớn từ Google, DeepSeek và Groq sử dụng cơ chế tương thích API OpenAI.

> [!IMPORTANT]
> Để chạy tích hợp đa mô hình trong bài học này, bạn cần có các API Keys tương ứng khai báo trong file `.env` (ví dụ `GOOGLE_API_KEY`, `DEEPSEEK_API_KEY`, `GROQ_API_KEY`). Nếu thiếu một trong số các key này, bạn hoàn toàn có thể tạm thời cấu hình quay về `"gpt-4o-mini"` (chuỗi ký tự mặc định) cho Agent đó để tiếp tục thực hành chạy thử nghiệm.

## 2. Executive Summary - Tóm tắt cốt lõi
- Hướng dẫn tích hợp các mô hình ngôn ngữ lớn từ nhiều nhà cung cấp khác nhau (Gemini, DeepSeek, Groq Llama 3.3) vào OpenAI Agents SDK.
- Sử dụng cơ chế tương thích API OpenAI (OpenAI-compatible endpoints) của các nhà cung cấp thông qua thư viện `AsyncOpenAI`.
- Đóng gói các client bất đồng bộ tùy chỉnh này thành đối tượng mô hình bằng lớp `OpenAIChatCompletionsModel`.
- Khởi tạo 3 Agent viết thư nháp chạy 3 mô hình khác nhau của các hãng.
- Tích hợp các Agent đa mô hình này làm công cụ cho Planning Agent `Sales Manager` chạy mô hình mặc định `gpt-4o-mini`.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cơ chế hoạt động của các API tương thích OpenAI (OpenAI-compatible API).
  - Nắm được cách OpenAI Agents SDK hỗ trợ đa mô hình thông qua Custom Clients.
- Practical goals - mục tiêu thực hành:
  - Khai báo các API keys và base URLs tương ứng cho từng hãng trong code Python.
  - Sử dụng `AsyncOpenAI` để khởi tạo custom clients.
  - Tạo các đối tượng model qua `OpenAIChatCompletionsModel` và gán chúng vào tham số `model` của Agent.
- What learner should be able to explain - người học cần giải thích được:
  - Khác biệt khi truyền tham số `model` cho Agent dưới dạng chuỗi ký tự (string) so với truyền dạng đối tượng mô hình (`OpenAIChatCompletionsModel`) là gì?
  - Tại sao OpenAI Agents SDK lại có thể gọi được mô hình của Google hay DeepSeek?

## 4. Previous Context - Liên hệ với bài trước
Phát triển trực tiếp từ cấu trúc hệ thống phân cấp (Hierarchical System) và Automated SDR ở Day 2, nâng cấp 3 agent viết email nháp từ việc dùng chung mô hình OpenAI sang sử dụng 3 mô hình độc lập của Google, DeepSeek và Groq.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: OpenAI-compatible Endpoints - Điểm cuối tương thích OpenAI
  - Meaning - nghĩa: Các địa chỉ API do bên thứ ba cung cấp được thiết kế với cấu trúc đường dẫn, tham số đầu vào và định dạng đầu ra giống hệt với API chuẩn của OpenAI.
  - Why it matters - vì sao quan trọng: Cho phép nhà phát triển sử dụng chính thư viện client của OpenAI (như `openai-python`) để tương tác với các mô hình khác mà không cần cài đặt thêm thư viện riêng biệt của từng hãng.
  - Relationship - liên hệ với khái niệm khác: Google Gemini, DeepSeek và Groq đều cung cấp các endpoint tương thích này để thu hút các nhà phát triển.
- Term - thuật ngữ: OpenAIChatCompletionsModel
  - Meaning - nghĩa: Lớp bọc mô hình trong OpenAI Agents SDK dùng để liên kết tên mô hình cụ thể với một thực thể client chỉ định.
  - Why it matters - vì sao quan trọng: Là khối xây dựng cho phép Agent chạy trên các Custom Clients trỏ tới các Base URLs tùy chỉnh thay vì trỏ về OpenAI mặc định.
  - Relationship - liên hệ với khái niệm khác: Nhận đối số `openai_client` là một thực thể của `AsyncOpenAI`.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình tích hợp và thực thi đa mô hình:
1. Input: API Keys, Base URLs của các nhà cung cấp, yêu cầu viết email nháp của người dùng.
2. Processing steps:
   - Bước 1: Khai báo các Base URLs tương thích OpenAI cho Gemini, DeepSeek và Groq.
   - Bước 2: Khởi tạo các client bất đồng bộ `AsyncOpenAI` tương ứng với API Key và Base URL.
   - Bước 3: Định nghĩa các thực thể `OpenAIChatCompletionsModel` bằng cách truyền tên model và client tương ứng.
   - Bước 4: Khởi tạo 3 Agent viết email nháp (`sales_agent1`, `2`, `3`) và gán các đối tượng model vừa tạo vào tham số `model`.
   - Bước 5: Đóng gói các Agent này thành tool và truyền cho `Sales Manager` điều phối chạy.
3. Output: Email nháp được sinh ra từ các mô hình khác nhau và gửi đi.
4. Control flow / data flow: Phân cấp (Sales Manager quản lý gọi các tool đa mô hình).
5. Decision points: Sales Manager đánh giá và chọn email tốt nhất dựa trên mô hình chạy mặc định của nó (`gpt-4o-mini`).

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Khởi tạo Custom Client bằng `AsyncOpenAI`
  - Purpose - mục đích: Trỏ đường dẫn API của thư viện OpenAI sang các máy chủ của hãng khác (Google, DeepSeek, Groq) để gọi mô hình của họ.
  - When to use - dùng khi nào: Khi cần sử dụng đa dạng các mô hình ngôn ngữ trong hệ thống Agent để tối ưu chi phí (như DeepSeek) hoặc tốc độ (như Groq).
  - Trade-off - đánh đổi: Tốn thêm thời gian thiết lập client thủ công thay vì để SDK tự động cấu hình mặc định.
  - Common mistake - lỗi dễ gặp: Viết sai Base URL (ví dụ thiếu ký tự gạch chéo cuối `/` hoặc cấu trúc `/v1` tùy theo yêu cầu của từng endpoint).

## 8. Code Walkthrough - Phân tích code nếu có
### File: [3_lab3.ipynb](file:///G:/Agent2026Win/agents/3_lab3.ipynb#L107-L137)
- Purpose - mục đích: Thiết lập các client tương thích OpenAI và khởi tạo các Agent chạy trên đa mô hình.
- Key logic:
  - Khai báo 3 Base URL tương thích OpenAI của Google, DeepSeek và Groq.
  - Khởi tạo client bất đồng bộ `AsyncOpenAI` cho từng hãng.
  - Định nghĩa các đối tượng model qua `OpenAIChatCompletionsModel` và truyền vào Agent.
- Important lines / functions:
  - Dòng 107-109:
    ```python
    GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
    DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
    GROQ_BASE_URL = "https://api.groq.com/openai/v1"
    ```
    - Ý nghĩa: Khai báo địa chỉ API tương thích của các nhà cung cấp.
  - Dòng 123-125:
    ```python
    deepseek_model = OpenAIChatCompletionsModel(model="deepseek-chat", openai_client=deepseek_client)
    gemini_model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=gemini_client)
    llama3_3_model = OpenAIChatCompletionsModel(model="llama-3.3-70b-versatile", openai_client=groq_client)
    ```
    - Ý nghĩa: Định nghĩa thực thể model liên kết model name và client cụ thể.
  - Dòng 134-136:
    ```python
    sales_agent1 = Agent(name="DeepSeek Sales Agent", instructions=instructions1, model=deepseek_model)
    ```
    - Ý nghĩa: Khởi tạo Agent sử dụng đối tượng model tùy chỉnh thay vì chuỗi ký tự mặc định.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Không áp dụng.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Ném ra lỗi `AuthenticationError` hoặc `APIConnectionError` ngay khi chạy Agent đa mô hình.
- Root cause: Quên cấu hình API Key tương ứng trong file `.env` hoặc truyền sai Base URL của nhà cung cấp.
- Fix / prevention: [Alert] Kiểm tra sự tồn tại của các API keys (`GOOGLE_API_KEY`, `DEEPSEEK_API_KEY`, `GROQ_API_KEY`) trong `.env`. Nếu thiếu key, có thể gán `model="gpt-4o-mini"` cho Agent đó để tiếp tục thực hành bình thường.

## 11. Knowledge Extension - Kiến thức mở rộng
Không có.

## 12. Study Pack - Gói ôn tập
### Must remember
1. OpenAI Agents SDK có thể điều phối mô hình của hãng khác nếu chúng hỗ trợ API tương thích OpenAI.
2. Khai báo client tùy chỉnh thông qua lớp `AsyncOpenAI` với `base_url` và `api_key` tương ứng.
3. Đối tượng `OpenAIChatCompletionsModel` dùng để bọc model name và custom client.
4. Gán thực thể `OpenAIChatCompletionsModel` vào tham số `model` khi khởi tạo Agent.
5. Việc chạy đa mô hình giúp tận dụng thế mạnh chuyên biệt của từng LLM (DeepSeek giá rẻ, Groq siêu nhanh, Gemini phân tích tốt).

### Self-check questions
1. Làm thế nào để khai báo một Agent chạy mô hình của DeepSeek trong OpenAI Agents SDK?
2. Base URL tương thích OpenAI của Google Gemini là gì?

### Flashcards
- Q: Lớp nào trong SDK dùng để bọc custom client và model name cho Agent?
  A: Lớp `OpenAIChatCompletionsModel`.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 41. Day 3 - Implementing Guardrails & Structured Outputs for Robust AI Agent Systems

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([3_lab3.ipynb](file:///G:/Agent2026Win/agents/3_lab3.ipynb#L279-L302))
- Summary lịch sử: đã dùng ([day2_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day2_summary.md) - lỗi vòng lặp của SDR ở bài 38)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học giới thiệu phương pháp thiết lập đầu ra cấu trúc Pydantic và Input Guardrails để bảo mật hệ thống.

## 2. Executive Summary - Tóm tắt cốt lõi
- Phân tích sự mất ổn định cố hữu (inherent instability) của Agent tự trị khi instructions cho phép gọi lại công cụ nhiều lần (gây ra vòng lặp vô hạn tốn hơn 300 giây và gọi 14 tools trên trace thực tế).
- Giới thiệu giải pháp **Structured Outputs** (Đầu ra có cấu trúc) sử dụng thư viện `pydantic` để ép buộc Agent phản hồi theo một schema đối tượng Python cụ thể thay vì dạng text tự do.
- Giới thiệu giải pháp **Guardrails** (Thanh chắn an toàn) để lọc thông tin đầu vào (input guardrails) hoặc đầu ra (output guardrails).
- Hướng dẫn viết một Input Guardrail: bọc hàm bất đồng bộ bằng `@input_guardrail` decorator và trả về đối tượng `GuardrailFunctionOutput` chứa trạng thái sập bẫy `tripwire_triggered`.
- Giải thích nguyên nhân mô hình Claude của Anthropic không thể tích hợp trực tiếp (do không cung cấp OpenAI-compatible API) và hướng dẫn giải pháp dùng Open Router.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cơ chế hoạt động của Structured Outputs và cách Pydantic định nghĩa schema cho LLM.
  - Hiểu nguyên lý hoạt động của cơ chế Guardrails và bẫy dây (tripwire).
  - Nắm được rủi ro vòng lặp vô hạn của Agent tự trị và tầm quan trọng của việc kiểm soát an toàn.
- Practical goals - mục tiêu thực hành:
  - Định nghĩa thành công một Pydantic `BaseModel` để quy định kiểu dữ liệu đầu ra của Agent.
  - Viết hàm Input Guardrail sử dụng decorator `@input_guardrail` và trả về `GuardrailFunctionOutput`.
  - Khai báo tham số `output_type` cho Agent.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao nói Structured Outputs giúp việc lập trình với Agent trở nên chặt chẽ và an toàn hơn?
  - Cơ chế hoạt động của `tripwire_triggered` trong Guardrail là gì?

## 4. Previous Context - Liên hệ với bài trước
Nối tiếp sự cố Sales Manager ở Bài 38 (Day 2) bị lặp lại cuộc gọi tool nhiều lần, cung cấp giải pháp bảo mật đầu vào và đầu ra để hệ thống chạy ổn định và tin cậy.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Structured Outputs - Đầu ra có cấu trúc
  - Meaning - nghĩa: Cơ chế bắt buộc LLM phải trả về kết quả tuân thủ nghiêm ngặt theo một cấu trúc dữ liệu JSON được định nghĩa trước (ở đây định nghĩa qua Pydantic).
  - Why it matters - vì sao quan trọng: Giúp việc lập trình an toàn hơn vì đầu ra của Agent được tự động parse thành một đối tượng Python có thuộc tính rõ ràng, loại bỏ hoàn toàn việc parse text thủ công bằng regex dễ sinh lỗi.
  - Relationship - liên hệ với khái niệm khác: Được kích hoạt bằng cách khai báo tham số `output_type` khi khởi tạo Agent.
- Term - thuật ngữ: Tripwire - Bẫy dây / Thanh chắn
  - Meaning - nghĩa: Một cờ hiệu boolean nằm trong đối tượng trả về của hàm guardrail; nếu mang giá trị `True`, nó báo hiệu dữ liệu vi phạm an toàn.
  - Why it matters - vì sao quan trọng: Khi bẫy dây sập (`tripwire_triggered=True`), hệ thống sẽ lập tức dừng thực thi Agent chính và ném ra exception để bảo vệ.
  - Relationship - liên hệ với khái niệm khác: Được khai báo bên trong đối tượng `GuardrailFunctionOutput`.
- Term - thuật ngữ: Input/Output Guardrails - Thanh chắn đầu vào/đầu ra
  - Meaning - nghĩa: Các bộ lọc kiểm duyệt dữ liệu an toàn chỉ có thể áp dụng tại thời điểm bắt đầu nhận prompt của người dùng hoặc thời điểm kết thúc trả kết quả của toàn bộ luồng chạy.
  - Why it matters - vì sao quan trọng: Là chốt chặn an toàn bảo vệ hệ thống AI khỏi mã độc, prompt injection hoặc rò rỉ thông tin nhạy cảm.
  - Relationship - liên hệ với khái niệm khác: Được bọc bằng decorator `@input_guardrail` hoặc `@output_guardrail`.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình thực thi của Input Guardrail:
1. Input: Tin nhắn (prompt) của người dùng gửi vào Agent chính.
2. Processing steps:
   - Bước 1: SDK chạy hàm guardrail được đăng ký trong danh sách `input_guardrails` trước khi gọi Agent chính.
   - Bước 2: Hàm guardrail chạy một `guardrail_agent` chuyên trách để kiểm tra tin nhắn.
   - Bước 3: `guardrail_agent` trả về kết quả có cấu trúc Pydantic (`NameCheckOutput`) chứa cờ `is_name_in_message`.
   - Bước 4: Hàm guardrail kiểm tra thuộc tính này; nếu là `True`, trả về `GuardrailFunctionOutput(..., tripwire_triggered=True)`.
   - Bước 5: SDK nhận diện bẫy dây đã sập, lập tức chặn đứng chương trình và ném ra Exception.
3. Output: Một Exception dừng chương trình (nếu vi phạm) hoặc cho phép tiếp tục gọi LLM của Agent chính (nếu an toàn).
4. Control flow / data flow: Kiểm duyệt tuần tự trước khi thực thi chính.
5. Decision points: Hàm guardrail quyết định chặn hay cho qua dựa trên thuộc tính của Pydantic object trả về từ guardrail agent.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Ép kiểu đầu ra cho Agent bằng `output_type`
  - Purpose - mục đích: Buộc LLM trả về đối tượng dữ liệu có cấu trúc thay vì chuỗi văn bản tự do.
  - When to use - dùng khi nào: Khi Agent thực hiện các nhiệm vụ trích xuất thực thể, phân loại, chấm điểm hoặc kiểm tra an toàn.
  - Trade-off - đánh đổi: LLM phải hỗ trợ Structured Outputs và có thể tiêu tốn thêm thời gian suy luận để định dạng JSON.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [3_lab3.ipynb](file:///G:/Agent2026Win/agents/3_lab3.ipynb#L279-L302)
- Purpose - mục đích: Định nghĩa cấu trúc Pydantic và thiết lập hàm Input Guardrail kiểm tra tên người dùng.
- Key logic:
  - Định nghĩa lớp `NameCheckOutput` kế thừa `BaseModel`.
  - Khởi tạo `guardrail_agent` có `output_type=NameCheckOutput`.
  - Viết hàm `guardrail_against_name` bọc decorator `@input_guardrail`.
- Important lines / functions:
  - Dòng 279: `class NameCheckOutput(BaseModel):`
    - Ý nghĩa: Định nghĩa schema đầu ra gồm hai thuộc tính `is_name_in_message` (bool) và `name` (str).
  - Dòng 286: `output_type=NameCheckOutput`
    - Ý nghĩa: Ép buộc `guardrail_agent` trả về kiểu dữ liệu có cấu trúc.
  - Dòng 297: `@input_guardrail`
    - Ý nghĩa: Decorator đăng ký hàm Python làm Input Guardrail.
  - Dòng 298: `async def guardrail_against_name(ctx, agent, message):`
    - Ý nghĩa: Khai báo hàm guardrail bất đồng bộ nhận 3 tham số bắt buộc.
  - Dòng 301:
    ```python
    return GuardrailFunctionOutput(output_info={"found_name": result.final_output}, tripwire_triggered=is_name_in_message)
    ```
    - Ghi chú: Trả về đối tượng `GuardrailFunctionOutput` của SDK, gán thuộc tính `tripwire_triggered` bằng giá trị boolean nhận diện vi phạm.

## 9. Options / Trade-offs - Bản đồ lựa chọn
So sánh các giải pháp tích hợp Anthropic's Claude vào OpenAI Agents SDK:
- Option: Không tích hợp Claude, sử dụng các mô hình tương thích mặc định (Gemini, DeepSeek, Groq)
  - Pros: Rất đơn giản, không cần cấu hình bên thứ ba, chạy trực tiếp qua client của OpenAI.
  - Cons: Không tận dụng được trí tuệ của Claude 3.5 Sonnet.
  - When to choose: Các bài thực hành cơ bản hoặc khi dự án không yêu cầu cụ thể về Claude.
- Option: Tích hợp Claude qua Open Router (Recommended)
  - Pros: Cho phép gọi Claude bằng chính thư viện `AsyncOpenAI` thông qua endpoint tương thích của Open Router, giữ nguyên cấu trúc code SDK.
  - Cons: Phải đăng ký tài khoản Open Router và nạp phí sử dụng.
  - When to choose: Khi dự án bắt buộc phải dùng mô hình Claude.

## 10. Pitfalls - Lỗi / bẫy thường gặp
Không áp dụng cho phần lý thuyết khai báo này.

## 11. Knowledge Extension - Kiến thức mở rộng
- *Giải pháp code mẫu tích hợp Claude qua Open Router*:
  - Cài đặt thư viện và cấu hình client:
    ```python
    from openai import AsyncOpenAI
    from agents import OpenAIChatCompletionsModel, Agent

    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    openrouter_key = "your_openrouter_api_key"

    openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=openrouter_key)
    claude_model = OpenAIChatCompletionsModel(model="anthropic/claude-3.5-sonnet", openai_client=openrouter_client)

    claude_agent = Agent(name="Claude Agent", instructions="You are a helpful assistant.", model=claude_model)
    ```

## 12. Study Pack - Gói ôn tập
### Must remember
1. Sử dụng Pydantic `BaseModel` và tham số `output_type` để ép buộc Agent trả về dữ liệu có cấu trúc.
2. Dữ liệu Structured Outputs được truy cập trực tiếp qua thuộc tính `result.final_output.thuộc_tính`.
3. Hàm Guardrail được đăng ký bằng `@input_guardrail` hoặc `@output_guardrail`.
4. Hàm Guardrail bắt buộc phải trả về đối tượng thực thể của lớp `GuardrailFunctionOutput`.
5. Đặt thuộc tính `tripwire_triggered=True` để lập tức chặn đứng Agent chính và ném ra Exception bảo vệ.

### Self-check questions
1. Tại sao OpenAI SDK không thể gọi trực tiếp API của Anthropic Claude qua `AsyncOpenAI` client thông thường?
2. Sự khác biệt giữa `GuardrailFunctionOutput` khi `tripwire_triggered` bằng `True` và `False` là gì?

### Flashcards
- Q: Thuộc tính nào của Agent dùng để quy định định dạng đầu ra có cấu trúc Pydantic?
  A: Tham số `output_type`.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 42. Day 3- AI Safety in Practice - Implementing Guardrails for LLM Agent Applications

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([3_lab3.ipynb](file:///G:/Agent2026Win/agents/3_lab3.ipynb#L310-L346))
- Summary lịch sử: đã dùng ([day2_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day2_summary.md) - cấu hình Sales Manager)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học thực hành tích hợp guardrail bảo vệ Planning Agent và kiểm chứng hành vi sập bẫy an toàn.

## 2. Executive Summary - Tóm tắt cốt lõi
- Tích hợp hàm guardrail `guardrail_against_name` vào Planning Agent để tạo ra `careful_sales_manager` có cơ chế bảo mật.
- Thực chứng kịch bản sập bẫy: Khi người dùng truyền tin nhắn chứa tên riêng ("Alice"), guardrail lập tức phát hiện, kích hoạt tripwire và ném ra exception dừng luồng chạy mà không gọi các agent viết email nháp.
- Phân tích ý nghĩa thương mại của Guardrails trong việc bảo vệ dữ liệu nhạy cảm PII (Personal Identifiable Information) như tên riêng, số điện thoại hoặc thông tin bảo mật của CEO khỏi việc bị rò rỉ ra các email chào hàng lạnh.
- Thực chứng kịch bản an toàn: Khi tin nhắn không chứa tên riêng, guardrail cho qua bình thường và email được sinh ra thành công.
- Giới thiệu các hướng mở rộng dự án: Thiết kế thêm output guardrails, thử nghiệm đa mô hình và sử dụng Structured Outputs để sinh nội dung email chuyên nghiệp.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu tầm quan trọng của Guardrails trong việc bảo vệ dữ liệu PII và an toàn thông tin doanh nghiệp thực tế.
  - Hiểu cách thức biểu diễn một guardrail bị lỗi trên giao diện OpenAI Platform Traces.
- Practical goals - mục tiêu thực hành:
  - Đăng ký bộ lọc vào tham số `input_guardrails` khi khởi tạo Agent.
  - Xử lý ngoại lệ (exception handling) trong Python khi chạy Agent có guardrail để tránh sập chương trình.
  - Chạy thử nghiệm thành công 2 kịch bản vi phạm an toàn và an toàn.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao Guardrail lại là chốt chặn bảo mật tin cậy hơn việc chỉ viết câu lệnh cấm trong system prompt của Agent?
  - Sự khác biệt về sơ đồ trace của kịch bản vi phạm và kịch bản an toàn là gì?

## 4. Previous Context - Liên hệ với bài trước
Hiện thực hóa và kiểm thử hàm guardrail đã thiết lập ở bài 41 để bảo vệ trực tiếp cho Sales Manager Agent của bài 38 (Day 2).

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: PII - Personally Identifiable Information - Thông tin nhận dạng cá nhân
  - Meaning - nghĩa: Bất kỳ thông tin nào có thể dùng để xác định, liên hệ hoặc định danh một cá nhân cụ thể (ví dụ tên riêng, số điện thoại, số định danh cá nhân).
  - Why it matters - vì sao quan trọng: Việc rò rỉ dữ liệu PII trong các email tự động gửi ra ngoài có thể dẫn đến rủi ro pháp lý nghiêm trọng cho doanh nghiệp.
  - Relationship - liên hệ với khái niệm khác: Là đối tượng chính cần được lọc bỏ bởi các Input/Output Guardrails trong ứng dụng AI thương mại.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Luồng kiểm tra và chặn đứng của careful_sales_manager:
1. Input: Prompt của người dùng chứa thông tin vi phạm (tên riêng "Alice").
2. Processing steps:
   - Bước 1: Người dùng gọi chạy `careful_sales_manager`.
   - Bước 2: SDK tự động chạy hàm `guardrail_against_name` trước.
   - Bước 3: Guardrail gọi `Name check` agent -> Agent phân tích và trả về `is_name_in_message = True`.
   - Bước 4: Hàm guardrail nhận diện vi phạm, trả về `tripwire_triggered=True`.
   - Bước 5: SDK dừng ngay lập tức và ném ra Exception `guardrail input guardrail triggered tripwire`.
3. Output: Lỗi Exception chặn chương trình, các agent bán hàng và công cụ gửi email hoàn toàn không được khởi động.
4. Control flow / data flow: Chặn đứng luồng chạy ở khâu kiểm duyệt đầu vào (input phase).
5. Decision points: Guardrail đưa ra quyết định dừng toàn bộ hệ thống để bảo vệ dữ liệu.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Khai báo danh sách Guardrails trong tham số `input_guardrails`
  - Purpose - mục đích: Tự động chạy tất cả các hàm kiểm duyệt an toàn đã đăng ký trước khi cho phép Agent chính và các công cụ con thực thi.
  - When to use - dùng khi nào: Cho mọi Agent cấp cao tiếp nhận thông tin trực tiếp từ người dùng cuối trong môi trường production.
  - Trade-off - đánh đổi: Tăng thời gian thực thi tổng thể do phải chạy thêm cuộc gọi LLM kiểm duyệt phụ trợ.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [3_lab3.ipynb](file:///G:/Agent2026Win/agents/3_lab3.ipynb#L310-L346)
- Purpose - mục đích: Khởi tạo Agent được bảo vệ bằng Guardrail và thực thi thử nghiệm hai trường hợp sập bẫy và cho qua.
- Key logic:
  - Khai báo `careful_sales_manager` nhận tham số `input_guardrails`.
  - Chạy thử với tin nhắn chứa tên "Alice" và bọc trong khối `try-except` để bắt lỗi tripwire.
  - Chạy thử với tin nhắn an toàn không chứa tên riêng.
- Important lines / functions:
  - Dòng 316: `input_guardrails=[guardrail_against_name]`
    - Ý nghĩa: Đăng ký hàm guardrail kiểm tra tên người cho Agent.
  - Dòng 322: `result = await Runner.run(careful_sales_manager, message)`
    - Ý nghĩa: Khởi chạy với tin nhắn chứa "from Alice". Dòng này sẽ kích hoạt lỗi dừng chương trình.
  - Dòng 344: `result = await Runner.run(careful_sales_manager, message)`
    - Ý nghĩa: Khởi chạy với tin nhắn an toàn "from Head of Business Development". Chạy thành công và gửi email nháp.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Không áp dụng.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Chương trình Python bị dừng đột ngột (crash) khi chạy thực tế do guardrail bị kích hoạt.
- Root cause: Lập trình viên không bọc lệnh chạy `Runner.run` trong khối xử lý ngoại lệ `try-except`.
- Fix / prevention: Luôn luôn sử dụng khối lệnh `try-except` để bắt các ngoại lệ liên quan đến guardrail và đưa ra thông báo thân thiện cho người dùng cuối thay vì để sập hệ thống.

## 11. Knowledge Extension - Kiến thức mở rộng
- *Phân tích Trace của Guardrail sập bẫy*:
  - Khi xem trace trên OpenAI Platform Traces, phiên chạy bị lỗi sẽ hiển thị một biểu tượng cảnh báo màu đỏ ở nút gốc.
  - Mở chi tiết trace sẽ thấy luồng chạy dừng ngay lập tức tại bước `guardrail_against_name` -> `Name check`. Hoàn toàn không có bất kỳ bước gọi `Sales Manager` chính hay các agent bán hàng con nào được thực thi phía sau. Điều này chứng minh tính hiệu quả của chốt chặn bảo mật đầu vào.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Guardrail được khai báo qua thuộc tính `input_guardrails` hoặc `output_guardrails` của Agent.
2. Khi guardrail bị kích hoạt, SDK dừng thực thi lập tức và ném ra Exception.
3. Guardrails là chốt chặn bảo mật dữ liệu PII thực tế và hiệu quả cho các ứng dụng AI doanh nghiệp.
4. Cần bọc lệnh chạy Agent trong khối `try-except` để xử lý ngoại lệ khi guardrail sập bẫy.
5. Vết trace của guardrail bị lỗi chỉ ra chính xác vị trí và nguyên nhân chặn đứng luồng chạy.

### Self-check questions
1. Tại sao việc dùng Guardrail độc lập lại an toàn hơn việc chỉ viết câu lệnh cấm trong system prompt của Agent?
2. Hãy mô tả hành vi của OpenAI Agents SDK khi một cuộc gọi sập bẫy guardrail.

### Flashcards
- Q: Điều gì xảy ra khi guardrail trả về `tripwire_triggered=True`?
  A: SDK lập tức chặn đứng tiến trình chạy và ném ra một Exception báo lỗi tripwire.

### Interview Q&A nếu phù hợp
- Q: Tại sao trong các hệ thống Agent thương mại thực tế, việc thiết lập Guardrails lại quan trọng hơn việc chỉ Prompting thông thường để kiểm soát hành vi?
  A: Prompting thông thường chỉ mang tính chất hướng dẫn cho mô hình ngôn ngữ lớn (LLM) và mô hình vẫn có thể bị vượt qua (jailbreak) hoặc bỏ qua chỉ dẫn do tính chất không xác định (non-deterministic) của LLM. Trái lại, Guardrails là một chốt chặn lập trình độc lập (được bọc ngoài luồng chạy chính). Khi Guardrail phát hiện vi phạm, nó trả về tín hiệu lập trình cứng (`tripwire_triggered=True`), buộc SDK phải chặn đứng luồng thực thi và ném ra exception ngay lập tức trước khi LLM chính hoặc các công cụ hệ thống có cơ hội hoạt động. Điều này giúp đảm bảo an toàn tuyệt đối và tính dự đoán được cho hệ thống.

## 13. Missing Inputs - Còn thiếu gì
- Không có.
