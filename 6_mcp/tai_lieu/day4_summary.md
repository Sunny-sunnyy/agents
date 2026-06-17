# 123. Day 4 - What’s Next - Launching Our Agent Trading Floor

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `123. Day 4 - What’s Next - Launching Our Agent Trading Floor.txt`
- Slide: không có
- Code: đã dùng — `4_lab4.ipynb` phần mở đầu và `push_server.py`
- Summary lịch sử: đã dùng — `day1_summary.md`, `day2_summary.md`, `day3_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript và notebook khớp nhau ở framing của capstone project. `push_server.py` được transcript gọi đích danh nên được dùng như code liên quan trực tiếp cho lesson này.

## 2. Executive Summary - Tóm tắt cốt lõi
- Day 4 mở đầu capstone project `Autonomous Traders` như một bài toán thương mại thực tế hơn các ví dụ code-centric trước đó.
- Mục tiêu là xây hệ thống trading simulation - mô phỏng giao dịch cổ phiếu, nơi agent có thể tự nghiên cứu thị trường và tự ra quyết định giao dịch trong tài khoản synthetic account - tài khoản mô phỏng.
- Instructor nhấn mạnh đây là project nhiều agent, nhiều MCP servers, có autonomy - tính tự chủ, nhưng tuyệt đối không dùng cho giao dịch thật.
- Hệ thống Day 4 dự kiến dùng nhiều năng lực đã học ở Day 1-3: accounts MCP server, fetch, memory, Brave Search, và market data từ Polygon.
- Research-first engineering - kỹ thuật bắt đầu bằng thử nghiệm được nhấn mạnh lại: phải dựng trong notebook/lab trước, rồi mới đóng gói thành module Python.
- `push_server.py` là ví dụ MCP server rất nhỏ, chỉ có một tool, được thêm vào để hệ thống gửi push notification - thông báo đẩy khi trader hoàn thành hành động.
- Lesson này chủ yếu đặt bối cảnh kiến trúc, mục tiêu dự án, và nguyên tắc làm việc cho toàn bộ Day 4.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu capstone trading floor nối lại toàn bộ kiến thức MCP của 3 ngày trước như thế nào.
  - Hiểu vì sao instructor chọn bài toán trading như một commercial problem - bài toán thương mại thay vì demo kỹ thuật thuần túy.
  - Hiểu vai trò của autonomy - tính tự chủ, researcher agent, trader agent, và nhiều MCP servers trong cùng một hệ thống.
- Practical goals - mục tiêu thực hành:
  - Biết các năng lực và MCP servers nào sẽ được dùng trong lab Day 4.
  - Biết vì sao nên thử nghiệm trong notebook trước khi chuyển sang module Python.
  - Nhìn được ví dụ nhỏ của một MCP server tự viết là `push_server.py`.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao capstone này là một bước tiến từ các demo MCP rời rạc sang một hệ thống agentic có mục tiêu kinh doanh rõ ràng.
  - Vì sao push notification được thêm vào như một cảm giác “autonomous” cho hệ thống.
  - Vì sao “start in the lab first” là nguyên tắc quan trọng khi xây agent systems - hệ thống agent.

## 4. Previous Context - Liên hệ với bài trước
- Day 1 đặt nền tảng MCP là protocol - giao thức và cách gắn nhiều MCP servers vào agent.
- Day 2 xây `accounts_server.py` và `accounts_client.py`, nên đến Day 4 trader có thể đọc account và strategy qua resources thay vì hardcode.
- Day 3 thêm 2 mảnh ghép quan trọng cho capstone: memory MCP server và market data qua Polygon hoặc custom market server.
- Lesson 123 là điểm hội tụ: accounts từ Day 2, memory/search/market từ Day 3, và multi-server orchestration - điều phối nhiều server từ Day 1.

## 5. Core Theory - Lý thuyết cốt lõi

### Capstone project - dự án tổng hợp cuối chặng
- Term - thuật ngữ: Capstone project - dự án tổng hợp cuối chặng
- Meaning - nghĩa: Một dự án gom nhiều kỹ thuật đã học thành một hệ thống đủ lớn để phản ánh cách áp dụng ngoài đời thật.
- Why it matters - vì sao quan trọng: Nó buộc người học chuyển từ “biết từng công cụ” sang “ghép các capability thành solution - giải pháp”.
- Relationship - liên hệ với khái niệm khác: Capstone này dùng MCP servers, multiple agents, resources, search, memory, market data, và tracing.

### Synthetic account - tài khoản mô phỏng
- Term - thuật ngữ: Synthetic account - tài khoản mô phỏng
- Meaning - nghĩa: Tài khoản giao dịch không phải tiền thật, dùng để agent thực hiện hành vi mua bán trong môi trường an toàn hơn.
- Why it matters - vì sao quan trọng: Cho phép thử nghiệm hành vi giao dịch tự động mà không đụng tới vốn thật.
- Relationship - liên hệ với khái niệm khác: Nó phụ thuộc trực tiếp vào accounts server từ Day 2.

### Agent autonomy - tính tự chủ của agent
- Term - thuật ngữ: Agent autonomy - tính tự chủ của agent
- Meaning - nghĩa: Agent không chỉ trả lời câu hỏi mà còn chủ động nghiên cứu, quyết định, và hành động trong ranh giới được giao.
- Why it matters - vì sao quan trọng: Đây là điểm khác biệt giữa chatbot có tool và autonomous workflow - luồng tự vận hành.
- Relationship - liên hệ với khái niệm khác: Tự chủ càng cao thì càng cần tracing, guardrails, và môi trường an toàn như synthetic account.

### MCP server bundle - bó capability qua nhiều MCP servers
- Term - thuật ngữ: MCP server bundle - bó capability qua nhiều MCP servers
- Meaning - nghĩa: Một agent được trang bị đồng thời nhiều server khác nhau, mỗi server giải một lớp nhu cầu riêng như account, market, search, memory, push.
- Why it matters - vì sao quan trọng: Thể hiện đúng sức mạnh “equip agents with capabilities” của MCP.
- Relationship - liên hệ với khái niệm khác: Đây là tiến hóa tự nhiên từ việc dùng 1 server ở Day 1 sang 1 hệ đa server ở Day 4.

### Lab-first development - phát triển bắt đầu từ phòng thí nghiệm
- Term - thuật ngữ: Lab-first development - phát triển bắt đầu từ phòng thí nghiệm
- Meaning - nghĩa: Dùng notebook để thử prompt, hành vi, tool mix, rồi mới đóng gói thành code module.
- Why it matters - vì sao quan trọng: Agent systems thường khó đoán; prototype - mẫu thử giúp giảm rủi ro trước khi architecture - kiến trúc hóa.
- Relationship - liên hệ với khái niệm khác: Lesson 125 và 126 chính là bước chuyển từ lab sang modules `mcp_params.py`, `templates.py`, `traders.py`.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - Nhiều MCP capabilities từ các ngày trước.
   - Một bài toán thương mại là autonomous equity trading simulation - mô phỏng giao dịch cổ phiếu tự động.
2. Processing steps:
   - Chọn market data path - đường đi dữ liệu thị trường tùy plan.
   - Gắn accounts server, push server, search, fetch, memory cho các agents.
   - Thử nghiệm hành vi trong notebook trước.
3. Output:
   - Một trading floor có thể nghiên cứu thị trường, đọc account, giao dịch, và báo kết quả.
4. Control flow / data flow:
   - Trader hoặc researcher gọi tools/resources từ nhiều MCP servers khác nhau.
5. Decision points:
   - Dùng free hay paid Polygon path.
   - Có chuyển từ notebook sang Python modules hay chưa.
   - Có nên thêm nhiều autonomy hơn hay chưa.

## 7. Techniques - Kỹ thuật sử dụng

### Commercial framing - đóng khung theo bài toán thương mại
- Technique - kỹ thuật: Commercial framing - đóng khung theo bài toán thương mại
- Purpose - mục đích: Đặt agent system vào một use case - trường hợp sử dụng gần với doanh nghiệp thật.
- When to use - dùng khi nào: Khi muốn kiểm tra tool stack có giải được vấn đề thực tế hay không.
- Trade-off - đánh đổi: Bài toán đời thực nhiều biến số hơn và khó kiểm soát hơn demo nhỏ.
- Common mistake - lỗi dễ gặp: Xem capstone như demo vui mà quên thiết kế boundary - ranh giới an toàn.

### Capability composition - ghép năng lực từ nhiều server
- Technique - kỹ thuật: Capability composition - ghép năng lực từ nhiều server
- Purpose - mục đích: Cho mỗi agent có đúng bộ khả năng cần thiết thay vì một tool monolith - khối đơn.
- When to use - dùng khi nào: Khi hệ thống có nhiều loại tác vụ như tìm kiếm, phân tích, giao dịch, thông báo.
- Trade-off - đánh đổi: Số tool tăng, routing - chọn tool phức tạp hơn.
- Common mistake - lỗi dễ gặp: Nhồi quá nhiều tools mà không nghĩ đến hành vi của model.

### Tiny MCP server pattern - mẫu server MCP siêu nhỏ
- Technique - kỹ thuật: Tiny MCP server pattern - mẫu server MCP siêu nhỏ
- Purpose - mục đích: Expose một chức năng cực nhỏ nhưng tách biệt rõ, như gửi push notification.
- When to use - dùng khi nào: Khi logic đơn giản nhưng muốn đồng nhất hóa cách agent truy cập capability.
- Trade-off - đánh đổi: Về kỹ thuật, local function có thể đơn giản hơn, nhưng MCP server cho kiến trúc nhất quán hơn.
- Common mistake - lỗi dễ gặp: Dùng pattern này cho mọi thứ, kể cả khi function local là đủ.

## 8. Code Walkthrough - Phân tích code nếu có

### File / block: `4_lab4.ipynb` phần mở đầu
- Purpose - mục đích: Đặt bối cảnh cho project `Autonomous Traders`, liệt kê các MCP servers sẽ dùng, và xác định mục tiêu tạo `traders.py`.
- Key logic - logic chính:
  - Project có 4 traders và 1 researcher.
  - Capabilities đến từ accounts, fetch, memory, Brave Search, Polygon market data.
  - Notebook là nơi để experiment - thử nghiệm trước.
- Important lines / functions:
  - Notebook heading `Autonomous Traders`
  - Mô tả “The goal of today's lab is to make a new python module, traders.py”
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là cell quan trọng để định nghĩa “phạm vi bài toán”, không chỉ là khởi tạo code.
  - Nó nói rất rõ Day 4 chưa bắt đầu từ production module; module là đích đến sau phần lab.

### File / block: `push_server.py`
- Purpose - mục đích: Cung cấp một MCP server nhỏ để trader có thể gửi push notification sau khi hoàn thành trading action.
- Key logic - logic chính:
  - Dùng `FastMCP("push_server")` để tạo server.
  - Định nghĩa model `PushModelArgs` với một trường `message`.
  - Tool `push()` nhận message, gửi HTTP request tới dịch vụ push, rồi trả chuỗi xác nhận.
- Important lines / functions:
  - `mcp = FastMCP("push_server")`
  - `@mcp.tool()`
  - `def push(args: PushModelArgs)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là ví dụ rất “thin” - mỏng: server gần như chứa toàn bộ logic trong một file duy nhất.
  - Transcript cũng nói thẳng rằng về thực dụng, đây không nhất thiết phải là MCP server; nó được làm vậy để luyện tư duy MCP-first architecture.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Local function cho push
