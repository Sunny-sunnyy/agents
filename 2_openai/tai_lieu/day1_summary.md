# Day 1 - OpenAI Agents SDK Fundamentals

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

---

# 29. Day 1 - Understanding Async Python - The Foundation for OpenAI Agents SDK

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này
- Summary lịch sử: không có
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học tập trung vào lý thuyết nền tảng của Asynchronous Python để chuẩn bị cho việc sử dụng OpenAI Agents SDK.

## 2. Executive Summary - Tóm tắt cốt lõi
- Khóa học giới thiệu tuần 2 tập trung vào OpenAI Agents SDK (tiền thân là dự án Swarm).
- Hiểu biết về Asynchronous Python - lập trình bất đồng bộ (async IO) là điều bắt buộc đối với tất cả các agent frameworks hiện nay.
- Async IO hoạt động như một cơ chế multithreading siêu nhẹ (lightweight) chạy trên một luồng duy nhất (single thread) ở cấp độ mã nguồn Python, thay vì tạo các luồng ở cấp độ hệ điều hành (OS-level threads).
- Cơ chế này cực kỳ tối ưu cho các tác vụ I/O bound (như việc chờ đợi phản hồi từ API của các mô hình ngôn ngữ lớn LLM qua mạng internet).
- Các hàm bất đồng bộ được định nghĩa bằng từ khóa `async def` và được gọi là các coroutine.
- Từ khóa `await` được dùng để lập lịch thực thi một coroutine và tạm dừng thực thi cho đến khi nhận được kết quả.
- Hàm `asyncio.gather` cho phép chạy đồng thời (concurrently) nhiều coroutine để rút ngắn thời gian xử lý tổng thể.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Phân biệt được cơ chế Async IO với Multithreading và Multiprocessing thông thường.
  - Hiểu cách thức hoạt động của Event Loop và khái niệm Coroutine trong Python.
  - Hiểu lý do tại sao lập trình bất đồng bộ lại cực kỳ quan trọng đối với các Multi-agent frameworks.
- Practical goals - mục tiêu thực hành:
  - Khai báo được các coroutine bằng từ khóa `async def`.
  - Thực thi coroutine bằng từ khóa `await` trong môi trường hỗ trợ bất đồng bộ.
  - Sử dụng được `asyncio.gather` để lập lịch chạy song song các tác vụ I/O bound.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao gọi trực tiếp một hàm `async def` lại không thực thi mã nguồn bên trong nó mà chỉ trả về một đối tượng coroutine?
  - Làm thế nào Event Loop có thể xử lý hàng ngàn tác vụ đồng thời trên một luồng duy nhất?

## 4. Previous Context - Liên hệ với bài trước
Đây là bài học mở đầu cho Tuần 2 (Day 1) và là bài học lý thuyết cơ sở đầu tiên về kỹ thuật lập trình bất đồng bộ trong Python phục vụ cho Agentic AI.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Asynchronous Python (async IO)
  - Meaning - nghĩa: Lập trình bất đồng bộ - mô hình lập trình cho phép thực hiện nhiều tác vụ đồng thời trên một luồng duy nhất mà không bị chặn (non-blocking).
  - Why it matters - vì sao quan trọng: Giúp tối ưu hóa tài nguyên phần cứng và giảm thời gian chờ đợi khi hệ thống phải xử lý nhiều yêu cầu mạng (network requests) hoặc gọi API bên ngoài.
  - Relationship - liên hệ với khái niệm khác: Đối lập với lập trình đồng bộ tuần tự (synchronous) và nhẹ hơn rất nhiều so với lập trình đa luồng (multithreading) cấp hệ điều hành.
- Term - thuật ngữ: Coroutine - hàm đồng bộ/bất đồng bộ đặc biệt
  - Meaning - nghĩa: Một đối tượng được tạo ra từ hàm khai báo bằng `async def`, có khả năng tạm dừng thực thi tại các điểm `await` và tiếp tục lại sau đó.
  - Why it matters - vì sao quan trọng: Đây là đơn vị thực thi cơ bản của thư viện `asyncio` trong Python.
  - Relationship - liên hệ với khái niệm khác: Khi gọi một hàm coroutine, Python chỉ trả về coroutine object chứ không tự chạy mã nguồn bên trong; nó cần được đưa vào Event Loop qua lệnh `await` hoặc `asyncio.run()`.
- Term - thuật ngữ: Event Loop - vòng lặp sự kiện
  - Meaning - nghĩa: Trình điều phối chạy ngầm liên tục để quản lý, phân bổ thời gian chạy cho các coroutine đang ở trạng thái sẵn sàng và tạm dừng các tác vụ đang chờ I/O.
  - Why it matters - vì sao quan trọng: Là trái tim của toàn bộ thư viện `asyncio`, giúp hiện thực hóa lập trình bất đồng bộ đơn luồng.
  - Relationship - liên hệ với khái niệm khác: Event Loop quản lý danh sách các coroutines và chuyển đổi ngữ cảnh giữa chúng khi gặp các điểm block I/O.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình điều phối tác vụ của Event Loop trong lập trình bất đồng bộ:
1. Input: Danh sách các coroutines được đăng ký vào Event Loop (ví dụ thông qua lệnh `asyncio.gather`).
2. Processing steps:
   - Event Loop lấy coroutine đầu tiên ra thực thi.
   - Khi gặp từ khóa `await` (đại diện cho một tác vụ chờ I/O như gọi LLM API), Event Loop tạm dừng coroutine này và ghi nhận trạng thái chờ.
   - Event Loop chuyển sang chạy coroutine tiếp theo trong hàng đợi.
   - Khi tác vụ I/O của coroutine trước đó hoàn thành, Event Loop nhận tín hiệu và đưa coroutine đó trở lại hàng đợi thực thi để chạy tiếp từ điểm bị dừng.
