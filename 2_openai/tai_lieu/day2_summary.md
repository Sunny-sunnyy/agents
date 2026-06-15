# Day 2 - Build AI Sales Agents with SendGrid - Tools & Collaboration in Agent SDK

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

---

# 34. Day 2 - Build AI Sales Agents with SendGrid - Tools & Collaboration in Agent SDK

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([2_lab2.ipynb](file:///G:/Agent2026Win/agents/2_openai/2_lab2.ipynb#L49-L185))
- Summary lịch sử: đã dùng ([day1_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day1_summary.md) - bối cảnh về OpenAI Agents SDK cơ bản)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học tập trung vào việc cài đặt ban đầu cho dự án SDR và giới thiệu cơ chế streaming.

## 2. Executive Summary - Tóm tắt cốt lõi
- Bắt đầu dự án Agentic Framework thực tế đầu tiên: Xây dựng hệ thống SDR - Sales Development Representative (đại lý phát triển bán hàng) chuyên gửi email chào hàng lạnh (cold sales email).
- Giới thiệu dịch vụ email giao dịch SendGrid (thuộc sở hữu của Twilio) và hướng dẫn xác thực tài khoản thông qua Sender Authentication.
- Hướng dẫn cấu hình API Key trong file `.env` với khóa `SENDGRID_API_KEY`.
- Khởi tạo 3 Agent bán hàng chuyên biệt với 3 phong cách khác nhau: Professional (nghiêm túc, chuyên nghiệp), Engaging (hài hước, thu hút), và Busy (ngắn gọn, trực diện).
- Giới thiệu cơ chế streaming phản hồi bất đồng bộ thông qua phương thức `Runner.run_streamed()` để cải thiện trải nghiệm người dùng cuối.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu kiến trúc cơ bản của hệ thống đại lý bán hàng tự động (SDR).
  - Hiểu cơ chế hoạt động của luồng streaming bất đồng bộ trong OpenAI Agents SDK.
- Practical goals - mục tiêu thực hành:
  - Thiết lập thành công tài khoản SendGrid và Sender Authentication để gửi mail thực tế.
  - Cấu hình API key an toàn trong file `.env`.
  - Khởi tạo các Agent với các chỉ dẫn hệ thống (instructions) khác nhau.
  - Viết code Python sử dụng `Runner.run_streamed` và lặp qua các sự kiện stream bất đồng bộ.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao việc phân chia các Agent theo nhiều phong cách viết email khác nhau lại đem lại hiệu quả cao hơn việc dùng một Agent chung chung?
  - Sự khác biệt về mặt lập trình giữa việc chạy Runner thông thường và chạy Runner dạng stream là gì?

## 4. Previous Context - Liên hệ với bài trước
Kế thừa trực tiếp cú pháp khai báo thực thể `Agent` và lớp `Runner` từ Day 1 để chuyển giao từ ví dụ kể chuyện cười Jokester sang dự án doanh nghiệp thực tế.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Transactional Email Service - Dịch vụ email giao dịch
  - Meaning - nghĩa: Hệ thống chuyên dụng để gửi email tự động từ ứng dụng đến người dùng cuối một cách nhanh chóng và tin cậy (ở đây dùng SendGrid).
  - Why it matters - vì sao quan trọng: Đảm bảo email của Agent được gửi đi thực tế qua internet thay vì chỉ in ra màn hình console.
  - Relationship - liên hệ với khái niệm khác: Tích hợp trực tiếp làm công cụ (tool) thực thi của Agent.
- Term - thuật ngữ: Sender Authentication - Xác thực người gửi
  - Meaning - nghĩa: Quy trình xác minh với nhà cung cấp email rằng bạn thực sự sở hữu địa chỉ email gửi đi.
  - Why it matters - vì sao quan trọng: Ngăn chặn email bị các bộ lọc thư rác đánh dấu là spam hoặc bị chặn hoàn toàn.
  - Relationship - liên hệ với khái niệm khác: Là bước bắt buộc phải thực hiện trong bảng điều khiển của SendGrid trước khi gọi API.
- Term - thuật ngữ: Streaming - Luồng dữ liệu thời gian thực
  - Meaning - nghĩa: Cơ chế truyền tải dữ liệu phản hồi từ LLM dưới dạng các mảnh nhỏ (tokens/deltas) ngay khi chúng vừa được sinh ra.
  - Why it matters - vì sao quan trọng: Giảm đáng kể thời gian chờ đợi cảm nhận (perceived latency) của người dùng, giúp giao diện ứng dụng mượt mà hơn.
  - Relationship - liên hệ với khái niệm khác: Được kích hoạt bằng hàm `Runner.run_streamed()` thay vì `Runner.run()`.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình thiết lập và chạy thử nghiệm email ban đầu:
1. Input: Địa chỉ email cá nhân, tài khoản SendGrid mới đăng ký.
2. Processing steps:
   - Bước 1: Tạo API Key trong Settings của SendGrid và lưu vào file `.env` dưới tên `SENDGRID_API_KEY`.
   - Bước 2: Thực hiện xác thực "Verify a Single Sender" trong SendGrid Sender Authentication.
   - Bước 3: Viết và chạy hàm `send_test_email()` để kiểm tra kết nối mạng và API Key (kỳ vọng nhận mã trạng thái HTTP 202).
   - Bước 4: Khởi tạo 3 thực thể Agent bán hàng với 3 bộ chỉ dẫn hệ thống phong cách (`instructions1`, `instructions2`, `instructions3`).
   - Bước 5: Thực thi `Runner.run_streamed()` trên `sales_agent1` và in trực tiếp các delta text nhận được ra terminal.
3. Output: Email test được gửi đến hòm thư cá nhân và bản nháp email chuyên nghiệp được stream thành công.
4. Control flow / data flow: Chạy tuần tự các bước cấu hình và gọi API bất đồng bộ.
5. Decision points: Nếu xuất hiện lỗi chứng chỉ bảo mật SSL, thực hiện cấu hình trỏ file chứng chỉ bảo mật thông qua thư viện `certifi`.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Lặp qua sự kiện stream bất đồng bộ bằng `async for`
  - Purpose - mục đích: Đọc và hiển thị từng từ (token) của email nháp ngay khi LLM vừa sinh ra.
  - When to use - dùng khi nào: Khi phát triển giao diện chat hoặc terminal tương tác thời gian thực với người dùng.
  - Trade-off - đánh đổi: Cấu trúc code phức tạp hơn do phải lọc các loại sự kiện hệ thống khác nhau của stream.
  - Common mistake - lỗi dễ gặp: Quên sử dụng từ khóa `async` trước vòng lặp `for` (`async for event in ...`) dẫn đến lỗi cú pháp bất đồng bộ.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [2_lab2.ipynb](file:///G:/Agent2026Win/agents/2_openai/2_lab2.ipynb#L49-L185)
- Purpose - mục đích: Thiết lập môi trường, kiểm tra gửi email qua SendGrid và khởi tạo các Sales Agent cùng luồng stream kết quả.
- Key logic - logic chính:
  - Khởi tạo thư viện SendGrid và nạp biến môi trường.
  - Định nghĩa 3 phong cách email khác nhau qua instructions.
  - Gọi chạy stream bất đồng bộ sử dụng `Runner.run_streamed` và kiểm tra kiểu sự kiện để in ra nội dung.
- Important lines / functions:
  - Dòng 56: `from openai.types.responses import ResponseTextDeltaEvent`
    - Ý nghĩa: Nạp lớp sự kiện đại diện cho dữ liệu chữ viết (text delta) nhận được từ stream.
  - Dòng 82: `def send_test_email():`
    - Ý nghĩa: Định nghĩa hàm kiểm tra kết nối với SendGrid API Client để gửi thư thử nghiệm.
  - Dòng 180: `result = Runner.run_streamed(sales_agent1, input="Write a cold sales email")`
    - Ý nghĩa: Khởi chạy agent dưới dạng stream sự kiện (không dùng `await` ở đây vì hàm này trả về một generator bất đồng bộ).
  - Dòng 181-183:
    ```python
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)
    ```
    - Ghi chú: Vòng lặp bất đồng bộ duyệt qua các sự kiện, kiểm tra nếu sự kiện là `raw_response_event` và chứa dữ liệu kiểu `ResponseTextDeltaEvent` thì in phần chữ mới sinh ra (`event.data.delta`) ra màn hình mà không xuống dòng.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Không áp dụng cho phần cài đặt cơ bản này.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Lỗi `SSL: CERTIFICATE_VERIFY_FAILED` khi gọi API của SendGrid từ Python.
- Root cause: Hệ thống Python cục bộ (đặc biệt trên Windows hoặc macOS) không tìm thấy hoặc chứa chứng chỉ bảo mật SSL cũ.
- Symptom: Tiến trình gửi email bị lỗi kết nối SSL và không có thư nào được gửi đi.
- Fix / prevention: Chạy lệnh `uv pip install --upgrade certifi` và bổ sung cấu hình trỏ đường dẫn chứng chỉ trong code Python:
  ```python
  import certifi
  import os
  os.environ['SSL_CERT_FILE'] = certifi.where()
  ```

## 11. Knowledge Extension - Kiến thức mở rộng
Không có.

## 12. Study Pack - Gói ôn tập
### Must remember
1. SendGrid API Key phải được lưu bảo mật trong file `.env` dưới biến `SENDGRID_API_KEY`.
2. Trước khi gửi email qua SendGrid, địa chỉ email gửi đi bắt buộc phải được xác thực Sender Authentication.
3. `Runner.run_streamed` được sử dụng thay thế cho `Runner.run` để sinh phản hồi dạng stream thời gian thực.
4. Lặp qua các sự kiện stream yêu cầu cú pháp vòng lặp bất đồng bộ `async for`.
5. Cảnh báo lỗi SSL thường gặp khi gọi API từ Python có thể được khắc phục bằng thư viện `certifi`.

### Self-check questions
1. Tại sao phải thực hiện Sender Authentication trong SendGrid?
2. Hãy giải thích ý nghĩa của lớp `ResponseTextDeltaEvent` trong vòng lặp stream.

### Flashcards
- Q: Vòng lặp nào dùng để duyệt qua các sự kiện của `Runner.run_streamed()`?
  A: `async for event in result.stream_events():`.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 35. Day 2 - Concurrent LLM Calls - Implementing Asyncio for Parallel Agent Execution

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([2_lab2.ipynb](file:///G:/Agent2026Win/agents/2_openai/2_lab2.ipynb#L191-L244))
- Summary lịch sử: đã dùng ([day1_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day1_summary.md) - lý thuyết Async Python bài 29)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học tập trung vào lập trình song song các cuộc gọi LLM và xây dựng agent chọn lọc.

## 2. Executive Summary - Tóm tắt cốt lõi
- Triển khai kỹ thuật chạy song song (concurrent execution) 3 Agent bán hàng để sinh 3 bản nháp email cùng lúc bằng `asyncio.gather`.
- Nhấn mạnh hiệu quả của Async Python khi làm việc với LLM API (tác vụ I/O bound): Tổng thời gian chờ đợi 3 agent chạy song song chỉ tương đương với thời gian chạy của 1 agent đơn lẻ.
- Tạo một Agent đánh giá chuyên biệt có tên `sales_picker` với nhiệm vụ đọc 3 bản nháp email và chọn ra bản nháp tốt nhất (dưới vai trò khách hàng).
- Bao bọc toàn bộ chuỗi tác vụ song song và chấm điểm này trong context manager `trace` để tạo sơ đồ giám sát tập trung trên OpenAI Platform.
- Định hình đây là một cấu trúc **Agentic Workflow** (luồng công việc AI) sơ khai, nơi các bước chạy được lập trình cứng (hard-coded) bằng Python.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách tối ưu hóa thời gian chạy của các Agent bằng cách gửi các yêu cầu LLM song song.
  - Hiểu mô hình luồng công việc AI (Agentic Workflow) và vai trò của Agent chấm điểm (Evaluation Agent).
- Practical goals - mục tiêu thực hành:
  - Sử dụng cú pháp `asyncio.gather` để chạy nhiều coroutine `Runner.run` đồng thời.
  - Khởi tạo và cấu hình `sales_picker` Agent để chấm điểm và lọc đầu ra.
  - Kiểm tra và phân tích vết trace song song trên OpenAI Platform Traces.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao gọi song song 3 API LLM lại không tốn gấp 3 lần thời gian chạy?
  - Sự khác biệt về luồng chạy giữa các tác vụ trong block `asyncio.gather` và các tác vụ tuần tự thông thường là gì?

## 4. Previous Context - Liên hệ với bài trước
Áp dụng trực tiếp lý thuyết Async Python và cơ chế hoạt động của `asyncio.gather` đã học ở Bài 29 để giải quyết bài toán sinh bản nháp email hàng loạt.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Agentic Workflow - Luồng công việc AI
  - Meaning - nghĩa: Mô hình lập trình trong đó các bước gọi LLM và xử lý dữ liệu được thiết lập cố định bằng mã nguồn (hard-coded), mô hình ngôn ngữ chỉ chịu trách nhiệm xử lý thông tin tại mỗi bước mà không tự quyết định luồng đi tiếp theo.
  - Why it matters - vì sao quan trọng: Đem lại tính ổn định, dễ dự đoán và dễ kiểm soát cho các quy trình nghiệp vụ doanh nghiệp chuẩn hóa.
  - Relationship - liên hệ với khái niệm khác: Đối lập với Autonomous Agent (Tác nhân tự trị) nơi LLM tự quyết định bước đi tiếp theo.
- Term - thuật ngữ: Evaluation Agent - Tác nhân đánh giá
  - Meaning - nghĩa: Agent được thiết lập chỉ dẫn hệ thống để đóng vai trò bộ lọc, chuyên chấm điểm, nhận xét hoặc lựa chọn kết quả đầu ra tốt nhất từ các tác nhân khác.
  - Why it matters - vì sao quan trọng: Giúp tự động hóa khâu kiểm soát chất lượng (QC) đầu ra của hệ thống AI.
  - Relationship - liên hệ với khái niệm khác: Là thành phần cốt lõi trong mẫu thiết kế Evaluator-Optimizer.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình Agentic Workflow sinh và chọn lọc email:
1. Input: Chuỗi prompt yêu cầu viết email nháp `"Write a cold sales email"`.
2. Processing steps:
   - Bước 1: Khởi chạy song song `Runner.run` cho `sales_agent1`, `sales_agent2` và `sales_agent3` qua `asyncio.gather`.
   - Bước 2: Nhận về danh sách kết quả chứa 3 bản nháp email từ 3 agent.
   - Bước 3: Gộp 3 bản nháp này thành một chuỗi văn bản lớn, phân tách rõ ràng bằng tiêu đề.
   - Bước 4: Gửi chuỗi văn bản gộp này cho `sales_picker` Agent để chọn ra email tốt nhất.
3. Output: Email duy nhất được `sales_picker` lựa chọn mà không kèm theo lời giải thích.
4. Control flow / data flow: Chạy song song ở bước 1, sau đó chạy tuần tự ở bước 4. Luồng điều khiển hoàn toàn cố định bằng code Python.
5. Decision points: `sales_picker` quyết định email chiến thắng dựa trên tiêu chí system prompt của nó.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Nhóm cuộc gọi song song vào `with trace`
  - Purpose - mục đích: Nhóm các cuộc gọi LLM chạy đồng thời lại dưới một trace cha duy nhất, giúp giao diện OpenAI Platform hiển thị chúng song song trên trục thời gian, dễ so sánh thời gian chạy và lượng token của từng nhánh.
  - When to use: Khi thực hiện các tác vụ sinh thử nghiệm song song (như A/B testing nội dung email).
  - Trade-off - đánh đổi: Tăng đột biến lượng token tiêu thụ tại cùng một thời điểm.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [2_lab2.ipynb](file:///G:/Agent2026Win/agents/2_openai/2_lab2.ipynb#L191-L244)
- Purpose - mục đích: Chạy song song 3 agent tạo email nháp và dùng agent thứ 4 để chọn ra email tốt nhất.
- Key logic - logic chính:
  - Cấu hình agent chấm điểm `sales_picker`.
  - Bọc khối lệnh trong `with trace`.
  - Thực thi song song bằng `asyncio.gather` và chuyển kết quả đến agent chấm điểm.
- Important lines / functions:
  - Dòng 213: Khởi tạo Agent `sales_picker` với chỉ dẫn rõ ràng: đóng vai khách hàng, chọn email dễ phản hồi nhất và chỉ trả về nội dung email được chọn (không giải thích).
  - Dòng 231-235:
    ```python
    results = await asyncio.gather(
        Runner.run(sales_agent1, message),
        Runner.run(sales_agent2, message),
        Runner.run(sales_agent3, message),
    )
    ```
    - Ghi chú: Gọi đồng thời 3 coroutine Runner.run. Event loop sẽ gửi cả 3 request lên OpenAI cùng lúc.
  - Dòng 240: `best = await Runner.run(sales_picker, emails)`
    - Ghi chú: Gửi văn bản gộp 3 email cho picker để lấy kết quả cuối cùng.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Không áp dụng.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Agent chấm điểm `sales_picker` vẫn viết thêm phần giải thích dài dòng ở đầu hoặc cuối câu trả lời thay vì chỉ trả về email được chọn.
- Root cause: Prompt chỉ dẫn cho picker chưa đủ mạnh hoặc thiếu ràng buộc định dạng đầu ra.
- Fix / prevention: Viết các câu lệnh ràng buộc (constraints) ở cuối system prompt của picker bằng chữ IN HOA hoặc sử dụng cơ chế Structured Outputs (sẽ học ở các bài sau).

## 11. Knowledge Extension - Kiến thức mở rộng
Không có.

## 12. Study Pack - Gói ôn tập
### Must remember
1. `asyncio.gather` là phương thức tối ưu để chạy song song nhiều agent gọi LLM API.
2. Vết trace của các tác vụ chạy song song sẽ hiển thị đồng thời (nằm đè lên nhau về mốc thời gian) trên giao diện OpenAI Platform Traces.
3. Luồng công việc có cấu trúc cố định và gọi LLM tại từng bước được gọi là Agentic Workflow.
4. Ràng buộc đầu ra của agent nên được đặt ở cuối system prompt để tăng hiệu quả kiểm soát.

### Self-check questions
1. Tại sao việc gộp các cuộc gọi LLM vào `asyncio.gather` lại giúp giảm tổng thời gian thực thi của chương trình?
2. Hãy mô tả cấu trúc hiển thị của trace khi chạy song song 3 agent trên OpenAI Platform.

### Flashcards
- Q: Cơ chế chạy song song các agent giúp tối ưu hóa loại tác vụ nào?
  A: Tác vụ I/O bound (như chờ phản hồi từ LLM API qua mạng internet).

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 36. Day 2 - Converting Agents into Tools - Building Hierarchical AI Systems

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([2_lab2.ipynb](file:///G:/Agent2026Win/agents/2_openai/2_lab2.ipynb#L258-L427))
- Summary lịch sử: đã dùng ([day1_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day1_summary.md) - vai trò của tool và runner ở bài 30 & 31)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học thực hành chuyển đổi Agent thành Tool và xây dựng hệ thống quản lý phân cấp.

## 2. Executive Summary - Tóm tắt cốt lõi
- Giới thiệu kỹ thuật chuyển đổi một đối tượng `Agent` hoàn chỉnh thành một `tool` bằng phương thức `.as_tool()`.
- Giải thích cơ chế tự động trích xuất và sinh JSON schema mô tả tham số công cụ từ docstring và kiểu dữ liệu (type hinting) của hàm Python khi sử dụng decorator `@function_tool`.
- Xây dựng một **Hệ thống AI phân cấp** (Hierarchical AI System) thông qua việc tạo ra một Agent lập kế hoạch cấp cao (Planning Agent) tên là `Sales Manager`.
- Cung cấp cho `Sales Manager` danh sách 4 công cụ bao gồm: 3 sales agents (đã bọc làm tool) và 1 hàm gửi email thực tế (`send_email`).
- Nhật ký trace của hệ thống phân cấp này hiển thị cấu trúc dạng cây trực quan: cuộc gọi từ `Sales Manager` -> gọi các sales agent tools -> thực thi cuộc gọi LLM thực tế của từng agent worker tương ứng.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cơ chế hoạt động của Agent-as-a-tool dưới góc độ mã nguồn.
  - Hiểu kiến trúc hệ thống AI phân cấp (Hierarchical AI System) và vai trò của Planning Agent.
- Practical goals - mục tiêu thực hành:
  - Chuyển đổi thành công các thực thể Agent thành Tool bằng `.as_tool()`.
  - Tạo công cụ tự động từ hàm Python bằng `@function_tool` và docstring chuẩn.
  - Cấu hình Planning Agent nhận và điều phối các công cụ đó.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao việc dùng `@function_tool` lại giúp loại bỏ hoàn toàn việc viết cấu hình JSON thô cho Function Calling?
  - Sự khác biệt về vết trace của hệ thống phân cấp so với hệ thống chạy song song thủ công ở bài trước là gì?

## 4. Previous Context - Liên hệ với bài trước
Hiện thực hóa triết lý thiết kế loại bỏ boilerplate code phiền toái khi viết JSON định nghĩa tools của OpenAI Agents SDK đã học ở Bài 30.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Agent-as-a-tool - Tác nhân đóng vai trò công cụ
  - Meaning - nghĩa: Kỹ thuật đóng gói toàn bộ quy trình chạy của một Agent (bao gồm system prompt, model) thành một giao diện công cụ chuẩn, cho phép Agent khác gọi thực thi nó như một hàm Python thông thường.
  - Why it matters - vì sao quan trọng: Giúp tái sử dụng các agent chuyên biệt như các module chức năng độc lập trong hệ thống lớn.
  - Relationship - liên hệ với khái niệm khác: Được tạo ra bằng cách gọi phương thức `agent.as_tool()` trên đối tượng agent đích.
- Term - thuật ngữ: Hierarchical AI System - Hệ thống AI phân cấp
  - Meaning - nghĩa: Mô hình kiến trúc AI Agent trong đó có một Agent cấp cao đóng vai trò quản lý/lập kế hoạch (Manager/Planner) để điều phối, phân chia công việc cho các Agent cấp thấp hơn (Workers) hoặc các công cụ thực thi cụ thể.
  - Why it matters - vì sao quan trọng: Phù hợp để giải quyết các bài toán phức tạp đòi hỏi nhiều bước lập kế hoạch và thực thi chuyên biệt.
  - Relationship - liên hệ với khái niệm khác: Luồng điều khiển thuộc về Manager, các worker nhận việc và phải trả kết quả về cho Manager.
- Term - thuật ngữ: @function_tool
  - Meaning - nghĩa: Decorator của SDK dùng để bọc một hàm Python thông thường, biến nó thành đối tượng công cụ có cấu trúc JSON schema tương thích với API của OpenAI.
  - Why it matters - vì sao quan trọng: Tự động hóa khâu sinh cấu hình Function Calling từ mã nguồn Python.
  - Relationship - liên hệ với khái niệm khác: Đọc docstring của hàm làm phần mô tả công cụ (tool description) và đọc type hinting của các tham số hàm làm định nghĩa schema.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình hoạt động phân cấp của Sales Manager Agent:
1. Input: Lệnh từ người dùng `"Send a cold sales email addressed to 'Dear CEO'"`.
2. Processing steps:
   - Bước 1: `Sales Manager` tiếp nhận yêu cầu và tự lập kế hoạch chạy.
   - Bước 2: `Sales Manager` gọi lần lượt 3 công cụ `sales_agent1`, `sales_agent2`, `sales_agent3` để lấy 3 bản nháp email.
   - Bước 3: `Sales Manager` tự so sánh và chọn ra email tốt nhất dựa trên tiêu chí của nó.
   - Bước 4: `Sales Manager` gọi công cụ `send_email` để gửi đi bản nháp tốt nhất đó.
3. Output: Mã phản hồi thành công và email được gửi đi thực tế.
4. Control flow / data flow: Luồng điều khiển phân cấp (Manager gọi và nhận kết quả từ Worker để xử lý tiếp).
5. Decision points: `Sales Manager` tự quyết định thứ tự gọi các công cụ và chọn email nào để gửi đi.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Tự động trích xuất Schema qua `@function_tool` và Docstring
  - Purpose - mục đích: Loại bỏ mã nguồn boilerplate cồng kềnh, giúp lập trình viên chỉ cần tập trung viết logic hàm Python thuần túy.
  - When to use - dùng khi nào: Khai báo công cụ từ các hàm hệ thống (như gửi mail, truy vấn cơ sở dữ liệu, đọc ghi file).
  - Trade-off - đánh đổi: Đòi hỏi lập trình viên phải viết docstring chuẩn chỉ và định nghĩa rõ ràng kiểu dữ liệu tham số (type hinting).
  - Common mistake - lỗi dễ gặp: Quên không viết docstring cho hàm dẫn đến việc LLM không hiểu chức năng của công cụ và gọi sai hoặc không gọi công cụ.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [2_lab2.ipynb](file:///G:/Agent2026Win/agents/2_openai/2_lab2.ipynb#L316-L427)
- Purpose - mục đích: Chuyển đổi hàm và Agent thành Tool, sau đó chạy thông qua Sales Manager.
- Key logic:
  - Khai báo hàm `send_email` có sử dụng decorator `@function_tool`.
  - Dùng phương thức `.as_tool` trên 3 Sales Agent.
  - Khởi tạo Sales Manager Agent nhận danh sách các tool này.
- Important lines / functions:
  - Dòng 316: `@function_tool`
    - Ý nghĩa: Decorator chuyển đổi hàm `send_email` thành công cụ có JSON schema tự động sinh từ docstring ở dòng 318.
  - Dòng 358: `tool1 = sales_agent1.as_tool(tool_name="sales_agent1", tool_description=description)`
    - Ý nghĩa: Chuyển đổi `sales_agent1` thành thực thể công cụ `tool1`.
  - Dòng 421: `sales_manager = Agent(name="Sales Manager", instructions=instructions, tools=tools, model="gpt-4o-mini")`
    - Ý nghĩa: Tạo Planning Agent nhận danh sách `tools` gồm cả agent tools và function tools.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Không áp dụng.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Agent Manager gọi công cụ nhưng truyền sai định dạng tham số hoặc bị báo lỗi thiếu tham số.
- Root cause: Lập trình viên không khai báo kiểu dữ liệu cho tham số của hàm Python (ví dụ chỉ ghi `def send_email(body):` thay vì `def send_email(body: str):`).
- Fix / prevention: Luôn luôn khai báo đầy đủ type hinting cho các đối số đầu vào của hàm khi sử dụng `@function_tool`.

## 11. Knowledge Extension - Kiến thức mở rộng
Không có.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Decorator `@function_tool` tự động sinh JSON schema cho công cụ từ docstring và chữ ký hàm Python.
2. Hàm Python làm công cụ bắt buộc phải có docstring để LLM hiểu chức năng của nó.
3. Dùng `agent.as_tool(...)` để biến một agent thành một công cụ cho agent khác gọi.
4. Vết trace của hệ thống phân cấp hiển thị cuộc gọi lồng nhau dạng cây (nested tree structure) trên OpenAI Platform.

### Self-check questions
1. SDK trích xuất thông tin gì từ hàm Python để gửi cho OpenAI mô tả công cụ?
2. Sự khác biệt về luồng kiểm soát giữa hệ thống phân cấp (hierarchical) và luồng chạy song song thủ công (asyncio.gather) là gì?

### Flashcards
- Q: Thư viện lấy thông tin mô tả công cụ cho LLM từ đâu trong hàm Python?
  A: Từ khối ghi chú docstring (nằm trong cặp dấu ba nháy kép `"""`).

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 37. Day 2 - Agent Control Flow - When to Use Handoffs vs. Agents as Tools

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([2_lab2.ipynb](file:///G:/Agent2026Win/agents/2_openai/2_lab2.ipynb#L484-L589))
- Summary lịch sử: đã dùng ([day1_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day1_summary.md) - khái niệm handoff giới thiệu ở bài 30)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học đi sâu phân tích hai cơ chế điều khiển luồng Agent quan trọng.

## 2. Executive Summary - Tóm tắt cốt lõi
- Phân tích cặn kẽ sự khác biệt về mặt triết lý và kỹ thuật giữa hai mẫu thiết kế kiểm soát luồng chạy của Agent: **Agents-as-tools** (Tác nhân làm công cụ) và **Handoffs** (Chuyển giao quyền lực).
- Agents-as-tools hoạt động theo cơ chế **Yêu cầu - Phản hồi** (Request-Response): Control quay trở lại agent cha sau khi worker chạy xong (passes back).
- Handoffs hoạt động theo cơ chế **Ủy thác** (Delegation): Control chuyển giao hoàn toàn một chiều sang agent mới (passes across), flow không quay lại agent cũ trừ khi agent mới chủ động thực hiện một cú handoff ngược lại.
- Xây dựng 2 agent phụ trợ mới: `subject_writer` (để viết tiêu đề email) và `html_converter` (để định dạng email sang HTML).
- Khởi tạo `emailer_agent` (Email Manager) nhận nhiệm vụ định dạng và gửi email HTML, khai báo tham số `handoff_description` để hệ thống biết khả năng tiếp nhận chuyển giao của nó.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Phân biệt rõ nét cơ chế Handoff và Agent-as-a-tool về cả mặt lý thuyết lẫn sơ đồ chạy thực tế.
  - Hiểu cách thức bối cảnh hội thoại (conversation history) được chia sẻ khi thực hiện Handoff.
- Practical goals - mục tiêu thực hành:
  - Cấu hình thuộc tính `handoff_description` cho Agent.
  - Xây dựng Email Manager Agent nhận bối cảnh và điều phối các công cụ định dạng HTML.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao Handoff lại được ví như việc chuyển máy điện thoại trong tổng đài chăm sóc khách hàng?
  - Khi nào nên dùng Handoff thay vì Agent-as-a-tool?

## 4. Previous Context - Liên hệ với bài trước
Phát triển chi tiết khái niệm Handoff sơ khai đã được giới thiệu ngắn gọn trong mô hình 3 khái niệm của SDK ở Bài 30.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Handoff - Chuyển giao quyền lực
  - Meaning - nghĩa: Hành động chuyển giao toàn bộ bối cảnh cuộc hội thoại (message history) và quyền điều khiển từ Agent này sang Agent khác một chiều.
  - Why it matters - vì sao quan trọng: Giúp cấu trúc hệ thống Multi-agent linh hoạt hơn, cho phép các agent chuyên gia xử lý trọn gói các giai đoạn nghiệp vụ khác nhau mà không làm quá tải bối cảnh của agent ban đầu.
  - Relationship - liên hệ với khái niệm khác: Khai báo bằng cách đưa Agent đích vào tham số `handoffs` của Agent nguồn.
- Term - thuật ngữ: Request-Response Pattern - Mẫu Yêu cầu - Phản hồi
  - Meaning - nghĩa: Mô hình giao tiếp trong đó agent gọi một công cụ (hoặc agent khác dưới dạng tool) để thực hiện tác vụ phụ trợ và đợi nhận lại kết quả để tiếp tục xử lý.
  - Why it matters - vì sao quan trọng: Là cơ chế mặc định của Agent-as-a-tool.
  - Relationship - liên hệ với khái niệm khác: Giữ quyền kiểm soát (control flow) tập trung tại Agent gọi.
- Term - thuật ngữ: Delegation Pattern - Mẫu ủy quyền
  - Meaning - nghĩa: Mô hình giao tiếp chuyển giao hoàn toàn trách nhiệm thực thi một tác vụ lớn cho một tác nhân chuyên biệt xử lý từ đầu đến cuối mà không cần báo cáo kết quả tức thì về cho tác nhân chuyển giao.
  - Why it matters - vì sao quan trọng: Là cơ chế mặc định của Handoffs.
  - Relationship - liên hệ với khái niệm khác: Giúp module hóa tốt hệ thống lớn và giảm sự phụ thuộc chéo.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình xử lý của Email Manager Agent khi nhận chuyển giao:
1. Input: Nội dung text/markdown của email nháp được chuyển giao từ Sales Manager.
2. Processing steps:
   - Bước 1: Gọi công cụ `subject_writer` để sinh tiêu đề email phù hợp.
   - Bước 2: Gọi công cụ `html_converter` để chuyển đổi nội dung email nháp sang HTML định dạngEditorial đẹp mắt.
   - Bước 3: Gọi công cụ `send_html_email` để thực hiện gửi mail thực tế qua SendGrid.
3. Output: Trạng thái thành công `{"status": "success"}` và email HTML được gửi đi.
4. Control flow / data flow: Email Manager giữ quyền điều khiển và gọi các công cụ phụ trợ dạng Request-Response.
5. Decision points: Email Manager tự động chạy tuần tự các công cụ theo chỉ dẫn của nó.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Thiết lập mô tả chuyển giao `handoff_description`
  - Purpose - mục đích: Khai báo rõ ràng nhiệm vụ chuyên môn của Agent dưới dạng ngôn ngữ tự nhiên để mô hình ngôn ngữ lớn (LLM) của Agent chuyển giao biết khi nào và tại sao nên chuyển việc cho Agent này.
  - When to use - dùng khi nào: Bắt buộc phải khai báo khi thiết lập Agent nằm trong danh sách chuyển giao (`handoffs`) của Agent khác.
  - Trade-off - đánh đổi: LLM phải tự suy luận thời điểm chuyển giao dựa trên mô tả này, đòi hỏi mô tả phải viết rất rõ ràng.
  - Common mistake: Viết mô tả quá ngắn hoặc quá chung chung khiến LLM hiểu lầm và chuyển giao sai thời điểm.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [2_lab2.ipynb](file:///G:/Agent2026Win/agents/2_openai/2_lab2.ipynb#L497-L589)
- Purpose - mục đích: Cấu hình các công cụ phụ trợ (tiêu đề, HTML) và khởi tạo Email Manager Agent có hỗ trợ Handoff.
- Key logic:
  - Khởi tạo 2 Agent: subject_writer và html_converter rồi bọc thành tool.
  - Định nghĩa hàm gửi email HTML `send_html_email` bọc decorator `@function_tool`.
  - Tạo `emailer_agent` nhận các tool trên và khai báo `handoff_description`.
- Important lines / functions:
  - Dòng 511: `subject_tool = subject_writer.as_tool(tool_name="subject_writer", tool_description="Write a subject for a cold sales email")`
    - Ý nghĩa: Biến subject writer agent thành tool để Email Manager gọi.
  - Dòng 564-570:
    ```python
    emailer_agent = Agent(
        name="Email Manager",
        instructions=instructions,
        tools=tools, # tools = [subject_tool, html_tool, send_html_email]
        model="gpt-4o-mini",
        handoff_description="Convert an email to HTML and send it")
    ```
    - Ghi chú: Dòng 569 khai báo `handoff_description` đóng vai trò là nhãn hướng dẫn cho LLM biết khi nào nên chuyển cuộc hội thoại cho `Email Manager`.

## 9. Options / Trade-offs - Bản đồ lựa chọn
So sánh hai cơ chế điều phối luồng Agent:
- Option: Agent-as-a-tool
  - Pros: Quản lý luồng chạy tập trung, dễ theo dõi trạng thái, bối cảnh hội thoại của Manager không bị phân mảnh.
  - Cons: Gây phình to bối cảnh hội thoại (context window) của Agent gọi do phải lưu toàn bộ lịch sử trả lời của các công cụ.
  - When to choose: Các tác vụ bổ trợ nhỏ, mang tính chất truy vấn hoặc xử lý tiện ích ngắn hạn.
- Option: Handoff
  - Pros: Giảm tải dung lượng tokens cho Agent ban đầu, module hóa tốt, các agent con tự quản lý lịch sử hội thoại của riêng mình.
  - Cons: Rủi ro tạo vòng lặp vô hạn nếu các Agent tự ý chuyển giao công việc qua lại cho nhau mà không có điều kiện dừng.
  - When to choose: Khi quy trình nghiệp vụ chuyển hẳn sang một giai đoạn mới do một chuyên gia khác chịu trách nhiệm hoàn toàn (ví dụ: chuyển từ khâu "Tư vấn" sang khâu "Bán hàng").

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Agent chuyển giao nhầm hoặc không chịu chuyển giao công việc cho Agent đích.
- Root cause: Chuỗi mô tả `handoff_description` viết quá mơ hồ hoặc instructions của Agent chuyển giao không ghi rõ điều kiện cần bàn giao.
- Fix / prevention: Viết mô tả `handoff_description` thật rõ ràng, ngắn gọn và trực diện vào chuyên môn của agent đó; đồng thời ghi rõ lệnh bàn giao trong instructions của Agent nguồn.

## 11. Knowledge Extension - Kiến thức mở rộng
- *Cơ chế chia sẻ lịch sử tin nhắn trong Handoff*: Khi Handoff diễn ra, OpenAI Agents SDK sẽ chuyển toàn bộ lịch sử tin nhắn hiện tại (messages history) sang cho Agent mới nhận việc. Agent mới sẽ đọc toàn bộ bối cảnh lịch sử này để tiếp tục thực hiện chỉ dẫn hệ thống của riêng nó, đảm bảo tính liên tục của cuộc hội thoại mà không bị mất dấu thông tin.

## 12. Study Pack - Gói ôn tập
### Must remember
1. `Agent-as-a-tool` trả quyền điều khiển về cho tác nhân gọi (passes back).
2. `Handoff` chuyển giao toàn bộ bối cảnh và quyền điều hành đi tiếp một chiều (passes across).
3. Agent nhận handoff phải được khai báo trong danh sách `handoffs` của Agent gửi và bắt buộc có `handoff_description`.
4. Handoff giúp giảm tải áp lực dung lượng context window cho Agent chính.

### Self-check questions
1. Hãy giải thích tại sao Handoff lại phù hợp hơn Agent-as-a-tool khi xây dựng luồng chuyển đổi trạng thái nghiệp vụ phức tạp.
2. Lịch sử hội thoại được xử lý thế nào khi một cú Handoff xảy ra trong OpenAI Agents SDK?

### Flashcards
- Q: Khi dùng Handoff, quyền điều khiển có tự động quay về Agent ban đầu không?
  A: Không, quyền điều khiển được chuyển giao hoàn toàn cho Agent mới nhận việc.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 38. Day 2 - From Function Calls to Agent Autonomy - Sales Automation with OpenAI SDK

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([2_lab2.ipynb](file:///G:/Agent2026Win/agents/2_openai/2_lab2.ipynb#L597-L628))
- Summary lịch sử: đã dùng ([day1_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day1_summary.md) - kiến thức cơ sở)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học thực hành tích hợp hệ thống SDR tự động hoàn chỉnh và thảo luận lý thuyết chuyên sâu về tính tự trị (autonomy).

## 2. Executive Summary - Tóm tắt cốt lõi
- Tích hợp tất cả các thành phần thành một hệ thống SDR tự động hóa bán hàng hoàn chỉnh (Automated SDR): `Sales Manager` Agent (nhận 3 sales agents làm tools và `emailer_agent` làm handoffs).
- Thực thi thử nghiệm và phân tích vết trace phức tạp gồm 9 bước gọi công cụ/chuyển giao trên OpenAI Platform Traces.
- Phân tích sự khác biệt bản chất giữa **Agentic Workflow** và **Autonomous Agent** theo định nghĩa chuẩn của hãng Anthropic.
- Chỉ ra dòng cấu hình duy nhất trong instructions giúp nâng cấp hệ thống từ workflow tĩnh lên agent tự trị: Cho phép mô hình tự quyết định lặp lại việc gọi công cụ nếu chưa hài lòng với kết quả thu được.
- Đề xuất các giải pháp thay thế SendGrid khi gặp sự cố, tiêu biểu là tích hợp **Resend Email API** từ cộng đồng.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Phân biệt sâu sắc giữa Workflow và Agent theo định nghĩa hiện đại của Anthropic.
  - Hiểu cách thức hoạt động của vòng lặp tự trị (Autonomy Loop) và cách kiểm soát nó.
- Practical goals - mục tiêu thực hành:
  - Chạy thành công luồng Automated SDR tích hợp đầy đủ cả tools và handoffs.
  - Phân tích sơ đồ thời gian thực thi phức tạp của nhiều agent trên OpenAI Platform.
  - Biết cách tích hợp Resend Email làm giải pháp thay thế dự phòng cho SendGrid.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao việc cho phép Agent gọi lại công cụ nhiều lần lại tạo nên tính tự trị (autonomy)?
  - So sánh ưu nhược điểm của việc dùng SendGrid và Resend Email khi thực hành.

## 4. Previous Context - Liên hệ với bài trước
Tổng hợp toàn bộ các mảnh ghép đơn lẻ ở bài 34, 35, 36, 37 thành một giải pháp tự động hóa quy trình kinh doanh (business process automation) khép kín.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Agentic Workflow (Anthropic definition)
  - Meaning - nghĩa: Mô hình lập trình trong đó các bước gọi LLM được thiết lập cố định bằng mã nguồn Python tuần tự hoặc song song (như bài 35), không có sự linh hoạt tự quyết định bước đi của mô hình.
  - Why it matters - vì sao quan trọng: Thích hợp cho các tác vụ cần độ chính xác và tính lặp lại cao.
  - Relationship - liên hệ với khái niệm khác: Có tính dự đoán cao nhưng thiếu linh hoạt khi gặp tình huống bất ngờ.
- Term - thuật ngữ: Autonomous Agent (Anthropic definition)
  - Meaning - nghĩa: Hệ thống trong đó lập trình viên chỉ cung cấp các công cụ và mục tiêu, còn LLM tự do quyết định gọi công cụ nào, khi nào và tự đánh giá chất lượng sản phẩm để quyết định chạy lại hay dừng luồng.
  - Why it matters - vì sao quan trọng: Giải quyết các bài toán sáng tạo, cần sự linh hoạt tự sửa sai của AI.
  - Relationship - liên hệ với khái niệm khác: Tính tự trị (autonomy) được kích hoạt qua việc cho phép agent tự lặp lại cuộc gọi công cụ.
- Term - thuật ngữ: Autonomy - Tính tự trị
  - Meaning - nghĩa: Khả năng tự đưa ra quyết định hành động và tự điều chỉnh hướng đi của Agent để đạt mục tiêu mà không cần con người can thiệp vào luồng chạy.
  - Why it matters - vì sao quan trọng: Là thuộc tính định nghĩa sự khác biệt giữa AI Agent thực thụ và một chương trình script gọi API thông thường.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình hoạt động tích hợp của Automated SDR:
1. Input: Lệnh từ người dùng `"Send out a cold sales email addressed to Dear CEO from Alice"`.
2. Processing steps:
   - Bước 1: `Sales Manager` tiếp nhận yêu cầu.
   - Bước 2: Gọi đồng thời 3 sales agent tools để lấy nháp.
   - Bước 3: Đánh giá chất lượng các nháp. (Có thể gọi lại công cụ nếu chưa ưng ý).
   - Bước 4: Chọn nháp tốt nhất và thực hiện **Handoff** sang cho `Email Manager`.
   - Bước 5: `Email Manager` tiếp nhận, gọi `subject_writer` tạo tiêu đề, gọi `html_converter` tạo HTML.
   - Bước 6: `Email Manager` gọi `send_html_email` để gửi mail HTML thực tế.
3. Output: Email HTML được gửi thành công đến hòm thư người nhận.
4. Control flow / data flow: Kết hợp cả phân cấp (tools) và phân tán (handoff).
5. Decision points: Sales Manager quyết định thời điểm chấm dứt chọn và bàn giao; Email Manager quyết định các tham số định dạng.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Thiết lập instructions cho phép lặp lại công cụ (Autonomy Loop)
  - Purpose - mục đích: Cho phép agent tự tối ưu hóa hoặc sửa lỗi sản phẩm của chính nó mà không cần viết vòng lặp `while` cứng trong Python.
  - When to use - dùng khi nào: Các tác vụ sáng tạo hoặc sinh nội dung chất lượng cao cần qua nhiều khâu chỉnh sửa.
  - Trade-off - đánh đổi: Có thể làm tăng chi phí token và thời gian thực thi nếu agent rơi vào vòng lặp vô hạn.
  - Common mistake - lỗi dễ gặp: Prompt không ghi rõ điều kiện dừng hoặc tiêu chuẩn đánh giá khiến agent gọi tool vô hạn.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [2_lab2.ipynb](file:///G:/Agent2026Win/agents/2_openai/2_lab2.ipynb#L597-L628)
- Purpose - mục đích: Cấu hình đầy đủ instructions tự trị cho Sales Manager và khởi chạy luồng SDR tự động.
- Key logic:
  - Định nghĩa system prompt cho Sales Manager cho phép gọi tool nhiều lần.
  - Khởi tạo Sales Manager nhận danh sách tools và handoffs.
  - Chạy và ghi nhận trace.
- Important lines / functions:
  - Dòng 606: `"You can use the tools multiple times if you're not satisfied with the results from the first try."`
    - Ý nghĩa: Câu prompt cốt lõi kích hoạt tính tự trị (autonomy) cho phép Agent tự động lặp lại vòng gọi tool nếu đánh giá kết quả chưa tốt.
  - Dòng 616: Khởi tạo `Sales Manager` với cả tham số `tools` và `handoffs`.

## 9. Options / Trade-offs - Bản đồ lựa chọn
So sánh các phương án gửi email khi thực hành dự án:
- Option: SendGrid API (Dịch vụ chính thức của khóa học)
  - Pros: Hạ tầng gửi thư mạnh mẽ, được tích hợp sẵn trong mã nguồn lab.
  - Cons: Đăng ký tài khoản mới dễ bị hệ thống bảo mật khóa tự động; thường gặp lỗi chứng chỉ SSL trên Windows.
  - When to choose: Lựa chọn mặc định khi tài khoản SendGrid hoạt động bình thường.
- Option: Resend Email API (Giải pháp thay thế từ cộng đồng - Recommended)
  - Pros: Đăng ký cực kỳ nhanh chóng và đơn giản, không bị kiểm duyệt tài khoản gắt gao, ít gặp lỗi SSL.
  - Cons: Cần thay đổi thư viện import và hàm gửi thư trong code lab.
  - When to choose: Phương án dự phòng hoàn hảo khi SendGrid bị khóa tài khoản hoặc lỗi SSL không thể tự xử lý.
- Option: Xuất ra file phẳng (Flat File Output)
  - Pros: Không cần kết nối internet, chạy offline 100%, không cần đăng ký tài khoản bên thứ ba.
  - Cons: Không gửi được email thực tế đến hòm thư người dùng để kiểm tra trực quan.
  - When to choose: Khi chỉ muốn test nhanh logic chạy của Agent mà không quan tâm đến việc gửi email thực.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Agent chạy quá lâu hoặc rơi vào vòng lặp gọi công cụ vô hạn.
- Root cause: Cho phép agent gọi lại công cụ nhiều lần nhưng không chỉ rõ điều kiện dừng hoặc tiêu chí đánh giá thế nào là "đạt yêu cầu".
- Fix / prevention: Bổ sung các tiêu chí đánh giá rõ ràng và giới hạn số lần thử (ví dụ: "thử tối đa 2 lần") trong chỉ dẫn hệ thống.

## 11. Knowledge Extension - Kiến thức mở rộng
- *Giải pháp tích hợp Resend Email dự phòng*:
  - Cài đặt: `uv add resend`
  - Mã nguồn Python gửi mail HTML bằng Resend:
    ```python
    import resend
    import os

    resend.api_key = os.environ.get("RESEND_API_KEY")

    def send_resend_html_email(subject: str, html_body: str):
        params = {
            "from": "onboarding@resend.dev", # Địa chỉ gửi thử nghiệm mặc định
            "to": "your_verified_email@gmail.com",
            "subject": subject,
            "html": html_body,
        }
        response = resend.Emails.send(params)
        return {"status": "success", "id": response["id"]}
    ```

## 12. Study Pack - Gói ôn tập
### Must remember
1. Dòng chỉ dẫn cho phép mô hình chạy lại công cụ khi chưa hài lòng chính là điểm phân biệt giữa Workflow và Agent tự trị theo định nghĩa của Anthropic.
2. Việc kết hợp cả tools và handoffs giúp xây dựng các hệ thống tự động hóa quy trình nghiệp vụ (business process automation) phức tạp.
3. Nhật ký trace hiển thị rõ nét thời gian thực thi của từng Agent dưới dạng thanh màu trực quan.
4. Resend Email là phương án dự phòng tuyệt vời thay cho SendGrid khi gặp sự cố SSL hoặc khóa tài khoản.

### Self-check questions
1. Theo Anthropic, tại sao việc lập trình cứng các bước chạy lại được coi là "workflow" chứ không phải là "agent"?
2. Làm thế nào để thiết lập một agent tự trị có khả năng tự sửa lỗi sản phẩm của chính nó?

### Flashcards
- Q: Anthropic định nghĩa thế nào là một Agent tự trị?
  A: Là hệ thống mà LLM tự quyết định hướng đi, lựa chọn công cụ và lặp lại hành động dựa trên đánh giá độc lập của nó mà không bị lập trình cứng luồng chạy.

### Interview Q&A nếu phù hợp
- Q: Hãy phân tích điểm khác biệt lớn nhất giữa Agentic Workflow và Autonomous Agent. Cho ví dụ minh họa bằng mã nguồn của OpenAI Agents SDK.
  A:
  - **Agentic Workflow**: Các bước thực thi được mã hóa cứng bằng Python. Ví dụ ở bài 35: Ta dùng Python để gọi song song 3 sales agents, nhận kết quả, sau đó truyền vào `sales_picker` để lấy email tốt nhất. Luồng chạy hoàn toàn cố định và không thể thay đổi.
  - **Autonomous Agent**: Ta giao mục tiêu cho Agent và để Agent tự quyết định hành động. Ví dụ ở bài 38: Ta tạo `sales_manager` Agent, truyền vào các công cụ và hướng dẫn: "Review the drafts and choose the best email. You can use the tools multiple times if you are not satisfied". Agent tự quyết định gọi công cụ nào, tự đánh giá và tự lặp lại cuộc gọi nếu thấy chất lượng nháp chưa tốt mà không cần viết vòng lặp cứng trong Python.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 39. Day 2 - Agentic AI for Business - Creating Interactive Sales Outreach Tools

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này
- Summary lịch sử: đã dùng ([day1_summary.md](file:///G:/Agent2026Win/agents/2_openai/tai_lieu/day1_summary.md) - kiến thức cơ sở)
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học tổng kết Day 2 và định hướng lộ trình tiếp theo.

## 2. Executive Summary - Tóm tắt cốt lõi
- Bài học đúc kết toàn bộ chặng đường thực hành dự án SDR của Day 2 về việc ứng dụng Agentic AI vào các quy trình doanh nghiệp thực tế.
- Khuyến khích học viên đóng góp mã nguồn (PR) vào thư mục đóng góp cộng đồng `community_contributions` và chia sẻ dự án lên LinkedIn để kết nối cộng đồng.
- Định hướng lộ trình sang Day 3: Tiếp tục thảo luận sâu hơn về sự khác biệt giữa Tools và Agents, và nghiên cứu cơ chế **Guardrails** (thanh chắn bảo mật) để kiểm soát an toàn cho Agent.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách thức mở rộng dự án SDR thành hệ thống phản hồi hai chiều (Interactive SDR).
  - Hiểu vai trò của việc kiểm soát an toàn (Guardrails) đối với các ứng dụng Agent thực tế.
- Practical goals - mục tiêu thực hành:
  - Chuẩn bị đầy đủ kiến thức nền tảng để tiếp cận cơ chế Guardrails ở Day 3.
- What learner should be able to explain - người học cần giải thích được:
  - Cơ chế hoạt động của Webhook để nhận phản hồi email từ khách hàng là gì?
  - Tại sao Guardrails lại cực kỳ quan trọng đối với các Agent chạy trong môi trường thực tế?

## 4. Previous Context - Liên hệ với bài trước
Hệ thống hóa toàn bộ các kỹ thuật thực hành SDR đã học trong Day 2 để hướng tới việc mở rộng tính năng và bảo mật hệ thống.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Guardrails - Thanh chắn an toàn
  - Meaning - nghĩa: Các lớp kiểm duyệt dữ liệu đầu vào hoặc đầu ra của LLM nhằm đảm bảo Agent hoạt động trong giới hạn cho phép và không tạo ra nội dung nguy hại hoặc lệch lạc.
  - Why it matters - vì sao quan trọng: Là chốt chặn bảo mật bắt buộc đối với các ứng dụng Agent thương mại để tránh rủi ro rò rỉ dữ liệu hoặc phát ngôn sai lệch.
  - Relationship - liên hệ với khái niệm khác: Sẽ được nghiên cứu chi tiết ở Day 3.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Không có pipeline rõ ràng trong tài liệu nguồn. Nội dung mang tính chất định hướng thương mại và chuyển giao bài học.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Thiết lập SDR tương tác hai chiều (Interactive SDR)
  - Purpose - mục đích: Tự động phản hồi email khi khách hàng trả lời thư chào hàng, duy trì cuộc hội thoại liên tục mà không cần con người can thiệp.
  - When to use - dùng khi nào: Các hệ thống tự động hóa chăm sóc khách hàng và bán hàng tự động nâng cao.
  - Trade-off - đánh đổi: Yêu cầu hạ tầng phần mềm phức tạp hơn (webhooks, máy chủ HTTP tiếp nhận, xác định danh tính khách hàng).
  - Common mistake - lỗi dễ gặp: Bỏ qua kiểm soát bảo mật khiến agent phản hồi nhầm các email spam hoặc bị tấn công prompt injection qua email.

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Không áp dụng.

## 10. Pitfalls - Lỗi / bẫy thường gặp
Không áp dụng.

## 11. Knowledge Extension - Kiến thức mở rộng
- *Cơ chế hoạt động của Webhook trong SDR hai chiều*:
  1. Khi khách hàng nhấn Reply email, thư được gửi về server của SendGrid.
  2. SendGrid phân tích email và kích hoạt một HTTP POST Request (Webhook) gửi đến địa chỉ URL máy chủ của bạn (ví dụ một ứng dụng FastAPI chạy công khai).
  3. Máy chủ tiếp nhận payload chứa nội dung email trả lời, lọc ID cuộc hội thoại để lấy bối cảnh cũ và kích hoạt Agent để sinh email phản hồi tiếp theo.

## 12. Study Pack - Gói ôn tập
### Must remember
1. AI Agent có tiềm năng cực lớn trong việc tự động hóa toàn bộ quy trình nghiệp vụ kinh doanh thực tế (end-to-end business automation).
2. Có thể xây dựng SDR hai chiều bằng cách tích hợp SendGrid Webhooks.
3. Guardrails là chủ đề cốt lõi của ngày tiếp theo (Day 3) nhằm đảm bảo an toàn cho Agent.

### Self-check questions
1. Hãy trình bày ý tưởng xây dựng một Agent chăm sóc khách hàng tự động qua email sử dụng Webhooks.
2. Tại sao việc đưa hệ thống Agent vào vận hành thương mại lại bắt buộc phải có Guardrails?

### Flashcards
- Q: Webhook đóng vai trò gì trong hệ thống SDR hai chiều?
  A: Là cơ chế giúp SendGrid gửi tín hiệu HTTP chứa nội dung email phản hồi của khách hàng về máy chủ Python của bạn theo thời gian thực.

## 13. Missing Inputs - Còn thiếu gì
- Không có.