- Option: Gọi function Python trực tiếp
- Pros: Đơn giản nhất, ít plumbing nhất.
- Cons: Không đồng nhất với phần còn lại của kiến trúc MCP.
- When to choose: Khi push chỉ là utility nội bộ và không cần chia sẻ dưới dạng server.

### Option 2: MCP push server
- Option: Đóng gói push thành MCP server
- Pros: Cùng abstraction layer - lớp trừu tượng với các capability khác của agent.
- Cons: Tăng thêm process và metadata cho một chức năng rất nhỏ.
- When to choose: Khi muốn agent truy cập push giống hệt các tool khác, hoặc muốn giữ kiến trúc nhất quán.

### Option 3: Bỏ hẳn push notification
- Option: Không gửi thông báo đẩy
- Pros: Giảm complexity - độ phức tạp.
- Cons: Mất cảm giác agent đang hoạt động tự trị và mất một đường quan sát hệ thống.
- When to choose: Khi muốn demo tối giản hoặc chưa cần external notification - thông báo ngoài hệ thống.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Lao ngay vào module hóa mà không thử trong notebook
  - Root cause: Quá nôn kiến trúc hóa hệ thống.
  - Symptom: Tốn thời gian debug nhiều lớp cùng lúc mà chưa rõ lỗi ở prompt, tool hay orchestration.
  - Fix / prevention: Giữ nguyên tắc lab-first, thử trong notebook trước khi di chuyển sang module.

- Failure mode: Dùng project này cho trading thật
  - Root cause: Nhầm giữa demo capstone và hệ thống tài chính production-grade.
  - Symptom: Tin vào quyết định giao dịch của agent mà không có quản trị rủi ro đúng chuẩn.
  - Fix / prevention: Xem project như sandbox học tập; synthetic account là boundary an toàn cơ bản.

- Failure mode: Coi mỗi MCP server là “bắt buộc”
  - Root cause: Đồng nhất mọi capability với MCP dù không cần.
  - Symptom: Kiến trúc nặng, nhiều process không cần thiết.
  - Fix / prevention: Chỉ dùng MCP khi nó phục vụ shareability - khả năng chia sẻ, modularity - tính mô-đun, hoặc mục tiêu học tập rõ ràng.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có nguyên văn trong buổi học.

- Trong production trading systems - hệ thống giao dịch thực tế, push notification thường chỉ là tầng observability - quan sát và alerting - cảnh báo, không phải logic cốt lõi.
- Một thiết kế agent tốt thường bắt đầu bằng “capability inventory” - kiểm kê năng lực: agent nào cần đọc gì, gọi gì, ghi gì, và mức tự chủ tới đâu.
- Với các hệ thống nhiều tools, việc có notebook prototype trước giúp đánh giá sớm token cost (chi phí token), tool routing, và failure modes - kiểu lỗi phổ biến.

## 12. Study Pack - Gói ôn tập
### Must remember
- Day 4 mở capstone bằng một bài toán thương mại: autonomous trading simulation.
- Hệ thống dùng lại gần như toàn bộ các capability MCP từ Day 1-3.
- Research-first, lab-first là nguyên tắc được nhấn mạnh nhiều lần.
- `push_server.py` là ví dụ MCP server cực nhỏ, thêm cảm giác hệ thống đang tự vận hành.
- Capstone này không dành cho giao dịch thật; synthetic account là môi trường thử nghiệm.

### Self-check questions
- Vì sao instructor chọn bài toán trading thay vì tiếp tục demo kỹ thuật thuần túy?
- Vì sao notebook là nơi bắt đầu tốt hơn module Python cho Day 4?
- `push_server.py` có thật sự cần là MCP server không? Nếu không, vì sao vẫn làm như vậy?
- Capstone Day 4 tận dụng những gì từ Day 2 và Day 3?
- Vì sao autonomy cần đi kèm tracing và môi trường an toàn?

### Flashcards
- Q: Capstone Day 4 tên gì?
  A: `Autonomous Traders` - một equity trading simulation dùng nhiều MCP servers và nhiều agents.

- Q: Vì sao có `push_server.py`?
  A: Để trader gửi push notification sau khi hành động, làm hệ thống có cảm giác autonomous hơn và tạo thêm observability.

- Q: Day 4 bắt đầu bằng module Python hay notebook?
  A: Bắt đầu bằng notebook/lab để experiment, rồi mới chuyển sang module Python.

### Interview Q&A nếu phù hợp
- Q: Vì sao khi xây agent systems bạn nên bắt đầu bằng notebook prototype trước khi module hóa?
  A: Vì notebook cho phép kiểm tra nhanh prompt behavior, tool usage, autonomy level, và trace flow trước khi phải quản lý thêm complexity của architecture - kiến trúc mô-đun. Với agentic systems, lỗi thường không chỉ nằm ở code mà còn nằm ở prompt, tool routing, context injection, và model behavior. Prototype trước giúp tách những biến số đó rõ hơn.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Không có ảnh chụp trace hoặc UI trong session cho lesson mở đầu này