3. Output: Kết quả trả về của tất cả các coroutine sau khi hoàn thành.
4. Control flow / data flow: Luồng điều khiển tập trung tại Event Loop đơn luồng.
5. Decision points: Khi một coroutine gặp điểm chặn I/O, nó chủ động nhường quyền điều khiển (yield) lại cho Event Loop để chạy tác vụ khác.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Chạy song song các coroutine bằng `asyncio.gather`
  - Purpose - mục đích: Gom nhiều tác vụ bất đồng bộ độc lập lại và thực thi chúng cùng lúc nhằm tối ưu hóa tổng thời gian chờ đợi.
  - When to use - dùng khi nào: Khi cần thực hiện nhiều cuộc gọi API LLM độc lập (ví dụ gửi câu hỏi cho 3 agent khác nhau cùng lúc).
  - Trade-off - đánh đổi: Phức tạp hơn trong việc xử lý lỗi (nếu một tác vụ lỗi có thể ảnh hưởng đến các tác vụ khác trong nhóm) và kết quả trả về dưới dạng một danh sách có thứ tự tương ứng nhưng thời gian hoàn thành thực tế của từng tác vụ là ngẫu nhiên.
  - Common mistake - lỗi dễ gặp: Quên đặt từ khóa `await` trước `asyncio.gather(...)` dẫn đến việc chương trình đi tiếp mà không đợi kết quả của các tác vụ con.

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này.

## 9. Options / Trade-offs - Bản đồ lựa chọn
So sánh các phương pháp xử lý tác vụ đồng thời trong Python:
- Option: Multiprocessing (Đa tiến trình)
  - Pros: Thực thi song song thực sự trên nhiều nhân CPU, tận dụng tốt phần cứng cho tính toán nặng.
  - Cons: Chi phí tài nguyên cực lớn (mỗi tiến trình có vùng nhớ riêng biệt), giao tiếp giữa các tiến trình phức tạp.
  - When to choose: Tác vụ CPU-bound (tính toán số học, xử lý ảnh, máy học cục bộ).
- Option: Multithreading (Đa luồng cấp OS)
  - Pros: Các luồng dùng chung vùng nhớ, thích hợp cho tác vụ I/O bound ở mức độ trung bình.
  - Cons: Bị giới hạn bởi GIL (Global Interpreter Lock) của Python, tiêu tốn tài nguyên bộ nhớ cho mỗi thread, dễ gặp lỗi tranh chấp dữ liệu (race conditions).
  - When to choose: Khi làm việc với các thư viện đồng bộ cũ không hỗ trợ async.
- Option: Async IO (Bất đồng bộ đơn luồng - Recommended)
  - Pros: Chi phí tài nguyên cực thấp (chạy trên 1 thread), xử lý hàng chục ngàn kết nối cùng lúc rất dễ dàng, loại bỏ rủi ro tranh chấp bộ nhớ.
  - Cons: Không giải quyết được tác vụ CPU-bound; nếu có một tác vụ tính toán nặng không nhường quyền điều khiển, nó sẽ block toàn bộ chương trình.
  - When to choose: Tác vụ I/O bound chiếm phần lớn thời gian (gọi API LLM qua mạng, đọc ghi file/database).

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Coroutine không thực thi và biến lưu kết quả chỉ chứa một đối tượng dạng `<coroutine object...>` kèm theo cảnh báo của Python.
- Root cause: Gọi một hàm bất đồng bộ (`async def`) nhưng quên đặt từ khóa `await` trước tên hàm.
- Symptom: Lập trình viên cố in kết quả nhưng chỉ nhận được thông tin định danh của coroutine object, mã nguồn bên trong hàm không được chạy.
- Fix / prevention: Luôn sử dụng cú pháp `result = await my_async_function()` khi gọi các hàm bất đồng bộ.

## 11. Knowledge Extension - Kiến thức mở rộng
*Dưới đây là ví dụ minh họa cách viết code Async Python với `asyncio.gather` để giải thích cơ chế lý thuyết của bài học (tự bổ sung để tăng tính thực hành):*

```python
import asyncio
import time

async def simulate_api_call(agent_name: str, wait_time: int):
    print(f"Agent {agent_name} bat dau goi API...")
    # asyncio.sleep la phien ban bat dong bo cua time.sleep (I/O bound)
    await asyncio.sleep(wait_time)
    print(f"Agent {agent_name} da nhan duoc phan hoi!")
    return f"Ket qua tu {agent_name}"

async def main():
    start_time = time.time()
    # Chay song song 3 API calls
    results = await asyncio.gather(
        simulate_api_call("A", 2),
        simulate_api_call("B", 3),
        simulate_api_call("C", 1)
    )
    print(f"Tat ca ket qua: {results}")
    print(f"Tong thoi gian cho doi: {time.time() - start_time:.2f} giay")

# Cach khoi chay Event Loop tu file Python thong thuong:
# asyncio.run(main())
```
*Ghi chú: Khi chạy chương trình trên, tổng thời gian thực thi chỉ mất xấp xỉ 3 giây (bằng thời gian chạy của tác vụ lâu nhất) thay vì mất 6 giây (2 + 3 + 1) nếu chạy tuần tự.*

## 12. Study Pack - Gói ôn tập
### Must remember
1. Async IO hoạt động trên một luồng duy nhất thông qua cơ chế vòng lặp sự kiện (Event Loop).
2. Định nghĩa hàm bất đồng bộ bằng `async def` tạo ra một Coroutine.
3. Khi gọi một Coroutine, bắt buộc phải dùng `await` để yêu cầu Event Loop lập lịch chạy và lấy kết quả.
4. Async IO cực kỳ phù hợp cho Multi-agent frameworks vì hầu hết thời gian hoạt động của agent là chờ phản hồi API từ LLM cloud.
5. Dùng `asyncio.gather` để thực thi đồng thời nhiều coroutines độc lập nhằm tăng tốc độ ứng dụng.

### Self-check questions
1. Sự khác biệt cốt lõi giữa Async IO và Multithreading truyền thống là gì?
2. Tại sao câu lệnh `result = call_api()` (trong đó `call_api` khai báo bằng `async def`) lại không thực thi API?
3. Cơ chế hoạt động của Event Loop khi gặp lệnh `await asyncio.sleep(3)` là gì?
4. Khi nào ta nên dùng `asyncio.gather` thay vì gọi các lệnh `await` tuần tự?
5. Nếu ứng dụng có tác vụ xử lý ma trận toán học rất nặng (CPU-bound), ta có nên dùng Async IO để tối ưu không? Giải thích.

### Flashcards
- Q: Coroutine trong Python là gì?
  A: Là một thực thể hàm đặc biệt được tạo bởi `async def`, có khả năng tạm dừng và khôi phục trạng thái thực thi bởi Event Loop.
- Q: Mục đích chính của từ khóa `await` là gì?
  A: Đăng ký coroutine vào Event Loop để thực thi và tạm dừng ngữ cảnh hiện tại cho đến khi coroutine đó hoàn thành.
