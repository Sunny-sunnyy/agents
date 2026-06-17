# 86. Day 5 - Agentic AI - Add Web Search, File System & Python REPL to Your Assistant

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng trực tiếp từ `G:\Agent2026Win\agents\4_langgraph\sidekick_tools.py`, đối chiếu thêm với `G:\Agent2026Win\agents\4_langgraph\sidekick.py`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript 86 khớp trực tiếp với `sidekick_tools.py`, đặc biệt ở các capability mới: Serper web search, file management sandbox, Wikipedia tool và Python REPL. Không có mâu thuẫn nguồn; phần cảnh báo an toàn trong transcript phù hợp với việc `PythonREPLTool` không được sandbox như Docker ở các bài trước.

## 2. Executive Summary - Tóm tắt cốt lõi
- Day 5 mở đầu bằng việc nâng `Sidekick - trợ lý đồng nghiệp cá nhân` từ browser assistant thành agent có bộ tool mạnh hơn nhiều.
- Toolset mới gồm `web search - tìm kiếm web`, `file system access - truy cập hệ thống file trong sandbox`, `Wikipedia lookup - tra cứu Wikipedia`, `push notifications - thông báo đẩy`, và `Python REPL - môi trường chạy Python`.
- Instructor nhấn mạnh đây là một `experimental app - ứng dụng thử nghiệm`, chưa có guardrails hoàn chỉnh, nên phải dùng với sự thận trọng thực sự.
- `Playwright` vẫn bị giới hạn ở browser riêng không dùng cookies hay password manager cá nhân, còn `FileManagementToolkit` bị giới hạn trong `sandbox`, nhưng `PythonREPLTool` là capability mở hơn và rủi ro hơn.
- Tư duy quan trọng của lesson là xem sidekick như một `canvas - tấm nền`, không phải một sản phẩm đóng gói hoàn chỉnh.
- Giá trị của app nằm ở chỗ nó có thể đem lại `commercial benefit - giá trị thương mại` thật, nhưng chỉ sau quá trình thử nghiệm, tinh chỉnh prompt và chọn tool phù hợp với nhu cầu riêng.
- Đây là bước chuyển từ “demo workflow” sang “agent có thể làm việc thực tế trên máy của bạn”, đồng thời kéo theo trách nhiệm kỹ thuật và trách nhiệm an toàn lớn hơn.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu vì sao thêm nhiều tools làm agent mạnh hơn nhưng cũng nguy hiểm hơn.
  - Hiểu sự khác biệt giữa browser tool, file tool và Python execution tool về mức độ rủi ro.
  - Hiểu sidekick nên được xem như một khung nền để tùy biến, không phải một baseline hoàn hảo cho mọi người.
- Practical goals - mục tiêu thực hành:
  - Có thể thêm nhiều tools vào sidekick thông qua module riêng.
  - Có thể giới hạn file operations vào một thư mục root rõ ràng.
  - Biết capability nào nên tắt nếu chưa sẵn sàng về mặt an toàn.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao `PythonREPLTool` là tool nhạy cảm nhất trong set này.
  - `sandbox` bảo vệ điều gì và không bảo vệ điều gì.
  - Vì sao app cần được theo dõi, thử nghiệm và cá nhân hóa thêm trước khi dùng nghiêm túc.

## 4. Previous Context - Liên hệ với bài trước
Lesson này tiếp nối trực tiếp Day 4. Nếu Day 4 đã có sidekick với Playwright, evaluator và Gradio UI, thì Day 5 bắt đầu bằng cách tăng capability surface của cùng một sidekick. Nó tái dùng kiến thức từ Day 3 lesson 77 về custom tools và Serper search, từ Day 4 về browser automation, và đưa tất cả vào một phiên bản module hóa hơn thay vì notebook rời rạc.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: capability expansion - mở rộng năng lực công cụ
  - Meaning - nghĩa: Quá trình gắn thêm nhiều tools để agent không chỉ trả lời text mà còn tác động lên thế giới ngoài model.
  - Why it matters - vì sao quan trọng: Tool breadth quyết định loại công việc agent có thể làm thật cho người dùng.
  - Relationship - liên hệ với khái niệm khác: Đi cùng với tăng rủi ro và tăng nhu cầu giám sát.
- Term - thuật ngữ: guardrails - rào chắn an toàn
  - Meaning - nghĩa: Các giới hạn kỹ thuật hoặc policy để ngăn agent làm việc ngoài phạm vi mong muốn.
  - Why it matters - vì sao quan trọng: Khi agent có file access và Python execution, rủi ro không còn thuần túy ở mức trả lời sai.
  - Relationship - liên hệ với khái niệm khác: `sandbox` là guardrail cho file system; transcript nói rõ Python REPL chưa có guardrail tương đương Docker.
- Term - thuật ngữ: PythonREPLTool - công cụ chạy Python
  - Meaning - nghĩa: Tool cho phép model gửi code Python để thực thi và nhận kết quả trả về.
  - Why it matters - vì sao quan trọng: Nó tạo ra khả năng tính toán, xử lý dữ liệu, chuyển đổi nội dung và tự động hóa logic tại chỗ.
  - Relationship - liên hệ với khái niệm khác: Mạnh hơn tool search hay file tool, nhưng cũng rủi ro hơn do không sandbox riêng.
- Term - thuật ngữ: FileManagementToolkit - bộ công cụ quản lý file
  - Meaning - nghĩa: Tập tools từ LangChain Community cho phép tạo, đọc, sửa, ghi file trong một root directory xác định.
  - Why it matters - vì sao quan trọng: Cho phép sidekick tạo artifacts thực sự như báo cáo Markdown.
  - Relationship - liên hệ với khái niệm khác: Được cấu hình `root_dir="sandbox"` để giới hạn phạm vi.
- Term - thuật ngữ: canvas - tấm nền để tùy biến
  - Meaning - nghĩa: Cách nhìn sản phẩm hiện tại như nền tảng mở để người học tự thêm tools, prompt và workflow.
  - Why it matters - vì sao quan trọng: Tránh hiểu sai rằng lesson đang cung cấp một product hoàn chỉnh và an toàn mặc định.
  - Relationship - liên hệ với khái niệm khác: Dẫn trực tiếp đến yêu cầu experimentation trong các lesson sau.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - Sidekick baseline từ Day 4.
   - Environment variables cho các tools ngoài.
   - Nhu cầu thêm năng lực thực tế cho assistant.
2. Processing steps:
   - Giữ lại browser tools từ Playwright.
   - Thêm search tool dựa trên Serper.
   - Thêm file tools bị giới hạn trong `sandbox`.
   - Thêm Wikipedia tool.
   - Thêm Python REPL tool.
   - Gộp các capability thành toolset chung để sidekick sử dụng.
3. Output:
   - Một agent có thể tìm kiếm, duyệt web, ghi file, tra cứu và chạy Python.
4. Control flow / data flow:
   - Tool requests từ worker được route qua graph và `ToolNode`.
   - File outputs và Python execution tạo side effects thực tế trong máy cục bộ của người dùng.
5. Decision points:
   - Có giữ `PythonREPLTool` hay tắt nếu chưa sẵn sàng.
   - Có giữ browser tools hay giảm capability surface.
   - Root directory nào nên được cho phép cho file operations.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Capability layering - xếp lớp công cụ theo nhu cầu
  - Purpose - mục đích: Bổ sung dần năng lực cho agent thay vì nhồi tất cả từ đầu.
  - When to use - dùng khi nào: Khi chuyển từ prototype sang assistant phục vụ công việc thực tế.
  - Trade-off - đánh đổi: Toolset lớn hơn làm prompt và routing khó ổn định hơn.
  - Common mistake - lỗi dễ gặp: Thêm quá nhiều tools mà không quan sát agent dùng chúng ra sao.
- Technique - kỹ thuật: Sandboxed file root - giới hạn file trong thư mục gốc
  - Purpose - mục đích: Giảm phạm vi rủi ro khi agent được phép thao tác file.
  - When to use - dùng khi nào: Với mọi agent có file IO trên máy cục bộ.
  - Trade-off - đánh đổi: Agent không thể chạm tới tài liệu ngoài phạm vi root đã định.
  - Common mistake - lỗi dễ gặp: Cho file tool truy cập cả filesystem rộng mà không có lý do rõ ràng.
- Technique - kỹ thuật: High-risk tool opt-out - cho phép tắt tool rủi ro cao
  - Purpose - mục đích: Cân bằng utility và safety theo mức chấp nhận của người dùng.
  - When to use - dùng khi nào: Khi có tool như Python REPL, shell, browser automation hoặc external writes.
  - Trade-off - đánh đổi: Ít capability hơn, nhưng safety dễ kiểm soát hơn.
  - Common mistake - lỗi dễ gặp: Xem tool mạnh là bắt buộc dù use case không cần.

## 8. Code Walkthrough - Phân tích code nếu có
- File / block: tool imports và environment setup trong `sidekick_tools.py`
  - Purpose - mục đích: Tập trung toàn bộ capability definitions vào một module duy nhất.
  - Key logic - logic chính: Load `.env`, khởi tạo wrappers như Serper và chuẩn bị các tool factories.
  - Important lines / functions:
    - `load_dotenv(override=True)`
    - `serper = GoogleSerperAPIWrapper()`
    - imports của `FileManagementToolkit`, `WikipediaQueryRun`, `PythonREPLTool`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Module này là capability layer, tách khỏi graph logic và UI.
    - Cách tổ chức này giúp thêm/bớt tools không phải chạm nhiều vào orchestration code.
- File / block: file tools và Python REPL trong `sidekick_tools.py`
  - Purpose - mục đích: Cấp cho sidekick quyền ghi file trong `sandbox` và chạy Python.
  - Key logic - logic chính: `FileManagementToolkit(root_dir="sandbox")` giới hạn phạm vi file; `PythonREPLTool()` mở capability chạy code.
  - Important lines / functions:
    - `def get_file_tools():`
    - `toolkit = FileManagementToolkit(root_dir="sandbox")`
    - `python_repl = PythonREPLTool()`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - `sandbox` là guardrail thật sự cho file operations.
    - `PythonREPLTool` không có lớp cô lập tương tự Docker ở code hiện tại.
- File / block: bộ tool tổng hợp trong `other_tools()`
  - Purpose - mục đích: Gom tất cả capability ngoài Playwright thành một danh sách thống nhất.
  - Key logic - logic chính: Tạo `push_tool`, `search` tool, `wiki_tool`, `python_repl`, rồi trả về cùng file tools.
  - Important lines / functions:
    - `push_tool = Tool(...)`
    - `tool_search = Tool(name="search", func=serper.run, ...)`
    - `wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)`
    - `return file_tools + [push_tool, tool_search, python_repl, wiki_tool]`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Cấu trúc này làm transcript 86 nói đúng: chỉ cần thêm tool vào list là sidekick có capability mới.
    - Đây là nền cho việc người học tự mở rộng app bằng các tools khác.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Chỉ giữ browser + push tools
  - Pros: Ít rủi ro hơn, dễ quan sát hơn.
  - Cons: Agent khó tạo artifacts và ít linh hoạt hơn với tác vụ thực tế.
  - When to choose: Khi chỉ cần browser-assisted tasks.