- Không có `market_server.py` hoặc repo `mcp_polygon` trong session hiện tại, nên phần market path chỉ được dùng như project context chứ chưa walkthrough sâu ở lesson này

---

# 124. Day 4 - Viewing the User Interface for Trading Activity

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `124. Day 4 - Viewing the User Interface for Trading Activity.txt`
- Slide: không có
- Code: đã dùng — `4_lab4.ipynb` phần tạo MCP servers, researcher agent, trader agent và chạy trace; `accounts_client.py` được đọc bổ sung vì transcript dùng trực tiếp account/strategy resources
- Summary lịch sử: đã dùng — `day1_summary.md`, `day2_summary.md`, `day3_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Tên file transcript nhắc tới UI, nhưng nội dung thực tế của lesson tập trung mạnh hơn vào lab setup của researcher/trader và cách chạy trace. Vì vậy phần summary bám nội dung transcript thực tế, không suy đoán thêm về UI ngoài nguồn.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này chuyển từ phần giới thiệu dự án sang phần “làm cho hệ thống sống dậy” trong lab: instantiate - khởi tạo các MCP servers và tạo 2 loại agent là researcher và trader.
- Researcher agent được xây như một specialist - agent chuyên trách nghiên cứu tài chính trên web, rồi được convert thành tool để trader có thể gọi như một năng lực phụ trợ.
- Transcript nhấn mạnh một pattern quan trọng của OpenAI Agents SDK: researcher-as-tool thay vì handoff - chuyển quyền điều phối, vì trader cần dùng researcher như một công cụ chứ không phải trao luôn phiên làm việc.
- Instructor thêm current date - ngày giờ hiện tại trực tiếp vào instructions thay vì cho agent một tool xem ngày tháng, để tránh tool call thừa.
- Trader agent đọc 2 resources là account details và strategy qua MCP resource path, rồi nhúng JSON vào prompt làm context ra quyết định.
- `Runner.run(..., max_turns=30)` được dùng cho cả researcher và trader để cho agent đủ không gian suy nghĩ và gọi tools sâu hơn mức mặc định.
- Tracing được xem như bước bắt buộc: phải quay lại trace để xem researcher đã search gì, fetch gì, trader đã mua bán gì và vì sao.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu pattern agent-as-tool trong OpenAI Agents SDK.
  - Hiểu resource injection - bơm tài nguyên vào prompt từ MCP resources thay vì hardcode state.
  - Hiểu vai trò của tracing trong việc kiểm tra hành vi của autonomous agents.
- Practical goals - mục tiêu thực hành:
  - Biết cách instantiate nhiều MCP servers cho researcher và trader.
  - Biết cách chạy researcher riêng để kiểm tra trước khi dùng làm tool.
  - Biết cách đọc account/strategy resource rồi khởi tạo trader bằng prompt có ngữ cảnh thật.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao researcher nên được biến thành tool.
  - Vì sao ngày giờ hiện tại nên được đưa vào prompt thay vì cấp một date tool riêng.
  - Vì sao JSON account details có ích cho LLM khi ra quyết định giao dịch.

## 4. Previous Context - Liên hệ với bài trước
- Day 2 đã tạo `accounts_server.py` và `accounts_client.py`, nên Day 4 có thể đọc account và strategy qua resources thay vì truyền tay dữ liệu.
- Day 3 đã tạo market intelligence path qua Brave Search, fetch, memory, và Polygon market data; lesson này là nơi các năng lực đó được gắn vào 2 agent khác vai trò.
- Day 1 từng cho thấy một agent có thể dùng nhiều MCP servers; lesson 124 nâng cấp lên một agent dùng một agent khác như tool trên nền nhiều servers.

## 5. Core Theory - Lý thuyết cốt lõi

### Researcher-as-tool - agent nghiên cứu dưới dạng công cụ
- Term - thuật ngữ: Researcher-as-tool - agent nghiên cứu dưới dạng công cụ
- Meaning - nghĩa: Một agent chuyên nghiên cứu được bọc thành tool để agent khác gọi khi cần.
- Why it matters - vì sao quan trọng: Nó giữ vai trò điều phối ở trader, nhưng vẫn tận dụng được một capability nghiên cứu giàu toolset.
- Relationship - liên hệ với khái niệm khác: Đây là một dạng hierarchical composition - ghép tầng tác nhân, nhẹ hơn handoff.

### Resource injection - đưa resource vào prompt
- Term - thuật ngữ: Resource injection - đưa resource vào prompt
- Meaning - nghĩa: Đọc dữ liệu từ MCP resources rồi nhúng thẳng vào prompt dưới dạng text hoặc JSON.
- Why it matters - vì sao quan trọng: Agent có context hiện tại về tài khoản và chiến lược mà không phải tự gọi thêm tool ở đầu phiên.
- Relationship - liên hệ với khái niệm khác: Nối trực tiếp Day 2 resources với Day 4 trader decision-making.

### Trace-first verification - kiểm chứng bằng trace
- Term - thuật ngữ: Trace-first verification - kiểm chứng bằng trace
- Meaning - nghĩa: Sau khi agent chạy, phải xem trace để xác nhận agent đã dùng tools ra sao, theo thứ tự nào, và có đi chệch không.
- Why it matters - vì sao quan trọng: Autonomous agent có thể cho ra output nghe hợp lý nhưng bên trong dùng tool sai hoặc reasoning sai.
- Relationship - liên hệ với khái niệm khác: Trace là lớp observability song hành với autonomy.

### Max turns - giới hạn số vòng suy nghĩ và tool call
- Term - thuật ngữ: Max turns - giới hạn số vòng suy nghĩ và tool call
- Meaning - nghĩa: Số vòng agent được phép suy nghĩ và gọi tools trước khi runner dừng.
- Why it matters - vì sao quan trọng: Các tác vụ research hoặc trading đa bước có thể cần nhiều hơn mặc định 10 turns.
- Relationship - liên hệ với khái niệm khác: Nó cân bằng giữa depth - độ sâu nghiên cứu và risk of looping - rủi ro lặp vòng.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - MCP server params cho trader và researcher.
   - Một câu hỏi research hoặc một trading prompt.
2. Processing steps:
   - Instantiate các MCP servers.
   - Tạo researcher agent với search/fetch/memory.
   - Convert researcher thành tool.
   - Đọc `account` và `strategy` resources.
   - Tạo trader agent với researcher tool + trader MCP servers.
   - Chạy `Runner.run(..., max_turns=30)`.
3. Output:
   - Research summary hoặc trading summary.
4. Control flow / data flow:
   - Trader -> Researcher tool -> search/fetch/memory -> quay lại Trader -> market/account tools -> trade actions.
5. Decision points:
   - Khi nào trader gọi researcher.
   - Dùng dữ liệu market nào theo plan.
   - Có dừng giao dịch vì market closed - thị trường đóng cửa hay vẫn hành động theo dữ liệu hiện có.

## 7. Techniques - Kỹ thuật sử dụng

### Agent specialization - chuyên môn hóa agent
- Technique - kỹ thuật: Agent specialization - chuyên môn hóa agent
- Purpose - mục đích: Tách nghiên cứu và hành động giao dịch thành hai vai trò riêng.
- When to use - dùng khi nào: Khi một agent chính cần năng lực phụ sâu nhưng không nên ôm toàn bộ instructions của vai trò phụ.
- Trade-off - đánh đổi: Thêm một lớp orchestration nhưng behavior rõ vai hơn.
- Common mistake - lỗi dễ gặp: Dồn mọi nhiệm vụ vào một agent duy nhất khiến prompt rối và tool usage lẫn lộn.

### Prompt grounding by live resources - neo prompt bằng tài nguyên sống
- Technique - kỹ thuật: Prompt grounding by live resources - neo prompt bằng tài nguyên sống
- Purpose - mục đích: Đưa state hiện tại của account và strategy vào quyết định giao dịch.
- When to use - dùng khi nào: Khi agent cần ra quyết định dựa trên state động của hệ thống.
- Trade-off - đánh đổi: Prompt dài hơn nhưng giảm số tool call mở đầu.
- Common mistake - lỗi dễ gặp: Đưa state tĩnh cũ vào prompt rồi quên refresh.

### Explicit temporal grounding - neo thời gian rõ ràng
- Technique - kỹ thuật: Explicit temporal grounding - neo thời gian rõ ràng
- Purpose - mục đích: Cho researcher biết “hôm nay” là khi nào để tìm tin tức đúng ngữ cảnh.
- When to use - dùng khi nào: Tác vụ search/news/market đều nhạy cảm thời gian.
- Trade-off - đánh đổi: Prompt dài thêm rất ít nhưng giảm sai lệch thời gian đáng kể.
- Common mistake - lỗi dễ gặp: Để model tự đoán “now” mà không cấp mốc thời gian cụ thể.

## 8. Code Walkthrough - Phân tích code nếu có

### File / block: `4_lab4.ipynb` cells tạo MCP server params
- Purpose - mục đích: Gom các MCP server parameters thành 2 nhóm: trader servers và researcher servers.
- Key logic - logic chính:
  - Trader có accounts server, push server, và market server.
  - Researcher có fetch, Brave Search, và memory.
  - Có nhánh chọn official Polygon MCP hay local `market_server.py` theo plan.
- Important lines / functions:
  - Danh sách params cho `accounts_server.py`, `push_server.py`, market MCP
  - Danh sách params cho fetch, Brave Search, memory
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là nơi cho thấy Day 4 không chỉ dùng MCP cho “tool đơn lẻ” mà dùng nó để lắp một capability graph - đồ thị năng lực.

### File / block: `4_lab4.ipynb` phần tạo Researcher agent
- Purpose - mục đích: Định nghĩa agent nghiên cứu tài chính và bọc nó thành tool.
- Key logic - logic chính:
  - Researcher có instructions riêng.
  - Current datetime được chèn trực tiếp vào prompt.
  - `researcher.as_tool(...)` biến cả agent thành tool để trader gọi.
- Important lines / functions:
  - `researcher = Agent(...)`
  - `researcher.as_tool(tool_name=..., tool_description=...)`
  - `Runner.run(researcher, research_question, max_turns=30)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - `as_tool()` là chiếc cầu giữa multi-agent collaboration - cộng tác đa agent và tool calling - gọi công cụ chuẩn của SDK.