- Q: Khi chạy 3 tác vụ async tốn lần lượt 1s, 2s, 3s bằng `asyncio.gather`, tổng thời gian chạy là bao lâu?
  A: Khoảng 3s (bằng thời gian của tác vụ dài nhất), vì các tác vụ chạy đồng thời.

### Interview Q&A nếu phù hợp
- Q: Hãy giải thích cách Event Loop xử lý khi một coroutine bị block bởi một tác vụ I/O (ví dụ như đợi API phản hồi).
  A: Khi gặp một lệnh `await` chỉ định một tác vụ I/O, coroutine hiện tại sẽ nhường quyền điều khiển (yield control) lại cho Event Loop. Event Loop sẽ lưu lại trạng thái của coroutine này và kiểm tra xem có tác vụ nào khác trong hàng đợi sẵn sàng chạy hay không để thực thi tiếp. Khi hệ điều hành thông báo tác vụ I/O hoàn thành, Event Loop sẽ đánh dấu coroutine đang chờ là sẵn sàng và xếp lịch cho nó chạy tiếp từ điểm bị dừng.

## 13. Missing Inputs - Còn thiếu gì
- Không có thiếu sót nghiêm trọng nào về mặt lý thuyết Async Python trong phạm vi bài học.

---

# 30. Day 1 - OpenAI Agents SDK Fundamentals - Creating, Tracing, and Running Agents

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này
- Summary lịch sử: không có
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học giới thiệu tổng quan các khái niệm cốt lõi của OpenAI Agents SDK.

## 2. Executive Summary - Tóm tắt cốt lõi
- OpenAI Agents SDK (tên cũ là Swarm) là một framework siêu nhẹ (lightweight), linh hoạt và không áp đặt cấu trúc (non-opinionated).
- SDK tự động xử lý và loại bỏ các đoạn mã boilerplate (mã nguồn lặp đi lặp lại vô ích) liên quan đến việc cấu hình JSON thô khi định nghĩa và gọi tools (Function Calling) của LLM.
- Ba khái niệm chính của SDK là: Agent, Handoff (chuyển giao giữa các agent), và Guardrails (thanh chắn kiểm soát dữ liệu).
- Quy trình 3 bước để khởi chạy một agent bao gồm: 1) Khởi tạo Agent; 2) Sử dụng `with trace` để ghi nhận nhật ký hoạt động; 3) Gọi coroutine `Runner.run` bằng `await`.
- Khóa học sẽ tái sử dụng OpenAI Agents SDK ở Tuần 6 khi xây dựng hệ thống nâng cao tích hợp giao thức MCP (Model Context Protocol).

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu triết lý thiết kế "non-opinionated" của OpenAI Agents SDK và sự khác biệt của nó với các framework khác.
  - Định nghĩa được 3 thành phần cốt lõi của SDK: Agent, Handoff, và Guardrails.
  - Hiểu cách thức hoạt động của lớp Runner trong việc điều phối vòng lặp tương tác LLM và gọi công cụ.
- Practical goals - mục tiêu thực hành:
  - Nắm được cấu trúc cơ bản của một ứng dụng Agent sử dụng SDK.
  - Hiểu cách bao bọc lời gọi agent bằng context manager `trace` để giám sát hệ thống.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao OpenAI Agents SDK lại là lựa chọn yêu thích của giảng viên đối với các dự án tùy biến cao?
  - Sự khác biệt về vai trò giữa Agent và Runner là gì?

## 4. Previous Context - Liên hệ với bài trước
Bài học áp dụng trực tiếp kiến thức Async Python ở Bài 29 để giải thích tại sao phương thức chạy agent (`Runner.run`) lại là một coroutine và bắt buộc phải dùng `await` để thực thi.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Non-opinionated framework - Framework không áp đặt
  - Meaning - nghĩa: Triết lý thiết kế phần mềm cung cấp các khối xây dựng cơ bản tối giản và cho phép lập trình viên tự do quyết định cấu trúc code cũng như luồng điều khiển (control flow).
  - Why it matters - vì sao quan trọng: Giúp nhà phát triển dễ dàng tùy biến hệ thống mà không bị giới hạn bởi các quy tắc cứng nhắc của framework.
  - Relationship - liên hệ với khái niệm khác: Đối lập hoàn toàn với "opinionated frameworks" (như LangChain hay CrewAI) vốn bắt buộc lập trình viên phải tuân theo các lớp trừu tượng (abstractions) có sẵn.
- Term - thuật ngữ: Agent
  - Meaning - nghĩa: Thực thể đại diện cho một vai trò LLM cụ thể trong hệ thống, được định nghĩa bằng tên (name), chỉ dẫn (instructions - system prompt), và mô hình sử dụng (model).
  - Why it matters - vì sao quan trọng: Là hạt nhân thực thi các tác vụ chuyên biệt trong mô hình Multi-agent.
  - Relationship - liên hệ với khái niệm khác: Có thể liên kết với các công cụ (tools) và thực hiện chuyển giao quyền kiểm soát (handoff) cho các agent khác.
- Term - thuật ngữ: Handoff - Chuyển giao công việc
  - Meaning - nghĩa: Cơ chế cho phép một Agent chuyển giao bối cảnh hội thoại và quyền điều khiển cuộc trò chuyện sang cho một Agent khác.
  - Why it matters - vì sao quan trọng: Giúp xây dựng các hệ thống đa tác nhân cộng tác mượt mà, phân chia công việc theo đúng chuyên môn.
  - Relationship - liên hệ với khái niệm khác: Được kích hoạt thông qua việc một Agent trả về thực thể của một Agent khác trong quá trình gọi công cụ (tool call).
- Term - thuật ngữ: Guardrails - Thanh chắn an toàn
  - Meaning - nghĩa: Các lớp kiểm duyệt dữ liệu đầu vào (input guardrails) hoặc đầu ra (output guardrails) để kiểm soát hành vi của agent.
  - Why it matters - vì sao quan trọng: Đảm bảo agent không đưa ra các câu trả lời sai lệch, lạc đề hoặc vi phạm các quy tắc an toàn hệ thống.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình 3 bước để khởi chạy một agent trong OpenAI Agents SDK:
1. Input: Định nghĩa vai trò (instructions), tên agent, và mô hình LLM.
2. Processing steps:
   - Bước 1: Khởi tạo thực thể của lớp `Agent` với cấu hình mong muốn.
   - Bước 2: Thiết lập context manager `with trace(...)` để bắt đầu ghi nhật ký phiên chạy (khuyến nghị để debug).
   - Bước 3: Gọi bất đồng bộ `Runner.run(agent, user_prompt)` để khởi động vòng lặp xử lý.