- Option: Thêm file tools và search tools
  - Pros: Tạo báo cáo, lưu output, tra cứu nguồn nhanh hơn.
  - Cons: Tăng complexity và cần giám sát side effects trên filesystem.
  - When to choose: Khi agent cần tạo deliverables chứ không chỉ trả lời chat.
- Option: Thêm Python REPL
  - Pros: Rất mạnh cho tính toán, chuyển đổi và xử lý dữ liệu.
  - Cons: Rủi ro nhất trong toolset hiện tại vì không có sandbox riêng.
  - When to choose: Chỉ khi người dùng hiểu rõ rủi ro và thực sự cần capability này.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Gắn Python REPL mà không hiểu mức rủi ro
  - Root cause: Quá tập trung vào capability, bỏ qua side effects.
  - Symptom: Agent có thể thực thi code ngoài dự tính của người dùng.
  - Fix / prevention: Tắt tool này nếu chưa thoải mái, hoặc thêm sandbox/guardrails riêng.
- Failure mode: Tưởng sandbox bảo vệ toàn bộ hệ thống
  - Root cause: Nhầm giữa file root restriction và toàn bộ execution environment.
  - Symptom: Đánh giá thấp rủi ro của Python execution hoặc browser automation.
  - Fix / prevention: Phân biệt rõ file sandbox với process-level sandbox.
- Failure mode: Xem sidekick hiện tại là production-ready
  - Root cause: Thấy app làm được việc thật nên bỏ qua nhu cầu tinh chỉnh.
  - Symptom: Kỳ vọng quá cao rồi thất vọng khi agent đi chệch hoặc dùng tool chưa tối ưu.
  - Fix / prevention: Xem đây là canvas để chỉnh prompt, toolset và workflow theo use case riêng.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: Khi capability surface của agent tăng, độ khó lớn nhất không phải là “thêm tool nữa” mà là `tool governance - quản trị công cụ`: cho phép gì, chặn gì, log gì, rollback gì.
- Mở rộng: Một chiến lược an toàn thực tế là tách tools thành tiers: low-risk read-only, medium-risk write-sandboxed, high-risk execution, rồi chỉ mở tier cao khi user explicit consent.
- Mở rộng: Nhiều sản phẩm agent hiện đại thành công không phải vì model tốt hơn hẳn, mà vì capability orchestration và guardrails quanh tool use tốt hơn.

## 12. Study Pack - Gói ôn tập
### Must remember
- Day 5 bắt đầu bằng việc mở rộng sidekick bằng nhiều tools mới.
- `FileManagementToolkit(root_dir="sandbox")` giới hạn phạm vi file operations.
- `PythonREPLTool` là tool nhạy cảm nhất trong set hiện tại.
- Browser không dùng cookie/password cá nhân của trình duyệt chính.
- Sidekick là một canvas để tùy biến, không phải sản phẩm hoàn chỉnh.
- Càng nhiều capability, càng cần giám sát và tinh chỉnh prompt.

### Self-check questions
- Vì sao transcript đặc biệt cảnh báo về Python REPL?
- `sandbox` bảo vệ được phần nào của hệ thống?
- Vì sao agent có nhiều tool hơn chưa chắc đã tốt hơn ngay?
- Tại sao sidekick được gọi là canvas chứ không phải completed product?
- Khi nào bạn nên bỏ bớt tools khỏi app thay vì thêm tiếp?

### Flashcards
- Q: Tool nào rủi ro cao nhất trong lesson 86?
  A: `PythonREPLTool`.
- Q: File tools của sidekick bị giới hạn ở đâu?
  A: Trong thư mục `sandbox`.
- Q: Tư duy đúng về sidekick hiện tại là gì?
  A: Một nền tảng thử nghiệm và tùy biến, không phải sản phẩm sẵn dùng không cần chỉnh sửa.

### Interview Q&A nếu phù hợp
- Q: Tại sao mở rộng toolset vừa là cơ hội vừa là rủi ro trong agent systems?
  A: Vì toolset rộng tăng khả năng tạo giá trị thực, nhưng cũng mở ra nhiều side effects hơn và đòi hỏi guardrails tốt hơn.
- Q: Nếu phải giảm rủi ro nhanh nhất cho sidekick, bạn tắt gì trước?
  A: Tôi sẽ tắt `PythonREPLTool` trước, sau đó cân nhắc giảm browser/file tools nếu use case không thật sự cần.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide Day 5 cho lesson này.
- Không có tài liệu policy/guardrail riêng ngoài transcript và code.
- Chưa cần scan thêm file/folder khác ngoài `sandbox` vì code và transcript đã đủ để xác định capability boundaries.

# 87. Day 5 - LangChain Tool Integration - Building a Powerful AI Sidekick from Scratch

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng trực tiếp từ `G:\Agent2026Win\agents\4_langgraph\sidekick_tools.py` và `G:\Agent2026Win\agents\4_langgraph\sidekick.py`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript 87 bám trực tiếp vào hai module `sidekick_tools.py` và `sidekick.py`, mô tả đúng cách chuyển prototype notebook sang Python modules. Có một điểm đáng chú ý trong transcript: instructor thừa nhận cleanup resource của Playwright có thể còn cần refinement; code hiện tại cũng phản ánh sự dè dặt đó trong `cleanup()`.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này giới thiệu cách tái cấu trúc sidekick thành ba Python modules: `sidekick_tools.py`, `sidekick.py`, và `app.py`.
- `sidekick_tools.py` trở thành nơi định nghĩa toàn bộ tool layer, gồm Playwright tools, push notifications, file tools, Serper search, Wikipedia và Python REPL.
- `sidekick.py` chứa phần cốt lõi của agent: state schema, structured output schema, worker node, evaluator node, routers, graph builder và super-step runtime.
- `app.py` giữ Gradio UI và callback plumbing, để frontend không phải gánh graph logic trực tiếp.
- Transcript cũng dùng lesson này để bảo vệ workflow `prototype in notebook -> move to module`, coi đó là phù hợp với tính chất thực nghiệm của AI engineering.
- Sidekick class dùng `async setup()` tách khỏi `__init__` vì quá trình khởi tạo tools/browser/graph có thành phần async.
- Đây là bài học về `modularization - module hóa` và `separation of concerns - tách biệt trách nhiệm` hơn là chỉ thêm tool đơn lẻ.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu vì sao app được tách thành ba module thay vì giữ tất cả trong notebook.
  - Hiểu prototype-driven workflow phù hợp với AI engineering ra sao.
  - Hiểu cách `async setup` giải quyết giới hạn của `__init__` trong lớp có phụ thuộc async.
- Practical goals - mục tiêu thực hành:
  - Có thể chuyển một LangGraph notebook thành code modules rõ ràng hơn.
  - Có thể tổ chức tool layer, orchestration layer và UI layer riêng nhau.
  - Có thể tạo class-based wrapper cho graph runtime.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao `sidekick_tools.py` không nên chứa graph logic.
  - Vì sao `Sidekick.setup()` cần async còn `__init__` thì không.
  - Tại sao notebook-first rồi module hóa lại là workflow hợp lý ở dự án agent này.

## 4. Previous Context - Liên hệ với bài trước
Lesson này lấy trực tiếp sidekick notebook từ Day 4 và chuyển nó thành một hình thái code bền hơn. Nó nối mạch với Day 2-4 về `state`, `worker/evaluator`, `tool calling`, `checkpointer`, nhưng thay đổi lớn nằm ở packaging và maintainability. Đây là bước đầu của `productionizing - đưa prototype gần hơn tới dạng ứng dụng thực`, dù transcript vẫn nhấn mạnh app chưa hoàn thiện.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: modularization - module hóa
  - Meaning - nghĩa: Tách hệ thống thành các file/module có trách nhiệm rõ ràng.
  - Why it matters - vì sao quan trọng: Khi sidekick lớn lên, giữ tất cả trong notebook sẽ khó debug và khó mở rộng.
  - Relationship - liên hệ với khái niệm khác: Gắn chặt với `separation of concerns`.
- Term - thuật ngữ: separation of concerns - tách biệt trách nhiệm
  - Meaning - nghĩa: Mỗi module hoặc lớp chỉ nên xử lý một nhóm trách nhiệm rõ ràng.
  - Why it matters - vì sao quan trọng: Giúp thêm tools, sửa prompt hay đổi UI mà không phá toàn hệ thống.
  - Relationship - liên hệ với khái niệm khác: `sidekick_tools.py` lo capability, `sidekick.py` lo graph, `app.py` lo UI.
- Term - thuật ngữ: notebook-to-module workflow - quy trình từ notebook sang module
  - Meaning - nghĩa: Dùng notebook để thử nghiệm nhanh, rồi đóng gói kết quả ổn định hơn vào code modules.
  - Why it matters - vì sao quan trọng: Phản ánh đúng bản chất thử nghiệm, prompt tuning và iteration của AI engineering.
  - Relationship - liên hệ với khái niệm khác: Được instructor đối chiếu với tư duy software engineering truyền thống như TDD.
- Term - thuật ngữ: async setup - khởi tạo bất đồng bộ riêng
  - Meaning - nghĩa: Pattern tách phần initialization cần `await` ra khỏi constructor.
  - Why it matters - vì sao quan trọng: Constructor Python không thể trực tiếp là async, nhưng sidekick cần setup browser/tools/graph.
  - Relationship - liên hệ với khái niệm khác: `Sidekick.__init__()` chỉ chuẩn bị fields, còn `setup()` mới dựng fully usable instance.
- Term - thuật ngữ: resource cleanup - dọn dẹp tài nguyên
  - Meaning - nghĩa: Đóng browser, dừng Playwright và giải phóng stateful runtime resources khi app kết thúc.
  - Why it matters - vì sao quan trọng: Browser leaks là vấn đề thực tế khi agent dùng Playwright theo session.
  - Relationship - liên hệ với khái niệm khác: Thể hiện ở `cleanup()` và delete callback từ Gradio.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - Prototype sidekick từ notebook Day 4.
   - Nhu cầu chuyển sang application structure rõ hơn.
2. Processing steps:
   - Tách definitions của tools sang `sidekick_tools.py`.
   - Tách graph state, worker, evaluator, routing, build graph sang `sidekick.py`.
   - Tách Gradio UI và callbacks sang `app.py`.
   - Dùng `Sidekick.setup()` để dựng tools, LLMs và graph.
3. Output:
   - Một sidekick app module hóa rõ hơn, chạy bằng `uv run app.py`.