### File / block: `accounts_client.py`
- Purpose - mục đích: Đọc resources `accounts://...` và `accounts://strategy/...` để trader có account state và strategy hiện thời.
- Key logic - logic chính:
  - Mỗi lần đọc resource đều mở `stdio_client`, tạo `ClientSession`, `initialize()`, rồi `read_resource(...)`.
  - Hai helper chính là `read_accounts_resource(name)` và `read_strategy_resource(name)`.
- Important lines / functions:
  - `read_accounts_resource(name)`
  - `read_strategy_resource(name)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là phần làm cho trading prompt có dữ liệu “sống”, không chỉ là text giả lập trong notebook.

### File / block: `4_lab4.ipynb` phần tạo Trader agent
- Purpose - mục đích: Tạo trader agent dùng researcher tool, market/account tools, và prompt có account + strategy.
- Key logic - logic chính:
  - Đọc `account_details` và `strategy` từ resources.
  - Chèn chúng vào system prompt của trader.
  - Chạy `Runner.run(trader, prompt, max_turns=30)` trong `trace(...)`.
- Important lines / functions:
  - `account_details = await read_accounts_resource(agent_name)`
  - `strategy = await read_strategy_resource(agent_name)`
  - `with trace(agent_name):`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - JSON account details được nhúng trực tiếp vào prompt vì transcript nhấn mạnh “LLMs love JSON” trong ngữ cảnh này.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Một agent làm tất cả
- Option: Single all-in-one trader
- Pros: Kiến trúc đơn giản hơn.
- Cons: Prompt và tool responsibilities dễ rối; nghiên cứu và giao dịch trộn vào nhau.
- When to choose: Chỉ khi bài toán đủ nhỏ và toolset ít.

### Option 2: Trader dùng Researcher như tool
- Option: Specialist researcher under trader control
- Pros: Giữ orchestration tập trung ở trader, nhưng vẫn có chuyên môn hóa mạnh.
- Cons: Tăng thêm một lớp setup và trace.
- When to choose: Khi nghiên cứu là tác vụ phụ nhưng quan trọng cho quyết định của agent chính.

### Option 3: Handoff hoàn toàn sang researcher
- Option: Delegate by handoff
- Pros: Phù hợp khi vai trò nghiên cứu tự giải quyết một subtask - tiểu tác vụ độc lập rồi trả kết quả ở mức phiên.
- Cons: Kém phù hợp hơn nếu trader vẫn phải giữ quyền quyết định và gọi thêm market/account tools sau nghiên cứu.
- When to choose: Khi subtask có ranh giới rõ và không cần agent chính giữ nhịp orchestration.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Không kiểm tra researcher riêng trước khi biến thành tool
  - Root cause: Vội tích hợp multi-agent pipeline.
  - Symptom: Trader gọi researcher nhưng lỗi đến từ search/fetch path mà khó tách ra debug.
  - Fix / prevention: Chạy researcher độc lập trước để xác nhận toolchain hoạt động.

- Failure mode: Không đưa account/strategy vào prompt
  - Root cause: Xem trader như agent “chung chung”.
  - Symptom: Agent giao dịch mà không bám portfolio hiện tại hoặc strategy cá nhân.
  - Fix / prevention: Đọc resources và inject vào prompt trước khi chạy.

- Failure mode: Chỉ nhìn final output mà không xem trace
  - Root cause: Tin câu trả lời văn bản của agent.
  - Symptom: Không thấy agent đã dùng search/fetch/market tools một cách lãng phí hoặc sai hướng.
  - Fix / prevention: Luôn xem trace sau run, nhất là với autonomous tasks.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có nguyên văn trong buổi học.

- Pattern “agent as tool” rất hữu ích khi bạn muốn giữ một main controller - bộ điều phối chính nhưng vẫn tận dụng được chuyên môn của sub-agent.
- Với các workflows nhạy thời gian như tài chính, explicit time grounding thường quan trọng hơn người mới học nghĩ.
- Resource injection thường rẻ token hơn nhiều lần tool call lặp lại ở đầu phiên, nhưng cần cẩn thận với kích thước dữ liệu đưa vào prompt.

## 12. Study Pack - Gói ôn tập
### Must remember
- Researcher được tạo như agent riêng rồi bọc thành tool cho trader.
- Trader đọc account và strategy qua MCP resources, không hardcode.
- `max_turns=30` được dùng để cho phép research/trading sâu hơn.
- Tracing là bắt buộc nếu muốn hiểu agent đã làm gì.
- Nội dung transcript lesson này nghiêng về lab setup và trace flow hơn là UI thuần túy.

### Self-check questions
- Vì sao `researcher.as_tool(...)` hợp lý hơn handoff trong bài toán này?
- Vì sao nên đưa current datetime trực tiếp vào researcher instructions?
- Vì sao account và strategy được đưa vào prompt dưới dạng resource?
- `max_turns` giải quyết vấn đề gì?
- Vì sao final output đẹp chưa đủ để kết luận agent hành xử tốt?

### Flashcards
- Q: Trader lấy `account` và `strategy` từ đâu?
  A: Từ MCP resources qua `accounts_client.py`, cụ thể là `read_accounts_resource()` và `read_strategy_resource()`.

- Q: Researcher trở thành tool bằng cách nào?
  A: Dùng `researcher.as_tool(...)` trong OpenAI Agents SDK.

- Q: Vì sao cần trace trong lesson này?
  A: Để xem researcher đã search/fetch gì và trader đã gọi market/account tools theo thứ tự nào.

### Interview Q&A nếu phù hợp
- Q: Khi nào pattern “agent as tool” tốt hơn việc để một agent đơn làm mọi thứ?
  A: Khi có một vai trò chuyên môn rõ ràng, như research, mà agent chính cần gọi theo nhu cầu chứ không muốn bàn giao hoàn toàn luồng điều phối. Pattern này giúp tách prompt, tách tool responsibilities, và làm trace dễ đọc hơn. Nó đặc biệt phù hợp khi main agent vẫn phải giữ quyền ra quyết định cuối cùng.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Không có ảnh UI hoặc trace screenshot đi kèm, chỉ có transcript mô tả
- Không có runtime output JSON đầy đủ từ các trade actions trong session hiện tại, nên phần chi tiết giao dịch được bám transcript thay vì tái dựng dữ liệu cụ thể

---

# 125. Day 4 - How Trading Agents Operate and Make Decisions

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `125. Day 4 - How Trading Agents Operate and Make Decisions.txt`
- Slide: không có
- Code: đã dùng — `4_lab4.ipynb` phần trace/error analysis, `mcp_params.py`, `templates.py`
- Summary lịch sử: đã dùng — `day1_summary.md`, `day2_summary.md`, `day3_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript có một đoạn rất quan trọng đi từ trace investigation sang module hóa. Các file `mcp_params.py` và `templates.py` được transcript gọi đích danh nên là nguồn code trực tiếp cho lesson này.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này mở đầu bằng việc đọc lại trace để giải thích một “hiccup” - trục trặc có chủ đích: trader từng cố mua Tesla nhưng giao dịch đó không xuất hiện trong holdings cuối cùng.
- Root cause - nguyên nhân gốc là `Insufficient funds to buy shares` từ business logic cũ của accounts system; đây là ví dụ rất tốt cho việc trace giúp giải thích hành vi agent thay vì chỉ nhìn summary cuối.
- Từ tình huống đó, instructor rút ra nguyên tắc lớn hơn: khi xây agent solutions - giải pháp agent, đừng thiết kế cả sơ đồ lớn rồi code lâu ngày mới chạy thử; hãy bắt đầu nhỏ trong lab và học qua thực nghiệm.
- Lesson sau đó chuyển sang module hóa: tách server params vào `mcp_params.py`, tách prompt text vào `templates.py`, và giữ code điều phối chính cho `traders.py`.
- `mcp_params.py` cho thấy cách project chọn market data path theo plan và phân tách server sets cho trader và researcher.
- `templates.py` cho thấy prompt engineering - kỹ nghệ prompt cũng nên được tổ chức như source code, tách riêng để dễ chỉnh sửa và giữ separation of concerns - phân tách mối quan tâm.
- Bài học lớn của lesson này là: behavior của agent phải được quan sát qua traces và được chỉnh dần trong lab trước khi đóng gói thành kiến trúc module sạch.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu vì sao trace là công cụ tìm root cause mạnh hơn việc chỉ đọc final answer.
  - Hiểu nguyên tắc lab-first experimentation trong phát triển agentic systems.
  - Hiểu lợi ích của việc tách configuration và prompt templates khỏi orchestration code.