3. Output: Đối tượng kết quả chứa đầu ra cuối cùng của cuộc hội thoại (`final_output`) và lịch sử tin nhắn.
4. Control flow / data flow: Runner quản lý luồng gửi tin nhắn lên LLM -> LLM phản hồi (có thể yêu cầu gọi tool) -> Runner thực thi tool -> Runner gửi lại kết quả cho LLM -> LLM đưa ra câu trả lời cuối cùng.
5. Decision points: Runner tự động điều phối vòng lặp tool calling cho đến khi LLM quyết định không cần gọi thêm công cụ nào nữa.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Sử dụng Tracing (`with trace`)
  - Purpose - mục đích: Ghi lại toàn bộ chuỗi sự kiện, các cuộc gọi LLM và việc thực thi công cụ trong suốt phiên chạy của agent.
  - When to use - dùng khi nào: Luôn sử dụng trong quá trình phát triển để giám sát và gỡ lỗi trên giao diện trực quan của OpenAI Platform.
  - Trade-off - đánh đổi: Cần kết nối mạng và tài khoản OpenAI để đẩy dữ liệu trace lên Cloud.
  - Common mistake - lỗi dễ gặp: Quên không thiết lập đúng API key dẫn đến trace không được đồng bộ hóa.

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này.

## 9. Options / Trade-offs - Bản đồ lựa chọn
So sánh triết lý xây dựng framework cho AI Agent:
- Option: Opinionated Frameworks (ví dụ: LangChain, CrewAI)
  - Pros: Cung cấp sẵn các mẫu thiết kế (templates) cho các bài toán phổ biến, tích hợp nhiều tính năng nâng cao ăn liền.
  - Cons: Rất cồng kềnh, khó tùy biến sâu khi gặp bài toán đặc thù, khó kiểm soát luồng chạy bên dưới (under the hood).
  - When to choose: Khi cần xây dựng nhanh các ứng dụng chuẩn hóa theo khuôn mẫu có sẵn của framework.
- Option: Non-opinionated Frameworks (OpenAI Agents SDK / Swarm - Recommended)
  - Pros: Siêu nhẹ, dễ học, cho phép lập trình viên kiểm soát hoàn toàn luồng điều khiển (control flow), dễ dàng debug.
  - Cons: Phải tự xây dựng các thành phần quản lý trạng thái phức tạp nếu hệ thống phình to.
  - When to choose: Khi dự án yêu cầu tính tùy biến cao, hiệu năng tối ưu và không muốn bị phụ thuộc vào các lớp trừu tượng phức tạp.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Runner không thể kết nối API hoặc tải sai các biến cấu hình cũ.
- Root cause: Quên không bật tham số `override=True` khi nạp file môi trường bằng `load_dotenv()`.
- Symptom: Lỗi xác thực API Key hoặc các cấu hình môi trường mới cập nhật không được áp dụng.
- Fix / prevention: Luôn gọi `load_dotenv(override=True)` ngay tại các dòng đầu tiên của chương trình.

## 11. Knowledge Extension - Kiến thức mở rộng
- *Swarm vs OpenAI Agents SDK*: OpenAI ban đầu phát hành mã nguồn mở của dự án dưới tên "Swarm" như một dự án thử nghiệm giáo dục (experimental) nhằm trình diễn mẫu thiết kế đa tác nhân đơn giản nhất. Sau đó, cộng đồng đón nhận nồng nhiệt và OpenAI đã nâng cấp nó thành *OpenAI Agents SDK* chính thức, bổ sung các lớp giám sát (Tracing) và tích hợp sâu với hạ tầng quản lý của hãng.

## 12. Study Pack - Gói ôn tập
### Must remember
1. OpenAI Agents SDK là framework tối giản (non-opinionated) và rất linh hoạt.
2. SDK tự động xử lý toàn bộ các cấu trúc JSON phức tạp của Function Calling.
3. Ba thực thể cốt lõi cần nhớ: Agent, Handoff, và Guardrails.
4. Tracing giúp ghi lại toàn bộ lịch sử chạy của agent và hiển thị trực quan trên OpenAI Platform.
5. Việc chạy agent (`Runner.run`) luôn yêu cầu từ khóa `await` vì nó là một tác vụ bất đồng bộ.

### Self-check questions
1. Tại sao nói OpenAI Agents SDK giúp loại bỏ mã nguồn boilerplate cho lập trình viên?
2. Hãy nêu sự khác biệt giữa triết lý thiết kế của Swarm/OpenAI Agents SDK và LangChain.
3. Handoff hoạt động như thế nào trong mô hình Multi-agent?
4. Tracing giải quyết bài toán gì khi phát triển ứng dụng AI Agent?
5. Runner đóng vai trò gì trong vòng lặp thực thi của SDK?

### Flashcards
- Q: 3 tham số cơ bản nhất để khởi tạo một Agent là gì?
  A: `name` (tên agent), `instructions` (chỉ dẫn/system prompt) và `model` (mô hình LLM sử dụng).
- Q: Handoff trong OpenAI Agents SDK được thực hiện như thế nào?
  A: Bằng cách trả về thực thể của một `Agent` khác từ bên trong một hàm công cụ (tool function).

## 13. Missing Inputs - Còn thiếu gì
- Không có thiếu sót nghiêm trọng nào trong phần lý thuyết giới thiệu SDK.

---