4. Control flow / data flow:
   - `app.py` khởi tạo `Sidekick`.
   - `Sidekick.setup()` gọi `playwright_tools()` và `other_tools()`.
   - `sidekick.py` xây graph và expose `run_superstep()`.
5. Decision points:
   - Cái gì thuộc tool layer, cái gì thuộc graph layer, cái gì thuộc UI.
   - Có dùng class wrapper hay giữ các hàm rời.
   - Khi nào cần resource cleanup chủ động.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Class-wrapped graph runtime - bọc graph runtime trong một class
  - Purpose - mục đích: Gom graph, tools, memory, browser handles và methods runtime vào một object có vòng đời rõ.
  - When to use - dùng khi nào: Khi app có session state, async setup và cleanup resources.
  - Trade-off - đánh đổi: Class có thể phình to nếu chưa refactor đủ sâu.
  - Common mistake - lỗi dễ gặp: Để class ôm quá nhiều trách nhiệm mà không có module boundaries rõ.
- Technique - kỹ thuật: Notebook-first experimentation
  - Purpose - mục đích: Cho phép prompt tuning và capability thử nghiệm nhanh hơn coding flow cứng.
  - When to use - dùng khi nào: Với tác vụ AI engineering nhiều trial-and-error.
  - Trade-off - đánh đổi: Cần bước module hóa sau đó để code maintainable hơn.
  - Common mistake - lỗi dễ gặp: Dừng ở notebook mãi và không chuyển sang cấu trúc code bền hơn.
- Technique - kỹ thuật: Async initialization split
  - Purpose - mục đích: Hợp thức hóa việc setup browser/tools/graph trong Python class.
  - When to use - dùng khi nào: Khi object cần async resources để usable.
  - Trade-off - đánh đổi: Người dùng class phải nhớ gọi `await setup()`.
  - Common mistake - lỗi dễ gặp: Tạo instance xong dùng ngay trước khi setup hoàn tất.

## 8. Code Walkthrough - Phân tích code nếu có
- File / block: `Sidekick.__init__` và `setup()` trong `sidekick.py`
  - Purpose - mục đích: Thiết lập vòng đời rõ cho instance sidekick.
  - Key logic - logic chính: Constructor tạo placeholders và memory; `setup()` lấy tools, bind LLMs, rồi build graph.
  - Important lines / functions:
    - `class Sidekick:`
    - `self.sidekick_id = str(uuid.uuid4())`
    - `self.memory = MemorySaver()`
    - `async def setup(self):`
    - `self.tools, self.browser, self.playwright = await playwright_tools()`
    - `self.tools += await other_tools()`
    - `await self.build_graph()`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - `__init__` chỉ chuẩn bị state ban đầu của object, chưa đủ để app chạy.
    - `setup()` là nơi thật sự dựng capability và graph executable.
- File / block: phân ranh module responsibilities
  - Purpose - mục đích: Giữ tool concerns, graph concerns và UI concerns không bị trộn.
  - Key logic - logic chính: `sidekick_tools.py` lo tools, `sidekick.py` lo runtime, `app.py` lo callbacks/UI.
  - Important lines / functions:
    - import từ `sidekick_tools` trong `sidekick.py`
    - import `Sidekick` trong `app.py`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Đây là chỗ lesson 87 nhấn mạnh code từ notebook được “đóng hộp” thành modules.
    - Mô hình này giúp thay toolset mà gần như không đổi phần Gradio.
- File / block: `cleanup()` trong `sidekick.py`
  - Purpose - mục đích: Giảm nguy cơ browser/process resources bị giữ lại sau session.
  - Key logic - logic chính: Đóng browser và stop Playwright qua running loop hoặc fallback `asyncio.run`.
  - Important lines / functions:
    - `def cleanup(self):`
    - `loop = asyncio.get_running_loop()`
    - `loop.create_task(self.browser.close())`
    - `loop.create_task(self.playwright.stop())`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Transcript nói đúng: phần cleanup này là chỗ còn cần quan sát thêm vì browser resources có thể chưa được dọn hoàn hảo trong mọi trường hợp.
    - Đây là technical debt được instructor chỉ ra khá thẳng thắn.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Giữ mọi thứ trong notebook
  - Pros: Nhanh cho thử nghiệm, dễ trình diễn.
  - Cons: Khó maintain, khó quản lý tài nguyên và khó mở rộng app.
  - When to choose: Chỉ cho giai đoạn rất sớm.
- Option: Tách thành ba modules như hiện tại
  - Pros: Rõ vai trò, dễ thêm tools và sửa UI độc lập hơn.
  - Cons: `sidekick.py` vẫn còn hơi to và có thể cần refactor tiếp.
  - When to choose: Đây là lựa chọn đúng cho Day 5.
- Option: Refactor sâu hơn thành nhiều lớp/khối nhỏ nữa
  - Pros: Bền hơn về dài hạn.
  - Cons: Tốn công hơn khi logic còn đang thay đổi nhanh.
  - When to choose: Khi sidekick bắt đầu ổn định hơn về capability và prompts.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Quên gọi `await setup()` sau khi tạo `Sidekick()`
  - Root cause: Nhìn class như object sync thông thường.
  - Symptom: Tools/graph chưa sẵn sàng khi app invoke.
  - Fix / prevention: Luôn coi `setup()` là bước bắt buộc của lifecycle.
- Failure mode: Refactor quá sớm theo chuẩn software truyền thống
  - Root cause: Áp mô hình production software vào lúc prompt/tool behavior còn dao động mạnh.
  - Symptom: Tốn công cấu trúc trong khi yêu cầu và prompt vẫn thay đổi liên tục.
  - Fix / prevention: Chấp nhận notebook-first rồi module hóa dần khi behavior đủ ổn.
- Failure mode: Bỏ qua cleanup resources
  - Root cause: Tập trung vào graph logic mà quên external resources như browser.
  - Symptom: Browser processes tồn đọng, memory leak hoặc session cleanup không sạch.
  - Fix / prevention: Gắn cleanup vào lifecycle UI/session rõ ràng.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: AI engineering thường yêu cầu `explore -> stabilize -> package -> harden`, khác nhịp với quy trình backend/web truyền thống vốn thường `spec -> implement -> test -> ship`.
- Mở rộng: Resourceful agents dùng browser, DB, file và external tools gần với “mini runtime system” hơn là một script đơn lẻ, nên module boundaries và lifecycle management càng sớm càng có giá trị.
- Mở rộng: Một dấu hiệu tốt của refactor là khi có thể thêm/bỏ tool trong capability layer mà UI và graph shell gần như không phải viết lại.

## 12. Study Pack - Gói ôn tập
### Must remember
- Day 5 sidekick được tách thành `sidekick_tools.py`, `sidekick.py`, `app.py`.
- `setup()` async tách khỏi `__init__`.
- Tool layer, graph layer và UI layer được phân ranh rõ hơn.
- Notebook-first rồi module hóa là workflow được lesson bảo vệ.
- `cleanup()` tồn tại vì sidekick dùng browser resources thật.
- `sidekick.py` hiện vẫn còn khá lớn và có thể refactor tiếp sau.

### Self-check questions
- Vì sao `__init__` không trực tiếp làm toàn bộ setup của sidekick?
- Lợi ích lớn nhất của việc tách `sidekick_tools.py` là gì?
- Vì sao instructor vẫn thích notebook ở giai đoạn đầu?
- `cleanup()` đang cố giải quyết loại vấn đề gì?
- Khi nào nên refactor `sidekick.py` sâu hơn nữa?

### Flashcards
- Q: Ba module chính của sidekick Day 5 là gì?
  A: `sidekick_tools.py`, `sidekick.py`, và `app.py`.
- Q: `Sidekick.setup()` làm gì?
  A: Lấy tools, bind LLMs và build graph để sidekick usable.
- Q: Vì sao cần `cleanup()`?
  A: Để dọn browser và Playwright resources gắn với session sidekick.

### Interview Q&A nếu phù hợp
- Q: Tại sao notebook-first hợp lý trong agent development?
  A: Vì prompt tuning, tool behavior và routing thường cần thử nghiệm nhanh nhiều vòng trước khi đóng gói thành code bền hơn.
- Q: Khi nào một class-based wrapper như `Sidekick` đáng dùng?
  A: Khi runtime có nhiều tài nguyên và lifecycle state như tools, memory, browser, graph và cleanup logic.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide Day 5 cho lesson này.
- Không có diagram module architecture ngoài transcript mô tả bằng lời.
- Không cần scan thêm code ngoài ba module chính để tổng hợp lesson này.

# 88. Day 5 - Creating AI Workflows - Graph Builders & Node Communication Techniques

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng trực tiếp từ `G:\Agent2026Win\agents\4_langgraph\sidekick.py`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript 88 khớp trực tiếp với các phần `State`, `EvaluatorOutput`, `worker`, `worker_router`, `format_conversation`, `evaluator`, `route_based_on_evaluation`, `build_graph()` và `run_superstep()` trong `sidekick.py`.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này đi sâu vào `sidekick.py`, nơi toàn bộ graph workflow của sidekick được hiện thực hóa trong một class.
- State của graph vẫn kế thừa thiết kế Day 4: `messages`, `success_criteria`, `feedback_on_work`, `success_criteria_met`, `user_input_needed`.
- Worker prompt được tinh chỉnh mạnh hơn notebook version: thêm `current date and time - ngày giờ hiện tại` trực tiếp vào prompt, thêm chỉ dẫn cụ thể cho `PythonREPLTool` phải dùng `print()` nếu muốn nhận output.
- Transcript dùng đây như ví dụ điển hình cho tính `experimental - thực nghiệm` của AI engineering: prompt phải sửa theo lỗi quan sát được chứ không theo quy tắc trừu tượng cố định.
- Evaluator prompt cũng được tinh chỉnh để `give the assistant the benefit of the doubt - cho assistant hưởng lợi của nghi ngờ`, nhất là khi assistant nói đã ghi file.
- `build_graph()` tạo ba nodes chính: `worker`, `tools`, `evaluator`, rồi nối chúng bằng một tool loop và một evaluation loop.
- `run_superstep()` là hàm runtime thật sự biến UI input thành initial state, invoke graph và dựng lại history hiển thị cho frontend.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu node communication trong sidekick diễn ra qua state fields như thế nào.
  - Hiểu cách graph builder trong module giữ nguyên mental model từ notebook nhưng production-like hơn.
  - Hiểu prompt engineering thực nghiệm gắn trực tiếp vào runtime workflow.
- Practical goals - mục tiêu thực hành:
  - Có thể đọc và sửa `worker` prompt theo hành vi tool thực tế.
  - Có thể đọc evaluator node và hiểu state update nào chi phối routing.
  - Có thể theo từ UI input tới graph state tới final history output.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao current time được chèn vào prompt thay vì làm thành tool.
  - Vì sao worker cần biết `print()` mới lấy được output từ Python REPL.
  - `build_graph()` và `run_superstep()` nối với nhau ra sao.