- Practical goals - mục tiêu thực hành:
  - Biết đọc trace để giải thích giao dịch không thành công.
  - Biết cấu trúc file nào nên nằm ở `mcp_params.py` và file nào nên nằm ở `templates.py`.
  - Biết cách giữ prompts có tổ chức thay vì nhét string dài vào thân hàm.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao “insufficient funds” là một thành công của business rule chứ không phải bug của agent.
  - Vì sao prompts là first-class artifact - tạo phẩm hạng nhất trong project agent.
  - Vì sao không nên nhảy thẳng từ ý tưởng sang kiến trúc module hoàn chỉnh mà bỏ qua lab.

## 4. Previous Context - Liên hệ với bài trước
- Day 2 đã tạo accounts business logic và business rule chặn mua quá sức; lesson này chứng minh rule đó sống lại trong Day 4 qua trace.
- Day 3 đã tạo market selection logic và memory logic; lesson 125 bắt đầu đóng gói chúng vào `mcp_params.py` và prompts theo context hiện tại.
- Lesson 124 đã chạy trader trong notebook; lesson 125 là bước suy ngẫm và rút quy luật từ chính run đó trước khi module hóa.

## 5. Core Theory - Lý thuyết cốt lõi

### Trace-driven debugging - debug dựa trên trace
- Term - thuật ngữ: Trace-driven debugging - debug dựa trên trace
- Meaning - nghĩa: Đi ngược từ hành vi quan sát được về từng tool call, từng error, từng decision trong trace.
- Why it matters - vì sao quan trọng: Agent có thể “nói hay” trong final output nhưng trace mới cho biết nó thực sự làm gì.
- Relationship - liên hệ với khái niệm khác: Nó là lớp quan sát cần thiết cho autonomy.

### Business rule enforcement - thực thi luật nghiệp vụ
- Term - thuật ngữ: Business rule enforcement - thực thi luật nghiệp vụ
- Meaning - nghĩa: Những ràng buộc như không được mua vượt quá số tiền có sẵn phải nằm ở business logic, không giao hoàn toàn cho prompt.
- Why it matters - vì sao quan trọng: Guardrails - hàng rào an toàn đáng tin nhất nên ở code và server logic, không chỉ ở lời dặn model.
- Relationship - liên hệ với khái niệm khác: `Insufficient funds` là ví dụ cụ thể của Day 2 logic được tái sử dụng.

### Separation of concerns - phân tách mối quan tâm
- Term - thuật ngữ: Separation of concerns - phân tách mối quan tâm
- Meaning - nghĩa: Tách config server, prompt templates, và orchestration logic thành các file riêng.
- Why it matters - vì sao quan trọng: Agent projects nhanh trở nên rối vì text prompts, model params, và tool logic thường trộn lẫn.
- Relationship - liên hệ với khái niệm khác: Day 4 chuyển từ notebook prototype sang module architecture theo đúng nguyên tắc này.

### Prompt templates as code assets - prompt templates như tài sản mã nguồn
- Term - thuật ngữ: Prompt templates as code assets - prompt templates như tài sản mã nguồn
- Meaning - nghĩa: Prompt không phải chuỗi text phụ; nó là phần logic hành vi cần được tổ chức, chỉnh sửa, và bảo trì nghiêm túc.
- Why it matters - vì sao quan trọng: Hành vi trader/researcher phụ thuộc trực tiếp vào instructions và message templates.
- Relationship - liên hệ với khái niệm khác: `templates.py` là nơi hiện thực hóa tư duy này.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - Kết quả chạy trader từ lesson trước.
   - Trace của tool calls.
2. Processing steps:
   - Kiểm tra trace để đối chiếu summary và holdings.
   - Xác định lỗi `Insufficient funds`.
   - Rút ra nguyên tắc build agent qua lab experimentation.
   - Tách project thành `mcp_params.py` và `templates.py`.
3. Output:
   - Hiểu rõ vì sao trade Tesla không thành công.
   - Có cấu trúc module sạch hơn cho project.
4. Control flow / data flow:
   - Trace -> tool error -> giải thích behavior -> tái cấu trúc project files.
5. Decision points:
   - Có coi hiện tượng vừa thấy là bug hay business rule hợp lệ.
   - Tách phần nào thành config, phần nào thành prompt templates.

## 7. Techniques - Kỹ thuật sử dụng

### Trace reconciliation - đối chiếu trace với kết quả cuối
- Technique - kỹ thuật: Trace reconciliation - đối chiếu trace với kết quả cuối
- Purpose - mục đích: Xác nhận xem output cuối có phản ánh đúng các hành động bên trong hay không.
- When to use - dùng khi nào: Khi final summary và system state dường như mâu thuẫn.
- Trade-off - đánh đổi: Tốn thời gian đọc trace nhưng cho ra root cause rõ.
- Common mistake - lỗi dễ gặp: Thấy mismatch rồi kết luận agent “ảo” mà không kiểm tra tool errors.

### Modular prompt storage - lưu prompt theo module riêng
- Technique - kỹ thuật: Modular prompt storage - lưu prompt theo module riêng
- Purpose - mục đích: Giữ cho prompt revisions - các lần chỉnh prompt dễ theo dõi và không lẫn với orchestration code.
- When to use - dùng khi nào: Khi dự án có nhiều agent, nhiều message types, hoặc prompts dài.
- Trade-off - đánh đổi: Thêm một file nhưng tăng tính tổ chức rõ rệt.
- Common mistake - lỗi dễ gặp: Để prompt strings rải rác khắp codebase.

