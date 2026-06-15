# Day 4 - Building Deep Research Agents, Structured Outputs, and Parallel Tasks in Agent SDK

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

---

# 43. Day 4 - Building Deep Research Agents - Implementing OpenAI's Web Search Tool

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([4_lab4.ipynb](file:///G:/Agent2026Win/agents/2_openai/4_lab4.ipynb#L81-L95))
- Summary lịch sử: đã dùng ([day1_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day1_summary.md), [day2_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day2_summary.md), [day3_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day3_summary.md) - để lấy bối cảnh về lập trình bất đồng bộ, sử dụng công cụ và thiết kế hệ thống Agent)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học thực hành khởi tạo Agent đầu tiên tích hợp công cụ tìm kiếm được lưu trữ sẵn để tóm tắt kết quả từ internet.

> [!IMPORTANT]
> OpenAI cung cấp các công cụ được lưu trữ từ xa giúp giảm thiểu thời gian phát triển các tính năng phổ biến. Tuy nhiên, việc gọi các công cụ này sẽ tốn chi phí trực tiếp trên tài khoản API của bạn.

## 2. Executive Summary - Tóm tắt cốt lõi
- Giới thiệu dự án nghiên cứu sâu (deep research agent) - một ca sử dụng kinh điển của Agentic AI để tự động tìm kiếm và tổng hợp thông tin từ web.
- Giới thiệu khái niệm Hosted Tools - công cụ được lưu trữ do OpenAI trực tiếp vận hành. Ba công cụ hiện có gồm: Web Search Tool - công cụ tìm kiếm web, File Search Tool - công cụ tìm kiếm tệp tin, và Computer Tool - công cụ tương tác máy tính.
- Tìm hiểu về chi phí của Web Search Tool: chi phí mặc định khoảng 2.5 cents ($0.025) cho mỗi lượt gọi, có thể tích lũy rất nhanh nếu chạy nhiều truy vấn song song hoặc lặp đi lặp lại.
- Xây dựng `search_agent` sử dụng `WebSearchTool` với cấu hình tiết kiệm `search_context_size="low"` (bối cảnh tìm kiếm thấp) để giảm chi phí token.
- Sử dụng mô hình `gpt-4o-mini` để giảm thiểu chi phí API tối đa khi thực nghiệm.
- Áp dụng cấu hình `tool_choice="required"` để bắt buộc Agent phải chạy công cụ tìm kiếm trước khi phản hồi người dùng.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu kiến trúc và cơ chế hoạt động của Hosted Tools do OpenAI quản lý.
  - Nắm bắt cơ cấu chi phí (cost) của việc cào và tìm kiếm thông tin web từ API OpenAI.
  - Nhận biết sự khác biệt giữa các mức độ bối cảnh tìm kiếm web (`low`, `medium`, `high`).
- Practical goals - mục tiêu thực hành:
  - Cấu hình và khởi tạo công cụ `WebSearchTool` trong OpenAI Agents SDK.
  - Thiết lập tham số `model_settings` với thuộc tính `tool_choice="required"`.
  - Thực thi Agent tìm kiếm đầu tiên và phân tích trace (vết chạy) trên OpenAI Traces portal.
- What learner should be able to explain - người học cần giải thích được:
  - Hosted tools khác biệt như thế nào so với custom tools tự định nghĩa?
  - Tại sao lại đặt thuộc tính `tool_choice="required"` cho một Agent thực hiện tìm kiếm chuyên biệt?

## 4. Previous Context - Liên hệ với bài trước
- Tiếp nối và nâng cao các khái niệm về Agent và công cụ (tools) ở Day 1 và Day 2. Thay vì tự phát triển custom tool để gọi API tìm kiếm bên thứ ba, chúng ta tận dụng hạ tầng tìm kiếm có sẵn của OpenAI để xây dựng Agent tìm kiếm thông tin trực tiếp từ internet.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Hosted Tools - công cụ được lưu trữ
  - Meaning - nghĩa: Các công cụ do chính nhà cung cấp mô hình (ở đây là OpenAI) triển khai, vận hành và duy trì trực tiếp trên máy chủ của họ.
  - Why it matters - vì sao quan trọng: Giúp nhà phát triển tích hợp các chức năng phức tạp như cào web, tìm kiếm ngữ nghĩa trên kho tài liệu hay tương tác màn hình mà không cần xây dựng và duy trì hạ tầng riêng.
  - Relationship - liên hệ với khái niệm khác: Tương đương với các công cụ mặc định tích hợp trong giao diện ChatGPT (như Bing Search, Code Interpreter).
- Term - thuật ngữ: Web Search Tool - công cụ tìm kiếm web
  - Meaning - nghĩa: Một hosted tool cụ thể của OpenAI cho phép Agent thực hiện các câu truy vấn tìm kiếm dữ liệu trực tuyến thời gian thực từ internet.
  - Why it matters - vì sao quan trọng: Khắc phục giới hạn về mặt thời gian của dữ liệu huấn luyện tĩnh của mô hình ngôn ngữ lớn.
  - Relationship - liên hệ với khái niệm khác: Một trong ba hosted tools cùng với File Search Tool và Computer Tool.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình tìm kiếm web đơn giản của search_agent:
1. Input: Lời nhắc của người dùng (user prompt) chứa nội dung cần tìm kiếm (ví dụ: "Latest AI Agent frameworks in 2025").
2. Processing steps:
   - Bước 1: Khởi tạo `WebSearchTool` với cấu hình bối cảnh thấp.
   - Bước 2: Khởi tạo `search_agent` với hướng dẫn và công cụ tìm kiếm, kèm cờ bắt buộc chạy công cụ.
   - Bước 3: Gọi `Runner.run(search_agent, message)` trong khối trace để giám sát.
   - Bước 4: OpenAI API tiếp nhận yêu cầu, kích hoạt bộ tìm kiếm, lấy dữ liệu và đưa lại cho mô hình để tóm tắt.
3. Output: Văn bản tóm tắt kết quả tìm kiếm dạng Markdown ngắn gọn từ 2-3 đoạn văn.
4. Control flow / data flow: Chạy tuần tự và trực diện: Yêu cầu -> Tìm kiếm -> Tóm tắt -> Hiển thị kết quả.
5. Decision points: Không có nhánh rẽ vì mô hình bị ép buộc gọi công cụ tìm kiếm qua cờ `tool_choice="required"`.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Bắt buộc chọn công cụ - Tool Choice Required
  - Purpose - mục đích: Ràng buộc mô hình ngôn ngữ lớn luôn luôn phải thực hiện cuộc gọi công cụ được chỉ định ở lượt chạy đầu tiên thay vì tự ý trả lời bằng văn bản thông thường.
  - When to use - dùng khi nào: Khi Agent đóng vai trò là một wrapper (bộ bọc) chuyên biệt cho một công cụ cụ thể và không được phép bỏ qua công cụ đó.
  - Trade-off - đánh đổi: Làm mất đi tính linh hoạt tự nhiên của Agent; nếu công cụ bị lỗi hoặc dữ liệu truyền vào sai cấu trúc, Agent sẽ không thể tự phục hồi bằng câu trả lời thông thường.
  - Common mistake - lỗi dễ gặp: Thiết lập `tool_choice="required"` nhưng danh sách `tools` của Agent lại bị trống, dẫn đến lỗi từ phía API.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [4_lab4.ipynb](file:///G:/Agent2026Win/agents/2_openai/4_lab4.ipynb#L81-L95)
- Purpose - mục đích: Thiết lập `search_agent` sử dụng Web Search Tool của OpenAI để tìm kiếm thông tin trực tuyến.
- Key logic: Khởi tạo Agent tìm kiếm với mô hình `gpt-4o-mini`, tích hợp `WebSearchTool` có bối cảnh thấp để tiết kiệm chi phí và thiết lập thuộc tính bắt buộc chạy công cụ.
- Important lines / functions:
  ```python
  search_agent = Agent(
      name="Search agent",
      instructions=INSTRUCTIONS,
      tools=[WebSearchTool(search_context_size="low")],
      model="gpt-4o-mini",
      model_settings=ModelSettings(tool_choice="required"),
  )
  ```
  - Vietnamese inline notes:
    - `WebSearchTool(search_context_size="low")`: Khởi tạo công cụ tìm kiếm web với bối cảnh thấp để giảm thiểu lượng token đầu vào, tiết kiệm chi phí sử dụng.
    - `model_settings=ModelSettings(tool_choice="required")`: Cấu hình ép buộc mô hình phải gọi công cụ tìm kiếm ở bước đầu tiên, tránh tự sinh câu trả lời tự do.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: search_context_size="low" (Bối cảnh thấp)
  - Pros: Tiết kiệm chi phí, giảm lượng token đầu vào đáng kể.
  - Cons: Dữ liệu tóm tắt trả về ít chi tiết hơn, có khả năng bỏ lỡ một số thông tin phụ.
  - When to choose: Trong giai đoạn phát triển và kiểm thử code để tối ưu hóa ngân sách.
- Option: search_context_size="high" (Bối cảnh cao)
  - Pros: Trả về kết quả tìm kiếm phong phú, chi tiết và toàn diện nhất.
  - Cons: Chi phí token tăng cao, hóa đơn API tăng nhanh.
  - When to choose: Khi triển khai hệ thống chạy thực tế cần lập báo cáo nghiên cứu chất lượng cao và chi tiết.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Chi phí API OpenAI tăng đột biến ngoài tầm kiểm soát.
- Root cause: Chạy thử nghiệm nhiều lần bằng mô hình đắt tiền (`gpt-4o`) hoặc đặt mức bối cảnh tìm kiếm ở mức cao (`high`).
- Symptom: Hóa đơn API tăng nhanh chóng sau vài lượt chạy.
- Fix / prevention: [Alert] Luôn đặt `gpt-4o-mini` làm mô hình mặc định trong lúc phát triển và đặt bối cảnh tìm kiếm là `low`. Giám sát chặt chẽ hoạt động trên OpenAI Traces portal.

## 11. Knowledge Extension - Kiến thức mở rộng
- Ba hosted tools hiện tại của OpenAI bao gồm:
  1. **WebSearchTool**: Cho phép Agent duyệt internet thông qua công cụ tìm kiếm Bing của Microsoft.
  2. **FileSearchTool**: Tích hợp sẵn cơ chế RAG (Retrieval-Augmented Generation) dựa trên Vector Store được quản lý bởi OpenAI để truy xuất thông tin từ tài liệu người dùng tải lên.
  3. **ComputerTool**: Công cụ thử nghiệm cho phép Agent tương tác trực tiếp với giao diện hệ điều hành thông qua chụp ảnh màn hình và click chuột.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Web Search Tool là công cụ tìm kiếm web được lưu trữ và vận hành trực tiếp bởi OpenAI.
2. Chi phí cho mỗi lần tìm kiếm web mặc định là khoảng 2.5 cents ($0.025).
3. Đặt `search_context_size="low"` để hạn chế kích thước dữ liệu phản hồi, tiết kiệm chi phí token.
4. Cấu hình `tool_choice="required"` trong `ModelSettings` buộc Agent phải sử dụng công cụ.
5. Luôn dùng `gpt-4o-mini` cho các tác vụ nghiên cứu thử nghiệm thông thường để tối ưu hóa ngân sách.

### Self-check questions
1. Làm cách nào để cấu hình một Agent bắt buộc phải thực thi một công cụ cụ thể khi bắt đầu chạy?
2. Hãy liệt kê các hosted tools hiện có của OpenAI và mục đích sử dụng tương ứng.

### Flashcards
- Q: Lớp nào được sử dụng để bắt buộc Agent gọi công cụ trong SDK?
  A: Lớp `ModelSettings` với cấu hình `tool_choice="required"`.
- Q: Chi phí ước tính cho mỗi lượt gọi Web Search Tool ở mức rẻ nhất là bao nhiêu?
  A: Khoảng 2.5 cents ($0.025) cho mỗi lượt chạy.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 44. Day 4 - Building a Planner Agent - Using Structured Outputs with Pydantic in AI

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([4_lab4.ipynb](file:///G:/Agent2026Win/agents/2_openai/4_lab4.ipynb#L133-L159))
- Summary lịch sử: đã dùng ([day3_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day3_summary.md) - về Structured Outputs)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học hướng dẫn xây dựng Agent lập kế hoạch tìm kiếm sử dụng định dạng đầu ra cấu trúc Pydantic để đảm bảo tính ổn định của dữ liệu.

## 2. Executive Summary - Tóm tắt cốt lõi
- Xây dựng Agent lập kế hoạch (Planner Agent) chịu trách nhiệm phân tích một truy vấn lớn và chia nhỏ thành một danh sách các từ khóa tìm kiếm trực tuyến cụ thể.
- Sử dụng tính năng Structured Outputs (Đầu ra có cấu trúc) của OpenAI thông qua thư viện `pydantic` để buộc Agent phản hồi theo đúng schema (lược đồ) mong muốn.
- Định nghĩa hai schema Pydantic: `WebSearchItem` (chứa lý do và từ khóa tìm kiếm) và `WebSearchPlan` (danh sách chứa các `WebSearchItem`).
- Tận dụng docstrings và tham số `Field(description=...)` để cung cấp thông tin ngữ nghĩa trực tiếp cho LLM, giúp định hướng chính xác dữ liệu sinh ra.
- Ứng dụng kỹ thuật Chain of Thought (CoT - chuỗi suy nghĩ) trong Structured Outputs: Bằng cách định nghĩa trường `reason` trước trường `query` trong `WebSearchItem`, chúng ta buộc mô hình phải lập luận lý do tìm kiếm trước, qua đó nâng cao chất lượng của từ khóa tìm kiếm tiếp theo.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cơ chế hoạt động của Structured Outputs bằng Pydantic trong việc ràng buộc định dạng JSON trả về từ API.
  - Hiểu cách thức hoạt động của Chain of Thought khi được lồng ghép vào thứ tự khai báo các trường dữ liệu trong Pydantic.
- Practical goals - mục tiêu thực hành:
  - Định nghĩa các lớp kế thừa từ `BaseModel` và sử dụng `Field` để định nghĩa mô tả trường.
  - Khởi tạo `planner_agent` với cấu hình `output_type=WebSearchPlan`.
  - Thực hiện chạy thử nghiệm lập kế hoạch cho truy vấn nghiên cứu và phân tích cấu trúc dữ liệu trả về.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao việc yêu cầu mô hình lập luận lý do trước khi đưa ra từ khóa tìm kiếm lại giúp cải thiện chất lượng từ khóa?
  - Làm thế nào các lớp Pydantic trong Python có thể ép buộc cấu hình JSON của mô hình OpenAI?

## 4. Previous Context - Liên hệ với bài trước
- Phát triển trực tiếp từ kỹ thuật Structured Outputs đã giới thiệu ở Day 3. Thay vì chỉ xuất ra các trường văn bản phẳng đơn giản, bài học này ứng dụng cấu trúc danh sách lồng nhau (`list[WebSearchItem]`) để tạo ra một bản kế hoạch hành động chi tiết.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Structured Outputs - đầu ra có cấu trúc
  - Meaning - nghĩa: Tính năng bảo đảm phản hồi của mô hình ngôn ngữ lớn luôn khớp chính xác 100% với một định dạng dữ liệu (JSON schema) được cấu hình sẵn.
  - Why it matters - vì sao quan trọng: Giúp tích hợp dữ liệu từ AI vào hệ thống phần mềm một cách an toàn mà không sợ lỗi định dạng hoặc lỗi phân tích cú pháp (parsing error).
  - Relationship - liên hệ với khái niệm khác: Tận dụng thư viện Pydantic trong Python để chuyển dịch thành JSON Schema ở tầng API.
- Term - thuật ngữ: Chain of Thought in Schema - chuỗi suy nghĩ trong cấu trúc dữ liệu
  - Meaning - nghĩa: Kỹ thuật cố ý sắp đặt các trường dữ liệu lập luận (như lý do, suy nghĩ) lên trước trường kết quả cuối cùng (như truy vấn, câu trả lời) trong schema Pydantic.
  - Why it matters - vì sao quan trọng: Mô hình ngôn ngữ lớn hoạt động theo nguyên lý dự đoán từ tiếp theo; việc viết ra lý do lập luận trước sẽ dẫn hướng cho từ khóa kết quả sau đó logic và bám sát ngữ cảnh hơn.
  - Relationship - liên hệ với khái niệm khác: Tương đương với việc viết nháp lập luận trước khi đưa ra đáp số.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình hoạt động của planner_agent:
1. Input: Câu hỏi nghiên cứu tổng quát từ người dùng (ví dụ: "Latest AI Agent frameworks in 2025").
2. Processing steps:
   - Bước 1: Khai báo lớp Pydantic `WebSearchItem` (chứa `reason` và `query`) và `WebSearchPlan` (danh sách `searches`).
   - Bước 2: Khởi tạo `planner_agent` với tham số `output_type=WebSearchPlan`.
   - Bước 3: Chạy Agent với lời nhắc của người dùng.
   - Bước 4: Mô hình tự động xuất ra chuỗi JSON khớp với schema, SDK tự động phân tích cú pháp thành thực thể Python `WebSearchPlan`.
3. Output: Một đối tượng `WebSearchPlan` chứa danh sách các từ khóa tìm kiếm đi kèm lý giải cụ thể.
4. Control flow / data flow: Luồng chuyển dịch dữ liệu tuần tự từ câu hỏi tự do thành đối tượng cấu trúc của hệ thống.
5. Decision points: Số lượng từ khóa tìm kiếm được khống chế theo hằng số cấu hình (mặc định là 3).

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Field Description via Annotations - mô tả trường qua chú thích
  - Purpose - mục đích: Sử dụng tham số `Field(description=...)` và chuỗi docstring để hướng dẫn chi tiết cách mô hình nên điền dữ liệu cho trường đó.
  - When to use - dùng khi nào: Sử dụng bất kỳ khi nào định nghĩa Pydantic models để làm đầu ra cấu trúc cho LLM.
  - Trade-off - đánh đổi: Làm tăng nhẹ kích thước lời nhắc hệ thống (system prompt), tốn thêm vài token bối cảnh.
  - Common mistake - lỗi dễ gặp: Định nghĩa trường nhưng bỏ trống mô tả, khiến mô hình tự suy luận mục đích của trường và dễ dẫn đến sai lệch dữ liệu.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [4_lab4.ipynb](file:///G:/Agent2026Win/agents/2_openai/4_lab4.ipynb#L133-L159)
- Purpose - mục đích: Định nghĩa cấu trúc dữ liệu bản kế hoạch tìm kiếm và khởi tạo Agent lập kế hoạch.
- Key logic: Định nghĩa schema bằng Pydantic với thứ tự các trường được sắp xếp khoa học (`reason` trước `query`) và cấu hình Agent trả về đầu ra dạng đối tượng.
- Important lines / functions:
  ```python
  class WebSearchItem(BaseModel):
      reason: str = Field(description="Your reasoning for why this search is important to the query.")
      query: str = Field(description="The search term to use for the web search.")

  class WebSearchPlan(BaseModel):
      searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")

  planner_agent = Agent(
      name="PlannerAgent",
      instructions=INSTRUCTIONS,
      model="gpt-4o-mini",
      output_type=WebSearchPlan,
  )
  ```
  - Vietnamese inline notes:
    - `class WebSearchItem(BaseModel)`: Schema đại diện cho một mục tìm kiếm đơn lẻ. Định nghĩa trường `reason` trước để kích hoạt lập luận Chain of Thought.
    - `searches: list[WebSearchItem]`: Định nghĩa một danh sách lồng nhau chứa nhiều mục tìm kiếm.
    - `output_type=WebSearchPlan`: Cấu hình buộc Agent phản hồi theo đúng lược đồ dữ liệu của lớp `WebSearchPlan`.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Không áp dụng.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Lỗi phân tích cú pháp hoặc mô hình trả về lỗi cấu trúc JSON.
- Root cause: Sử dụng các mô hình ngôn ngữ lớn đời cũ không hỗ trợ tính năng Structured Outputs của OpenAI, hoặc định nghĩa các kiểu dữ liệu trong Pydantic quá phức tạp khiến bộ chuyển đổi JSON Schema của SDK bị lỗi.
- Symptom: Lỗi ném ra tại thời điểm runtime khi SDK parse kết quả từ API.
- Fix / prevention: [Alert] Hãy đảm bảo sử dụng các dòng mô hình hỗ trợ Structured Outputs tốt (như `gpt-4o-mini` hoặc `gpt-4o`). Giữ cấu trúc dữ liệu Pydantic đơn giản, chỉ sử dụng các kiểu dữ liệu cơ bản (str, int, list, dict).

## 11. Knowledge Extension - Kiến thức mở rộng
- Khi thuộc tính `output_type` được cấu hình, OpenAI Agents SDK sẽ biên dịch Pydantic Model thành một cấu trúc JSON Schema tiêu chuẩn (với cờ đặc tả `"strict": true`) và truyền vào tham số `response_format` trong cuộc gọi API. Mô hình ở phía OpenAI sẽ áp dụng cơ chế ngữ pháp ràng buộc (constrained grammar) ở tầng sinh token, chỉ cho phép sinh ra các token phù hợp với cấu trúc schema đó, đảm bảo tỷ lệ định dạng đầu ra chuẩn xác là 100%.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Structured Outputs ép mô hình trả về dữ liệu tuân thủ chính xác 100% schema Pydantic.
2. Dùng tham số `output_type` khi khởi tạo Agent để cấu hình tính năng này.
3. Thứ tự các trường trong Pydantic rất quan trọng; đặt lập luận (`reason`) trước kết quả (`query`) để kích hoạt Chain of Thought.
4. Sử dụng `Field(description=...)` để chỉ dẫn mô hình điền dữ liệu đúng ngữ nghĩa.
5. Cấu trúc lồng nhau (`list[BaseModel]`) được hỗ trợ đầy đủ để tạo các kế hoạch phức tạp.

### Self-check questions
1. Chain of Thought hoạt động như thế nào thông qua việc sắp xếp thứ tự các trường trong Pydantic schema?
2. OpenAI đảm bảo đầu ra khớp 100% với JSON Schema bằng cơ chế nào ở tầng API?

### Flashcards
- Q: Tham số nào của Agent trong SDK dùng để ép cấu trúc dữ liệu đầu ra?
  A: Tham số `output_type`.
- Q: Tại sao cần viết docstring hoặc `Field(description=...)` cho các trường trong Pydantic?
  A: Vì chúng được dịch thành mô tả trường trong JSON Schema để chỉ dẫn cho mô hình.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 45. Day 4 - Building an End-to-End Research Pipeline with GPT-4 Agents & Async Tasks

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([4_lab4.ipynb](file:///G:/Agent2026Win/agents/2_openai/4_lab4.ipynb#L181-L315))
- Summary lịch sử: đã dùng ([day2_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day2_summary.md) - về tích hợp SendGrid và tự động hóa email)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học thực hành xây dựng các Agent bổ trợ và viết các hàm điều phối bất đồng bộ để hoàn thiện đường ống nghiên cứu đầu cuối.

## 2. Executive Summary - Tóm tắt cốt lõi
- Xây dựng hoàn chỉnh các mảnh ghép của đường ống nghiên cứu đầu cuối (end-to-end research pipeline) thông qua việc phân rã tác vụ (task decomposition).
- Tái sử dụng và đóng gói công cụ gửi thư `send_email` bằng dịch vụ SendGrid thông qua bộ trang trí `@function_tool` để LLM có thể nhận diện và gọi tự động.
- Khởi tạo `email_agent` có nhiệm vụ tiếp nhận báo cáo nghiên cứu thô, định dạng thành mẫu email HTML chuyên nghiệp và tự động soạn thảo tiêu đề email phù hợp.
- Khởi tạo `writer_agent` đóng vai trò là nhà nghiên cứu cấp cao, chịu trách nhiệm tổng hợp toàn bộ kết quả tìm kiếm web thô thu thập được để viết thành một báo cáo nghiên cứu chi tiết (khoảng 5-10 trang, tối thiểu 1000 từ).
- Định nghĩa cấu trúc báo cáo đầu ra qua lớp Pydantic `ReportData` gồm: tóm tắt ngắn (`short_summary`), báo cáo Markdown chính (`markdown_report`), và các gợi ý chủ đề nghiên cứu tiếp theo (`follow_up_questions`).
- Viết các hàm điều phối bất đồng bộ để kiểm soát luồng chạy của hệ thống: `plan_searches` (lập kế hoạch), `perform_searches` (tìm kiếm song song), `search` (gọi tác vụ tìm kiếm lẻ), `write_report` (viết báo cáo) và `send_email` (gửi mail).

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu triết lý phân rã tác vụ (task decomposition) trong thiết kế hệ thống đa Agent phức tạp.
  - Hiểu cách thức truyền nhận dữ liệu tuần tự và song song giữa các Agent trong hệ thống bất đồng bộ.
- Practical goals - mục tiêu thực hành:
  - Định nghĩa công cụ hàm gửi email dạng HTML bằng SendGrid sử dụng decorator `@function_tool`.
  - Khởi tạo `writer_agent` và `email_agent` với đầy đủ cấu hình.
  - Viết các hàm Python bất đồng bộ kết nối các bước xử lý dữ liệu của đường ống nghiên cứu.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao nên chia nhỏ hệ thống nghiên cứu sâu thành nhiều Agent chuyên biệt thay vì để một Agent duy nhất xử lý toàn bộ?
  - Cơ chế tự động sinh schema của decorator `@function_tool` hoạt động như thế nào?

## 4. Previous Context - Liên hệ với bài trước
- Tái sử dụng công cụ gửi thư SendGrid đã phát triển từ Day 2. Kế thừa tư duy thiết kế luồng công việc (Agentic Workflow) để phân tách rõ ràng nhiệm vụ tìm kiếm thông tin và nhiệm vụ tổng hợp thông tin, giúp giảm tải ngữ cảnh cho mô hình và loại bỏ lỗi lặp vô hạn.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Function Tool - công cụ hàm
  - Meaning - nghĩa: Phương pháp chuyển đổi một hàm Python thông thường thành một công cụ mà Agent có thể gọi bằng cách sử dụng decorator `@function_tool`.
  - Why it matters - vì sao quan trọng: Đơn giản hóa việc khai báo và cấu hình công cụ, tự động hóa việc đồng bộ mô tả hàm (docstring) thành mô tả công cụ gửi cho mô hình.
  - Relationship - liên hệ với khái niệm khác: Tương tự như cơ chế tự động sinh JSON schema của các framework Agent khác.
- Term - thuật ngữ: Task Decomposition - phân rã tác vụ
  - Meaning - nghĩa: Thiết kế hệ thống chia nhỏ một tác vụ lớn, phức tạp thành nhiều bước nhỏ độc lập và gán mỗi bước cho một Agent hoặc tiến trình chuyên môn hóa xử lý.
  - Why it matters - vì sao quan trọng: Giảm thiểu sự phức tạp của lời nhắc hệ thống, tối ưu hóa độ chính xác và độ tin cậy của kết quả đầu ra.
  - Relationship - liên hệ với khái niệm khác: Một mẫu thiết kế (design pattern) phổ biến trong kiến trúc đa Agent (multi-agent architecture).

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình xử lý dữ liệu của đường ống nghiên cứu đầu cuối:
1. Input: Truy vấn nghiên cứu gốc (Query) từ người dùng.
2. Processing steps:
   - Bước 1: `plan_searches` nhận truy vấn, sử dụng Planner Agent để đưa ra danh sách N từ khóa tìm kiếm.
   - Bước 2: `perform_searches` nhận danh sách, kích hoạt song song N tác vụ tìm kiếm web bằng cách gọi `search` (Search Agent sử dụng `WebSearchTool`).
   - Bước 3: `write_report` gom toàn bộ kết quả tìm kiếm thô gửi cho Writer Agent để viết báo cáo cấu trúc `ReportData`.
   - Bước 4: `send_email` nhận báo cáo Markdown từ `ReportData`, truyền sang Email Agent để sinh email HTML và gọi công cụ `send_email` gửi đi.
3. Output: Báo cáo nghiên cứu định dạng HTML được gửi thành công đến hòm thư người dùng qua SendGrid API.
4. Control flow / data flow: Luồng kết hợp: Planner (tuần tự) -> Searches (song song qua AsyncIO) -> Writer (tuần tự) -> Email (tuần tự).
5. Decision points: Email Agent tự quyết định nội dung tiêu đề thư (`subject`) và cấu trúc trình bày HTML của email.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Task-Specific Agents - các Agent chuyên biệt theo tác vụ
  - Purpose - mục đích: Thiết kế mỗi Agent chỉ có một trách nhiệm duy nhất (Planner chỉ lập kế hoạch, Searcher chỉ cào web, Writer chỉ viết báo cáo, Emailer chỉ gửi mail).
  - When to use - dùng khi nào: Khi xây dựng các hệ thống Agent quy mô lớn hoặc các pipeline xử lý dữ liệu dài.
  - Trade-off - đánh đổi: Làm tăng số lượng Agent cần quản lý và tăng số lượt gọi API trung gian.
  - Common mistake - lỗi dễ gặp: Gán quá nhiều công cụ hoặc chỉ dẫn mâu thuẫn cho một Agent, làm mô hình bị quá tải ngữ cảnh và hoạt động kém hiệu quả.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [4_lab4.ipynb](file:///G:/Agent2026Win/agents/2_openai/4_lab4.ipynb#L181-L315)
- Purpose - mục đích: Định nghĩa công cụ gửi email, các Agent phụ trợ và toàn bộ các hàm bất đồng bộ điều phối quy trình nghiên cứu sâu.
- Key logic: Khai báo công cụ SendGrid với địa chỉ email mẫu bảo mật, định nghĩa schema `ReportData` cho báo cáo đầu ra, và viết các hàm điều phối luồng xử lý dữ liệu tuần tự và song song.
- Important lines / functions:
  ```python
  @function_tool
  def send_email(subject: str, html_body: str) -> Dict[str, str]:
      """ Send out an email with the given subject and HTML body """
      sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
      from_email = Email("sender@example.com") # Đã thay bằng email mẫu bảo mật
      to_email = To("recipient@example.com")   # Đã thay bằng email mẫu bảo mật
      content = Content("text/html", html_body)
      mail = Mail(from_email, to_email, subject, content).get()
      sg.client.mail.send.post(request_body=mail)
      return "success"

  class ReportData(BaseModel):
      short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
      markdown_report: str = Field(description="The final report")
      follow_up_questions: list[str] = Field(description="Suggested topics to research further")
  ```
  - Vietnamese inline notes:
    - `@function_tool`: Đóng gói hàm Python thông thường thành một công cụ mà LLM có thể gọi thông qua phân tích cú pháp docstring của hàm.
    - `from_email` và `to_email`: Sử dụng địa chỉ email mẫu an toàn. Khi chạy thực tế, người dùng phải thay thế bằng các địa chỉ email đã được xác minh trên hệ thống SendGrid cá nhân.
    - `ReportData`: Schema Pydantic đặc tả cấu trúc đầu ra của báo cáo nghiên cứu chi tiết.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Không áp dụng.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Không gửi được email và gặp lỗi API từ SendGrid.
- Root cause: Chưa cấu hình hoặc cấu hình sai biến môi trường `SENDGRID_API_KEY`, hoặc sử dụng địa chỉ email gửi (`from_email`) chưa được xác thực thông qua cơ chế Single Sender Verification của SendGrid.
- Symptom: Tiến trình điều phối báo lỗi và dừng chạy ở bước gửi email.
- Fix / prevention: [Alert] Luôn kiểm tra xem `SENDGRID_API_KEY` đã được khai báo đầy đủ trong tệp tin `.env` chưa. Đảm bảo địa chỉ email truyền vào `from_email` là địa chỉ email bạn đã thực hiện xác minh thành công trên trang quản trị của SendGrid.

## 11. Knowledge Extension - Kiến thức mở rộng
- Bộ trang trí `@function_tool` sử dụng cơ chế phản chiếu mã nguồn (reflection) của Python để phân tích tên hàm, các tham số đầu vào (cùng gợi ý kiểu dữ liệu - type hints) và chuỗi tài liệu (docstring). SDK sẽ biên dịch các thông tin này thành cấu trúc JSON Schema tiêu chuẩn của OpenAI để mô hình LLM hiểu được cách thức và thời điểm cần gọi công cụ này.

## 12. Study Pack - Gói ôn tập
### Must remember
1. `@function_tool` tự động chuyển đổi hàm Python thông thường thành công cụ của Agent.
2. Phân rã tác vụ (Task Decomposition) giúp hệ thống Agent hoạt động ổn định và tin cậy hơn.
3. Báo cáo nghiên cứu cuối cùng được định hình cấu trúc qua Pydantic Model `ReportData`.
4. Cần sử dụng địa chỉ email đã xác minh của SendGrid để đảm bảo gửi thư thành công.
5. Email Agent chịu trách nhiệm chuyển đổi báo cáo dạng Markdown sang HTML và tự soạn thảo tiêu đề thư.

### Self-check questions
1. Nêu vai trò và mục đích của việc sử dụng `@function_tool` decorator trong SDK.
2. Tại sao việc chia nhỏ hệ thống thành Planner Agent và Writer Agent lại giúp nâng cao chất lượng báo cáo?

### Flashcards
- Q: Lớp Pydantic nào định nghĩa cấu trúc của báo cáo nghiên cứu cuối cùng trong bài học?
  A: Lớp `ReportData`.
- Q: Cơ chế nào giúp chuyển đổi báo cáo Markdown thành thư điện tử dạng HTML trong bài học?
  A: Email Agent tiếp nhận Markdown, tự thiết kế cấu trúc HTML và gọi công cụ gửi thư.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 46. Day 4 - Building a Deep Research Agent - Parallel Searches with AsyncIO

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([4_lab4.ipynb](file:///G:/Agent2026Win/agents/2_openai/4_lab4.ipynb#L325-L339))
- Summary lịch sử: đã dùng ([day1_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day1_summary.md) - về lập trình bất đồng bộ AsyncIO, [day3_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day3_summary.md) - về vết chạy trace)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học thực thi chạy thử nghiệm toàn bộ hệ thống nghiên cứu sâu và tìm hiểu cơ chế giám sát trace bất đồng bộ.

## 2. Executive Summary - Tóm tắt cốt lõi
- Thực thi toàn bộ đường ống nghiên cứu đầu cuối (Showtime!) trong khối bọc giám sát `trace("Research trace")`.
- Phân tích và so sánh chi tiết hiệu năng giữa các bước xử lý dữ liệu tuần tự và xử lý dữ liệu song song trong Agentic Workflows.
- Ứng dụng hàm `asyncio.gather(*tasks)` để chạy song song toàn bộ các yêu cầu tìm kiếm web (ban đầu thử nghiệm với 3 searches, sau đó nâng cấp lên 20 searches).
- Sử dụng OpenAI Traces portal để trực quan hóa đồ thị thời gian chạy: các lượt tìm kiếm chạy song song hoàn toàn (dải thời gian chồng chéo), trong khi các bước lập kế hoạch, viết báo cáo và gửi email diễn ra tuần tự (xếp đuôi nhau).
- Khảo sát kết quả nghiên cứu: khi nâng số lượng tìm kiếm lên 20, báo cáo thu được chi tiết hơn rất nhiều, có cấu trúc sâu sắc hơn và cung cấp nhiều thông tin so sánh giá trị thương mại.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu sâu sắc sự khác biệt về mặt kiến trúc và hiệu năng giữa thực thi tuần tự (sequential) và thực thi song song (parallel) trong hệ thống Agent.
  - Hiểu cách phân tích đồ thị vết chạy và thời gian xử lý của các tiến trình bất đồng bộ.
- Practical goals - mục tiêu thực hành:
  - Chạy thử nghiệm pipeline nghiên cứu đầu cuối với 3 truy vấn tìm kiếm song song.
  - Sửa đổi tham số cấu hình để nâng số lượng tìm kiếm lên 20 và đánh giá kết quả.
  - Truy cập OpenAI Traces portal để kiểm tra và phân tích biểu đồ tiến trình thời gian thực.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao việc tìm kiếm song song lại giúp tiết kiệm thời gian đáng kể so với tìm kiếm tuần tự?
  - Cách nhận diện tác vụ song song và tác vụ tuần tự trên biểu đồ trace?

## 4. Previous Context - Liên hệ với bài trước
- Áp dụng trực tiếp kiến thức lập trình bất đồng bộ AsyncIO từ Day 1 vào một quy trình đa Agent thực tế. Kết nối toàn bộ các Agent độc lập đã xây dựng từ các bài học trước thành một hệ thống nghiên cứu hoàn chỉnh hoạt động trơn tru.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Parallel Execution - thực thi song song
  - Meaning - nghĩa: Trạng thái nhiều tác vụ I/O (như gọi API tìm kiếm web) được kích hoạt và xử lý đồng thời thay vì phải đợi tác vụ trước hoàn thành mới bắt đầu tác vụ sau.
  - Why it matters - vì sao quan trọng: Giúp tối ưu hóa tài nguyên mạng và giảm tổng thời gian phản hồi của hệ thống Agent một cách đáng kể.
  - Relationship - liên hệ với khái niệm khác: Tương phản với thực thi tuần tự (Sequential Execution).
- Term - thuật ngữ: OpenAI Traces Portal - cổng thông tin vết chạy OpenAI
  - Meaning - nghĩa: Giao diện giám sát trực quan các cuộc gọi API từ Agent SDK, cung cấp thông tin về số lượng token, thời gian chạy và đồ thị liên kết giữa các Agent và công cụ.
  - Why it matters - vì sao quan trọng: Giúp nhà phát triển dễ dàng gỡ lỗi, tối ưu hóa các điểm nghẽn hiệu năng (performance bottlenecks) của hệ thống.
  - Relationship - liên hệ với khái niệm khác: Một công cụ giám sát phân tán dành riêng cho các ứng dụng Agentic AI của OpenAI.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Đồ thị thực thi thời gian thực của pipeline:
1. Bắt đầu: Khởi tạo trace tổng quát `Research trace`.
2. Bước 1 (Tuần tự): Planner Agent thực thi để đưa ra kế hoạch gồm N từ khóa tìm kiếm.
3. Bước 2 (Song song): Kích hoạt `asyncio.gather` gửi đồng thời N truy vấn cào dữ liệu web đến OpenAI API. Các dải thời gian thực thi của các tác vụ tìm kiếm này diễn ra song song.
4. Bước 3 (Tuần tự): Đợi toàn bộ các tìm kiếm hoàn tất, gom kết quả gửi sang Writer Agent để tổng hợp báo cáo.
5. Bước 4 (Tuần tự): Chuyển báo cáo sang Email Agent để định dạng HTML và gọi API gửi thư điện tử đi.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Concurrency via asyncio.gather - tính đồng thời qua asyncio.gather
  - Purpose - mục đích: Gửi đồng loạt nhiều yêu cầu API độc lập lên mạng internet để tận dụng tối đa băng thông và giảm thiểu thời gian chờ đợi phản hồi I/O.
  - When to use - dùng khi nào: Khi hệ thống cần gọi nhiều API độc lập (như tìm kiếm nhiều từ khóa khác nhau) không phụ thuộc dữ liệu vào nhau.
  - Trade-off - đánh đổi: Có thể chạm giới hạn tần suất gọi API (Rate Limit) của nhà cung cấp nếu số lượng tác vụ song song quá lớn.
  - Common mistake - lỗi dễ gặp: Quên ký tự unpacked `*` trước danh sách tác vụ khi truyền vào `asyncio.gather()`, dẫn đến lỗi cú pháp runtime.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [4_lab4.ipynb](file:///G:/Agent2026Win/agents/2_openai/4_lab4.ipynb#L325-L339)
- Purpose - mục đích: Thực thi toàn bộ chu trình nghiên cứu sâu đầu cuối và giám sát thời gian chạy bất đồng bộ thông qua trace.
- Key logic: Sử dụng từ khóa `await` để điều phối tuần tự các giai đoạn chính, kết hợp với các hàm phụ trợ bên trong đã đóng gói cơ chế chạy song song `asyncio.gather`.
- Important lines / functions:
  ```python
  query = "Latest AI Agent frameworks in 2025"

  with trace("Research trace"):
      print("Starting research...")
      search_plan = await plan_searches(query)
      search_results = await perform_searches(search_plan)
      report = await write_report(query, search_results)
      await send_email(report)  
      print("Hooray!")
  ```
  - Vietnamese inline notes:
    - `with trace("Research trace")`: Thiết lập một bộ bọc trace để ghi nhận toàn bộ hoạt động của các Agent con và công cụ trong phiên chạy này.
    - `await plan_searches(query)`: Lập kế hoạch tìm kiếm tuần tự.
    - `await perform_searches(search_plan)`: Hàm này bên trong sử dụng `asyncio.gather` để gửi các yêu cầu tìm kiếm web song song, tiết kiệm thời gian chạy.
    - `await write_report(...)` và `await send_email(...)`: Tổng hợp báo cáo và gửi email tuần tự sau khi đã thu thập đủ dữ liệu.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: 3 searches (Tìm kiếm quy mô nhỏ)
  - Pros: Chi phí chạy cực kỳ thấp (khoảng 7.5 cents), tốc độ hoàn thành nhanh.
  - Cons: Báo cáo có độ sâu thông tin trung bình, dễ thiếu các phân tích so sánh chi tiết.
  - When to choose: Thích hợp kiểm thử nhanh logic của code.
- Option: 20 searches (Tìm kiếm quy mô lớn)
  - Pros: Báo cáo chất lượng cao, phân tích đa chiều và cung cấp nhiều ứng dụng thương mại thực tiễn.
  - Cons: Thời gian chạy lâu hơn, tốn chi phí API nhiều hơn (khoảng 50 cents).
  - When to choose: Khi cần báo cáo nghiên cứu hoàn chỉnh, phục vụ mục đích học tập hoặc công việc thực tiễn.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Hệ thống bị lỗi hoặc phản hồi rất chậm khi tăng số lượng tìm kiếm lên mức cao (ví dụ 20 searches).
- Root cause: Gửi quá nhiều yêu cầu đồng thời vượt quá giới hạn tần suất (Rate Limit) cho phép của OpenAI API hoặc dịch vụ tìm kiếm Bing.
- Symptom: Lỗi `RateLimitError` ném ra giữa chừng làm gián đoạn toàn bộ đường ống nghiên cứu.
- Fix / prevention: [Alert] Sử dụng cơ chế giới hạn luồng đồng thời bằng cách khai báo `asyncio.Semaphore(value)` để chỉ cho phép tối đa một số lượng yêu cầu (ví dụ 5 requests) được thực thi song song tại một thời điểm, tránh bị nhà cung cấp khóa API tạm thời.

## 11. Knowledge Extension - Kiến thức mở rộng
- Không có.

## 12. Study Pack - Gói ôn tập
### Must remember
1. `asyncio.gather(*tasks)` được sử dụng để thực thi song song các yêu cầu tìm kiếm web.
2. Tác vụ song song hiển thị các dải thời gian chạy chồng lấp lên nhau trên giao diện OpenAI Traces portal.
3. Các tác vụ xử lý thông tin tuần tự (như lập kế hoạch, tổng hợp báo cáo) hiển thị nối đuôi nhau.
4. Tăng số lượng tìm kiếm giúp nâng cao chất lượng báo cáo nhưng tỷ lệ thuận với việc tăng chi phí API.
5. Luồng dữ liệu tổng thể: tuần tự (plan) -> song song (searches) -> tuần tự (write) -> tuần tự (send email).

### Self-check questions
1. Tại sao các tác vụ lập kế hoạch và tổng hợp báo cáo lại bắt buộc phải chạy tuần tự mà không thể chạy song song?
2. Hãy mô tả cách bạn có thể tối ưu hóa pipeline bất đồng bộ để tránh lỗi Rate Limit khi số lượng truy vấn tìm kiếm tăng lên rất lớn.

### Flashcards
- Q: Cơ chế nào giúp gửi đồng loạt các request tìm kiếm web trong bài thực hành?
  A: Sử dụng hàm `asyncio.gather(*tasks)` trong Python.
- Q: Công cụ trực quan nào giúp đánh giá sự chênh lệch thời gian thực thi giữa tìm kiếm song song và tuần tự?
  A: Trang quản lý OpenAI Traces portal.

## 13. Missing Inputs - Còn thiếu gì
- Không có.