# 31. Day 1 - Introduction to Agent, Runner, and Trace Classes in OpenAI Agents SDK

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: đã dùng ([1_lab1.ipynb](file:///G:/Agent2026Win/agents/2_openai/1_lab1.ipynb))
- Summary lịch sử: không có
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học thực hành trực tiếp các bước viết code Python để chạy Agent cơ bản.

## 2. Executive Summary - Tóm tắt cốt lõi
- Bài học thực hành đầu tiên sử dụng IDE (Cursor) để viết code khởi tạo và thực thi Agent.
- Hướng dẫn chi tiết cách import các lớp `Agent`, `Runner` và `trace` từ thư viện `agents` của OpenAI.
- Khởi tạo thực thể `Agent` với vai trò kể chuyện cười (Jokester) sử dụng mô hình mặc định `gpt-4o-mini`.
- Trực quan hóa lỗi phổ biến: gọi `Runner.run` mà quên từ khóa `await` dẫn đến việc chương trình chỉ trả về một coroutine object chưa thực thi.
- Bao bọc lời gọi chạy agent bằng context manager `trace` để ghi nhận hoạt động.
- Trình bày cách truy cập giao diện OpenAI Platform Traces (`platform.openai.com/traces`) để theo dõi chi tiết cấu trúc Input/Output của cuộc hội thoại.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách thức hoạt động thực tế của lớp `Agent`, `Runner` và context manager `trace`.
  - Hiểu cách thức Jupyter Notebook xử lý các câu lệnh bất đồng bộ cấp cao (top-level await).
- Practical goals - mục tiêu thực hành:
  - Viết code Python khởi tạo thành công một Agent với chỉ dẫn hệ thống cụ thể.
  - Sử dụng đúng cú pháp `await Runner.run(...)` để chạy agent.
  - Cấu hình và xem thành công vết thực thi (trace) trên giao diện web của OpenAI.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao thuộc tính `final_output` của đối tượng kết quả lại quan trọng?
  - Cách thức đọc hiểu một sơ đồ trace trên OpenAI Platform.

## 4. Previous Context - Liên hệ với bài trước
Bài học hiện thực hóa trực tiếp quy trình 3 bước lý thuyết đã học ở Bài 30 thành các dòng code Python chạy được trong file notebook `1_lab1.ipynb`.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: `agents` Package
  - Meaning - nghĩa: Thư viện chính thức của OpenAI Agents SDK trên Python (cài đặt qua pip/uv).
  - Why it matters - vì sao quan trọng: Cung cấp tất cả các lớp và phương thức cần thiết để làm việc với Agent của OpenAI.
  - Relationship - liên hệ với khái niệm khác: Cần phân biệt tên package này với thư mục chứa code `agents` nội bộ trong dự án của người dùng để tránh xung đột import.
- Term - thuật ngữ: Top-level Await
  - Meaning - nghĩa: Khả năng cho phép sử dụng từ khóa `await` trực tiếp ở cấp cao nhất của mã nguồn mà không cần phải bọc nó bên trong một hàm khai báo `async def`.
  - Why it matters - vì sao quan trọng: Giúp viết code thử nghiệm nhanh, trực quan trong môi trường tương tác như Jupyter Notebook.
  - Relationship - liên hệ với khái niệm khác: Chỉ hoạt động trong Jupyter/IPython; nếu chạy file script `.py` thông thường, Python sẽ báo lỗi cú pháp (SyntaxError).
- Term - thuật ngữ: `final_output`
  - Meaning - nghĩa: Thuộc tính của đối tượng kết quả trả về từ `Runner.run` chứa nội dung phản hồi dạng chuỗi ký tự (string) cuối cùng của Agent.
  - Why it matters - vì sao quan trọng: Là dữ liệu đầu ra chính mà lập trình viên cần trích xuất để hiển thị cho người dùng cuối.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Luồng thực thi mã nguồn thực tế của chương trình:
1. Input: User prompt `"Tell a joke about Autonomous AI Agents"`.
2. Processing steps:
   - Load các biến môi trường từ `.env` bằng `load_dotenv(override=True)`.
   - Khởi tạo thực thể agent Jokester với cấu hình: `Agent(name="Jokester", instructions="You are a joke teller", model="gpt-4o-mini")`.
   - Mở context manager `with trace("Telling a joke"):`.
   - Chạy bất đồng bộ và đợi kết quả: `result = await Runner.run(agent, user_prompt)`.
   - Trích xuất và in kết quả ra terminal: `print(result.final_output)`.
3. Output: Đoạn văn kể chuyện cười của agent Jokester.
4. Control flow / data flow: Chạy bất đồng bộ đơn luồng được điều phối trực tiếp bởi kernel của Jupyter Notebook.
5. Decision points: Không có nhánh rẽ logic trong ví dụ thực hành cơ bản này.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Bọc cuộc gọi trong `with trace(...)`
  - Purpose - mục đích: Nhóm các cuộc gọi LLM và các bước trung gian của Agent lại dưới một nhãn duy nhất phục vụ giám sát.
  - When to use - dùng khi nào: Khi thực hiện các tác vụ chạy Agent từ đơn giản đến phức tạp trong môi trường phát triển (development) lẫn vận hành (production).
  - Trade-off - đánh đổi: Gửi dữ liệu telemetry lên máy chủ của OpenAI, có thể tăng nhẹ độ trễ mạng.
  - Common mistake: Không bọc lệnh `await Runner.run(...)` vào bên trong block thụt lề của `with trace` dẫn đến việc trace không ghi nhận cuộc gọi đó.

## 8. Code Walkthrough - Phân tích code nếu có
### File: [1_lab1.ipynb](file:///G:/Agent2026Win/agents/2_openai/1_lab1.ipynb)
- Purpose - mục đích: Khởi tạo và thực thi Agent kể chuyện cười sử dụng OpenAI Agents SDK và ghi nhận Trace.
- Key logic - logic chính:
  - Import các thư viện cần thiết.
  - Nạp cấu hình từ file `.env` chứa API Key của OpenAI.
  - Tạo đối tượng `Agent` với hướng dẫn hệ thống là kể chuyện cười và mô hình `gpt-4o-mini`.
  - Thực thi tác vụ bất đồng bộ trong context manager `trace`.
- Important lines / functions:
  - Dòng 41: `from agents import Agent, Runner, trace`
    - Ý nghĩa: Nạp các lớp chính của SDK để làm việc.
  - Dòng 53: `load_dotenv(override=True)`
    - Ý nghĩa: Nạp API key từ file `.env` cục bộ, ghi đè lên các cấu hình cũ của hệ thống.
  - Dòng 65: `agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-4o-mini")`
    - Ý nghĩa: Định nghĩa Agent kể chuyện cười sử dụng mô hình gpt-4o-mini.
  - Dòng 76-78:
    ```python
    with trace("Telling a joke"):
        result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
        print(result.final_output)
    ```
    - Ý nghĩa: Khởi chạy bất đồng bộ trong khối giám sát Trace và in kết quả cuối cùng ra màn hình.
- Vietnamese inline notes - ghi chú tiếng Việt giải thích snippet:
  - `with trace("Telling a joke")`: Mở một phiên giám sát có tên là "Telling a joke" trên hệ thống OpenAI.
  - `await Runner.run(...)`: Chờ đợi phản hồi từ agent bất đồng bộ, nhường luồng chạy cho các tác vụ khác nếu có.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Không áp dụng (Bài thực hành cơ bản không có các phương án kỹ thuật thay thế phức tạp).

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Không thể thực thi file Python thông thường dưới dạng `.py` khi viết lệnh `await Runner.run(...)` ở ngoài cùng mà không bọc trong hàm async.
- Root cause: Python chuẩn không hỗ trợ top-level await ngoài môi trường Jupyter Notebook.
- Symptom: Lỗi cú pháp `SyntaxError: 'await' outside function`.
- Fix / prevention: Bọc toàn bộ logic chạy vào trong một hàm `async def main():` và thực thi thông qua `asyncio.run(main())`.

## 11. Knowledge Extension - Kiến thức mở rộng
- *Cách xem Trace chi tiết*:
  - Lập trình viên truy cập vào `platform.openai.com/traces`.
  - Trên bảng điều khiển sẽ hiển thị danh sách các trace đã ghi nhận.
  - Click vào trace "Telling a joke", giao diện sẽ phân tích chi tiết:
    - Nhãn hệ thống (System instructions): "You are a joke teller".
    - Tin nhắn người dùng (User message): "Tell a joke about Autonomous AI Agents".
    - Phản hồi của trợ lý (Assistant response): Chứa câu chuyện cười hoàn chỉnh.
    - Thời gian thực thi và lượng token tiêu thụ.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Thư viện để import SDK là `agents`.
2. Khởi tạo `Agent` cần khai báo tên, chỉ dẫn (instructions), và mô hình.
3. `Runner.run` yêu cầu truyền vào thực thể agent và chuỗi prompt của người dùng.
4. Phải viết `await` trước `Runner.run` để thực thi coroutine này.
5. In ra thuộc tính `final_output` của kết quả để lấy nội dung văn bản phản hồi.

### Self-check questions
1. Làm thế nào để giải quyết lỗi "never awaited" khi làm việc với Runner?
2. Hãy nêu cách import đúng các thành phần cốt lõi của OpenAI Agents SDK.
3. Làm cách nào để chạy được lệnh `await` ngoài môi trường Jupyter Notebook?
4. Trình bày các bước để truy cập giao diện xem Trace của OpenAI.
5. Thuộc tính nào của đối tượng kết quả trả về từ Runner chứa nội dung phản hồi cuối cùng?

### Flashcards
- Q: Lớp nào chịu trách nhiệm thực thi các câu lệnh gửi đến Agent?
  A: Lớp `Runner` (qua phương thức static `Runner.run`).
- Q: Làm thế nào để nạp API key từ file `.env` an toàn trong code?
  A: Sử dụng thư viện `dotenv` với hàm `load_dotenv(override=True)`.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 32. Day 1 - Vibe Coding - 5 Essential Tips for Efficient Code Generation with LLMs

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này
- Summary lịch sử: không có
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học bàn về phương pháp luận lập trình hiệu quả với LLM (Vibe Coding).

## 2. Executive Summary - Tóm tắt cốt lõi
- Vibe Coding là thuật ngữ được Andrej Karpathy (cựu Giám đốc AI Tesla) phổ biến, mô tả phong cách lập trình ad-hoc, tương tác nhanh, nơi lập trình viên đóng vai trò định hướng và để LLM tự sinh code.
- Vibe Coding rất hữu ích khi tiếp cận các công nghệ hoặc framework mới nhưng dễ dẫn đến bẫy "mã nguồn rác/lỗi" (code slop) nếu thiếu kỷ luật.
- Trình bày 5 lời khuyên sinh tồn (survival tips) khi Vibe Coding:
  1. **Good vibes**: Viết prompt chất lượng, yêu cầu code ngắn gọn, chỉ rõ ngày hiện tại để tránh thư viện cũ.
  2. **Vibe but verify**: Hỏi nhiều mô hình khác nhau (như ChatGPT, Claude) để đối chiếu câu trả lời.
  3. **Step up the vibe**: Chia nhỏ bài toán thành các phần độc lập có thể kiểm thử (viết khoảng 10 dòng code mỗi lượt).
  4. **Vibe and validate**: Sử dụng mô hình này để kiểm tra và tối ưu mã nguồn của mô hình khác (mô phỏng mô hình Evaluator-Optimizer).
  5. **Vibe with variety**: Yêu cầu mô hình đưa ra 3 giải pháp khác nhau kèm giải thích để lựa chọn hướng tối ưu nhất.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu rõ khái niệm, nguồn gốc và ý nghĩa của phong cách lập trình Vibe Coding.
  - Nhận diện các rủi ro của việc lạm dụng LLM tạo code quy mô lớn mà không kiểm soát (code slop).
  - Hiểu cách áp dụng mẫu thiết kế Evaluator-Optimizer một cách thủ công trong quy trình làm việc cá nhân.
- Practical goals - mục tiêu thực hành:
  - Áp dụng thành thạo 5 tips Vibe Coding vào việc sinh code hàng ngày.
  - Biết cách viết prompt tối ưu và phân rã bài toán lớn thành các phần nhỏ trước khi yêu cầu LLM viết code.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao không nên yêu cầu LLM sinh một khối lượng code lớn (ví dụ 200 dòng) cùng một lúc?
  - Làm thế nào để tận dụng thế mạnh của nhiều mô hình ngôn ngữ lớn khác nhau khi lập trình?

## 4. Previous Context - Liên hệ với bài trước
Nêu bật phong cách và tư duy lập trình thực hành mà học viên nên áp dụng khi làm việc với OpenAI Agents SDK ở các bài trước và các dự án thực tế sắp tới.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: Vibe Coding
  - Meaning - nghĩa: Phong cách lập trình trong đó con người đóng vai trò kiến trúc sư, thiết kế luồng chạy và đưa ra định hướng, còn LLM chịu trách nhiệm viết mã nguồn trực tiếp, tiến hành thử nghiệm và sửa đổi nhanh chóng.
  - Why it matters - vì sao quan trọng: Tăng đáng kể hiệu suất lập trình và giúp tiếp cận nhanh chóng với các công nghệ mới.
  - Relationship - liên hệ với khái niệm khác: Yêu cầu sự kết hợp giữa tư duy thiết kế hệ thống và khả năng đánh giá mã nguồn để tránh tạo ra code rác.
- Term - thuật ngữ: Divide and Conquer - Chia để trị
  - Meaning - nghĩa: Nguyên tắc phân chia một bài toán lớn thành các tác vụ con độc lập, giải quyết từng tác vụ con rồi tích hợp lại thành giải pháp tổng thể.
  - Why it matters - vì sao quan trọng: Giúp kiểm soát chất lượng code của LLM và dễ dàng khoanh vùng gỡ lỗi khi có sự cố.
  - Relationship - liên hệ với khái niệm khác: Trong Vibe Coding, điều này tương đương với việc viết và kiểm thử độc lập khoảng 10 dòng code mỗi lượt.
- Term - thuật ngữ: Evaluator-Optimizer Pattern - Mẫu thiết kế Đánh giá - Tối ưu
  - Meaning - nghĩa: Một mẫu thiết kế kiến trúc AI Agent trong đó một tác nhân chịu trách nhiệm tạo ra kết quả (Optimizer) và tác nhân còn lại thực hiện kiểm tra, đánh giá chất lượng (Evaluator) để phản hồi lại cho tác nhân thứ nhất tối ưu hóa.
  - Why it matters - vì sao quan trọng: Giúp nâng cao chất lượng và độ tin cậy của mã nguồn tự động sinh ra.
  - Relationship - liên hệ với khái niệm khác: Có thể áp dụng thủ công bằng cách đưa kết quả code của ChatGPT cho Claude đánh giá và ngược lại.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Quy trình phân rã bài toán và sinh code an toàn trong Vibe Coding:
1. Input: Yêu cầu tính năng lớn từ lập trình viên.
2. Processing steps:
   - Bước 1: Yêu cầu LLM phân tích yêu cầu lớn thành 4-5 bước thực hiện nhỏ, tự chứa và có thể kiểm thử độc lập (chưa yêu cầu viết code ngay).
   - Bước 2: Với từng bước nhỏ, yêu cầu LLM sinh khoảng 10 dòng code kèm theo đoạn mã hoặc phương án kiểm thử tương ứng.
   - Bước 3: Thực thi và xác minh chạy thành công từng mảnh code nhỏ.
   - Bước 4: Tích hợp các mảnh code đã được xác minh thành chương trình hoàn chỉnh.
3. Output: Chương trình hoàn chỉnh hoạt động chính xác và không có bug tiềm ẩn.
4. Control flow / data flow: Quy trình tuần tự do lập trình viên điều phối thủ công qua giao diện chat với LLM.
5. Decision points: Lập trình viên quyết định chuyển sang bước tiếp theo sau khi đã kiểm thử chạy tốt bước hiện tại.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Xác minh chéo đa mô hình (Cross-model validation)
  - Purpose - mục đích: Đối chiếu câu trả lời của các mô hình khác nhau để lọc bỏ thông tin nhiễu, lỗi thời và tìm ra giải pháp tối ưu nhất.
  - When to use - dùng khi nào: Khi gặp lỗi phức tạp hoặc cần tối ưu hóa hiệu năng của một đoạn code quan trọng.
  - Trade-off - đánh đổi: Mất nhiều thời gian đặt câu hỏi và quản lý các tab chat khác nhau.
  - Common mistake - lỗi dễ gặp: Chỉ tin tưởng vào một mô hình duy nhất và liên tục sa vào vòng lặp sửa lỗi của mô hình đó.

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này.

## 9. Options / Trade-offs - Bản đồ lựa chọn
So sánh các chiến lược yêu cầu LLM sinh code:
- Option: Sinh code hàng loạt (Large-scale generation)
  - Pros: Nhanh chóng tạo ra khung chương trình lớn, tiết kiệm số lượng prompt ban đầu.
  - Cons: Dễ sinh ra mã nguồn lỗi thời, chứa nhiều bug logic ẩn rất khó tìm và sửa, code thường quá verbose.
  - When to choose: Chỉ dùng khi tạo các template khung dự án rất cơ bản mà lập trình viên đã cực kỳ quen thuộc.
- Option: Sinh code từng bước nhỏ (Incremental generation - Recommended)
  - Pros: Đảm bảo kiểm soát chất lượng từng dòng code, dễ dàng debug, cấu trúc mã nguồn clean và tối giản.
  - Cons: Yêu cầu lập trình viên phải có kỷ luật và tốn nhiều lượt chat hơn.
  - When to choose: Khuyên dùng cho mọi tác vụ lập trình từ trung bình đến phức tạp.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Chương trình bị lỗi khi chạy nhưng lập trình viên hoàn toàn bất lực không thể debug và sa vào vòng lặp sửa lỗi vô hạn của LLM.
- Root cause: Copy-paste một khối lượng lớn code do LLM sinh ra mà không hiểu rõ logic hoạt động của từng dòng.
- Symptom: Xuất hiện nhiều lỗi cú pháp, thư viện không tương thích hoặc lỗi logic nghiệp vụ chồng chéo.
- Fix / prevention: Tuân thủ nghiêm ngặt nguyên tắc chỉ sinh khoảng 10 dòng code mỗi lượt, kiểm thử chạy được mới đi tiếp, và luôn yêu cầu LLM giải thích cặn kẽ những đoạn code chưa hiểu rõ.

## 11. Knowledge Extension - Kiến thức mở rộng
- *Nguồn gốc thuật ngữ Vibe Coding*: Thuật ngữ này bùng nổ trên mạng xã hội X (Twitter) sau một bài đăng vào cuối năm 2024 của Andrej Karpathy. Ông chia sẻ cảm giác phấn khích khi phát triển các dự án nhỏ mà hầu như không cần tự gõ phím viết code, thay vào đó chỉ tập trung vào việc suy nghĩ kiến trúc và giao tiếp định hướng cho AI thực thi.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Vibe Coding là phương pháp lập trình tương tác cao với LLM nhưng yêu cầu lập trình viên phải giữ quyền kiểm soát.
2. Luôn yêu cầu LLM viết code conciseness (ngắn gọn) và chỉ rõ ngày tháng hiện tại để tránh API cũ.
3. Chia nhỏ chương trình thành các phần khoảng 10 dòng code để viết và kiểm thử độc lập.
4. Sử dụng mô hình thứ hai để đánh giá và tối ưu hóa code của mô hình thứ nhất.
5. Đừng bao giờ copy code mà bản thân không hiểu cơ chế hoạt động của nó.

### Self-check questions
1. Vibe Coding là gì và ai là người phổ biến khái niệm này?
2. Tại sao việc đưa ngày hiện tại vào prompt lại giúp tránh được lỗi gọi API cũ?
3. Mô tả quy trình chia để trị áp dụng trong việc sinh code với LLM.
4. Làm thế nào để áp dụng thủ công mẫu thiết kế Evaluator-Optimizer khi lập trình?
5. Bạn nên làm gì để thoát khỏi vòng lặp sửa lỗi liên tục của một LLM?

### Flashcards
- Q: 5 tips cốt lõi của Vibe Coding là gì?
  A: 1) Good vibes, 2) Vibe but verify, 3) Step up the vibe, 4) Vibe and validate, 5) Vibe with variety.