## 4. Previous Context - Liên hệ với bài trước
Lesson này nối thẳng Day 4 lesson 83-85 nhưng ở phiên bản module hóa hơn và mạnh hơn về capability. Nó giữ nguyên worker-evaluator pattern, checkpointer và state design từ Day 4, đồng thời cho thấy khi toolset tăng lên thì prompt cũng phải được nâng cấp theo. Nó cũng là cầu nối tự nhiên giữa Day 4 “graph demo” và Day 5 “working local agent app”.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: resource vs tool - tài nguyên so với công cụ
  - Meaning - nghĩa: Có những thông tin nên chèn trực tiếp vào prompt như current date/time thay vì biến thành tool call.
  - Why it matters - vì sao quan trọng: Không phải mọi capability đều nên được mô hình hóa như tool.
  - Relationship - liên hệ với khái niệm khác: Transcript dùng current datetime làm ví dụ điển hình.
- Term - thuật ngữ: tool-specific prompt grounding - neo prompt theo đặc tính từng tool
  - Meaning - nghĩa: Bổ sung hướng dẫn riêng cho tool behavior gây lỗi lặp lại, như Python REPL cần `print()`.
  - Why it matters - vì sao quan trọng: Tool abstractions không đảm bảo model luôn hiểu chính xác cách dùng chúng.
  - Relationship - liên hệ với khái niệm khác: Đây là tinh chỉnh dựa trên quan sát thực tế, không chỉ trên docs.
- Term - thuật ngữ: worker-evaluator graph - đồ thị worker-evaluator
  - Meaning - nghĩa: Workflow trong đó worker tạo output/tool calls, evaluator chấm rồi route tiếp.
  - Why it matters - vì sao quan trọng: Đây là “bộ não” cốt lõi của sidekick.
  - Relationship - liên hệ với khái niệm khác: Gồm `worker`, `ToolNode`, `evaluator`, và các routers.
- Term - thuật ngữ: super-step runtime wrapper - lớp bọc runtime cho siêu bước
  - Meaning - nghĩa: Hàm `run_superstep()` đóng vai trò chuẩn hóa mỗi lần invoke graph từ phía app.
  - Why it matters - vì sao quan trọng: UI không cần biết chi tiết graph internals, chỉ cần gọi wrapper này.
  - Relationship - liên hệ với khái niệm khác: Dùng state defaults, thread id và result unpacking.
- Term - thuật ngữ: prompt refinement - tinh chỉnh prompt
  - Meaning - nghĩa: Điều chỉnh prompt sau khi quan sát lỗi thực tế của model/tool interaction.
  - Why it matters - vì sao quan trọng: Là cách chính để cải thiện coherence của sidekick ở giai đoạn này.
  - Relationship - liên hệ với khái niệm khác: Xuất hiện ở cả worker lẫn evaluator prompts.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - User message.
   - Success criteria.
   - Toolset đã được setup.
2. Processing steps:
   - Worker prompt được build từ current time, success criteria và feedback nếu có.
   - Worker chạy và có thể gọi tools.
   - `worker_router` chọn `tools` hoặc `evaluator`.
   - Evaluator đọc conversation + criteria + final response.
   - `route_based_on_evaluation` chọn quay lại worker hoặc kết thúc.
   - `run_superstep()` trả history đã dựng cho UI.
3. Output:
   - History mới gồm user message, worker reply và evaluator feedback.
4. Control flow / data flow:
   - State là kênh giao tiếp duy nhất giữa nodes.
   - `messages` tích lũy qua reducer; flags và feedback ghi đè theo vòng loop.
5. Decision points:
   - Có cần tool call không.
   - Đã đạt success criteria chưa.
   - Có cần user input không.
   - Prompt có cần thêm grounding riêng cho tool behavior nào không.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Inline resource injection - chèn resource trực tiếp vào prompt
  - Purpose - mục đích: Cung cấp thông tin luôn-cần mà không tốn tool call.
  - When to use - dùng khi nào: Với date/time, mode flags, hoặc session facts ổn định.
  - Trade-off - đánh đổi: Prompt dài hơn và thông tin được refresh theo mỗi call.
  - Common mistake - lỗi dễ gặp: Biến mọi thứ thành tool dù nó chỉ là context tĩnh nên đưa thẳng vào prompt.
- Technique - kỹ thuật: Tool-behavior patching bằng prompt
  - Purpose - mục đích: Sửa lệch nhận thức của model về cách tool hoạt động.
  - When to use - dùng khi nào: Khi model lặp lại một hiểu nhầm cụ thể với tool.
  - Trade-off - đánh đổi: Prompt ngày càng dài và hơi “fragile” nếu tool đổi behavior.
  - Common mistake - lỗi dễ gặp: Cố sửa hoàn toàn bằng code wrapper khi vấn đề thực ra là prompt grounding.
- Technique - kỹ thuật: State-mediated node communication - giao tiếp giữa nodes qua state
  - Purpose - mục đích: Giữ graph reasoning minh bạch và route dựa trên state thay vì biến cục bộ.
  - When to use - dùng khi nào: Với mọi multi-node LangGraph workflow.
  - Trade-off - đánh đổi: Cần thiết kế state fields rõ semantics.
  - Common mistake - lỗi dễ gặp: Để quá nhiều ngầm định ở vị trí `messages[-1]`, `messages[-2]` mà không chuẩn hóa thêm.

## 8. Code Walkthrough - Phân tích code nếu có
- File / block: worker prompt trong `sidekick.py`
  - Purpose - mục đích: Điều phối toàn bộ tool-using behavior của sidekick.
  - Key logic - logic chính: Chèn current datetime, success criteria, Python REPL note và feedback loop hints vào system prompt.
  - Important lines / functions:
    - `The current date and time is {datetime.now().strftime(...)}`
    - `You have a tool to run python code, but note that you would need to include a print() statement...`
    - `if state.get("feedback_on_work"):`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - `datetime` được coi là resource nên đưa thẳng vào prompt, không cần tool.
    - Dòng về `print()` là ví dụ rất điển hình của prompt patch dựa trên lỗi thật quan sát được.
- File / block: evaluator prompt và state update
  - Purpose - mục đích: Đánh giá output của worker trong bối cảnh có file-writing và nhiều tools hơn.
  - Key logic - logic chính: Cho evaluator lợi ích của nghi ngờ với việc assistant nói đã ghi file, rồi trả structured state.
  - Important lines / functions:
    - `The Assistant has access to a tool to write files...`
    - `eval_result = self.evaluator_llm_with_output.invoke(evaluator_messages)`
    - `"feedback_on_work": eval_result.feedback`
    - `"success_criteria_met": eval_result.success_criteria_met`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Transcript nói rõ evaluator trước đó quá khắt khe nên prompt này được thêm để giảm false rejections.
    - Đây là ví dụ về evaluator cũng cần tuning chứ không chỉ worker.
- File / block: `build_graph()` và `run_superstep()`
  - Purpose - mục đích: Nối graph definition với runtime invocation thực tế.
  - Key logic - logic chính: Dựng nodes/edges/checkpointer rồi cung cấp wrapper `run_superstep()` cho app.
  - Important lines / functions:
    - `graph_builder.add_node("worker", self.worker)`
    - `graph_builder.add_node("tools", ToolNode(tools=self.tools))`
    - `graph_builder.add_node("evaluator", self.evaluator)`
    - `self.graph = graph_builder.compile(checkpointer=self.memory)`
    - `result = await self.graph.ainvoke(state, config=config)`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - `build_graph()` là phase định nghĩa; `run_superstep()` là phase thực thi.
    - Đây là nhịp execution quen thuộc của LangGraph nhưng nay đã được đóng trong class.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Đưa current time thành tool
  - Pros: Rõ ràng hơn về capability.
  - Cons: Tốn tool call không cần thiết và còn phải ép model nhớ dùng tool.
  - When to choose: Hiếm khi đáng dùng trong trường hợp này.
- Option: Chèn current time trực tiếp vào prompt
  - Pros: Đơn giản, rẻ, luôn sẵn.
  - Cons: Làm prompt dài thêm chút ít.
  - When to choose: Đây là lựa chọn đúng của lesson.
- Option: Tinh chỉnh tool behavior qua prompt
  - Pros: Nhanh, hiệu quả khi bug nằm ở model understanding.
  - Cons: Có thể trở nên vá víu nếu lạm dụng quá nhiều.
  - When to choose: Khi quan sát được lỗi lặp có pattern rõ ràng như Python REPL output.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Biến current datetime thành một tool riêng
  - Root cause: Cực đoan hóa tư duy “mọi capability đều là tool”.
  - Symptom: Model có thể quên gọi tool hoặc tốn call vô ích.
  - Fix / prevention: Với resource luôn-cần, chèn thẳng vào prompt.
- Failure mode: Python REPL trả output trống khiến worker lặp vô ích
  - Root cause: Model không biết phải dùng `print()` mới nhận được text trả về.
  - Symptom: Worker thử đi thử lại hoặc hiểu sai tool result.
  - Fix / prevention: Grounding rõ trong prompt hoặc bọc tool với behavior rõ hơn.
- Failure mode: Evaluator quá cứng và reject cả khi worker đã làm xong việc thực tế
  - Root cause: Prompt evaluator thiếu hướng dẫn về mức độ tin tưởng hợp lý.
  - Symptom: Loop kéo dài, user thấy app có vẻ “khó tính vô ích”.
  - Fix / prevention: Cho evaluator benefit-of-the-doubt trong các trường hợp như file creation claims.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: Một khác biệt lớn giữa classic software workflows và agent workflows là `behavior patching` nhiều khi diễn ra ở prompt layer, không phải code layer.
- Mở rộng: Khi toolset lớn hơn, `context engineering - kỹ thuật điều phối ngữ cảnh` trở thành năng lực quan trọng không kém code orchestration.
- Mở rộng: Việc xác định cái gì là tool, cái gì là resource, cái gì là state, cái gì là prompt hint là một trong những kỹ năng thiết kế agent quan trọng nhất.

## 12. Study Pack - Gói ôn tập
### Must remember
- `sidekick.py` là nơi sidekick graph thực sự sống.
- Worker prompt được thêm current time trực tiếp.
- Worker được nhắc riêng về `print()` cho Python REPL.
- Evaluator cũng được tuning để bớt reject oan.
- `build_graph()` định nghĩa workflow; `run_superstep()` thực thi workflow.
- Giao tiếp giữa nodes vẫn hoàn toàn qua state.

### Self-check questions
- Vì sao current date/time không nên là tool trong lesson này?
- Tại sao worker bị nhắc phải dùng `print()` với Python REPL?
- `feedback_on_work` ảnh hưởng tới worker prompt như thế nào?
- Điều gì khiến evaluator cho “benefit of the doubt” quan trọng hơn ở Day 5?
- `run_superstep()` khác `build_graph()` ở vai trò nào?