### Parameterized MCP bundles - bó server tham số hóa
- Technique - kỹ thuật: Parameterized MCP bundles - bó server tham số hóa
- Purpose - mục đích: Tái sử dụng logic lựa chọn server sets cho nhiều agent và nhiều plan khác nhau.
- When to use - dùng khi nào: Khi cùng project phải chạy ở free, paid, hoặc nhiều persona khác nhau.
- Trade-off - đánh đổi: Thêm abstraction nhưng giảm duplicate - trùng lặp.
- Common mistake - lỗi dễ gặp: Hardcode từng server list ở nhiều chỗ khác nhau.

## 8. Code Walkthrough - Phân tích code nếu có

### File / block: `4_lab4.ipynb` phần trace hiccup
- Purpose - mục đích: Chứng minh trace có thể giải thích vì sao Tesla trade không xuất hiện trong holdings cuối.
- Key logic - logic chính:
  - Trace cho thấy agent từng gọi lệnh mua Disney và Tesla.
  - Tool execution trả về lỗi `Insufficient funds to buy shares` cho giao dịch Tesla.
  - Vì lệnh bị chặn ở business logic, holdings cuối không có Tesla là đúng.
- Important lines / functions:
  - Các span tool call mua Disney/Tesla trong trace
  - Tool error `Insufficient funds to buy shares`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là ví dụ textbook cho câu “trace mới là sự thật vận hành”, không phải đoạn summary đẹp của agent.

### File / block: `mcp_params.py`
- Purpose - mục đích: Tập trung toàn bộ logic lựa chọn và phân nhóm MCP server parameters.
- Key logic - logic chính:
  - Nếu `is_paid_polygon` hoặc `is_realtime_polygon`, dùng official Polygon MCP server.
  - Nếu không, dùng local `market_server.py`.
  - Tạo `trader_mcp_server_params` và `researcher_mcp_server_params(name)`.
- Important lines / functions:
  - `market_mcp = ...`
  - `trader_mcp_server_params = [...]`
  - `def researcher_mcp_server_params(name: str)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - File này đóng vai “wiring manifest” - bản khai đấu nối cho toàn bộ hệ thống MCP của Day 4.

### File / block: `templates.py`
- Purpose - mục đích: Chứa toàn bộ instructions và message templates cho researcher và trader.
- Key logic - logic chính:
  - `researcher_instructions()` nhấn mạnh search nhiều nguồn, dùng knowledge graph memory, và có current datetime.
  - `trader_instructions(name)` định nghĩa vai trò trader và mục tiêu lợi nhuận.
  - `trade_message(...)` và `rebalance_message(...)` tạo user prompt theo từng mode hoạt động.
- Important lines / functions:
  - `researcher_instructions()`
  - `research_tool()`
  - `trader_instructions(name)`
  - `trade_message(...)`
  - `rebalance_message(...)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - `templates.py` là nơi hành vi được “nắn” - điều chỉnh. Chỉnh file này thường thay đổi agent behavior rõ hơn nhiều so với chỉnh code Python thuần.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Nhét prompt và params vào notebook/orchestration file
- Option: Inline everything
- Pros: Nhanh cho demo ngắn.
- Cons: Khó bảo trì, khó so sánh prompt revisions, dễ lặp lại cấu hình.
- When to choose: Chỉ cho prototype rất ngắn chưa vượt qua giai đoạn thử sơ bộ.

### Option 2: Tách `mcp_params.py` và `templates.py`
- Option: Clean modular split
- Pros: Dễ sửa, dễ đọc, hợp với project đang lớn dần.
- Cons: Thêm file và cần discipline - kỷ luật tổ chức.
- When to choose: Khi prototype đã chứng minh ý tưởng và sẵn sàng đóng gói.

### Option 3: Dựng kiến trúc lớn từ đầu
- Option: Big upfront design
- Pros: Có vẻ “chuyên nghiệp” trên giấy.
- Cons: Dễ sai vì agent behavior chưa được hiểu đủ qua thực nghiệm.
- When to choose: Hiếm khi là lựa chọn tốt cho dự án agentic mới.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Xem tool error như bug của hệ thống thay vì business rule hợp lệ
  - Root cause: Không phân biệt agent reasoning và domain constraints.
  - Symptom: Cố “sửa” một hành vi thực ra đang bảo vệ hệ thống.
  - Fix / prevention: Đối chiếu trace với rule nghiệp vụ trước khi kết luận có bug.

- Failure mode: Đóng gói module quá sớm
  - Root cause: Muốn kiến trúc đẹp trước khi hiểu hành vi.
  - Symptom: Refactor nhiều lần vì prompt/tool mix chưa ổn định.
  - Fix / prevention: Thử trong lab cho đến khi hiểu được behavior đủ sâu.

- Failure mode: Coi prompts là phần phụ
  - Root cause: Tư duy quá thiên code.
  - Symptom: Prompt nằm lẫn trong code, khó tối ưu hành vi agent.
  - Fix / prevention: Quản lý prompts như một asset riêng của hệ thống.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có nguyên văn trong buổi học.

- Nhiều đội làm agent production coi trace review là phần tương đương unit test cho giai đoạn hành vi sớm của agent.
- Business rules - luật nghiệp vụ như balance checks thường nên nằm ở tool/server layer thay vì chỉ giao cho model tự “có trách nhiệm”.
- Khi project chuyển từ notebook sang modules, việc tách prompt/config thường là refactor có ROI - hiệu quả đầu tư cao nhất đầu tiên.

## 12. Study Pack - Gói ôn tập
### Must remember
- Trace đã giải thích rõ vì sao Tesla purchase không thành công.
- `Insufficient funds` là dấu hiệu rule nghiệp vụ hoạt động đúng.
- Day 4 nhấn mạnh mạnh mẽ nguyên tắc: start in the lab, then package into modules.
- `mcp_params.py` gom logic chọn server; `templates.py` gom prompt logic.
- Prompt text là logic hành vi, không phải nội dung phụ.

### Self-check questions
- Vì sao trace quan trọng hơn final summary khi debug agent?
- Vì sao trade Tesla không thành công lại không phải bug?
- Vì sao nên tách `mcp_params.py` khỏi file orchestration chính?
- Vì sao `templates.py` giúp project agent dễ tiến hóa hơn?
- “Big upfront design” nguy hiểm như thế nào trong agentic development?

### Flashcards
- Q: Lỗi nào xuất hiện khi trader cố mua quá khả năng?
  A: `Insufficient funds to buy shares`.

- Q: `mcp_params.py` giải quyết việc gì?
  A: Tập trung logic cấu hình và chọn MCP servers cho trader/researcher.

- Q: `templates.py` giải quyết việc gì?
  A: Tập trung instructions và messages cho researcher/trader để dễ chỉnh hành vi.

### Interview Q&A nếu phù hợp
- Q: Bạn sẽ giải thích thế nào cho một team mới rằng vì sao trace review nên đứng trước refactor khi phát triển agent systems?
  A: Vì nếu chưa hiểu hành vi thật của agent trong trace, refactor dễ trở thành tối ưu sai chỗ. Trace cho biết model đã gọi tool nào, bị lỗi ở đâu, loop ra sao, và có đi đúng policy không. Chỉ sau khi có bức tranh đó, bạn mới biết nên sửa prompt, sửa business logic, hay sửa kiến trúc module.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Không có ảnh trace trực tiếp trong session, chỉ có transcript mô tả trace
- Không có file `market_server.py` trong bộ code được chỉ định cho session này, nên market-free-path chỉ được hiểu gián tiếp qua `mcp_params.py`

---

