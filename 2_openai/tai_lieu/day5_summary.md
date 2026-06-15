# Day 5 - Modular Agent Design, Gradio UI, and Cloud Deployment in Agent SDK

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

---

# 47. Day 5 - Building a Modular AI Research System with Gradio UI Implementation

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([deep_research.py](file:///G:/Agent2026Win/agents/2_openai/deep_research/deep_research.py), [planner_agent.py](file:///G:/Agent2026Win/agents/2_openai/deep_research/planner_agent.py), [search_agent.py](file:///G:/Agent2026Win/agents/2_openai/deep_research/search_agent.py), [writer_agent.py](file:///G:/Agent2026Win/agents/2_openai/deep_research/writer_agent.py))
- Summary lịch sử: đã dùng ([day4_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day4_summary.md) - làm bối cảnh cho các Agent và luồng nghiên cứu sâu)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học thực hiện chuyển đổi mã nguồn từ Jupyter Notebook sang các mô-đun Python độc lập và xây dựng giao diện web bằng thư viện Gradio.

## 2. Executive Summary - Tóm tắt cốt lõi
- Chuyển đổi toàn bộ mã nguồn thử nghiệm từ môi trường Jupyter Notebook sang cơ sở mã nguồn dạng mô-đun (modular codebase) với các tệp tin Python chuyên biệt (`.py`).
- Cấu trúc hệ thống bao gồm các tác vụ đơn lẻ cho từng Agent: [planner_agent.py](file:///G:/Agent2026Win/agents/2_openai/deep_research/planner_agent.py), [search_agent.py](file:///G:/Agent2026Win/agents/2_openai/deep_research/search_agent.py), [writer_agent.py](file:///G:/Agent2026Win/agents/2_openai/deep_research/writer_agent.py) giúp tối ưu hóa cấu trúc dự án.
- Giới thiệu và tích hợp thư viện Gradio để tạo giao diện web nhanh chóng mà không cần kiến thức chuyên sâu về phát triển giao diện người dùng (frontend).
- Sử dụng cú pháp `gr.Blocks` để tự xây dựng giao diện tùy chỉnh với chủ đề (theme) màu trời `primary_hue="sky"`.
- Triển khai bộ sinh bất đồng bộ (asynchronous generator) sử dụng từ khóa `yield` trong hàm `run` để thực hiện cập nhật trạng thái (status update) liên tục lên giao diện mà không làm treo ứng dụng.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách thức tổ chức dự án Agent từ dạng thử nghiệm (notebook) sang dạng mô-đun Python tiêu chuẩn.
  - Nắm bắt cơ chế dựng giao diện tùy chỉnh bằng cách sử dụng `gr.Blocks` của Gradio.
  - Hiểu nguyên lý truyền dữ liệu thời gian thực (real-time streaming) giữa Agent Manager và giao diện người dùng thông qua bộ sinh bất đồng bộ.
- Practical goals - mục tiêu thực hành:
  - Cấu trúc lại các Agent thành các tệp tin cấu hình độc lập.
  - Xây dựng giao diện Gradio bao gồm hộp văn bản (textbox), nút bấm (button), và vùng hiển thị định dạng Markdown.
  - Thực hiện liên kết sự kiện (event binding) của Gradio trỏ tới callback đồng trình (coroutine callback) hỗ trợ từ khóa `yield`.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao việc chuyển đổi từ notebook sang cấu trúc mô-đun lại quan trọng khi xây dựng ứng dụng thực tế?
  - Cơ chế `async for ... yield` hoạt động thế nào để cập nhật giao diện người dùng theo thời gian thực?

## 4. Previous Context - Liên hệ với bài trước
- Bài học này kế thừa và đóng gói toàn bộ logic nghiên cứu sâu, bao gồm các cấu hình Agent và Structured Outputs đã được giới thiệu tại Day 4. Nó nâng cấp quy trình thực thi mã nguồn từ các ô lệnh tuần tự sang ứng dụng có giao diện hoàn chỉnh.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Modular Codebase - cơ sở mã nguồn dạng mô-đun
  - Meaning - nghĩa: Phương pháp tổ chức mã nguồn bằng cách chia nhỏ chương trình thành các tệp tin độc lập, mỗi tệp phụ trách một thành phần logic chuyên biệt (như Agent định nghĩa riêng, hàm điều phối riêng).
  - Why it matters - vì sao quan trọng: Giúp mã nguồn dễ bảo trì, tái sử dụng, dễ viết kiểm thử đơn vị và dễ làm việc nhóm.
  - Relationship - liên hệ với khái niệm khác: Trái ngược với cấu trúc tệp tin đơn lẻ chứa mọi logic (monolithic file).
- Term - thuật ngữ: Asynchronous Generator - bộ sinh bất đồng bộ
  - Meaning - nghĩa: Một hàm đặc biệt trong Python được định nghĩa bằng `async def` và chứa từ khóa `yield`, cho phép sinh ra một chuỗi kết quả bất đồng bộ theo thời gian.
  - Why it matters - vì sao quan trọng: Cho phép các tác vụ tốn thời gian (như chạy Agent cào web) có thể gửi thông tin trạng thái trung gian về giao diện mà không làm chặn luồng xử lý chính.
  - Relationship - liên hệ với khái niệm khác: Sử dụng kết hợp với vòng lặp `async for` để duyệt qua các kết quả được sinh ra.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình hoạt động của giao diện Gradio và callback:
1. Input: Văn bản truy vấn nhập vào từ `query_textbox` trên giao diện web.
2. Processing steps:
   - Bước 1: Người dùng nhấn nút "Run" hoặc nhấn phím Enter để gửi yêu cầu.
   - Bước 2: Sự kiện click kích hoạt hàm gọi lại (callback) `run`.
   - Bước 3: Hàm `run` gọi phương thức chạy của `ResearchManager` và dùng vòng lặp `async for` để hứng dữ liệu.
   - Bước 4: Mỗi khi có trạng thái mới (ví dụ: đang lập kế hoạch, đang tìm kiếm), hàm `run` dùng `yield` để gửi văn bản này lên giao diện.
3. Output: Bộ phận hiển thị `report` định dạng Markdown của Gradio nhận kết quả và cập nhật liên tục lên màn hình người dùng.
4. Control flow / data flow: Luồng chạy tương tác hai chiều bất đồng bộ: Giao diện -> Callback phát sinh trạng thái -> Cập nhật hiển thị giao diện.
5. Decision points: Sự kiện kích hoạt do người dùng quyết định qua hành động click chuột hoặc gửi form văn bản.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Event Binding in gr.Blocks - liên kết sự kiện trong Blocks
  - Purpose - mục đích: Đăng ký các hàm Python để xử lý khi người dùng tương tác với các thành phần trên giao diện Gradio.
  - When to use - dùng khi nào: Khi tự xây dựng giao diện tùy chỉnh bằng `gr.Blocks` thay vì sử dụng các giao diện mặc định có sẵn (như `gr.Interface`).
  - Trade-off - đánh đổi: Yêu cầu nhà phát triển phải tự quản lý luồng dữ liệu đầu vào (inputs) và đầu ra (outputs) giữa các thành phần giao diện, tăng độ phức tạp của mã nguồn.
  - Common mistake - lỗi dễ gặp: Khai báo sai tên thành phần đầu vào hoặc đầu ra trong hàm đăng ký sự kiện, dẫn đến lỗi không tìm thấy widget khi kích hoạt.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [deep_research.py](file:///G:/Agent2026Win/agents/2_openai/deep_research/deep_research.py)
- Purpose - mục đích: Thiết lập cấu trúc giao diện người dùng Gradio và liên kết các sự kiện tương tác của hộp văn bản và nút bấm với hàm xử lý bất đồng bộ.
- Key logic: Khởi tạo khối ứng dụng `gr.Blocks`, định nghĩa các ô nhập liệu, vùng kết quả và đăng ký sự kiện chạy ứng dụng có hỗ trợ truyền dữ liệu thời gian thực.
- Important lines / functions:
  ```python
  async def run(query: str):
      async for chunk in ResearchManager().run(query):
          yield chunk

  with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
      gr.Markdown("# Deep Research")
      query_textbox = gr.Textbox(label="What topic would you like to research?")
      run_button = gr.Button("Run", variant="primary")
      report = gr.Markdown(label="Report")
      
      run_button.click(fn=run, inputs=query_textbox, outputs=report)
      query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)
  ```
  - Vietnamese inline notes:
    - `async def run(query: str)`: Định nghĩa hàm gọi lại bất đồng bộ. Sử dụng vòng lặp `async for` để duyệt qua từng trạng thái hoặc nội dung báo cáo sinh ra từ `ResearchManager`.
    - `yield chunk`: Trả về dữ liệu trung gian cho Gradio cập nhật trực tiếp lên thành phần giao diện Markdown.
    - `theme=gr.themes.Default(primary_hue="sky")`: Cấu hình chủ đề mặc định với gam màu chủ đạo xanh da trời.
    - `run_button.click(...)` và `query_textbox.submit(...)`: Liên kết hành động click nút bấm và ấn phím Enter gửi hộp văn bản với hàm xử lý `run`.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Sử dụng gr.Blocks (Tự dựng giao diện tùy chỉnh)
  - Pros: Cho phép sắp xếp bố cục tự do, cấu hình các sự kiện tương tác phức tạp và tối ưu hóa trải nghiệm người dùng.
  - Cons: Đòi hỏi viết nhiều dòng code cấu hình hơn so với các giao diện mặc định.
  - When to choose: Khi cần xây dựng các ứng dụng có luồng dữ liệu đặc thù (như luồng sinh trạng thái trung gian trước khi in báo cáo lớn).
- Option: Sử dụng gr.Interface (Giao diện đơn giản mặc định)
  - Pros: Rất nhanh chóng, chỉ cần truyền hàm xử lý và các kiểu dữ liệu đầu vào/đầu ra là tự sinh giao diện.
  - Cons: Bố cục cố định, khó can thiệp sâu vào các luồng sự kiện trung gian.
  - When to choose: Khi cần tạo nhanh một bản thử nghiệm chức năng (MVP) đơn giản trong vòng vài phút.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Giao diện web bị đóng băng hoàn toàn hoặc không hiển thị các cập nhật trạng thái trong lúc Agent đang tìm kiếm trực tuyến.
- Root cause: Quên sử dụng từ khóa `yield` trong hàm callback hoặc không sử dụng cấu trúc bất đồng bộ (`async def` kết hợp `async for`), dẫn đến việc Gradio phải đợi hàm Python chạy xong hoàn toàn mới hiển thị một kết quả duy nhất.
- Symptom: Màn hình trống trơn trong suốt thời gian Agent thực thi tìm kiếm và viết báo cáo (khoảng 30-60 giây), sau đó hiển thị đột ngột báo cáo cuối cùng.
- Fix / prevention: Chuyển đổi hàm callback thành dạng bất đồng bộ có sử dụng `yield` để đẩy dữ liệu trạng thái lên màn hình từng bước.

## 11. Knowledge Extension - Kiến thức mở rộng
- Cơ chế hoạt động của Gradio Streams: Khi một hàm Python trả về bằng từ khóa `yield`, Gradio sẽ thiết lập một kết nối Server-Sent Events (SSE) hoặc WebSockets giữa trình duyệt và máy chủ backend Python. Mỗi khi có giá trị `yield` mới, backend sẽ gửi một thông điệp nhỏ qua kết nối này, giúp trình duyệt cập nhật lại DOM (giao diện) của thành phần tương ứng ngay lập tức mà không cần tải lại toàn bộ trang web.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Modular Codebase giúp chia nhỏ logic ứng dụng thành các tệp tin Python độc lập để dễ phát triển và bảo trì.
2. Thư viện Gradio hỗ trợ xây dựng giao diện web trực quan mà không cần viết mã HTML/CSS/JS.
3. Cú pháp `gr.Blocks` được sử dụng để xây dựng giao diện tùy chỉnh phức tạp.
4. Bộ sinh bất đồng bộ với cú pháp `async for ... yield` giúp truyền cập nhật trạng thái thời gian thực lên giao diện.
5. Sự kiện `click` của nút bấm và `submit` của hộp văn bản được liên kết bằng các tham số `fn`, `inputs`, và `outputs`.

### Self-check questions
1. Giải thích sự khác biệt về vai trò giữa `gr.Interface` và `gr.Blocks` trong Gradio.
2. Làm thế nào để Gradio có thể cập nhật kết quả từng bước lên màn hình mà không cần người dùng tải lại trang?

### Flashcards
- Q: Từ khóa nào trong Python được sử dụng trong hàm để sinh dữ liệu trạng thái trung gian bất đồng bộ?
  A: Từ khóa `yield` trong hàm định nghĩa dạng `async def`.
- Q: Sự kiện nào được kích hoạt khi người dùng ấn phím Enter trên ô nhập liệu của Gradio?
  A: Sự kiện `submit` của thành phần `gr.Textbox`.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 48. Day 5 - Deep Research App - Gradio to Visualize & Monitor Autonomous AI Agents

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([research_manager.py](file:///G:/Agent2026Win/agents/2_openai/deep_research/research_manager.py#L1-L27))
- Summary lịch sử: đã dùng ([day4_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day4_summary.md) - về tích hợp trace và lập trình bất đồng bộ song song)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học thực hành khởi chạy và kiểm thử ứng dụng Gradio, phân tích cơ chế theo dõi tiến trình chạy của các tác vụ tìm kiếm song song.

## 2. Executive Summary - Tóm tắt cốt lõi
- Hướng dẫn khởi chạy ứng dụng Gradio thông qua công cụ quản lý môi trường ảo `uv` bằng lệnh `uv run deep_research.py` để đảm bảo nạp đúng các thư viện phụ thuộc.
- Sử dụng hàm `gen_trace_id()` của OpenAI Agents SDK để sinh mã định danh vết chạy (trace ID) độc bản cho từng lượt chạy nghiên cứu.
- Trả về đường link trace trực tiếp dạng `https://platform.openai.com/traces/trace?trace_id={trace_id}` lên giao diện người dùng ngay khi bắt đầu tiến trình để hỗ trợ giám sát.
- Phân tích cơ chế theo dõi tiến độ tìm kiếm bằng cách sử dụng `asyncio.as_completed` để cập nhật số lượng tác vụ đã hoàn thành lên màn hình (ví dụ: `Searching... 1/5 completed`).
- Đánh giá luồng chạy thực tế: 20 tác vụ tìm kiếm được thực thi song song hoàn toàn nhờ AsyncIO, sau đó Writer Agent và Email Agent được chạy tuần tự.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách sinh và quản lý mã vết chạy (trace ID) trong quá trình thực thi đa Agent.
  - Hiểu nguyên lý theo dõi trạng thái các tác vụ đồng thời sử dụng `asyncio.as_completed`.
- Practical goals - mục tiêu thực hành:
  - Chạy ứng dụng Gradio thông qua terminal của Cursor bằng công cụ `uv`.
  - Thực hiện câu hỏi nghiên cứu thực tế và theo dõi tiến trình cập nhật trạng thái trực quan trên UI.
  - Truy cập OpenAI Traces portal từ liên kết được sinh tự động để đánh giá biểu đồ hiệu năng.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao việc in ra đường link trace trực tiếp trên giao diện lại hữu ích cho quá trình phát triển?
  - Sự khác biệt về mặt hoạt động giữa `asyncio.gather` và `asyncio.as_completed` khi xử lý danh sách tác vụ song song là gì?

## 4. Previous Context - Liên hệ với bài trước
- Kết nối trực tiếp với cổng thông tin vết chạy OpenAI Traces đã thảo luận ở Day 3 và Day 4. Bài học này tự động hóa việc sinh và hiển thị liên kết trace trực tiếp trên UI người dùng thay vì chỉ ghi nhận thụ động trong log terminal.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Trace ID - mã định danh vết chạy
  - Meaning - nghĩa: Chuỗi ký tự độc nhất được sinh ra để nhận diện toàn bộ chuỗi cuộc gọi API và tương tác của các Agent trong một phiên làm việc cụ thể.
  - Why it matters - vì sao quan trọng: Giúp liên kết các log phân tán trong hệ thống Agent phức tạp về chung một đầu mối để dễ phân tích và gỡ lỗi.
  - Relationship - liên hệ with khái niệm khác: Được truyền trực tiếp vào tham số `trace_id` trong khối lệnh `with trace(...)`.
- Term - thuật ngữ: asyncio.as_completed - hoàn thành bất đồng bộ
  - Meaning - nghĩa: Một hàm trong thư viện AsyncIO trả về một bộ lặp (iterator) sinh ra các coroutine khi chúng hoàn thành, bất kể thứ tự bắt đầu của chúng.
  - Why it matters - vì sao quan trọng: Cho phép cập nhật tiến độ chạy của các tác vụ song song ngay lập tức khi có bất kỳ tác vụ nào hoàn thành, giúp nâng cao trải nghiệm người dùng.
  - Relationship - liên hệ với khái niệm khác: Khác với `asyncio.gather` vốn đợi toàn bộ danh sách tác vụ hoàn thành mới trả về một lần duy nhất.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình theo dõi tiến độ bất đồng bộ của ResearchManager:
1. Input: Danh sách các tác vụ tìm kiếm được bao bọc trong `asyncio.create_task`.
2. Processing steps:
   - Bước 1: Sử dụng vòng lặp `for task in asyncio.as_completed(tasks):` để duyệt qua các tác vụ đang chạy.
   - Bước 2: Dùng `await task` để nhận kết quả của tác vụ vừa hoàn thành.
   - Bước 3: Tăng biến đếm `num_completed` lên 1 đơn vị.
   - Bước 4: In hoặc yield trạng thái tiến độ tìm kiếm (ví dụ: "Searching... 3/5 completed") để thông báo cho người dùng.
3. Output: Danh sách đầy đủ các kết quả tìm kiếm sau khi tất cả các tác vụ trong cụm hoàn thành.
4. Control flow / data flow: Luồng lặp lấy kết quả theo cơ chế tác vụ nào xong trước trả kết quả trước (first-come, first-served).
5. Decision points: Trình tự lấy kết quả phụ thuộc hoàn toàn vào tốc độ phản hồi thực tế của các cuộc gọi API mạng.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Tiến trình phản hồi thời gian thực qua as_completed
  - Purpose - mục đích: Đo lường và hiển thị tiến độ hoàn thành của các tác vụ I/O song song cho người dùng biết hệ thống đang hoạt động bình thường.
  - When to use - dùng khi nào: Khi thực hiện nhiều cuộc gọi API song song và thời gian chờ đợi phản hồi của mỗi cuộc gọi là khác nhau.
  - Trade-off - đánh đổi: Cần quản lý cấu trúc code phức tạp hơn so với việc chỉ gọi `asyncio.gather`.
  - Common mistake - lỗi dễ gặp: Quên xử lý lỗi ngoại lệ bên trong tác vụ con, dẫn đến việc khi một tác vụ gặp sự cố, vòng lặp `as_completed` sẽ bị gián đoạn và các tác vụ sau không được xử lý tiếp.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [research_manager.py](file:///G:/Agent2026Win/agents/2_openai/deep_research/research_manager.py#L1-L51)
- Purpose - mục đích: Tạo trace ID, liên kết phiên chạy với cổng OpenAI Traces và theo dõi tiến độ tìm kiếm web song song của Agent.
- Key logic: Sử dụng `gen_trace_id()` để gán trace ID duy nhất, yield link trace ra giao diện web, và sử dụng `asyncio.as_completed` để theo dõi tiến độ của các tác vụ song song.
- Important lines / functions:
  ```python
  trace_id = gen_trace_id()
  with trace("Research trace", trace_id=trace_id):
      print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
      yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
      
      # perform_searches logic
      tasks = [asyncio.create_task(self.search(item)) for item in search_plan.searches]
      results = []
      for task in asyncio.as_completed(tasks):
          result = await task
          if result is not None:
              results.append(result)
          num_completed += 1
          print(f"Searching... {num_completed}/{len(tasks)} completed")
  ```
  - Vietnamese inline notes:
    - `trace_id = gen_trace_id()`: Tạo một chuỗi định danh duy nhất cho vết chạy của cuộc nghiên cứu hiện tại.
    - `yield f"View trace: ..."`: Đẩy đường link trace trực tiếp lên màn hình Gradio của người dùng để họ có thể click theo dõi ngay lập tức.
    - `asyncio.as_completed(tasks)`: Duyệt qua các tác vụ cào dữ liệu web theo cơ chế tác vụ nào hoàn thành trước thì xử lý trước để cập nhật tiến độ phản hồi lên log.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Sử dụng asyncio.as_completed
  - Pros: Có thể cập nhật phần trăm/số lượng hoàn thành ngay lập tức cho người dùng, mang lại cảm giác phản hồi nhanh chóng.
  - Cons: Không giữ nguyên thứ tự ban đầu của danh sách tác vụ khi trả về kết quả (tuy nhiên với tác vụ tìm kiếm web thì thứ tự trả về không quan trọng).
  - When to choose: Phù hợp cho việc tối ưu trải nghiệm người dùng trên giao diện ứng dụng.
- Option: Sử dụng asyncio.gather
  - Pros: Giữ nguyên thứ tự kết quả trả về trùng khớp với thứ tự danh sách tác vụ truyền vào, viết code cực kỳ ngắn gọn.
  - Cons: Phải đợi toàn bộ tất cả tác vụ xong xuôi mới trả kết quả, không thể cập nhật tiến độ trung gian một cách tự nhiên.
  - When to choose: Khi thứ tự của kết quả đầu ra là bắt buộc phải chuẩn xác theo danh sách đầu vào.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Link trace hiển thị trên Gradio nhưng khi click vào thì báo lỗi không tìm thấy thông tin trace trên OpenAI Dashboard.
- Root cause: Quên khai báo hoặc khai báo sai biến môi trường liên quan đến logging/tracing của SDK, hoặc do tài khoản API OpenAI chưa kích hoạt tính năng lưu giữ trace hoặc dùng sai project workspace.
- Symptom: Trang web traces của OpenAI báo lỗi 404 hoặc không có dữ liệu tải lên.
- Fix / prevention: [Alert] Hãy đảm bảo bạn đã đăng nhập đúng tài khoản OpenAI có quyền truy cập project tương ứng và kiểm tra xem thư viện `agents` có đang ghi nhận trace thành công ở terminal cục bộ hay không.

## 11. Knowledge Extension - Kiến thức mở rộng
- Cơ chế hoạt động của `asyncio.as_completed`: Bản chất của hàm này là tạo ra một hàng đợi nội bộ (internal queue) lưu trữ các tác vụ. Mỗi khi một tác vụ hoàn thành (done), nó sẽ tự động đẩy kết quả của mình vào hàng đợi này. Vòng lặp `await task` thực chất là đang chờ và rút dữ liệu ra khỏi hàng đợi đó theo đúng trình tự thời gian hoàn thành của các tác vụ mạng.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Khởi chạy ứng dụng Gradio an toàn bằng lệnh `uv run deep_research.py`.
2. Hàm `gen_trace_id()` tạo ra mã vết chạy ngẫu nhiên độc bản để liên kết log API.
3. Địa chỉ truy cập vết chạy trực tiếp có cấu trúc: `https://platform.openai.com/traces/trace?trace_id={trace_id}`.
4. `asyncio.as_completed` trả về kết quả tác vụ theo trình tự thời gian hoàn thành thực tế.
5. Cập nhật trạng thái tiến độ (ví dụ: `3/5 completed`) giúp người dùng theo dõi hoạt động của hệ thống Agent.

### Self-check questions
1. Tại sao lệnh `uv run` lại được khuyến nghị sử dụng thay thế cho lệnh `python` thông thường khi chạy dự án Agent?
2. Sự khác biệt chính về hành vi thu thập kết quả giữa `asyncio.gather` và `asyncio.as_completed` là gì?

### Flashcards
- Q: Hàm nào của SDK dùng để tự động sinh mã định danh vết chạy duy nhất cho Agent?
  A: Hàm `gen_trace_id()`.
- Q: Khi sử dụng `asyncio.as_completed`, kết quả của tác vụ con nào sẽ được trả về trước?
  A: Tác vụ con nào hoàn thành tác vụ I/O trước sẽ được trả về trước.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 49. Day 5 - Deploying Smart Research Agents with Gradio and HuggingFace Spaces

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: không có code trực tiếp cho các tính năng mở rộng nâng cao trong thư mục nguồn (đây là bài thảo luận về các thử thách kiến trúc mở rộng và cách thức triển khai ứng dụng web lên máy chủ đám mây)
- Summary lịch sử: đã dùng ([day2_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day2_summary.md) - về thiết kế Agent đóng vai trò công cụ và bàn giao quyền điều khiển)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học định hướng phương pháp mở rộng năng lực tự trị của Agent và cách chia sẻ ứng dụng qua Hugging Face Spaces.

## 2. Executive Summary - Tóm tắt cốt lõi
- Bài học đưa ra thách thức nâng cao chất lượng báo cáo nghiên cứu sâu để đạt tới cấp độ sản phẩm thương mại hoàn chỉnh.
- Đề xuất quy trình tương tác Clarifying Questions (Câu hỏi làm rõ): Trước khi nghiên cứu, Agent tự động sinh ra 3 câu hỏi làm rõ để khảo sát ý định người dùng và tích hợp câu trả lời của họ vào các truy vấn tìm kiếm web sau đó.
- Nâng cấp bộ điều phối thành bộ quản lý tự trị (autonomous manager): Ứng dụng các mẫu thiết kế Agent đóng vai trò công cụ (agents as tools) hoặc bàn giao quyền lực (handoffs) để Agent tự trị quyết định có cần thực hiện thêm các lượt tìm kiếm bổ sung hay không dựa trên thông tin đã thu thập.
- Đề xuất tích hợp mẫu thiết kế Evaluator-Optimizer (Đánh giá - tối ưu): Bổ sung một Agent kiểm định chất lượng để phê duyệt hoặc yêu cầu chỉnh sửa báo cáo trước khi hoàn tất đường ống.
- Hướng dẫn triển khai (deploy) ứng dụng Gradio lên Hugging Face Spaces bằng lệnh dòng lệnh đơn giản `gradio deploy`.
- Tổng kết tuần 2 (làm việc với OpenAI Agents SDK) và giới thiệu sơ lược về tuần 3 (chuyển sang nghiên cứu khung làm việc CrewAI).

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu kiến trúc xây dựng luồng tương tác đa bước (multi-step interaction) để thu thập thông tin làm rõ từ người dùng.
  - Hiểu cách thức hoạt động của một Agent điều phối có tính năng tự lập luận và quyết định kết thúc vòng lặp (loop control).
  - Nắm bắt quy trình vận hành và lưu trữ ứng dụng Python lên nền tảng đám mây Hugging Face.
- Practical goals - mục tiêu thực hành:
  - Phác thảo thiết kế hệ thống tương tác thu thập câu hỏi làm rõ.
  - Tìm hiểu cách sử dụng lệnh `gradio deploy` từ cửa sổ terminal để đẩy mã nguồn lên Hugging Face Spaces.
- What learner should be able to explain - người học cần giải thích được:
  - Việc hỏi câu hỏi làm rõ trước khi nghiên cứu giúp cải thiện chất lượng kết quả đầu ra như thế nào?
  - Sự khác nhau cơ bản giữa triết lý thiết kế của OpenAI Agents SDK và CrewAI là gì?

## 4. Previous Context - Liên hệ với bài trước
- Kết nối trực tiếp với triết lý thiết kế hệ thống SDR phân cấp, cơ chế handoffs và gọi Agent con làm công cụ đã học ở Day 2 để ứng dụng vào việc xây dựng bộ quản lý nghiên cứu tự trị và linh hoạt hơn.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Clarifying Questions - câu hỏi làm rõ
  - Meaning - nghĩa: Các câu hỏi do hệ thống tự động sinh ra nhằm làm sáng tỏ những điểm còn mơ hồ, thiếu chi tiết hoặc chưa rõ ý định trong yêu cầu ban đầu của người dùng.
  - Why it matters - vì sao quan trọng: Giúp định hình chính xác phạm vi nghiên cứu, tránh việc Agent tìm kiếm lan man các thông tin không đúng trọng tâm.
  - Relationship - liên hệ với khái niệm khác: Một bước thu thập dữ liệu đầu vào (input alignment) trước khi kích hoạt bộ lập kế hoạch tìm kiếm.
- Term - thuật ngữ: Evaluator-Optimizer Pattern - mẫu thiết kế đánh giá - tối ưu
  - Meaning - nghĩa: Mẫu thiết kế trong đó một mô hình ngôn ngữ lớn sinh ra kết quả (optimizer) và một mô hình khác đóng vai trò kiểm định, chấm điểm và đưa ra phản hồi chỉnh sửa (evaluator) cho đến khi đạt tiêu chuẩn chất lượng.
  - Why it matters - vì sao quan trọng: Đảm bảo chất lượng đầu ra ổn định, giảm thiểu lỗi ngụy tạo thông tin (hallucination) của AI.
  - Relationship - liên hệ với khái niệm khác: Tương tự như cơ chế kiểm duyệt nội dung trước khi xuất bản.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Không có pipeline mã nguồn chạy trực tiếp cho bài học này. Tuy nhiên, luồng kiến trúc đề xuất cho hệ thống tự trị nâng cao bao gồm:
1. Input: Yêu cầu nghiên cứu ban đầu từ người dùng.
2. Processing steps:
   - Bước 1: Agent hỏi làm rõ tự động sinh ra 3 câu hỏi sâu.
   - Bước 2: Người dùng nhập câu trả lời.
   - Bước 3: Planner Agent kết hợp yêu cầu ban đầu và câu trả lời để lên phương án tìm kiếm.
   - Bước 4: Search Agent chạy tìm kiếm song song.
   - Bước 5: Review Agent (Evaluator) kiểm tra dữ liệu tìm được. Nếu thấy thiếu thông tin quan trọng, bàn giao (handoff) ngược lại cho Search Agent để tìm thêm từ khóa mới. Nếu đủ, chuyển tiếp cho Writer Agent.
   - Bước 6: Writer Agent viết báo cáo.
3. Output: Báo cáo chất lượng cao đã qua kiểm định và gửi email HTML.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Cloud Deployment via Gradio CLI - triển khai đám mây qua dòng lệnh Gradio
  - Purpose - mục đích: Lưu trữ ứng dụng giao diện Gradio lên máy chủ công cộng trực tuyến để người khác có thể truy cập qua link web và chia sẻ rộng rãi.
  - When to use - dùng khi nào: Khi muốn xuất bản sản phẩm Agent cá nhân làm portfolio chia sẻ lên các mạng xã hội như LinkedIn.
  - Trade-off - đánh đổi: Cần quản lý cấu hình các biến môi trường nhạy cảm (như API Keys) trên bảng thiết lập của Hugging Face để tránh rò rỉ mã bảo mật.
  - Common mistake - lỗi dễ gặp: Chạy lệnh triển khai nhưng quên thiết lập các secret variables (như `OPENAI_API_KEY`, `SENDGRID_API_KEY`) trên Hugging Face Spaces dashboard, dẫn đến ứng dụng bị sập ngay khi người dùng nhấn nút chạy thử trực tuyến.

## 8. Code Walkthrough - Phân tích code nếu có
- Buổi học này thảo luận về các thử thách kiến trúc mở rộng và triển khai ứng dụng Gradio lên Hugging Face Spaces bằng lệnh `gradio deploy`, không có file code riêng biệt cho tính năng mở rộng này trong thư mục nguồn cung cấp.

## 9. Options / Trade-offs - Bản đồ lựa chọn
- Option: Triển khai lên Hugging Face Spaces (Không gian Hugging Face)
  - Pros: Hoàn toàn miễn phí, tích hợp rất sâu với các ứng dụng Gradio, tự động hóa toàn bộ hạ tầng container phía sau, dễ dàng chia sẻ công khai.
  - Cons: Giới hạn cấu hình phần cứng miễn phí (CPU thường chạy chậm), mã nguồn ứng dụng mặc định sẽ ở chế độ công khai (public) trừ khi trả phí cấu hình private.
  - When to choose: Phù hợp nhất cho các dự án demo cá nhân, học tập và giới thiệu năng lực kỹ thuật trên mạng xã hội.
- Option: Tự lưu trữ trên máy chủ đám mây riêng (AWS, GCP, VPS)
  - Pros: Bảo mật mã nguồn tuyệt đối, tùy biến hiệu năng phần cứng tùy ý.
  - Cons: Tốn chi phí vận hành hàng tháng, đòi hỏi kiến thức sâu về quản trị hệ thống và triển khai mạng (DevOps).
  - When to choose: Khi phát triển các ứng dụng doanh nghiệp thương mại có yêu cầu bảo mật thông tin cao.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Triển khai ứng dụng lên Hugging Face Spaces thành công nhưng ứng dụng báo lỗi đỏ ngay khi người dùng nhập câu hỏi đầu tiên.
- Root cause: Quên không thiết lập các khóa bí mật (secrets) như `OPENAI_API_KEY` và `SENDGRID_API_KEY` trong phần cấu hình của Hugging Face Spaces, dẫn đến việc ứng dụng không thể kết nối tới các dịch vụ API bên ngoài.
- Symptom: Trạng thái ứng dụng hiển thị `Runtime Error` hoặc log báo lỗi `KeyError` do thiếu biến môi trường.
- Fix / prevention: [Alert] Sau khi thực hiện lệnh `gradio deploy`, hãy truy cập ngay vào phần Settings trên trang Hugging Face Space của bạn, tìm mục **Variables and secrets** để khai báo đầy đủ các API Keys cần thiết cho hệ thống Agent hoạt động.

## 11. Knowledge Extension - Kiến thức mở rộng
- Hugging Face Spaces sử dụng công nghệ ảo hóa Docker ở phía sau. Khi bạn chạy lệnh `gradio deploy`, Gradio CLI sẽ tự động đóng gói mã nguồn của bạn, tạo ra một tệp tin cấu hình môi trường tương thích và tải lên Hugging Face. Máy chủ Hugging Face sẽ dựng một Docker image dựa trên phiên bản Python được yêu cầu, cài đặt các thư viện trong file `requirements.txt` (nếu có) và khởi chạy container để chạy file ứng dụng Gradio của bạn trực tuyến.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Việc thêm cơ chế Clarifying Questions giúp Agent nắm bắt đúng ý định nghiên cứu của người dùng trước khi tìm kiếm.
2. Ứng dụng mô hình Evaluator-Optimizer để tạo vòng lặp kiểm tra chất lượng báo cáo tự động.
3. Bàn giao quyền điều khiển (handoffs) cho phép Agent tự quyết định tiếp tục tìm kiếm hoặc dừng luồng chạy.
4. Triển khai nhanh ứng dụng web Gradio lên Hugging Face Spaces bằng dòng lệnh `gradio deploy`.
5. [Alert] Phải thiết lập các khóa bí mật API Keys trong phần Settings của Hugging Face Spaces sau khi deploy.

### Self-check questions
1. Hãy mô tả cách bạn có thể thiết lập một Agent đánh giá (Evaluator) kiểm định chất lượng báo cáo và hướng dẫn sửa đổi cho Agent viết bài.
2. Nêu các bước cần thực hiện để cấu hình an toàn các API keys khi deploy ứng dụng lên Hugging Face Spaces.

### Flashcards
- Q: Lệnh CLI nào dùng để xuất bản nhanh ứng dụng Gradio lên đám mây Hugging Face?
  A: Lệnh `gradio deploy`.
- Q: Tại sao cần cấu hình API keys trong mục Settings Secrets của Hugging Face Space thay vì viết trực tiếp vào code?
  A: Để tránh việc rò rỉ khóa bảo mật công khai khi mã nguồn được đẩy lên cộng đồng Hugging Face.

## 13. Missing Inputs - Còn thiếu gì
- Không có.