- Q: Kích thước đoạn code lý tưởng được khuyên sinh ra mỗi lượt là bao nhiêu?
  A: Khoảng 10 dòng code để dễ dàng kiểm thử và khoanh vùng lỗi.

## 13. Missing Inputs - Còn thiếu gì
- Không có.

---

# 33. Day 1 - OpenAI Agents SDK - Understanding Core Concepts for AI Development

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng
- Slide: không có
- Code: Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này
- Summary lịch sử: không có
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Không có mâu thuẫn. Bài học là phần kết thúc ngắn gọn của Day 1.

## 2. Executive Summary - Tóm tắt cốt lõi
- Bài học chốt lại toàn bộ chặng đường học tập của Day 1 về nền tảng của OpenAI Agents SDK.
- Học viên đã đi qua các chủ đề: lý thuyết lập trình bất đồng bộ Async Python, các lớp cơ bản của SDK (Agent, Runner, Trace) và phương pháp luận Vibe Coding.
- Bài học định hướng lộ trình sang Day 2 với dự án thực tế đầu tiên: Xây dựng một SDR (Sales Development Representative) Agent tự động hóa quy trình bán hàng.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Củng cố lại các khối kiến thức cốt lõi đã học trong suốt Day 1.
  - Nắm được lộ trình học tập và mục tiêu thực hành của ngày tiếp theo.