### Flashcards
- Q: `run_superstep()` làm gì?
  A: Nó dựng initial state, invoke graph và trả history mới cho UI.
- Q: Worker router trong sidekick chọn giữa gì?
  A: `tools` hoặc `evaluator`.
- Q: Tại sao evaluator prompt nhắc rằng assistant có thể thật sự đã ghi file?
  A: Để giảm việc evaluator reject những tác vụ file-write mà assistant đã thực hiện.

### Interview Q&A nếu phù hợp
- Q: Khi nào một thông tin nên được coi là resource thay vì tool?
  A: Khi nó luôn cần sẵn, rẻ để chèn trực tiếp, và không đáng để model phải “nhớ” gọi một tool riêng chỉ để lấy nó.
- Q: Nếu model hiểu sai cách một tool hoạt động, bạn sửa ở đâu trước?
  A: Tôi sẽ xem trước ở prompt grounding, rồi mới cân nhắc thay wrapper/tool description nếu prompt fix không đủ.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide cho lesson này.
- Không có unit tests hoặc logs chi tiết ngoài transcript để đối chiếu các prompt patches.
- Không cần scan thêm file nào khác ngoài `sidekick.py` cho lesson này.

# 89. Day 5 - Creating Isolated User Sessions in Gradio Apps Using State Management

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng trực tiếp từ `G:\Agent2026Win\agents\4_langgraph\app.py`, đối chiếu thêm với `G:\Agent2026Win\agents\4_langgraph\sidekick.py`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript 89 khớp trực tiếp với `gr.State(delete_callback=free_resources)`, `ui.load(setup, ...)`, `process_message`, `reset`, và callback wiring trong `app.py`. Không có mâu thuẫn nguồn.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này tập trung vào `session isolation - cô lập phiên người dùng` trong Gradio app của sidekick.
- Thay vì để nhiều người dùng chia sẻ cùng một object toàn cục, app dùng `gr.State` để gắn mỗi session với một `Sidekick` instance riêng.
- `ui.load(setup, [], [sidekick])` là callback quan trọng: khi một UI session mới được mở, nó tạo sidekick riêng cho session đó.
- `delete_callback=free_resources` được dùng để dọn các tài nguyên đi kèm như browser/Playwright khi state bị hủy.
- `process_message` nhận sidekick instance từ state, gọi `run_superstep()` rồi trả lại cả history lẫn sidekick để session giữ continuity.
- Transcript chỉ ra đây là một cải tiến quan trọng so với nhiều app Gradio đơn giản trước đó, nơi nhiều người dùng có thể vô tình dùng chung biến và làm lẫn state.
- Đây là bài học về `stateful app plumbing - đường ống ứng dụng có trạng thái` nhiều hơn là về graph logic mới.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu vì sao Gradio state cần gắn với từng user session.
  - Hiểu lifecycle của sidekick instance từ `load` đến `delete_callback`.
  - Hiểu callback-based mental model của Gradio.
- Practical goals - mục tiêu thực hành:
  - Có thể dùng `gr.State` để giữ một object runtime phức tạp.
  - Có thể setup app để mỗi người dùng có graph/browser/state riêng.
  - Có thể reset session bằng việc tạo instance sidekick mới.
- What learner should be able to explain - người học cần giải thích được:
  - `ui.load()` làm gì trong bài này.
  - Vì sao `free_resources()` liên quan trực tiếp tới session management.
  - Tại sao một app dùng biến toàn cục sẽ dễ gặp lỗi khi có nhiều user.

## 4. Previous Context - Liên hệ với bài trước
Lesson này kế thừa trực tiếp lesson 85 của Day 4 và lesson 87-88 của Day 5, nơi sidekick đã có runtime state, browser handle và graph memory riêng. Khi app còn là notebook demo, session isolation có thể bị xem nhẹ; nhưng khi chuyển sang module app có thể nhiều người dùng truy cập, state management ở frontend/backend layer trở thành bắt buộc.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Gradio state - trạng thái gắn với phiên Gradio
  - Meaning - nghĩa: Cơ chế của Gradio để giữ object/data qua các callbacks trong một phiên giao diện cụ thể.
  - Why it matters - vì sao quan trọng: Cho phép mỗi người dùng có runtime riêng mà không chia sẻ object toàn cục.
  - Relationship - liên hệ với khái niệm khác: Ở đây state giữ cả `Sidekick` instance.
- Term - thuật ngữ: load callback - callback lúc giao diện được tải
  - Meaning - nghĩa: Hàm được Gradio gọi khi một session mới mở ra.
  - Why it matters - vì sao quan trọng: Đây là điểm sidekick instance được tạo và setup cho session đó.
  - Relationship - liên hệ với khái niệm khác: Gắn với `ui.load(setup, ...)`.
- Term - thuật ngữ: delete callback - callback lúc state bị xóa
  - Meaning - nghĩa: Hàm được gọi để cleanup tài nguyên khi state/session bị dọn.
  - Why it matters - vì sao quan trọng: Sidekick không chỉ là data object; nó còn giữ browser/runtime resources.
  - Relationship - liên hệ với khái niệm khác: Gọi `sidekick.cleanup()`.
- Term - thuật ngữ: callback plumbing - đường ống callback
  - Meaning - nghĩa: Mô hình kết nối inputs/outputs của Gradio để frontend events gọi backend logic.
  - Why it matters - vì sao quan trọng: Hiểu được điều này thì mới hiểu sidekick được invoke từ UI ra sao.
  - Relationship - liên hệ với khái niệm khác: `go_button.click`, `message.submit`, `success_criteria.submit`.
- Term - thuật ngữ: per-session runtime object - đối tượng runtime theo từng phiên
  - Meaning - nghĩa: Mỗi session giữ instance riêng của object logic backend.
  - Why it matters - vì sao quan trọng: Rất quan trọng cho agents có memory và external resources như browser.
  - Relationship - liên hệ với khái niệm khác: `Sidekick` instance là ví dụ cụ thể của lesson.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - Một người dùng mở Gradio UI.
2. Processing steps:
   - `ui.load()` gọi `setup()`.
   - `setup()` tạo `Sidekick()` rồi `await sidekick.setup()`.
   - Sidekick instance được lưu vào `gr.State`.
   - User nhập message hoặc success criteria, callback `process_message` được gọi.
   - Callback dùng đúng sidekick instance của session đó để chạy `run_superstep()`.
   - Khi reset, app tạo sidekick mới và trả object mới vào state.
   - Khi state bị dọn, `free_resources()` gọi `cleanup()`.
3. Output:
   - Mỗi user session có sidekick riêng, memory riêng và cleanup riêng.
4. Control flow / data flow:
   - Frontend event -> Gradio callback -> session-specific sidekick instance -> graph runtime -> updated state/UI.
5. Decision points:
   - Có lưu sidekick trong session state hay dùng global singleton.
   - Có cleanup resources khi session chết hay không.
   - Reset session sẽ xóa text/history thôi hay tạo runtime object mới hoàn toàn.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Session-bound backend object - gắn object backend theo phiên
  - Purpose - mục đích: Tránh lẫn memory và browser state giữa người dùng.
  - When to use - dùng khi nào: Với mọi agent app có runtime state không thể chia sẻ.
  - Trade-off - đánh đổi: Tốn tài nguyên hơn vì mỗi session có instance riêng.
  - Common mistake - lỗi dễ gặp: Dùng một object sidekick chung cho mọi session.
- Technique - kỹ thuật: Lifecycle-aware cleanup - dọn dẹp theo vòng đời session
  - Purpose - mục đích: Hạn chế browser/resource leaks.
  - When to use - dùng khi nào: Khi object state giữ external handles như browser, DB connection hoặc worker threads.
  - Trade-off - đánh đổi: Cleanup logic phải robust với nhiều trường hợp loop đang/chưa chạy.
  - Common mistake - lỗi dễ gặp: Chỉ reset UI mà không cleanup backend resources.
- Technique - kỹ thuật: Callback-first UI architecture
  - Purpose - mục đích: Giữ UI wiring rõ ràng và không nhét graph logic trực tiếp vào frontend definitions.
  - When to use - dùng khi nào: Với Gradio và các UI frameworks dạng callback.
  - Trade-off - đánh đổi: Cần hiểu mapping input/output state khá kỹ.
  - Common mistake - lỗi dễ gặp: Wiring outputs sai, khiến state hoặc history không được giữ đúng.

## 8. Code Walkthrough - Phân tích code nếu có
- File / block: Gradio state và setup lifecycle trong `app.py`
  - Purpose - mục đích: Cấp cho mỗi session một sidekick riêng.
  - Key logic - logic chính: Dùng `gr.State` để giữ object, `ui.load()` để setup lúc session mở.
  - Important lines / functions:
    - `sidekick = gr.State(delete_callback=free_resources)`
    - `ui.load(setup, [], [sidekick])`
    - `async def setup():`
    - `sidekick = Sidekick()`
    - `await sidekick.setup()`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Đây là nơi session mới được gắn với runtime riêng.
    - `setup()` trả object đã fully initialized chứ không chỉ object rỗng.
- File / block: `process_message` callback
  - Purpose - mục đích: Nối UI inputs với graph super-step runtime của sidekick.
  - Key logic - logic chính: Nhận `sidekick`, `message`, `success_criteria`, `history`, gọi `run_superstep()`, rồi trả `results, sidekick`.
  - Important lines / functions:
    - `async def process_message(sidekick, message, success_criteria, history):`
    - `results = await sidekick.run_superstep(message, success_criteria, history)`
    - `return results, sidekick`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Callback không tự build graph; nó chỉ điều phối đúng sidekick instance của session hiện tại.
    - Việc trả lại `sidekick` vào outputs giữ state nhất quán theo mô hình Gradio.
- File / block: reset và cleanup
  - Purpose - mục đích: Tạo lại session state sạch và dọn tài nguyên cũ.
  - Key logic - logic chính: `reset()` dựng sidekick mới; `free_resources()` gọi cleanup an toàn.
  - Important lines / functions:
    - `async def reset():`
    - `new_sidekick = Sidekick()`
    - `await new_sidekick.setup()`
    - `def free_resources(sidekick):`
    - `sidekick.cleanup()`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Reset không chỉ xóa fields mà thay cả backend runtime object.
    - `free_resources()` là defense line quan trọng với browser-based agents.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Session-specific sidekick instances
  - Pros: An toàn hơn, memory sạch, multi-user đúng nghĩa.
  - Cons: Tốn setup và resource mỗi phiên.
  - When to choose: Đây là lựa chọn đúng cho app kiểu này.
- Option: Global singleton sidekick
  - Pros: Đơn giản hơn về code và ít setup lặp.
  - Cons: State lẫn giữa users, cleanup khó, browser/resources chia sẻ nguy hiểm.
  - When to choose: Hầu như không nên dùng cho app multi-user.