# 126. Day 4 - Portfolio Management with Four Autonomous Agents

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `126. Day 4 - Portfolio Management with Four Autonomous Agents.txt`
- Slide: không có
- Code: đã dùng — `traders.py`, `mcp_params.py`, `templates.py`, `accounts_client.py`; `tracers.py` được đọc bổ sung để hiểu `trace_id` helper nhưng chỉ dùng như dependency context
- Summary lịch sử: đã dùng — `day1_summary.md`, `day2_summary.md`, `day3_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript mô tả trực tiếp `traders.py` và cách chạy class `Trader`. `tracers.py` không được transcript giải thích sâu, nên chỉ được dùng như ngữ cảnh phụ cho trace flow, không dùng để suy diễn quá mức.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson này hoàn tất bước chuyển từ notebook prototype sang Python module `traders.py`, nơi trader trở thành một class có thể được khởi tạo và chạy như business component - thành phần nghiệp vụ.
- `AsyncExitStack` được dùng để mở nhiều `MCPServerStdio` context managers mà không phải lồng quá nhiều `async with`, giúp code gọn hơn khi có nhiều MCP servers.
- `Trader` class chịu trách nhiệm tạo researcher tool, tạo trader agent, đọc account report, chọn giữa trade mode và rebalance mode, rồi chạy trong trace.
- Project được thiết kế để hỗ trợ nhiều model providers như OpenAI, DeepSeek, Grok, Gemini, hoặc OpenRouter thông qua `get_model(model_name)`.
- Trader được cho khả năng alternate - luân phiên giữa trading và rebalancing bằng cờ `do_trade`, nghĩa là mỗi lần chạy có thể làm vai trò khác nhau.
- Transcript cho thấy một run hoàn chỉnh: researcher search web, trader đọc market data, mua bán cổ phiếu, rồi gửi push notification ở cuối.
- Một error thú vị xuất hiện ở push tool dù notification vẫn đến điện thoại, cho thấy hệ thống agent hoạt động được nhưng observability vẫn cần tinh chỉnh.
- Cuối lesson, tổng số capability được lắp vào hệ thống được đếm là 6 MCP servers và 44 tools, minh họa rõ mức độ “tool-rich” - giàu công cụ của trading floor.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách đóng gói trader thành class để chuyển từ lab experiment sang reusable component - thành phần tái sử dụng.
  - Hiểu lợi ích của `AsyncExitStack` khi quản lý nhiều async context managers.
  - Hiểu một architecture agentic có thể hỗ trợ nhiều model providers mà không đổi logic nghiệp vụ chính.
- Practical goals - mục tiêu thực hành:
  - Biết cấu trúc chính của `Trader` class.
  - Biết cách luân phiên trade/rebalance qua `do_trade`.
  - Biết cách chạy trader trong trace và đọc kết quả sau khi module hóa.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao `AsyncExitStack` giúp code gọn hơn với nhiều MCP servers.
  - Vì sao module hóa trader sau notebook là bước hợp lý.
  - Vì sao multi-model support - hỗ trợ nhiều mô hình là phần mở rộng hợp lý của project nhưng không làm đổi lõi orchestration.

## 4. Previous Context - Liên hệ với bài trước
- Lesson 124 đã chứng minh prototype notebook chạy được; lesson 125 đã rút ra bài học và tách `mcp_params.py`, `templates.py`; lesson 126 đưa phần còn lại vào `traders.py`.
- Day 2 cung cấp `accounts_client.py` để trader đọc resources.
- Day 3 cung cấp market plan logic và researcher capabilities như search/fetch/memory để `Trader` class tái sử dụng.
- Lesson này là endpoint tự nhiên của nguyên tắc “prototype in lab, then package into module” được nhấn mạnh ở lesson 125.

## 5. Core Theory - Lý thuyết cốt lõi

### AsyncExitStack - bộ gom context manager bất đồng bộ
- Term - thuật ngữ: AsyncExitStack - bộ gom context manager bất đồng bộ
- Meaning - nghĩa: Một kỹ thuật Python cho phép mở động nhiều async context managers trong một stack - ngăn xếp thay vì viết `async with` lồng nhau rất sâu.
- Why it matters - vì sao quan trọng: Hệ thống nhiều MCP servers sẽ nhanh chóng trở nên khó đọc nếu lồng `async with` thủ công.
- Relationship - liên hệ với khái niệm khác: Nó giải quyết complexity - độ phức tạp hạ tầng, không đổi logic agent.

### Trader class - lớp trader điều phối nghiệp vụ
- Term - thuật ngữ: Trader class - lớp trader điều phối nghiệp vụ
- Meaning - nghĩa: Một abstraction bọc toàn bộ logic tạo agent, đọc state, chọn message mode, chạy trace, và lật trạng thái trade/rebalance.
- Why it matters - vì sao quan trọng: Cho phép trading floor tạo nhiều trader độc lập theo tên và model.
- Relationship - liên hệ với khái niệm khác: Nó dùng `mcp_params.py`, `templates.py`, và `accounts_client.py` như dependency modules.

### Rebalance mode - chế độ tái cân bằng danh mục
- Term - thuật ngữ: Rebalance mode - chế độ tái cân bằng danh mục
- Meaning - nghĩa: Thay vì chỉ tìm cơ hội mua mới, trader có thể xem lại danh mục hiện có và điều chỉnh tỷ trọng.
- Why it matters - vì sao quan trọng: Nó làm trader gần với portfolio management - quản trị danh mục hơn là chỉ “đánh lệnh”.
- Relationship - liên hệ với khái niệm khác: `rebalance_message(...)` là prompt counterpart - prompt đối ứng của mode này trong `templates.py`.

### Multi-model abstraction - lớp trừu tượng đa mô hình
- Term - thuật ngữ: Multi-model abstraction - lớp trừu tượng đa mô hình
- Meaning - nghĩa: Một hàm như `get_model()` chọn provider/model backend dựa trên tên model.
- Why it matters - vì sao quan trọng: Logic agent không bị khóa vào một nhà cung cấp duy nhất.
- Relationship - liên hệ với khái niệm khác: Nó mở đường cho Day 5 và các mở rộng sau này mà không phải thay đổi `Trader` workflow.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - `Trader(name, model_name)`
   - MCP server params cho trader và researcher
   - Account state và strategy từ resources
2. Processing steps:
   - `get_researcher_tool(...)` tạo researcher tool.
   - `create_agent(...)` tạo trader agent.
   - `get_account_report()` đọc account report và bỏ bớt `portfolio_value_time_series`.
   - Chọn `trade_message(...)` hoặc `rebalance_message(...)` theo `do_trade`.
   - Mở trader và researcher MCP servers bằng `AsyncExitStack`.
   - Chạy `Runner.run(...)` trong `trace(...)`.
   - Lật `do_trade` cho lần chạy tiếp theo.
3. Output:
   - Trader appraisal - nhận định ngắn của trader.
   - Trade actions và push notification.
4. Control flow / data flow:
   - Trader class -> researcher tool -> search/fetch/memory -> trader tools/resources -> market/account/push -> trace logs.
5. Decision points:
   - Chọn model provider nào.
   - Chọn trade hay rebalance cho lượt hiện tại.
   - Chọn plan market data nào trong `mcp_params.py`.

## 7. Techniques - Kỹ thuật sử dụng

### Dynamic server lifecycle management - quản lý vòng đời server động
- Technique - kỹ thuật: Dynamic server lifecycle management - quản lý vòng đời server động
- Purpose - mục đích: Mở và đóng tập MCP servers theo từng run mà không làm code lồng quá sâu.
- When to use - dùng khi nào: Khi agent cần nhiều server và server list có thể thay đổi theo cấu hình.
- Trade-off - đánh đổi: Khó đọc hơn với người mới thấy `AsyncExitStack`, nhưng clean hơn nhiều về cấu trúc tổng thể.
- Common mistake - lỗi dễ gặp: Né kỹ thuật này nhưng đổi lại viết hàng loạt `async with` lồng nhau khó bảo trì.

### Stateful agent mode switching - chuyển mode có state
- Technique - kỹ thuật: Stateful agent mode switching - chuyển mode có state
- Purpose - mục đích: Cho cùng một trader luân phiên giữa tìm cơ hội mới và tái cân bằng danh mục.
- When to use - dùng khi nào: Khi hành vi agent có nhịp lặp hoặc chu kỳ qua nhiều runs.
- Trade-off - đánh đổi: Phải giữ state đơn giản giữa các lần chạy.
- Common mistake - lỗi dễ gặp: Chỉ chạy một mode duy nhất khiến trader thiếu chiều sâu quản lý danh mục.

### Thin orchestration class - lớp điều phối mỏng
- Technique - kỹ thuật: Thin orchestration class - lớp điều phối mỏng
- Purpose - mục đích: Để class chủ yếu lo wiring và flow, còn prompts/resources/server manifests nằm ở module riêng.
- When to use - dùng khi nào: Khi project chuyển từ notebook sang package/module hóa.
- Trade-off - đánh đổi: Cần discipline trong module boundaries nhưng đổi lại rất dễ mở rộng.
- Common mistake - lỗi dễ gặp: Nhét lại prompt text và config vào class, phá vỡ separation of concerns.

## 8. Code Walkthrough - Phân tích code nếu có

### File / block: `traders.py` phần `get_model(model_name)`
- Purpose - mục đích: Cho phép cùng một orchestration logic chạy trên nhiều model providers.
- Key logic - logic chính:
  - Nếu tên model có `/` thì dùng OpenRouter.
  - Nếu chứa `deepseek`, `grok`, `gemini` thì dùng client tương ứng.
  - Nếu không, trả về tên model mặc định cho OpenAI path.
- Important lines / functions:
  - `def get_model(model_name: str)`
  - Các `AsyncOpenAI(base_url=..., api_key=...)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là lớp compatibility - tương thích khá gọn: thay backend nhưng giữ nguyên `Agent(...)`.