- Practical goals - mục tiêu thực hành:
  - Chuẩn bị đầy đủ môi trường phát triển (API keys, thư viện) để sẵn sàng xây dựng SDR Agent ở Day 2.
- What learner should be able to explain - người học cần giải thích được:
  - Mối liên kết giữa các bài học Day 1 (Async, SDK basics, Vibe Coding) phục vụ như thế nào cho dự án Day 2.

## 4. Previous Context - Liên hệ với bài trước
Hệ thống hóa toàn bộ nội dung của các bài học 29, 30, 31, 32 và chuẩn bị bối cảnh thực hành cho các bài học của Day 2.

## 5. Core Theory - Lý thuyết cốt lõi
- Term - thuật ngữ: SDR - Sales Development Representative - Đại lý phát triển bán hàng
  - Meaning - nghĩa: Vai trò trong bộ phận kinh doanh chịu trách nhiệm tìm kiếm, tiếp cận, tương tác ban đầu và lọc khách hàng tiềm năng.
  - Why it matters - vì sao quan trọng: Đây là một trong những vị trí công việc được tự động hóa bằng AI Agent nhiều nhất trong doanh nghiệp thực tế.
  - Relationship - liên hệ với khái niệm khác: SDR Agent sẽ được xây dựng ở Day 2 sử dụng các kỹ thuật chuyển giao công việc (handoff) và tích hợp công cụ (tools) của OpenAI Agents SDK.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Không có pipeline rõ ràng trong tài liệu nguồn. Nội dung bài học chỉ mang tính chất tổng kết ngày học và chuyển giao lộ trình.