- Option: Reset chỉ xóa history UI
  - Pros: Nhanh.
  - Cons: Backend memory/browser state có thể vẫn sống và gây lẫn hành vi.
  - When to choose: Chỉ khi backend object thật sự stateless, mà sidekick thì không phải vậy.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Dùng chung sidekick instance cho nhiều người
  - Root cause: Không gắn runtime object vào session state.
  - Symptom: Memory, browser context hoặc tasks của người này lẫn với người khác.
  - Fix / prevention: Mỗi session phải có `Sidekick()` riêng.
- Failure mode: Browser leaks sau nhiều lần mở/đóng session
  - Root cause: Không gắn delete callback hoặc cleanup chưa đủ chắc.
  - Symptom: Chromium processes còn tồn tại sau khi session đã rời đi.
  - Fix / prevention: Gọi cleanup theo lifecycle và tiếp tục theo dõi resource behavior như transcript khuyến nghị.
- Failure mode: Wiring callback outputs không đúng
  - Root cause: Không hiểu Gradio state propagation.
  - Symptom: Sidekick state không được giữ hoặc history không update đúng.
  - Fix / prevention: Kiểm tra kỹ input/output mapping của từng callback.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: Session isolation là một yêu cầu kiến trúc thực sự, không phải chi tiết UI. Nó quyết định correctness của cả memory semantics và external side effects.
- Mở rộng: Với stateful agents, frontend framework chỉ là vỏ; thứ quan trọng hơn là lifecycle management của backend object mà frontend đang giữ tham chiếu tới.
- Mở rộng: Khi app chuyển lên production, các session-bound objects như sidekick thường cần thêm timeout/TTL, cleanup sweeper và resource quotas.

## 12. Study Pack - Gói ôn tập
### Must remember
- Gradio `State` được dùng để giữ `Sidekick` riêng cho từng session.
- `ui.load(setup, ...)` tạo sidekick lúc giao diện mở.
- `delete_callback=free_resources` dùng để cleanup resources.
- `process_message` gọi `run_superstep()` trên đúng sidekick của session.
- Reset tạo `Sidekick` mới thay vì chỉ xóa UI.
- Session isolation là bắt buộc cho app sidekick nhiều người dùng.

### Self-check questions
- Vì sao sidekick không nên là biến toàn cục chung?
- `ui.load()` giúp giải quyết bài toán gì trong lesson này?
- Khác nhau giữa reset UI và reset backend runtime là gì?
- Vì sao cleanup được gắn vào `delete_callback`?
- Nếu nhiều session dùng chung browser resources thì vấn đề gì có thể phát sinh?

### Flashcards
- Q: `gr.State` giữ gì trong lesson 89?
  A: Một instance `Sidekick` gắn với phiên người dùng hiện tại.
- Q: `ui.load(setup, [], [sidekick])` làm gì?
  A: Nó khởi tạo sidekick khi session UI được mở và lưu nó vào session state.
- Q: `free_resources()` dùng để làm gì?
  A: Dọn cleanup cho sidekick và các tài nguyên như browser/Playwright.

### Interview Q&A nếu phù hợp
- Q: Tại sao session isolation lại đặc biệt quan trọng với agent apps?
  A: Vì agent apps không chỉ giữ text history, mà còn giữ memory, resources, và side effects gắn với từng người dùng.
- Q: Khi nào bạn cần lifecycle cleanup chủ động trong một app LLM?
  A: Khi app tạo external resources như browser sessions, DB handles, workers hoặc temporary runtimes.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide cho lesson này.
- Không có instrumentation riêng để xác nhận cleanup luôn thành công trong mọi trường hợp.
- Không cần scan thêm file/folder khác ngoài `app.py` và liên kết tới `sidekick.py`.

# 90. Day 5 - Inside AI Feedback Loops - Seeing How AI Evaluates & Corrects Errors

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng trực tiếp từ `G:\Agent2026Win\agents\4_langgraph\sidekick.py`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Ngoài code, tôi đã scan bổ sung `G:\Agent2026Win\agents\4_langgraph\sandbox\dinner.md` vì transcript 90 mô tả rõ sidekick đã tạo và cập nhật file báo cáo trong sandbox. Scan này cần thiết để xác nhận project context thực tế liên quan trực tiếp đến lesson.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này cho người học nhìn trực tiếp vào `feedback loop - vòng lặp phản hồi` bên trong sidekick thông qua các ví dụ thực chạy.
- Ví dụ `pi times three` cho thấy worker dùng web search rồi Python REPL, evaluator reject vì độ chính xác chưa đủ, worker thử lại, mắc syntax error, rồi sửa và cuối cùng được chấp nhận.
- Đây là minh họa rất rõ rằng evaluator không chỉ “chấm cho vui”, mà có thể buộc worker lặp lại công việc cho tới khi output đạt success criteria.
- Ví dụ nhà hàng Pháp ở New York cho thấy sidekick vừa tìm thông tin, vừa ghi báo cáo Markdown ra file, vừa gửi push notification và vẫn nhớ được file đã tạo trước đó ở turn sau.
- Transcript đặc biệt nhấn mạnh sidekick có thể cập nhật file cũ dựa trên memory checkpointing, dù user chỉ nói “the file” mà không nhắc tên file.
- `dinner.md` trong `sandbox` xác nhận sidekick thực sự tạo artifact Markdown có cấu trúc, không chỉ nói miệng rằng đã làm.
- Lesson này là phần “inside the machine” quan trọng nhất của Day 5 vì nó cho thấy quality loop, tool loop, memory và artifact creation cùng làm việc trong một system.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu feedback loop nội bộ giúp sửa lỗi tool use và độ chính xác ra sao.
  - Hiểu evaluator có thể reject cả lỗi nhỏ như thiếu precision.
  - Hiểu checkpointing cho phép follow-up actions trên artifacts đã tạo ở turn trước.
- Practical goals - mục tiêu thực hành:
  - Có thể đọc trace mental model của một agent từ prompt đến tool calls đến evaluator feedback.
  - Có thể dùng sidekick để tạo/cập nhật file báo cáo thực tế trong sandbox.
  - Có thể quan sát khi nào evaluator nên nghiêm khắc và khi nào worker nên thử lại.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao ví dụ `pi times three` đã loop nhiều bước trước khi trả kết quả đúng.
  - Vì sao sidekick nhớ được file `dinner.md` ở lần chỉnh sửa sau.
  - Làm sao worker, tools, evaluator và checkpointing cùng phối hợp trong ví dụ nhà hàng.

## 4. Previous Context - Liên hệ với bài trước
Lesson này là phần “runtime proof” cho những gì Day 4 lesson 84 và Day 5 lesson 88 đã xây. Nếu Day 4 giải thích worker-evaluator loop về mặt lý thuyết và code, thì lesson 90 cho thấy nó vận hành thật: evaluator reject, worker retry, tools được gọi lại, rồi final answer mới được chấp nhận. Nó cũng nối với Day 3 checkpointing lessons khi sidekick nhớ và cập nhật file đã tạo ở turn trước.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: evaluator rejection loop - vòng lặp evaluator từ chối
  - Meaning - nghĩa: Trường hợp evaluator không chấp nhận output hiện tại và buộc worker làm tiếp.
  - Why it matters - vì sao quan trọng: Đây là cơ chế sửa sai nội bộ của sidekick.
  - Relationship - liên hệ với khái niệm khác: Kích hoạt route từ evaluator quay về worker.
- Term - thuật ngữ: precision-sensitive criteria - tiêu chí nhạy với độ chính xác
  - Meaning - nghĩa: Success criteria mà evaluator có thể dùng để reject câu trả lời đúng ý nhưng chưa đủ chuẩn chi tiết.
  - Why it matters - vì sao quan trọng: Cho thấy evaluator có thể nâng quality bar chứ không chỉ check pass/fail thô.
  - Relationship - liên hệ với khái niệm khác: Ví dụ `pi times three` minh họa rất rõ.
- Term - thuật ngữ: artifact continuity - tính liên tục của artifact
  - Meaning - nghĩa: Khả năng sidekick nhớ và thao tác tiếp trên file/artifact đã tạo ở turn trước.
  - Why it matters - vì sao quan trọng: Đưa sidekick từ chat assistant thành work assistant thật.
  - Relationship - liên hệ với khái niệm khác: Dựa trên checkpointing và file tools.
- Term - thuật ngữ: sandbox artifact - hiện vật trong sandbox
  - Meaning - nghĩa: File đầu ra thực tế do sidekick tạo trong root directory giới hạn.
  - Why it matters - vì sao quan trọng: Đây là bằng chứng agent tạo side effects đúng như transcript mô tả.
  - Relationship - liên hệ với khái niệm khác: `dinner.md` là ví dụ trực tiếp.
- Term - thuật ngữ: hidden internal history - lịch sử nội bộ không hiển thị hết cho user
  - Meaning - nghĩa: Những lượt tool use, evaluator feedback và retry có thể diễn ra mà user không thấy toàn bộ trên UI.
  - Why it matters - vì sao quan trọng: User thấy kết quả nhanh nhưng bên trong graph có thể đã đi qua nhiều vòng reasoning/action/review.
  - Relationship - liên hệ với khái niệm khác: LangSmith trace là nơi nhìn rõ phần này.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - User task, ví dụ phép tính hoặc yêu cầu tìm nhà hàng và viết báo cáo.
2. Processing steps:
   - Worker chọn tools phù hợp.
   - Tool calls được thực thi.
   - Worker tạo answer tạm thời.
   - Evaluator chấm theo success criteria.
   - Nếu chưa đạt, worker nhận feedback và thử tiếp.
   - Nếu task liên quan file, artifact được ghi vào `sandbox`.
   - Turn sau có thể nhắc lại “the file” và sidekick dựa trên memory để tiếp tục chỉnh sửa.
3. Output:
   - Final answer tốt hơn, push notification, và/hoặc artifact file như `dinner.md`.
4. Control flow / data flow:
   - User request -> worker -> tools -> evaluator -> retry/END.
   - File artifact nằm ngoài state nhưng tên/ngữ cảnh của nó được giữ qua memory/checkpointing.
5. Decision points:
   - Evaluator có reject vì độ chính xác hay không.
   - Worker có cần gọi tool lại sau feedback hay không.
   - Follow-up action có đang nhắm đúng artifact cũ hay không.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Evaluator-enforced precision - ép độ chính xác qua evaluator
  - Purpose - mục đích: Nâng chất lượng output mà không phải hard-code mọi rule vào worker.
  - When to use - dùng khi nào: Khi output có tiêu chí rõ như chính xác số liệu, đúng định dạng, đủ nội dung.
  - Trade-off - đánh đổi: Tăng số vòng lặp và token cost.
  - Common mistake - lỗi dễ gặp: Xem evaluator như layer tùy chọn và không đưa tiêu chí đủ rõ.