### File / block: `traders.py` phần `get_researcher()` và `get_researcher_tool()`
- Purpose - mục đích: Tạo researcher agent và chuyển nó thành tool cho trader.
- Key logic - logic chính:
  - Researcher dùng `researcher_instructions()` từ `templates.py`.
  - `get_researcher_tool()` gọi `researcher.as_tool(...)`.
- Important lines / functions:
  - `async def get_researcher(...)`
  - `async def get_researcher_tool(...)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Nó đóng gói đúng pattern đã thử trong notebook, không phát minh thêm abstraction không cần thiết.

### File / block: `traders.py` phần `Trader.create_agent()` và `run_agent()`
- Purpose - mục đích: Tạo trader agent thật, lấy account/strategy, và chọn message mode để chạy.
- Key logic - logic chính:
  - `create_agent()` xây agent với researcher tool và trader MCP servers.
  - `get_account_report()` loại bỏ `portfolio_value_time_series` để prompt gọn hơn.
  - `run_agent()` chọn `trade_message(...)` hoặc `rebalance_message(...)`.
- Important lines / functions:
  - `self.agent = Agent(...)`
  - `account_json.pop("portfolio_value_time_series", None)`
  - `await Runner.run(self.agent, message, max_turns=MAX_TURNS)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Bỏ `portfolio_value_time_series` là quyết định prompt hygiene - vệ sinh prompt: giữ context hữu ích, bỏ dữ liệu cồng kềnh.

### File / block: `traders.py` phần `run_with_mcp_servers()` và `run_with_trace()`
- Purpose - mục đích: Mở tập servers bằng `AsyncExitStack`, chạy agent trong trace, và quản lý lifecycle gọn gàng.
- Key logic - logic chính:
  - Tạo list `trader_mcp_servers` từ `trader_mcp_server_params`.
  - Tạo list `researcher_mcp_servers` từ `researcher_mcp_server_params(self.name)`.
  - Bọc run trong `trace(...)` với `trace_id` từ helper.
- Important lines / functions:
  - `async with AsyncExitStack() as stack:`
  - `await stack.enter_async_context(MCPServerStdio(...))`
  - `with trace(trace_name, trace_id=trace_id):`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là phần transcript gọi là “fancy Python”, nhưng thực chất chỉ là một cách gọn hơn để quản lý nhiều context managers.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Nested `async with` thủ công
- Option: Manual nesting
- Pros: Dễ hiểu với người mới học.
- Cons: Rất dài và xấu khi số server tăng.
- When to choose: Khi chỉ có 1-2 servers hoặc khi đang dạy người mới về lifecycle cơ bản.

### Option 2: `AsyncExitStack`
- Option: Dynamic async context stack
- Pros: Scale tốt hơn với nhiều servers, code sạch hơn, dễ tạo list động.
- Cons: Khó hiểu hơn lúc đầu.
- When to choose: Khi hệ thống MCP đã đủ lớn như Day 4 trading floor.

### Option 3: Gộp toàn bộ vào notebook, không class hóa
- Option: Stay in notebook only
- Pros: Nhanh cho thử nghiệm.
- Cons: Khó tái sử dụng, khó tạo nhiều traders, khó mở rộng lên app/UI.
- When to choose: Chỉ cho giai đoạn prototype sớm trước khi logic tương đối ổn.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Đưa toàn bộ account JSON, kể cả time series lớn, vào prompt
  - Root cause: Không tối giản context trước khi gửi cho LLM.
  - Symptom: Prompt dài, tốn token, nhiễu quyết định.
  - Fix / prevention: Lọc bớt các trường không cần cho decision hiện tại như `portfolio_value_time_series`.

- Failure mode: Để orchestration class phình to
  - Root cause: Kéo lại config và prompts vào cùng một file.
  - Symptom: `traders.py` khó đọc, khó bảo trì, khó test.
  - Fix / prevention: Giữ `mcp_params.py` và `templates.py` làm dependency rõ vai.

- Failure mode: Cho rằng push error đồng nghĩa hệ thống hỏng hoàn toàn
  - Root cause: Không đối chiếu side effect thực tế với error reporting.
  - Symptom: Đánh giá sai mức độ nghiêm trọng của lỗi.
  - Fix / prevention: So sánh trace, output, và side effect thật; ở đây notification vẫn được gửi nên lỗi có thể nằm ở return handling hoặc tracing layer.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có nguyên văn trong buổi học.

- `AsyncExitStack` rất hữu ích trong bất kỳ hệ thống plugin/tool runtime nào, không riêng MCP, khi số tài nguyên cần mở là động.
- Multi-model support thường đáng giá nhất khi orchestration logic đã đủ ổn định; nếu chưa, đổi model quá sớm có thể che mất vấn đề prompt/tool design.
- Việc luân phiên trade/rebalance là một bước đầu của cyclic agent workflows - workflow vòng lặp, nơi mỗi lượt chạy có mục tiêu hơi khác nhau nhưng vẫn dùng chung agent identity.

## 12. Study Pack - Gói ôn tập
### Must remember
- `traders.py` là bước module hóa cuối của Day 4.
- `AsyncExitStack` giúp quản lý nhiều MCP servers sạch hơn nested `async with`.
- `Trader` class đọc account, chọn trade/rebalance mode, rồi chạy trong trace.
- `get_model()` mở đường cho multi-provider execution mà không đổi orchestration lõi.
- Hệ thống Day 4 sau module hóa dùng tổng cộng 6 MCP servers và 44 tools theo transcript.

### Self-check questions
- Vì sao `AsyncExitStack` phù hợp với Day 4 hơn nested `async with`?
- Vì sao `Trader` class nên giữ orchestration mỏng thay vì ôm cả prompt/config?
- Vì sao loại bỏ `portfolio_value_time_series` trước khi đưa vào prompt?
- `do_trade` giúp hệ thống có hành vi gì?
- Multi-model support mang lại lợi ích gì và rủi ro gì?

### Flashcards
- Q: `Trader.run()` làm gì sau khi chạy xong một lượt?
  A: Nó lật `self.do_trade = not self.do_trade` để lần sau chuyển giữa trade và rebalance.

- Q: `AsyncExitStack` giải quyết vấn đề gì?
  A: Quản lý nhiều `MCPServerStdio` async context managers gọn hơn khi số server lớn.

- Q: Vì sao `get_account_report()` bỏ `portfolio_value_time_series`?
  A: Để giảm prompt noise - nhiễu prompt và chỉ giữ state hữu ích cho quyết định hiện tại.

### Interview Q&A nếu phù hợp
- Q: Bạn sẽ mô tả thiết kế `Trader` class của Day 4 như thế nào dưới góc nhìn software engineering?
  A: Đây là một orchestration class tương đối mỏng: nó không chứa business logic market, không chứa prompt text thô, và cũng không tự định nghĩa server manifests. Thay vào đó nó phối hợp các dependency modules để tạo agent, nạp state, chọn mode hoạt động, quản lý lifecycle của MCP servers, và chạy trace. Thiết kế này giúp project đi từ notebook prototype sang reusable component mà vẫn giữ được modular boundaries rõ ràng.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Không có toàn bộ app/UI Day 5 trong phạm vi Day 4, nên trading floor ở đây mới dừng ở lớp module/orchestration chứ chưa phải giao diện hoàn chỉnh
- Không có trace screenshot hoặc log output đầy đủ của push error, nên phần phân tích lỗi push được giữ ở mức đúng như transcript mô tả