## 7. Techniques - Kỹ thuật sử dụng
- Technique - kỹ thuật: Tổng hợp và hệ thống hóa kiến thức định kỳ
  - Purpose - mục đích: Giúp ghi nhớ sâu các khái niệm nền tảng trước khi bước vào xây dựng các dự án lớn hơn để tránh bị ngợp.
  - When to use - dùng khi nào: Cuối mỗi ngày học hoặc trước khi bắt đầu một chương thực hành lớn.
  - Trade-off - đánh đổi: Mất thêm thời gian ôn tập nhưng giúp giảm thiểu lỗi cú pháp và lỗi logic cơ bản khi lập trình thực tế.
  - Common mistake - lỗi dễ gặp: Bỏ qua bước hệ thống hóa kiến thức cơ bản, nhảy thẳng vào viết code dự án lớn dẫn đến việc liên tục bị lỗi "never awaited" hoặc cấu hình sai biến môi trường mà không tự khắc phục được.

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Không áp dụng.

## 10. Pitfalls - Lỗi / bẫy thường gặp
Không áp dụng.

## 11. Knowledge Extension - Kiến thức mở rộng
- *Định hướng Day 2*: Trong dự án xây dựng SDR Agent ở ngày tiếp theo, học viên sẽ được tiếp cận cách tích hợp các API dịch vụ bên ngoài (như SendGrid để tự động gửi email) làm công cụ cho Agent, đồng thời áp dụng mô hình cộng tác đa tác nhân (Multi-agent collaboration) để xử lý luồng công việc bán hàng khép kín.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Day 1 đã xây dựng thành công nền móng vững chắc về lập trình bất đồng bộ Async Python.
2. Đã nắm vững cách import và sử dụng các lớp `Agent`, `Runner` và `trace` của OpenAI Agents SDK.
3. Vibe Coding là công cụ mạnh mẽ nhưng cần áp dụng có kỷ luật (sinh code từng mảnh nhỏ 10 dòng, kiểm thử liên tục).
4. Đọc trace trên giao diện OpenAI Platform là kỹ năng quan trọng để gỡ lỗi hành vi agent.
5. Đích đến tiếp theo ở Day 2 là dự án SDR Agent.

### Self-check questions
1. Bạn đã thực sự hiểu tại sao cần viết `await Runner.run(...)` chưa?
2. Hãy nêu cách thức truy cập giao diện xem Trace của OpenAI.
3. Kể tên 5 tips Vibe Coding đã học.
4. SDR Agent ở Day 2 sẽ giải quyết bài toán nghiệp vụ gì?

### Flashcards
- Q: Tác vụ thực hành chính của Day 2 là gì?
  A: Xây dựng một SDR (Sales Development Representative) Agent tự động hóa quy trình bán hàng.

## 13. Missing Inputs - Còn thiếu gì
- Không có.