- Technique - kỹ thuật: Artifact follow-up via memory - theo đuổi artifact qua memory
  - Purpose - mục đích: Cho phép user tiếp tục chỉnh sửa output cũ mà không phải nhắc lại toàn bộ context.
  - When to use - dùng khi nào: Khi agent tạo file, report, note hoặc deliverable nhiều bước.
  - Trade-off - đánh đổi: Cần memory semantics ổn định và session identity đúng.
  - Common mistake - lỗi dễ gặp: Trông cậy vào UI history thuần thay vì graph memory/checkpointing.
- Technique - kỹ thuật: Observe hidden loops - quan sát các vòng lặp nội bộ
  - Purpose - mục đích: Hiểu tại sao output cuối lại như vậy và phát hiện prompt/tool issues.
  - When to use - dùng khi nào: Khi agent behavior trông “lạ” hoặc quality bất thường.
  - Trade-off - đánh đổi: Cần observability tooling hoặc trace discipline.
  - Common mistake - lỗi dễ gặp: Chỉ nhìn answer cuối rồi đoán nguyên nhân khi có lỗi.

## 8. Code Walkthrough - Phân tích code nếu có
- File / block: retry-capable loop trong `sidekick.py`
  - Purpose - mục đích: Cho phép worker thử lại sau khi evaluator reject.
  - Key logic - logic chính: Worker/evaluator routing giữ loop chạy cho tới khi đạt hoặc cần user input.
  - Important lines / functions:
    - `def evaluator(self, state: State) -> State:`
    - `def route_based_on_evaluation(self, state: State) -> str:`
    - `if state["success_criteria_met"] or state["user_input_needed"]: return "END"`
    - `else: return "worker"`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Đây là lý do ví dụ `pi times three` có thể bị chê rồi chạy lại nhiều lần.
    - Loop không cần UI xen vào cho đến khi evaluator quyết định dừng.
- File / block: file tool context trong `sidekick_tools.py`
  - Purpose - mục đích: Cho sidekick khả năng tạo và cập nhật artifacts thực tế.
  - Key logic - logic chính: File tools bị giới hạn trong `sandbox`, nhưng đủ để sidekick ghi report Markdown.
  - Important lines / functions:
    - `FileManagementToolkit(root_dir="sandbox")`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - `sandbox` là nơi transcript 90 nói agent tạo report nhà hàng.
    - Tool này biến sidekick từ chat assistant thành artifact-producing agent.
- File / block: artifact thực tế `sandbox/dinner.md`
  - Purpose - mục đích: Xác nhận project context rằng sidekick đã thực sự tạo file báo cáo.
  - Key logic - logic chính: File chứa report về Le Bernardin với địa chỉ, phone, menu highlights và summary reviews.
  - Important lines / functions:
    - tiêu đề `# Dinner Report: Le Bernardin`
    - các phần `Restaurant Overview`, `Menu Highlights`, `Summary of Reviews`
  - Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
    - Đây là bằng chứng grounded rằng file-write path của sidekick đã được dùng thật trong session/project context.
    - Transcript nói sidekick cập nhật file; file hiện có trạng thái sau khi thu gọn về Le Bernardin.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Trả answer đầu tiên của worker
  - Pros: Nhanh hơn, rẻ hơn.
  - Cons: Dễ sai precision, bỏ sót lỗi tool use hoặc syntax errors.
  - When to choose: Chỉ khi latency là ưu tiên lớn hơn chất lượng.
- Option: Dùng evaluator loop như hiện tại
  - Pros: Chất lượng cao hơn, sửa lỗi tự động.
  - Cons: Có thể tốn nhiều tool calls và token hơn.
  - When to choose: Khi output accuracy và task completion đáng giá hơn chút độ trễ.
- Option: Tạo file rồi không hỗ trợ follow-up trên file cũ
  - Pros: Logic đơn giản hơn.
  - Cons: Agent không trở thành cộng sự làm việc nhiều bước thật sự.
  - When to choose: Khi workflow chỉ là one-shot report generation.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Chỉ nhìn answer cuối và tưởng agent “trả lời ngay”
  - Root cause: Không thấy internal history.
  - Symptom: Không hiểu vì sao cost hoặc latency tăng.
  - Fix / prevention: Quan sát trace hoặc ít nhất hiểu rằng có thể đã có nhiều loops nội bộ.
- Failure mode: Tưởng file follow-up là do UI history nhớ tên file
  - Root cause: Nhầm frontend history với graph memory.
  - Symptom: Thiết kế sai phần persistence nếu muốn productionize.
  - Fix / prevention: Gắn file continuity với checkpointing/thread memory semantics.
- Failure mode: Evaluator quá khó tính hoặc quá dễ tính
  - Root cause: Prompt/evaluation criteria chưa cân bằng.
  - Symptom: Hoặc retry quá nhiều, hoặc chấp nhận output chưa đủ tốt.
  - Fix / prevention: Tuning success criteria và evaluator prompt theo use case thật.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: `Artifact memory - bộ nhớ về hiện vật công việc` là một bước tiến lớn so với chat memory thông thường; nó cho phép agent thực hiện công việc nhiều vòng trên cùng deliverable.
- Mở rộng: Ở hệ production, các artifacts như report files thường nên có metadata layer đi kèm: creator, timestamp, session id, revision history.
- Mở rộng: Quan sát syntax error rồi auto-retry như ví dụ `pi times three` là dấu hiệu feedback loops có thể bù cho tool unreliability hoặc model slips, miễn là có stopping conditions hợp lý.

## 12. Study Pack - Gói ôn tập
### Must remember
- Lesson 90 cho thấy feedback loop hoạt động thật chứ không chỉ là ý tưởng.
- Evaluator có thể reject vì thiếu precision.
- Worker có thể retry, thậm chí sau khi gặp syntax error.
- Sidekick có thể tạo và cập nhật file trong `sandbox`.
- Memory giúp sidekick nhớ “the file” ở turn tiếp theo.
- `dinner.md` là ví dụ artifact thực tế của sidekick.

### Self-check questions
- Vì sao ví dụ `pi times three` cần nhiều vòng lặp?
- Evaluator đã chê worker ở điểm nào trong ví dụ đầu?
- Tại sao sidekick nhớ được file `dinner.md` ở lượt sau?
- Bằng chứng nào cho thấy sidekick thật sự đã tạo file?
- Nếu evaluator quá nghiêm khắc thì hệ quả gì có thể xảy ra?

### Flashcards
- Q: Tại sao answer `9.45` bị reject trong lesson 90?
  A: Vì evaluator coi nó chưa đủ chính xác so với success criteria.
- Q: `dinner.md` minh họa điều gì?
  A: Sidekick đã thực sự ghi artifact Markdown vào file system sandbox.
- Q: Điều gì cho phép sidekick hiểu “the file” ở turn sau?
  A: Memory/checkpointing của graph trong cùng session.

### Interview Q&A nếu phù hợp
- Q: Tại sao feedback loop quan trọng hơn khi agent có tools mạnh?
  A: Vì tools mạnh làm side effects lớn hơn, nên việc kiểm định và sửa sai trước khi chốt output càng có giá trị.
- Q: Làm sao bạn chứng minh một agent không chỉ “nói đã làm” mà thực sự tạo artifact?
  A: Kiểm tra trực tiếp artifact trong filesystem hoặc storage, như `sandbox/dinner.md` trong lesson này.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide Day 5 cho lesson này.
- Không có trace export LangSmith đầy đủ ngoài mô tả transcript.
- Không có metadata revision history cho `dinner.md`; chỉ thấy trạng thái file hiện tại trong sandbox.

# 91. Day 5 - AI Assistant Upgrades - Memory, Clarifying Questions & Custom Tools

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã đối chiếu với `G:\Agent2026Win\agents\4_langgraph\sidekick.py`, `G:\Agent2026Win\agents\4_langgraph\sidekick_tools.py`, `G:\Agent2026Win\agents\4_langgraph\app.py`
- Summary lịch sử: đã dùng
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Lesson 91 chủ yếu là roadmap nâng cấp dựa trên baseline sidekick hiện tại. Code được cung cấp trong session nhưng chưa thấy code mới trực tiếp cho các nâng cấp được đề xuất như clarifying-first flow, planning agent hay SQLite memory trong app hiện tại.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson cuối của Day 5 chuyển từ “đây là sidekick hiện tại” sang “bạn nên nâng nó thế nào tiếp”.
- Hướng nâng cấp đầu tiên là `clarifying questions - câu hỏi làm rõ`, có thể buộc assistant hỏi 3 câu làm rõ trước khi bắt đầu công việc.
- Hướng nâng cấp thứ hai là `multi-agent decomposition - phân rã nhiều agent`, ví dụ có planner agent tách vấn đề thành các bước rồi giao worker thực thi.
- Instructor phân tích trade-off của planner: chia nhỏ task giúp coherence tốt hơn, nhưng làm agent bớt linh hoạt trong việc đổi hướng khi phát sinh thông tin mới.
- Một nâng cấp rất thực dụng là thay memory hiện tại từ `in-memory` sang `SQLite-backed memory`, tái dùng lại kỹ thuật từ đầu tuần.
- Nếu Gradio có user login/identity, có thể dùng username làm conversation thread để sidekick nhớ liên tục qua nhiều phiên.
- Lesson này thực chất là roadmap cho việc biến sidekick từ một demo mạnh thành một personal work platform mạnh hơn và bền hơn.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu các hướng mở rộng thực tế cho sidekick sau baseline Day 5.
  - Hiểu planner-vs-single-agent là một đánh đổi kiến trúc, không có đáp án tuyệt đối.
  - Hiểu memory persistence và user identity có thể gắn với nhau ra sao.
- Practical goals - mục tiêu thực hành:
  - Biết những thay đổi nào đáng ưu tiên tiếp theo nếu tiếp tục phát triển sidekick.
  - Có thể chuyển từ `MemorySaver` sang persistent backend.
  - Có thể thiết kế clarifying-first flow hoặc thêm tools mới phục vụ công việc riêng.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao clarifying questions có thể giúp sidekick tốt hơn.
  - Vì sao thêm planner agent vừa có lợi vừa có hại.
  - Vì sao username-based thread identity có thể biến sidekick thành assistant nhớ lâu dài.

## 4. Previous Context - Liên hệ với bài trước
Lesson này nối toàn bộ Week 4 lại với nhau. Nó tham chiếu Day 3 cho `SQLite memory`, Day 4 cho `multi-agent/evaluator loops`, và Day 5 cho baseline sidekick module hóa, tool-rich. Khác với các lesson trước, đây là bài về `next-step architecture - kiến trúc bước tiếp theo`, không phải lesson triển khai code mới ngay trong session.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: clarifying-first workflow - luồng hỏi làm rõ trước
  - Meaning - nghĩa: Cho assistant ưu tiên hỏi lại các câu quan trọng trước khi bắt tay vào làm việc.
  - Why it matters - vì sao quan trọng: Giảm rủi ro làm sai từ đầu khi task của user còn mơ hồ.
  - Relationship - liên hệ với khái niệm khác: Có thể được cài như rule prompt hoặc tách thành node/agent riêng.
- Term - thuật ngữ: planner agent - tác tử lập kế hoạch
  - Meaning - nghĩa: Agent hoặc node chịu trách nhiệm phân rã task lớn thành nhiều bước con trước khi execution bắt đầu.
  - Why it matters - vì sao quan trọng: Có thể cải thiện coherence khi một worker phải gánh quá nhiều tools và context.
  - Relationship - liên hệ với khái niệm khác: Đối lập với current baseline là một worker lớn làm gần như mọi thứ.
- Term - thuật ngữ: planning trade-off - đánh đổi của lập kế hoạch
  - Meaning - nghĩa: Lập kế hoạch giúp cấu trúc hóa công việc nhưng làm giảm phần nào sự linh hoạt ứng biến của một agent tự do hơn.
  - Why it matters - vì sao quan trọng: Đây là quyết định kiến trúc quan trọng khi phát triển sidekick tiếp.
  - Relationship - liên hệ với khái niệm khác: Liên quan trực tiếp tới `single powerful worker` hiện tại.
- Term - thuật ngữ: persistent user identity memory - bộ nhớ lâu dài theo định danh người dùng
  - Meaning - nghĩa: Dùng một định danh ổn định như username làm thread key để memory kéo dài qua nhiều phiên.
  - Why it matters - vì sao quan trọng: Đây là bước biến sidekick từ chat demo thành assistant cá nhân nhớ liên tục.
  - Relationship - liên hệ với khái niệm khác: Phụ thuộc vào persistent checkpoint backend như SQLite.
- Term - thuật ngữ: custom tool growth path - lộ trình mở rộng tool riêng
  - Meaning - nghĩa: Ý tưởng để người học tiếp tục thêm tools đặc thù như SQL, calendar, markdown-to-PDF.
  - Why it matters - vì sao quan trọng: Giá trị thật của sidekick đến từ việc gắn nó với công việc của chính người dùng.
  - Relationship - liên hệ với khái niệm khác: Dựa trên nền capability layer của `sidekick_tools.py`.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - Sidekick baseline hiện tại.
   - Những điểm yếu quan sát được: context dài, đôi khi mất coherence, memory mới chỉ in-memory.
2. Processing steps:
   - Cân nhắc thêm clarifying step trước khi thực thi.
   - Cân nhắc thêm planner agent để tách bài toán thành bước nhỏ.
   - Cân nhắc thay `MemorySaver` bằng SQLite memory.
   - Cân nhắc gắn login identity vào thread key.
   - Cân nhắc thêm tools đặc thù theo workflow cá nhân.
3. Output:
   - Một roadmap nâng cấp có định hướng rõ cho sidekick.
4. Control flow / data flow:
   - User request có thể đi qua clarifying step -> planning step -> worker execution -> evaluator loop.
   - User identity có thể được dùng làm key để persistent memory gắn với đúng người dùng.
5. Decision points:
   - Ưu tiên clarifying-first hay planner-first.
   - Giữ one-agent baseline hay tách thêm agents.
   - Chuyển memory backend khi nào.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Clarify before execute - hỏi rõ trước khi làm
  - Purpose - mục đích: Giảm sai lệch mục tiêu và tiết kiệm tool calls vô ích.
  - When to use - dùng khi nào: Khi task của user thường mơ hồ hoặc có nhiều cách hiểu.
  - Trade-off - đánh đổi: Tăng một lượt tương tác ban đầu và có thể làm user thấy chậm hơn.
  - Common mistake - lỗi dễ gặp: Cho agent lao vào làm ngay dù đầu bài còn thiếu ràng buộc quan trọng.
- Technique - kỹ thuật: Planning before doing - lập kế hoạch trước khi hành động
  - Purpose - mục đích: Chia bài toán lớn thành sub-tasks dễ thực thi hơn.
  - When to use - dùng khi nào: Khi current worker bị quá tải vì toolset và context lớn.
  - Trade-off - đánh đổi: Có thể làm giảm tính linh hoạt ứng biến nếu kế hoạch ban đầu chưa tốt.
  - Common mistake - lỗi dễ gặp: Tưởng planning luôn tốt hơn mà quên cost và loss of flexibility.
- Technique - kỹ thuật: Persistent identity threads - luồng bộ nhớ theo định danh ổn định
  - Purpose - mục đích: Biến nhiều phiên rời rạc thành một quan hệ lâu dài giữa user và assistant.
  - When to use - dùng khi nào: Khi app có login hoặc ít nhất có durable user identifier.
  - Trade-off - đánh đổi: Cần quản lý identity, privacy và retention cẩn thận hơn.
  - Common mistake - lỗi dễ gặp: Dùng memory lâu dài mà không có key người dùng ổn định.

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session nhưng chưa thấy code mới liên quan trực tiếp tới các nâng cấp được mô tả trong lesson này.

Baseline code có liên quan để hiểu roadmap:
- `sidekick.py` hiện đang dùng `self.memory = MemorySaver()`, nên lesson 91 đề xuất thay bằng backend persistent như SQLite.
- `worker` hiện chưa có luồng bắt buộc “ask 3 clarifying questions first”, nên đây là chỗ logic có thể được sửa.
- Graph hiện chỉ có một worker lớn + tools + evaluator, nên ý tưởng planner agent là một mở rộng kiến trúc chứ chưa có sẵn trong code hiện tại.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Giữ single powerful worker như hiện tại
  - Pros: Linh hoạt, ít nodes hơn, app đơn giản hơn.
  - Cons: Context dễ dài, coherence có thể giảm khi tools quá nhiều.
  - When to choose: Khi baseline còn đủ tốt và muốn iteration nhanh.
- Option: Thêm planner agent
  - Pros: Chia task lớn rõ hơn, giúp execution có cấu trúc hơn.
  - Cons: Tăng complexity và có thể làm agent bớt tự do điều chỉnh kế hoạch theo tình huống.
  - When to choose: Khi sidekick bắt đầu xử lý tác vụ dài/phức tạp và hay bị lạc hướng.
- Option: Ép clarifying questions trước
  - Pros: Tăng độ chính xác đầu bài, giảm rework.
  - Cons: Tăng thêm một lượt chat, đôi khi gây khó chịu nếu task vốn đã rõ.
  - When to choose: Khi user requests thường mơ hồ hoặc thiếu constraints.
- Option: Chuyển sang SQLite memory + identity-based threads
  - Pros: Cho memory lâu dài và continuity qua nhiều phiên.
  - Cons: Thêm persistence layer và trách nhiệm quản lý dữ liệu.
  - When to choose: Khi sidekick bắt đầu được dùng lặp lại như assistant cá nhân thật.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Thêm quá nhiều agent quá sớm
  - Root cause: Muốn “kiến trúc hóa” trước khi baseline one-worker đã được hiểu kỹ.
  - Symptom: Graph khó debug hơn trong khi lợi ích chưa rõ.
  - Fix / prevention: Chỉ tách planner/extra agents khi có evidence current worker quá tải.
- Failure mode: Bật persistent memory mà không có identity model tốt
  - Root cause: Chỉ nhìn khía cạnh kỹ thuật của SQLite/checkpointer.
  - Symptom: Memory lẫn người dùng hoặc khó quản trị retention.
  - Fix / prevention: Gắn memory với key người dùng ổn định như login username.
- Failure mode: Ép clarifying questions cho mọi task
  - Root cause: Cực đoan hóa một pattern tốt.
  - Symptom: UX chậm và rườm rà cho những yêu cầu vốn đã rõ.
  - Fix / prevention: Dùng clarifying-first như strategy có điều kiện hoặc chỉ cho lớp task mơ hồ.

## 11. Knowledge Extension - Kiến thức mở rộng
- Mở rộng: `Planner-executor architectures - kiến trúc planner-executor` là một pattern rất phổ biến trong agent systems, nhưng hiệu quả của nó phụ thuộc mạnh vào độ ổn định của planner prompt và granularity của tasks.
- Mở rộng: Persistent memory cá nhân hóa giúp agent hữu ích hơn rất nhiều, nhưng đồng thời kéo theo các vấn đề `privacy - riêng tư`, `retention - lưu giữ`, và `user control - quyền kiểm soát của người dùng`.
- Mở rộng: Một lộ trình nâng cấp thực tế thường là: thêm durable memory trước, rồi thêm clarifying behavior, rồi mới cân nhắc multi-agent planning nếu cần.

## 12. Study Pack - Gói ôn tập
### Must remember
- Lesson 91 là roadmap nâng cấp sidekick, không phải triển khai tính năng mới ngay.
- Hai hướng lớn là clarifying questions và planner agent.
- Planner giúp chia nhỏ việc nhưng có thể giảm flexibility.
- Sidekick hiện còn dùng in-memory memory, nên SQLite là nâng cấp tự nhiên.
- Username hoặc login identity có thể làm key cho memory lâu dài.
- Giá trị thật của sidekick đến từ việc bạn thêm tools phù hợp công việc riêng.

### Self-check questions
- Vì sao clarifying questions có thể cải thiện sidekick?
- Khi nào planner agent đáng thêm vào hệ thống?
- Trade-off lớn nhất của planner là gì?
- Tại sao persistent memory nên gắn với user identity?
- Nếu bạn chỉ được làm một nâng cấp tiếp theo, bạn chọn gì và vì sao?

### Flashcards
- Q: Lesson 91 nói nên thay `MemorySaver` bằng gì?
  A: Một backend persistent như SQLite memory.
- Q: Planner agent dùng để làm gì?
  A: Để phân rã task lớn thành các bước hoặc sub-tasks trước khi execution.
- Q: Vì sao không phải lúc nào clarifying questions cũng nên hỏi?
  A: Vì với task đã rõ, chúng làm UX chậm và rườm rà không cần thiết.

### Interview Q&A nếu phù hợp
- Q: Khi nào bạn giữ một worker lớn thay vì tách planner và executors?
  A: Khi flexibility quan trọng và current workload vẫn còn nằm trong khả năng điều phối ổn định của một worker duy nhất.
- Q: Tại sao memory lâu dài cần đi cùng identity?
  A: Vì nếu không có identity ổn định thì memory không thể gắn chính xác với đúng người dùng hoặc đúng cuộc hội thoại dài hạn.

## 13. Missing Inputs - Còn thiếu gì
- Không có slide cho lesson này.
- Không có code patch trực tiếp cho clarifying-first flow, planner agent hay SQLite migration trong session hiện tại.
- Không có so sánh benchmark giữa single-worker và planner-based variants.
