# 115. Day 2 - Intro to Week 6 Day 2 - Building Your Own MCP Server

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `115. Day 2 - Intro to Week 6 Day 2 - Building Your Own MCP Server.txt`
- Slide: không có
- Code: Code được cung cấp trong session (`2_lab2.ipynb`, `accounts.py`, `accounts_server.py`, `accounts_client.py`) nhưng chưa thấy code liên quan trực tiếp tới lesson mở đầu này; `1_lab1.ipynb` được dùng như previous context vì được gửi nhầm vào session Day 2
- Summary lịch sử: đã dùng — `day1_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript rõ ràng, không có mâu thuẫn. Bài này chủ yếu định vị khi nào nên và không nên tự viết MCP server.

## 2. Executive Summary - Tóm tắt cốt lõi
- Bài học mở Day 2 bằng việc chuyển trọng tâm từ “dùng MCP server của người khác” sang “tự xây MCP server và MCP client”.
- Giá trị chính của việc tự viết MCP server là để chia sẻ tool (công cụ), resource (tài nguyên), hoặc prompt cho agent của người khác dùng lại.
- Nếu tool chỉ để chính bạn dùng trong agent của mình, MCP thường là overkill (quá tay); dùng `@function_tool` hoặc tool JSON trực tiếp đơn giản hơn nhiều.
- MCP không làm việc “tạo tool riêng” dễ hơn; nó thêm plumbing (đường ống tích hợp) như process riêng, transport, description, packaging.
- Việc tự viết MCP server vẫn đáng học vì nó giúp hiểu rõ plumbing (cơ chế vận hành bên dưới) của Host, Client, Server.
- Bài học cũng nhắc lại 3 kiểu triển khai MCP: local server thuần local, local server gọi remote service, và hosted/managed remote MCP server.
- Python và JavaScript là hai lựa chọn phổ biến để viết MCP server; cách gọi thường gặp là `uvx`/`uv run` cho Python và `npx` cho JavaScript.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu tại sao lại muốn tự xây MCP server thay vì chỉ dùng MCP server có sẵn.
  - Phân biệt rõ use case (trường hợp sử dụng) phù hợp của MCP server với use case chỉ cần function tool nội bộ.
  - Củng cố lại kiến trúc Host - Client - Server và các mô hình transport trong MCP.
- Practical goals - mục tiêu thực hành:
  - Chuẩn bị tư duy để bước sang các bài code trực tiếp ở lesson 116 và 117.
  - Biết tiêu chí ra quyết định trước khi bọc business logic vào MCP server.
- What learner should be able to explain - người học cần giải thích được:
  - Khi nào MCP server có giá trị thực sự.
  - Tại sao MCP không phải lựa chọn mặc định cho mọi tool bạn viết.
  - Tại sao bài học vẫn yêu cầu tự viết MCP server dù OpenAI Agents SDK đã hỗ trợ dùng MCP khá tiện.

## 4. Previous Context - Liên hệ với bài trước
- Day 1 đã xây nền tảng về MCP là protocol (giao thức), không phải framework, và đã giới thiệu Host, Client, Server cùng transport Stdio/SSE.
- `day1_summary.md` cho thấy Day 1 tập trung vào dùng MCP server bên ngoài như fetch, Playwright, file system, rồi gắn chúng vào OpenAI Agents SDK.
- `1_lab1.ipynb` được dùng như previous context để nối mạch: Day 1 dạy “consumer mindset” — cách dùng MCP server sẵn có; Day 2 chuyển sang “producer mindset” — cách đóng gói logic của mình thành MCP server.
- Bài 115 là cầu nối tư duy giữa hai ngày: từ ecosystem consumption (tiêu thụ hệ sinh thái) sang tool sharing (chia sẻ công cụ).

## 5. Core Theory - Lý thuyết cốt lõi

### MCP server as packaging layer - MCP server như lớp đóng gói
- Term - thuật ngữ: MCP server as packaging layer - MCP server như lớp đóng gói
- Meaning - nghĩa: MCP server là lớp bọc quanh business logic hiện có, giúp logic đó được công bố ra ngoài dưới dạng tool/resource/prompt chuẩn hóa.
- Why it matters - vì sao quan trọng: Nó biến code nội bộ thành thứ có thể tái sử dụng bởi agent hoặc developer khác mà không cần hiểu chi tiết implementation bên trong.
- Relationship - liên hệ với khái niệm khác: Liên hệ trực tiếp với lesson 116, nơi `accounts_server.py` bọc business logic trong `accounts.py`.

### Shareability - khả năng chia sẻ
- Term - thuật ngữ: Shareability - khả năng chia sẻ
- Meaning - nghĩa: Lợi ích số một của MCP là làm cho tool của bạn dễ chia sẻ và dễ tích hợp bởi người khác.
- Why it matters - vì sao quan trọng: Nếu không có nhu cầu chia sẻ, MCP thường chỉ thêm overhead (chi phí tích hợp) mà không tăng giá trị thực dụng.
- Relationship - liên hệ với khái niệm khác: Đây là tiêu chí chính để chọn giữa MCP server và `@function_tool`.

### Internal tool vs shared tool - tool nội bộ vs tool chia sẻ
- Term - thuật ngữ: Internal tool vs shared tool - công cụ nội bộ vs công cụ chia sẻ
- Meaning - nghĩa: Internal tool chỉ phục vụ agent/app của riêng bạn; shared tool được đóng gói để agent khác gọi qua giao thức chung.
- Why it matters - vì sao quan trọng: Nó quyết định mức độ plumbing bạn có nên chấp nhận.
- Relationship - liên hệ với khái niệm khác: Gắn với decision point (điểm quyết định) quan trọng nhất của Day 2.

### Extra plumbing - phần tích hợp bổ sung
- Term - thuật ngữ: Extra plumbing - phần tích hợp bổ sung
- Meaning - nghĩa: Khi dùng MCP, bạn phải chấp nhận thêm process riêng, transport, session/client setup, mô tả tool/resource, và lifecycle quản lý server.
- Why it matters - vì sao quan trọng: Đây là “giá phải trả” để đổi lấy chuẩn hóa và shareability.
- Relationship - liên hệ với khái niệm khác: Được thấy rõ ở lesson 117 khi viết client hoặc dùng `MCPServerStdio`.

### Resource - tài nguyên truy cập qua URI
- Term - thuật ngữ: Resource - tài nguyên
- Meaning - nghĩa: Một kiểu primitive của MCP ngoài tools, thường dùng để trả context hoặc dữ liệu có thể đọc theo URI pattern.
- Why it matters - vì sao quan trọng: Bài 115 báo trước rằng Day 2 sẽ không chỉ có tools mà còn đụng nhẹ tới resources.
- Relationship - liên hệ với khái niệm khác: Sẽ xuất hiện trực tiếp trong `accounts_server.py` và `accounts_client.py`.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Khong co pipeline ro rang trong tai lieu nguon.

Luồng tư duy của bài học:
1. Nhắc lại mô hình Host - Client - Server và các kiểu triển khai MCP từ Day 1.
2. Đặt câu hỏi “tại sao phải tự viết MCP server?” thay vì đi vào code ngay.
3. Khẳng định lợi ích chính là shareability (chia sẻ được cho người khác) và nhất quán đóng gói.
4. Đưa phản biện quan trọng: nếu chỉ dùng nội bộ, MCP là overhead không cần thiết.
5. Kết luận rằng việc tự viết MCP server vẫn đáng học để hiểu plumbing và chuẩn bị cho các bài code tiếp theo.

## 7. Techniques - Kỹ thuật sử dụng

### Problem framing before implementation - đóng khung bài toán trước khi code
- Technique - kỹ thuật: Problem framing before implementation - đóng khung bài toán trước khi code
- Purpose - mục đích: Quyết định xem nhu cầu là “share tool” hay chỉ “call local function”.
- When to use - dùng khi nào: Dùng trước khi bạn bọc bất kỳ business logic nào thành MCP server.
- Trade-off - đánh đổi: Tốn thêm thời gian suy nghĩ ban đầu nhưng tránh overengineering (thiết kế quá mức).
- Common mistake - lỗi dễ gặp: Hễ học MCP là biến mọi function thành MCP server.

### Consistency by protocol - nhất quán hóa bằng giao thức
- Technique - kỹ thuật: Consistency by protocol - nhất quán hóa bằng giao thức
- Purpose - mục đích: Đóng gói tool của mình cùng kiểu với các MCP server khác để hệ thống agent có cách gắn tool đồng nhất.
- When to use - dùng khi nào: Khi một hệ thống muốn tất cả capability (năng lực) đều đi qua cùng một abstraction layer (lớp trừu tượng).
- Trade-off - đánh đổi: Kiến trúc thống nhất hơn nhưng phức tạp hơn so với gọi function trực tiếp.
- Common mistake - lỗi dễ gặp: Nhầm “nhất quán kỹ thuật” với “luôn là lựa chọn tốt nhất”.

### Learning by rebuilding plumbing - học bằng cách tự dựng plumbing
- Technique - kỹ thuật: Learning by rebuilding plumbing - học bằng cách tự dựng plumbing
- Purpose - mục đích: Hiểu tận gốc lifecycle (vòng đời) của server, client, transport và mapping tool.
- When to use - dùng khi nào: Khi học hệ sinh thái MCP, debug integration, hoặc cần custom client/resource behavior.
- Trade-off - đánh đổi: Tốn công hơn nhiều so với chỉ dùng tính năng built-in của SDK.
- Common mistake - lỗi dễ gặp: Biến bài học plumbing thành production pattern bắt buộc cho mọi dự án.

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này. Bài 115 là bài định hướng lý thuyết, giải thích tiêu chí “khi nào nên tự viết MCP server” trước khi đi vào code ở các lesson sau.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Dùng `@function_tool` hoặc tool JSON trực tiếp
- Option: Dùng function tool nội bộ
- Pros: Đơn giản, ít plumbing, chạy ngay trong Python process hiện tại, dễ debug.
- Cons: Khó chia sẻ cho người khác dưới dạng chuẩn hóa như MCP.
- When to choose: Khi tool chỉ phục vụ agent của riêng bạn và không cần công bố ra ecosystem.

### Option 2: Đóng gói thành MCP server
- Option: Viết MCP server riêng
- Pros: Dễ chia sẻ, mô tả tool/resource chuẩn hóa, dùng được với nhiều host/client khác nhau.
- Cons: Cần process riêng, transport, cấu hình spawn, thêm boilerplate.
- When to choose: Khi muốn tool của mình trở thành capability dùng lại được bởi người khác hoặc bởi nhiều ứng dụng.

### Option 3: Đóng gói vì mục tiêu học tập/kiến trúc
- Option: Viết MCP server để hiểu internals hoặc để thống nhất kiến trúc
- Pros: Hiểu rõ plumbing, dễ chuẩn hóa một hệ thống đa tool.
- Cons: Có thể thừa nếu mục tiêu chỉ là ship nhanh một feature nhỏ.
- When to choose: Khi học MCP sâu, debug protocol, hoặc có chủ đích kiến trúc rõ ràng.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Bọc mọi function thành MCP server
  - Root cause: Hype quanh MCP khiến người học tưởng MCP luôn là lựa chọn tốt nhất.
  - Symptom: Nhiều file cấu hình/plumbing hơn business logic thực tế.
  - Fix / prevention: Hỏi trước “tool này có cần chia sẻ hoặc chuẩn hóa như MCP không?”.

- Failure mode: Nhầm MCP giúp tạo tool dễ hơn
  - Root cause: Không tách biệt giữa “công bố tool” và “thực thi tool”.
  - Symptom: Viết nhiều boilerplate chỉ để gọi một hàm nội bộ.
  - Fix / prevention: Với tool cá nhân, ưu tiên function tool hoặc JSON tool call.

- Failure mode: Học MCP mà bỏ qua logic nền
  - Root cause: Chú ý vào transport/protocol nhiều hơn business logic.
  - Symptom: MCP server có hình thức đúng nhưng tool bên trong nghèo nàn hoặc không hữu ích.
  - Fix / prevention: Xem MCP như lớp bọc; giá trị thật vẫn nằm ở business logic.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có nguyên văn trong buổi học.

- Trong thực tế, nhiều team dùng hybrid approach (cách tiếp cận lai): tool nội bộ quan trọng thì để local function, còn tool muốn chia sẻ hoặc plug-and-play thì đóng gói bằng MCP.
- Về vận hành, MCP server giúp tách process nên có thể cô lập dependency (phụ thuộc) tốt hơn, nhưng đổi lại tăng chi phí setup và quan sát lỗi liên tiến trình.
- Nếu system về sau có nhiều host khác nhau như IDE assistant, desktop app, backend agent, MCP trở nên hấp dẫn hơn vì cùng một server có thể phục vụ nhiều nơi.

## 12. Study Pack - Gói ôn tập
### Must remember
- MCP server có giá trị lớn nhất khi bạn muốn chia sẻ tool/resource/prompt.
- Nếu chỉ dùng nội bộ, `@function_tool` thường hợp lý hơn MCP.
- MCP thêm plumbing chứ không làm business logic tốt hơn.
- Day 2 chuyển từ “dùng MCP” sang “tự tạo MCP”.
- Viết MCP server vẫn là bài học tốt để hiểu Host - Client - Server sâu hơn.

### Self-check questions
- Lý do số một để tự viết MCP server là gì?
- Khi nào `@function_tool` tốt hơn MCP server?
- MCP có giúp bạn tạo business logic dễ hơn không?
- “Extra plumbing” trong MCP gồm những phần nào?
- Vì sao bài học vẫn yêu cầu viết MCP server dù SDK đã hỗ trợ nhiều thứ sẵn?

### Flashcards
- Q: Khi nào nên viết MCP server?
  A: Khi cần chia sẻ tool/resource/prompt cho agent hoặc developer khác, hoặc khi có lý do kiến trúc/học tập rõ ràng.

- Q: Khi nào không nên viết MCP server?
  A: Khi tool chỉ dùng nội bộ cho agent của chính bạn và không cần shareability.

- Q: MCP thêm gì vào hệ thống?
  A: Thêm process riêng, transport, session/client setup, metadata mô tả tool/resource, và lifecycle quản lý server.

### Interview Q&A nếu phù hợp
- Q: Hãy giải thích khi nào một team nên chọn MCP server thay vì local function tools.
  A: Team nên chọn MCP server khi muốn chuẩn hóa cách công bố capability, chia sẻ tool cho nhiều host/client, hoặc tái sử dụng cùng một capability across applications. Nếu tool chỉ phục vụ một agent nội bộ, local function tools gọn hơn, ít plumbing hơn và thường là lựa chọn đúng.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Transcript chỉ là bài mở đầu, không có demo code riêng cho lesson này
- Không thiếu ngữ cảnh nghiêm trọng vì `day1_summary.md` và `1_lab1.ipynb` đã đủ để nối mạch Day 1 sang Day 2

---

# 116. Day 2 - Wiring Business Logic into Your MCP Server

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `116. Day 2 - Wiring Business Logic into Your MCP Server.txt`
- Slide: không có
- Code: đã dùng — `2_lab2.ipynb`, `accounts.py`, `accounts_server.py`, `database.py`
- Summary lịch sử: đã dùng — `day1_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript khớp tốt với notebook và module Python. Đã đọc thêm `database.py` theo hybrid discovery vì transcript nói instructor đã tách persistence (lưu trữ) ra module riêng dùng SQLite.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson 116 lấy business logic quản lý tài khoản/chứng khoán có sẵn trong `accounts.py` và bọc nó thành MCP server bằng `FastMCP`.
- Business logic này không phải code “toy” riêng cho bài học, mà là code tái sử dụng từ project agent trước đó, nay được dùng lại như một domain service.
- `Account.get()` đọc trạng thái tài khoản từ SQLite thông qua `database.py`, giúp tool MCP làm việc với dữ liệu có persistence (lưu trữ bền vững).
- Trong `accounts_server.py`, mỗi capability quan trọng được expose (công bố) bằng `@mcp.tool()` như `get_balance`, `get_holdings`, `buy_shares`, `sell_shares`, `change_strategy`.
- Lesson cũng cho thấy MCP không chỉ có tools; có thể expose resource bằng URI như `accounts://accounts_server/{name}` và `accounts://strategy/{name}`.
- Điểm chốt của file server là `mcp.run(transport='stdio')`, biến module Python thành một MCP server local có thể được spawn bởi client/host.
- Bài học nhấn mạnh rằng phần khó không nằm ở `FastMCP` API, mà nằm ở việc bạn đã có business logic đáng để bọc và chia sẻ hay chưa.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách business logic có sẵn được biến thành MCP tools và resources.
  - Hiểu vai trò của `FastMCP` như lớp server wrapper (lớp bọc máy chủ).
  - Hiểu quan hệ giữa logic domain, persistence, và giao thức MCP.
- Practical goals - mục tiêu thực hành:
  - Biết cấu trúc tối thiểu của một MCP server Python chạy qua Stdio.
  - Biết cách viết tool wrappers có docstring để mô tả input/output cho client và LLM.
  - Biết cách công bố resources bằng URI pattern.
- What learner should be able to explain - người học cần giải thích được:
  - `accounts_server.py` đang bọc `accounts.py` như thế nào.
  - Vì sao `database.py` cần thiết để business logic có state lâu dài.
  - Sự khác nhau giữa một MCP tool và một MCP resource trong ví dụ này.

## 4. Previous Context - Liên hệ với bài trước
- Day 1 đã cho thấy agent có thể dùng các MCP server có sẵn như fetch và filesystem. Lesson 116 đảo chiều: giờ người học trở thành người viết server.
- Lesson 115 vừa nhấn mạnh rằng MCP đáng dùng khi muốn chia sẻ logic; lesson 116 chính là triển khai cụ thể luận điểm đó.
- `day1_summary.md` cũng đã giới thiệu resources là primitive ít phổ biến hơn tools; lesson này là lần đầu có ví dụ code cụ thể về resources.
- Project accounts liên hệ với các tuần trước của khóa: transcript nói rõ đây là code từ team engineering ở week 3, nay được tái sử dụng trong tuần MCP.

## 5. Core Theory - Lý thuyết cốt lõi

### Business logic wrapping - bọc logic nghiệp vụ
- Term - thuật ngữ: Business logic wrapping - bọc logic nghiệp vụ
- Meaning - nghĩa: Dùng một MCP layer để expose các hành vi nghiệp vụ hiện có mà không phải viết lại logic lõi.
- Why it matters - vì sao quan trọng: Đây là con đường thực tế nhất để tạo MCP server hữu ích; bạn không bắt đầu từ protocol mà bắt đầu từ logic domain.
- Relationship - liên hệ với khái niệm khác: `accounts_server.py` gọi trực tiếp `Account.get(...).method(...)`.

### FastMCP - server scaffold của Python MCP
- Term - thuật ngữ: FastMCP - bộ khung server MCP nhanh
- Meaning - nghĩa: Một abstraction (lớp trừu tượng) từ thư viện MCP Python, giúp khai báo server, tools, resources bằng decorator.
- Why it matters - vì sao quan trọng: Nó giảm boilerplate, cho phép tập trung vào mô tả và nối business logic.
- Relationship - liên hệ với khái niệm khác: Đóng vai trò tương tự một mini-framework dành cho việc xuất bản MCP server.

### Tool decorator - decorator công bố tool
- Term - thuật ngữ: `@mcp.tool()` decorator - decorator công bố tool
- Meaning - nghĩa: Đánh dấu một hàm là MCP tool để client có thể discover (khám phá) và gọi nó.
- Why it matters - vì sao quan trọng: Đây là điểm nối giữa function Python và protocol-level tool.
- Relationship - liên hệ với khái niệm khác: Khái niệm tương tự `@function_tool`, nhưng ở đây tool nằm trong process server riêng.

### Resource URI - định danh tài nguyên bằng URI
- Term - thuật ngữ: Resource URI - URI tài nguyên
- Meaning - nghĩa: Một pattern URI như `accounts://accounts_server/{name}` để client đọc dữ liệu contextualized (theo ngữ cảnh) thay vì gọi action tool.
- Why it matters - vì sao quan trọng: Resources mở rộng MCP vượt ra ngoài thao tác kiểu RPC (remote procedure call).
- Relationship - liên hệ với khái niệm khác: Lesson 117 sẽ cho thấy dùng client tự viết để đọc resource.

### Persistence layer - lớp lưu trữ bền vững
- Term - thuật ngữ: Persistence layer - lớp lưu trữ bền vững
- Meaning - nghĩa: Cơ chế lưu account và logs xuống SQLite trong `database.py`.
- Why it matters - vì sao quan trọng: Nếu không có persistence, tool chỉ thao tác state tạm thời trong memory.
- Relationship - liên hệ với khái niệm khác: `Account.get()` đọc từ database; `save()` và `write_log()` ghi lại thay đổi.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - Tên tài khoản, mã cổ phiếu, số lượng, chiến lược, hoặc yêu cầu đọc report/strategy.
2. Processing steps:
   - Business logic trong `accounts.py` đọc account từ SQLite qua `database.py`.
   - `accounts_server.py` khai báo tool/resource wrappers bằng `FastMCP`.
   - Khi server được spawn, các wrapper này được expose như MCP capabilities.
3. Output:
   - Tool trả về balance, holdings, hoặc chuỗi report/trạng thái cập nhật.
   - Resource trả về report hoặc strategy theo URI tương ứng.
4. Control flow / data flow:
   - MCP client/host spawn `accounts_server.py` bằng Stdio.
   - Tool call đi vào hàm decorated trong server.
   - Hàm server delegate (ủy quyền) cho `Account` methods.
   - `Account` đọc/ghi SQLite rồi trả kết quả ngược ra client.
5. Decision points:
   - Chọn expose logic nào dưới dạng tool và logic nào dưới dạng resource.
   - Chọn transport `stdio` cho local server.
   - Chọn mức abstraction: wrapper mỏng hay logic xử lý nằm ngay trong server.

## 7. Techniques - Kỹ thuật sử dụng

### Thin wrapper pattern - mẫu wrapper mỏng
- Technique - kỹ thuật: Thin wrapper pattern - mẫu wrapper mỏng
- Purpose - mục đích: Giữ MCP server chỉ làm nhiệm vụ công bố capability, còn business logic ở module riêng.
- When to use - dùng khi nào: Khi bạn đã có domain module tốt và không muốn protocol layer làm bẩn logic lõi.
- Trade-off - đánh đổi: Kiến trúc sạch hơn nhưng cần quản lý thêm module/persistence riêng.
- Common mistake - lỗi dễ gặp: Dồn hết logic vào file server cho nhanh, làm server trở nên khó test và khó tái sử dụng.

### Docstring-driven tool metadata - mô tả tool bằng docstring
- Technique - kỹ thuật: Docstring-driven tool metadata - mô tả tool bằng docstring
- Purpose - mục đích: Giúp tool có mô tả và ngữ nghĩa đầu vào rõ ràng cho client/LLM.
- When to use - dùng khi nào: Với mọi MCP tool có input parameters mà agent cần hiểu chính xác.
- Trade-off - đánh đổi: Tốn công viết mô tả kỹ hơn, đổi lại improve discoverability (khả năng khám phá) và tool selection (chọn tool).
- Common mistake - lỗi dễ gặp: Viết mô tả quá ngắn khiến LLM khó hiểu khi nào nên gọi tool.

### URI-based resource exposure - công bố tài nguyên qua URI
- Technique - kỹ thuật: URI-based resource exposure - công bố tài nguyên qua URI
- Purpose - mục đích: Cho phép đọc context theo pattern nhất quán thay vì chỉ gọi action functions.
- When to use - dùng khi nào: Khi dữ liệu phù hợp với mô hình “read-only contextual resource”.
- Trade-off - đánh đổi: Cần client hỗ trợ đọc resource; không phải SDK nào cũng đưa resources vào agent loop sẵn.
- Common mistake - lỗi dễ gặp: Dùng resource cho mọi thứ, kể cả tác vụ nên là tool có side effect (tác dụng phụ).

### Persistence-backed demo - demo có state lưu trữ
- Technique - kỹ thuật: Persistence-backed demo - demo có lưu trữ trạng thái
- Purpose - mục đích: Làm ví dụ thực tế hơn bằng cách giữ account state giữa các lần gọi.
- When to use - dùng khi nào: Khi muốn tool phản ánh hệ thống gần với production hơn toy in-memory demo.
- Trade-off - đánh đổi: Cần database setup và code lưu/đọc dữ liệu.
- Common mistake - lỗi dễ gặp: Bỏ qua persistence khiến demo khó thấy giá trị của “account management”.

## 8. Code Walkthrough - Phân tích code nếu có

### File / block: `2_lab2.ipynb` cells 2-6
- Purpose - mục đích: Xác nhận business logic `Account` đã tồn tại và có thể thao tác trực tiếp trước khi bọc bằng MCP.
- Key logic - logic chính:
  - `Account.get("Ed")` lấy account hiện có hoặc khởi tạo account mới.
  - `buy_shares(...)`, `report()`, `list_transactions()` cho thấy module `accounts.py` đã tự đứng vững như domain layer.
- Important lines / functions:
  - `from accounts import Account`
  - `account = Account.get("Ed")`
  - `account.buy_shares(...)`
  - `account.report()`
  - `account.list_transactions()`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Bước này rất quan trọng vì instructor không viết MCP server từ số 0; ông bắt đầu từ business logic đã chạy được.
  - Đây là pattern thực tế: validate domain logic trước, sau đó mới expose ra protocol.

### File / block: [accounts.py](G:\Agent2026Win\agents\6_mcp\accounts.py)
- Purpose - mục đích: Chứa business logic quản lý tài khoản, giao dịch mua/bán cổ phiếu, báo cáo và chiến lược đầu tư.
- Key logic - logic chính:
  - `Account.get()` đọc dữ liệu account từ SQLite qua `read_account`.
  - `buy_shares()` và `sell_shares()` kiểm tra điều kiện, cập nhật holdings, transactions, balance rồi lưu lại.
  - `report()` tổng hợp account state, thêm portfolio value (giá trị danh mục) và PnL, rồi trả JSON string.
- Important lines / functions:
  - `class Account(BaseModel)`
  - `@classmethod def get(cls, name: str)`
  - `def buy_shares(...)`
  - `def sell_shares(...)`
  - `def report(self) -> str`
  - `def change_strategy(self, strategy: str) -> str`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - `Account.get()` là điểm vào trung tâm: vừa load state, vừa tạo mặc định nếu account chưa tồn tại.
  - `report()` không chỉ “đọc”; nó còn append time series rồi save lại, nên đọc report cũng có side effect nhẹ.
  - Business logic tách biệt khỏi MCP nên cùng module này có thể được dùng trực tiếp hoặc qua server.

### File / block: [database.py](G:\Agent2026Win\agents\6_mcp\database.py)
- Purpose - mục đích: Cung cấp persistence layer bằng SQLite cho accounts, logs và market data.
- Key logic - logic chính:
  - Tạo các bảng `accounts`, `logs`, `market` nếu chưa tồn tại.
  - `write_account()` upsert JSON account state theo tên.
  - `read_account()` khôi phục account state từ database.
  - `write_log()` lưu audit-style entries (log kiểu nhật ký).
- Important lines / functions:
  - `DB = "accounts.db"`
  - `CREATE TABLE IF NOT EXISTS accounts`
  - `def write_account(...)`
  - `def read_account(...)`
  - `def write_log(...)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Instructor nói “rất vanilla” là chính xác: SQLite giúp demo đơn giản nhưng đủ thực tế.
  - Tầng này làm cho MCP tool có trạng thái bền vững qua nhiều lần gọi khác nhau.

### File / block: [accounts_server.py](G:\Agent2026Win\agents\6_mcp\accounts_server.py)
- Purpose - mục đích: Bọc business logic `Account` thành MCP server với tools và resources.
- Key logic - logic chính:
  - `mcp = FastMCP("accounts_server")` khởi tạo server.
  - Mỗi hàm `@mcp.tool()` delegate sang `Account.get(name)...`.
  - Hai `@mcp.resource(...)` công bố report và strategy theo URI.
  - `mcp.run(transport='stdio')` khởi chạy server local dùng Stdio.
- Important lines / functions:
  - `from mcp.server.fastmcp import FastMCP`
  - `mcp = FastMCP("accounts_server")`
  - `@mcp.tool() async def get_balance(...)`
  - `@mcp.tool() async def buy_shares(...)`
  - `@mcp.resource("accounts://accounts_server/{name}")`
  - `if __name__ == "__main__": mcp.run(transport='stdio')`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là thin wrapper đúng nghĩa: file server gần như không chứa nghiệp vụ mới.
  - Tools là hành động hoặc truy vấn callable; resources là điểm đọc dữ liệu theo URI.
  - `stdio` phù hợp vì đây là local MCP server được host spawn như process con.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Giữ business logic trong module riêng, server chỉ wrapper
- Option: Thin wrapper architecture
- Pros: Tách bạch trách nhiệm, dễ test business logic độc lập, dễ tái dùng ngoài MCP.
- Cons: Nhiều file hơn, cần hiểu data flow qua nhiều lớp.
- When to choose: Khi logic đủ lớn hoặc có khả năng tái sử dụng trong app khác.

### Option 2: Viết logic trực tiếp trong MCP server
- Option: All-in-one server file
- Pros: Nhanh để demo rất nhỏ.
- Cons: Protocol layer và business logic bị trộn, khó mở rộng, khó test.
- When to choose: Chỉ phù hợp với toy demo cực nhỏ.

### Option 3: Expose tool và resource song song
- Option: Mixed capability design
- Pros: Linh hoạt; tool cho hành động, resource cho ngữ cảnh đọc.
- Cons: Client/consumer phải hiểu hai cơ chế khác nhau.
- When to choose: Khi hệ thống có cả action-oriented behavior và contextual read access.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Nhồi business logic vào file MCP server
  - Root cause: Muốn làm nhanh, bỏ qua phân tách module.
  - Symptom: File server dài, khó đọc, khó kiểm thử độc lập.
  - Fix / prevention: Để server làm wrapper mỏng, giữ domain logic ở module riêng như `accounts.py`.

- Failure mode: Chỉ expose tools, bỏ qua use case của resources
  - Root cause: Nghĩ MCP chỉ là tool calling.
  - Symptom: Mọi hành vi kể cả đọc context đều bị ép thành tool calls.
  - Fix / prevention: Dùng resource cho dữ liệu ngữ cảnh đọc theo URI khi phù hợp.

- Failure mode: Demo không có persistence
  - Root cause: Chỉ dùng biến in-memory để đơn giản hóa.
  - Symptom: State mất sau mỗi lần chạy, khó thấy giá trị thực tế của account management.
  - Fix / prevention: Dùng persistence layer đơn giản như SQLite.

- Failure mode: Mô tả tool quá sơ sài
  - Root cause: Xem docstring là phụ.
  - Symptom: LLM khó chọn đúng tool hoặc dùng sai arguments.
  - Fix / prevention: Viết docstring rõ tên tham số, ý nghĩa và ngữ cảnh sử dụng.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- `FastMCP` thường tận dụng type hints và metadata của hàm Python để suy ra schema đầu vào tốt hơn, nên kiểu dữ liệu rõ ràng giúp improve tool interoperability (khả năng tương tác công cụ).
- Trong hệ thống production, persistence layer thường không dừng ở SQLite; nhưng việc giữ nó ở module riêng như `database.py` giúp thay backend dễ hơn mà không ảnh hưởng surface MCP.
- Pattern “domain module + MCP wrapper” cũng tương tự cách một backend app thường tách service layer khỏi API layer.

## 12. Study Pack - Gói ôn tập
### Must remember
- Hãy bắt đầu từ business logic có giá trị rồi mới bọc nó bằng MCP.
- `FastMCP` giúp công bố tool/resource bằng decorator.
- `accounts_server.py` là wrapper mỏng quanh `accounts.py`.
- `database.py` cung cấp persistence để account state sống lâu hơn một lần chạy.
- Resources trong ví dụ này dùng URI `accounts://...`.
- `mcp.run(transport='stdio')` là điểm biến module thành local MCP server.

### Self-check questions
- `FastMCP` đang giúp những gì trong `accounts_server.py`?
- Tại sao `accounts.py` nên tồn tại độc lập với `accounts_server.py`?
- `database.py` giải quyết vấn đề gì cho ví dụ này?
- Sự khác nhau giữa `@mcp.tool()` và `@mcp.resource(...)` trong lesson này là gì?
- Vì sao transport `stdio` là lựa chọn hợp lý cho demo hiện tại?

### Flashcards
- Q: Lớp nào chịu trách nhiệm persistence?
  A: `database.py` với SQLite, thông qua các hàm như `write_account()` và `read_account()`.

- Q: File nào biến business logic thành MCP capabilities?
  A: `accounts_server.py`.

- Q: `Account.get(name)` làm gì?
  A: Đọc account từ database; nếu chưa có thì tạo mặc định rồi lưu lại.

- Q: Resource URI chính của report account là gì?
  A: `accounts://accounts_server/{name}`.

### Interview Q&A nếu phù hợp
- Q: Nếu bạn có một module domain Python đã hoàn chỉnh, làm thế nào để biến nó thành MCP server sạch và dễ bảo trì?
  A: Hãy giữ domain logic trong module riêng, tạo một MCP wrapper mỏng bằng `FastMCP`, expose những thao tác cần thiết dưới dạng tools/resources, viết docstring rõ ràng cho schema/tool semantics, và để persistence hoặc external integration ở các module phụ trợ riêng. Cách này giúp protocol layer tách biệt khỏi domain layer, dễ test và dễ thay đổi hơn.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Không có screenshot hoặc output runtime của notebook cells, nhưng transcript và code đã đủ để tổng hợp chính xác
- Chưa cần scan rộng hơn trong `6_mcp` vì lesson này đã đủ ngữ cảnh từ các file trực tiếp liên quan

---

# 117. Day 2 - Creating Client Code to Use Your MCP Server

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `117. Day 2 - Creating Client Code to Use Your MCP Server.txt`
- Slide: không có
- Code: đã dùng — `2_lab2.ipynb`, `accounts_client.py`, `accounts_server.py`, `accounts.py`
- Summary lịch sử: đã dùng — `day1_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript, notebook và module khớp nhau. Bài này còn nêu rõ bối cảnh lịch sử: phần client thủ công từng cần thiết trước khi OpenAI Agents SDK hỗ trợ MCP trực tiếp.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson 117 cho thấy hai cách dùng MCP server vừa viết: cách hiện đại là đưa thẳng `MCPServerStdio` vào `Agent`, còn cách thủ công là tự viết MCP client trong `accounts_client.py`.
- Ở mức tối thiểu, SDK chỉ cần params như `{"command": "uv", "args": ["run", "accounts_server.py"]}` để spawn server rồi `list_tools()`.
- Khi agent nhận `mcp_servers=[mcp_server]`, OpenAI Agents SDK tự làm phần lớn plumbing client phía sau: tạo client, khởi tạo session, lấy tools, và cho LLM gọi chúng.
- `accounts_client.py` minh họa rõ plumbing bên dưới: `stdio_client`, `ClientSession.initialize()`, `list_tools()`, `call_tool()`, `read_resource()`.
- Lesson cũng chỉ ra một việc quan trọng: tool descriptions từ MCP không hoàn toàn giống OpenAI function tool schema, nên client thủ công phải map giữa hai định dạng.
- Resources không được tích hợp “free” vào agent flow như tools, nên client tự viết vẫn hữu ích khi bạn muốn đọc resource chủ động.
- Bài học kết thúc bằng exercise: tự viết MCP server đơn giản cho current date, và tùy chọn viết luôn MCP client để hiểu MCP ở mức bare metal (sát phần lõi).

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu sự khác nhau giữa “SDK-managed MCP usage” và “handwritten MCP client”.
  - Hiểu MCP client thực sự phải làm những gì: spawn server, initialize session, list tools, call tools, read resources.
  - Hiểu vai trò của schema mapping từ MCP tools sang OpenAI function tools.
- Practical goals - mục tiêu thực hành:
  - Biết cách dùng `MCPServerStdio` để list tools và gắn trực tiếp server vào agent.
  - Biết cấu trúc cơ bản của một MCP client Python viết tay.
  - Biết cách đọc resource qua client thủ công.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao ngày nay thường không cần tự viết MCP client nữa.
  - Trường hợp nào resource access vẫn khiến handwritten client hữu ích.
  - `accounts_client.py` đang bridge (bắc cầu) MCP world sang OpenAI tool world như thế nào.

## 4. Previous Context - Liên hệ với bài trước
- Lesson 116 đã tạo MCP server từ business logic. Lesson 117 là bước tiếp theo tự nhiên: tiêu thụ server đó.
- Day 1 từng dùng `MCPServerStdio` với fetch, Playwright và filesystem servers; lesson này áp dụng cùng pattern nhưng với server do chính ta viết.
- `day1_summary.md` cũng đã cho thấy OpenAI Agents SDK có thể aggregate tools từ MCP servers. Lesson 117 xác thực lại điều đó với server accounts.
- Lesson 115 nhấn mạnh MCP là về sharing. Lesson 117 minh họa phía consumer: người dùng server không cần biết chi tiết `accounts.py`.

## 5. Core Theory - Lý thuyết cốt lõi

### SDK-managed MCP client - client MCP do SDK quản lý
- Term - thuật ngữ: SDK-managed MCP client - client MCP do SDK quản lý
- Meaning - nghĩa: Khi dùng `MCPServerStdio` và truyền `mcp_servers=[...]` vào `Agent`, OpenAI Agents SDK tự xử lý phần lớn client plumbing.
- Why it matters - vì sao quan trọng: Đây là con đường hiện đại, đơn giản, ít mã hơn nhiều.
- Relationship - liên hệ với khái niệm khác: Đối lập với handwritten client trong `accounts_client.py`.

### Handwritten MCP client - client MCP viết tay
- Term - thuật ngữ: Handwritten MCP client - client MCP viết tay
- Meaning - nghĩa: Một module tự mở session tới server, liệt kê tools, gọi tools và đọc resources.
- Why it matters - vì sao quan trọng: Giúp hiểu cơ chế nền và vẫn hữu ích khi bạn cần kiểm soát sâu hơn.
- Relationship - liên hệ với khái niệm khác: `accounts_client.py` là ví dụ trực tiếp.

### Tool discovery - khám phá tool
- Term - thuật ngữ: Tool discovery - khám phá tool
- Meaning - nghĩa: Quá trình client hỏi server “bạn có những tool nào?” rồi lấy metadata của chúng.
- Why it matters - vì sao quan trọng: Không có tool discovery, LLM/agent không thể biết capability surface của server.
- Relationship - liên hệ với khái niệm khác: `session.list_tools()` là lời gọi trung tâm cho bước này.

### Schema translation - dịch schema
- Term - thuật ngữ: Schema translation - dịch schema
- Meaning - nghĩa: Chuyển metadata/tool schema từ định dạng MCP sang định dạng `FunctionTool` mà OpenAI Agents SDK cần.
- Why it matters - vì sao quan trọng: Cho thấy interoperability (khả năng tương tác) giữa hai abstraction layers không hoàn toàn “miễn phí”.
- Relationship - liên hệ với khái niệm khác: Hàm `get_accounts_tools_openai()` thực hiện nhiệm vụ này.

### Resource access - truy cập tài nguyên
- Term - thuật ngữ: Resource access - truy cập tài nguyên
- Meaning - nghĩa: Đọc dữ liệu công bố bởi server qua `read_resource(...)` thay vì tool call.
- Why it matters - vì sao quan trọng: Chứng minh MCP không chỉ là function calling; nó còn mang tính context distribution (phân phối ngữ cảnh).
- Relationship - liên hệ với khái niệm khác: `read_accounts_resource(name)` và `read_strategy_resource(name)` minh họa phần này.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động

### Luồng 1: Dùng OpenAI Agents SDK trực tiếp với MCP server
1. Input:
   - `params = {"command": "uv", "args": ["run", "accounts_server.py"]}`
   - Agent instructions và user request.
2. Processing steps:
   - `MCPServerStdio` spawn `accounts_server.py`.
   - SDK khởi tạo MCP client/session nội bộ.
   - SDK list tools từ server và cung cấp chúng cho agent loop.
   - LLM chọn tool phù hợp, SDK gọi tool qua MCP server.
3. Output:
   - Câu trả lời như balance/holdings của account.
4. Control flow / data flow:
   - User request -> Agent -> SDK-managed MCP client -> MCP server -> `accounts.py` -> result -> Agent response.
5. Decision points:
   - Chọn timeout session.
   - Chọn dùng `mcp_servers=[...]` thay vì tools thủ công.

### Luồng 2: Viết client thủ công
1. Input:
   - `StdioServerParameters` để spawn server.
   - Tên tool, args, hoặc resource name.
2. Processing steps:
   - `stdio_client(params)` mở streams.
   - `mcp.ClientSession(*streams)` tạo session.
   - `await session.initialize()`.
   - Tùy use case: `list_tools()`, `call_tool()`, hoặc `read_resource()`.
   - Nếu muốn dùng với OpenAI agent tools, map tool schema sang `FunctionTool`.
3. Output:
   - Danh sách MCP tools, kết quả tool call, hoặc nội dung resource.
4. Control flow / data flow:
   - Handwritten client -> MCP server -> business logic -> result -> client -> optional OpenAI tool wrapper.
5. Decision points:
   - Có cần handwritten client không, hay để SDK làm tự động.
   - Có cần đọc resource không.

## 7. Techniques - Kỹ thuật sử dụng

### Context manager lifecycle - quản lý vòng đời bằng context manager
- Technique - kỹ thuật: Context manager lifecycle - quản lý vòng đời bằng context manager
- Purpose - mục đích: Bảo đảm server process và session được mở/đóng đúng cách.
- When to use - dùng khi nào: Mỗi khi spawn MCP server bằng Stdio trong Python.
- Trade-off - đánh đổi: Mã lồng nhau hơn một chút nhưng tránh resource leaks (rò rỉ tài nguyên) và shutdown lỗi.
- Common mistake - lỗi dễ gặp: Tạo agent hoặc tool wrappers ngoài lifetime của server session.

### Tool inspection before agent run - kiểm tra tool trước khi chạy agent
- Technique - kỹ thuật: Tool inspection before agent run - kiểm tra tool trước khi chạy agent
- Purpose - mục đích: Xác nhận server expose đúng tools như kỳ vọng trước khi debug hành vi agent.
- When to use - dùng khi nào: Sau khi viết MCP server mới hoặc nghi ngờ metadata sai.
- Trade-off - đánh đổi: Thêm bước kiểm tra nhưng giảm khó khăn debug ở tầng LLM.
- Common mistake - lỗi dễ gặp: Chạy agent ngay rồi tưởng LLM sai, trong khi server chưa expose tool đúng.

### Schema bridging - bắc cầu schema
- Technique - kỹ thuật: Schema bridging - bắc cầu schema
- Purpose - mục đích: Chuyển MCP tool metadata thành `FunctionTool` để dùng với OpenAI Agents SDK kiểu cũ/thủ công.
- When to use - dùng khi nào: Khi tự viết client hoặc phải tích hợp MCP vào framework không hỗ trợ native MCP đầy đủ.
- Trade-off - đánh đổi: Thêm mã chuyển đổi và hiểu biết về hai schema khác nhau.
- Common mistake - lỗi dễ gặp: Giả định schema MCP và OpenAI function schema hoàn toàn giống nhau.

### Resource-first access pattern - pattern truy cập resource trực tiếp
- Technique - kỹ thuật: Resource-first access pattern - pattern truy cập resource trực tiếp
- Purpose - mục đích: Lấy context/report mà không cần ép LLM gọi tool.
- When to use - dùng khi nào: Khi app muốn chủ động tải context trước hoặc khi SDK không surface resources tự động.
- Trade-off - đánh đổi: Cần client code riêng, ít “magical automation” hơn.
- Common mistake - lỗi dễ gặp: Trông chờ resources xuất hiện trong agent tools giống hệt MCP tools.

## 8. Code Walkthrough - Phân tích code nếu có

### File / block: `2_lab2.ipynb` cells 8-11
- Purpose - mục đích: Minh họa cách hiện đại dùng trực tiếp MCP server vừa viết với OpenAI Agents SDK.
- Key logic - logic chính:
  - Tạo `params` cho lệnh `uv run accounts_server.py`.
  - Dùng `async with MCPServerStdio(...) as server:` rồi `await server.list_tools()` để xác nhận tool exposure.
  - Dùng `async with MCPServerStdio(...) as mcp_server:` và truyền `mcp_servers=[mcp_server]` vào `Agent`.
- Important lines / functions:
  - `params = {"command": "uv", "args": ["run", "accounts_server.py"]}`
  - `await server.list_tools()`
  - `Agent(..., mcp_servers=[mcp_server])`
  - `Runner.run(agent, request)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là “happy path” hiện đại: gần như không cần viết MCP client riêng.
  - Việc list tools trước khi chạy agent là bước sanity check rất tốt.

### File / block: [accounts_client.py](G:\Agent2026Win\agents\6_mcp\accounts_client.py)
- Purpose - mục đích: Viết một MCP client thủ công cho accounts server, bao gồm tool discovery, tool calling, resource reading và OpenAI tool mapping.
- Key logic - logic chính:
  - `params = StdioServerParameters(...)` mô tả cách spawn server.
  - `list_accounts_tools()` mở stdio streams, tạo `ClientSession`, initialize rồi lấy `tools_result.tools`.
  - `call_accounts_tool()` gọi một tool bất kỳ theo tên và arguments.
  - `read_accounts_resource()` và `read_strategy_resource()` đọc resources qua URI tương ứng.
  - `get_accounts_tools_openai()` map MCP tools thành `FunctionTool`.
- Important lines / functions:
  - `from mcp.client.stdio import stdio_client`
  - `async def list_accounts_tools()`
  - `async def call_accounts_tool(tool_name, tool_args)`
  - `async def read_accounts_resource(name)`
  - `async def get_accounts_tools_openai()`
  - `on_invoke_tool=lambda ctx, args, toolname=tool.name: call_accounts_tool(toolname, json.loads(args))`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - `session.initialize()` là bước handshake nền tảng; bỏ qua bước này thì client chưa sẵn sàng.
  - `tools_result.tools` cho thấy SDK MCP client trả về object model riêng, không phải plain JSON ngay lập tức.
  - Phần lambda `on_invoke_tool` chính là cầu nối từ lời gọi tool kiểu OpenAI sang `call_accounts_tool(...)`.

### File / block: `2_lab2.ipynb` cells 13-16
- Purpose - mục đích: Chạy client thủ công để so sánh với cách dùng trực tiếp qua SDK và minh họa đọc resource.
- Key logic - logic chính:
  - Gọi `list_accounts_tools()` và `get_accounts_tools_openai()` để xem hai representation khác nhau.
  - Gắn `openai_tools` vào `Agent(..., tools=openai_tools)`.
  - Gọi `read_accounts_resource("ed")` để lấy report qua URI resource.
  - So sánh với `Account.get("ed").report()` để thấy resource thực chất đang bọc business logic cũ.
- Important lines / functions:
  - `from accounts_client import get_accounts_tools_openai, read_accounts_resource, list_accounts_tools`
  - `openai_tools = await get_accounts_tools_openai()`
  - `Agent(..., tools=openai_tools)`
  - `context = await read_accounts_resource("ed")`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Bài học cho thấy hai “bề mặt tiêu thụ” của cùng một capability: native MCP consumption và tool wrapper consumption.
  - Đây cũng là lý do instructor gọi phần client là “plumbing” hơn là pattern phải dùng mỗi ngày.

### File / block: [accounts_server.py](G:\Agent2026Win\agents\6_mcp\accounts_server.py) và [accounts.py](G:\Agent2026Win\agents\6_mcp\accounts.py)
- Purpose - mục đích: Đối chiếu để hiểu tool/resource client đang nói chuyện với cái gì ở phía server.
- Key logic - logic chính:
  - `accounts_client.py` không làm business logic; nó chỉ gửi call sang tool/resource đã khai báo ở server.
  - Kết quả cuối cùng vẫn được tính bởi `Account` methods trong `accounts.py`.
- Important lines / functions:
  - `@mcp.tool()` và `@mcp.resource(...)` ở server
  - `report()` và `get_strategy()` ở `Account`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Khi debug, cần nhớ lỗi có thể nằm ở 3 nơi: client plumbing, server wrapper, hoặc domain logic.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Dùng `mcp_servers=[...]` với OpenAI Agents SDK
- Option: Native SDK MCP integration
- Pros: Ít code nhất, dễ dùng, SDK tự lo phần lớn client plumbing.
- Cons: Ít lộ chi tiết nội bộ hơn; tài nguyên kiểu resource không luôn được surface trực tiếp trong agent flow.
- When to choose: Lựa chọn mặc định cho hầu hết use case hiện đại.

### Option 2: Viết MCP client thủ công
- Option: Handwritten client
- Pros: Hiểu sâu internals, kiểm soát được discovery/call/resource access, hữu ích cho tích hợp đặc thù.
- Cons: Nhiều plumbing code, dễ phát sinh lỗi lifecycle/schema mapping.
- When to choose: Khi cần custom integration hoặc mục tiêu học tập/debug.

### Option 3: Chuyển MCP tools sang OpenAI `FunctionTool`
- Option: Bridging MCP -> OpenAI tool wrappers
- Pros: Dùng được với flow tool-based quen thuộc, hữu ích khi framework không nhận native MCP server trực tiếp.
- Cons: Thêm tầng chuyển đổi, phải xử lý khác biệt schema.
- When to choose: Khi bạn cần compatibility (khả năng tương thích) với tool interface hiện có.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Dùng handwritten client như pattern mặc định
  - Root cause: Học từ plumbing demo rồi áp vào mọi dự án.
  - Symptom: Code client lặp lại nhiều thứ SDK đã làm sẵn.
  - Fix / prevention: Với hầu hết trường hợp, ưu tiên native SDK integration.

- Failure mode: Quên initialize session
  - Root cause: Không hiểu lifecycle MCP client.
  - Symptom: `list_tools()` hoặc `call_tool()` lỗi vì session chưa sẵn sàng.
  - Fix / prevention: Luôn `await session.initialize()` trước khi tương tác.

- Failure mode: Nhầm tool schema MCP với OpenAI function schema
  - Root cause: Tưởng metadata hai bên đồng nhất hoàn toàn.
  - Symptom: Wrapper tool sai schema hoặc gọi tool lỗi argument shape.
  - Fix / prevention: Tạo hàm chuyển đổi rõ ràng như `get_accounts_tools_openai()`.

- Failure mode: Tưởng resources cũng “miễn phí” như tools trong SDK flow
  - Root cause: Đồng nhất mọi primitive của MCP.
  - Symptom: Chờ agent tự đọc resource mà không có client logic hỗ trợ.
  - Fix / prevention: Khi cần resources, cân nhắc client code chủ động hoặc cách preload context khác.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- Một handwritten MCP client về bản chất là một adapter layer (lớp thích nghi), rất hữu ích khi bạn muốn nối MCP vào framework nội bộ hoặc hệ thống không hỗ trợ protocol này native.
- Trong production, schema translation thường cần xử lý thêm validation, timeout, retries và error normalization (chuẩn hóa lỗi), chứ không chỉ mỗi mapping trường dữ liệu.
- Pattern “resource preload rồi mới chạy agent” có thể giúp tiết kiệm tool calls trong một số tình huống cần context tĩnh ban đầu.

## 12. Study Pack - Gói ôn tập
### Must remember
- Cách đơn giản nhất hiện nay là truyền `mcp_servers=[...]` vào `Agent`.
- `MCPServerStdio` vừa spawn server vừa giúp SDK nói chuyện với server qua Stdio.
- `accounts_client.py` minh họa đủ 4 việc: initialize, list tools, call tool, read resource.
- Tools và resources là hai primitive khác nhau của MCP.
- Mapping schema từ MCP tools sang `FunctionTool` là việc client thủ công phải lo.
- Viết client thủ công chủ yếu hữu ích cho học tập, debug, hoặc custom integration.

### Self-check questions
- Tại sao instructor nói việc tự viết MCP client “không còn thường gặp”?
- `session.initialize()` có vai trò gì?
- `get_accounts_tools_openai()` đang bridge giữa hai thế giới nào?
- Tại sao resource access vẫn là một lý do hợp lý để viết client thủ công?
- Khi nào nên chọn `mcp_servers=[...]` thay vì `tools=openai_tools`?

### Flashcards
- Q: Cách hiện đại nhất để dùng MCP server trong OpenAI Agents SDK là gì?
  A: Dùng `MCPServerStdio(...)` và truyền server object vào `Agent(..., mcp_servers=[...])`.

- Q: Hàm nào trong client đọc MCP resources?
  A: `read_accounts_resource(name)` và `read_strategy_resource(name)`.

- Q: Hàm nào list tool metadata từ server?
  A: `list_accounts_tools()`.

- Q: Vì sao cần `get_accounts_tools_openai()`?
  A: Để chuyển MCP tool definitions thành `FunctionTool` dùng được với OpenAI Agents SDK theo kiểu tools trực tiếp.

### Interview Q&A nếu phù hợp
- Q: So sánh native MCP integration của OpenAI Agents SDK với handwritten MCP client.
  A: Native integration gọn hơn nhiều: SDK tự tạo client, lấy tools và cho agent gọi chúng qua `mcp_servers`. Handwritten client cho bạn hiểu internals và kiểm soát tốt hơn việc list/call/read resources, nhưng đổi lại cần thêm code quản lý session, schema mapping và lifecycle. Trong đa số use case, native integration là lựa chọn mặc định; handwritten client phù hợp cho debug, custom bridges và resource-centric workflows.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Không có runtime trace hoặc ảnh chụp output, nhưng transcript và code đủ rõ
- Transcript không đi sâu vào error handling của client; đây là phần có thể mở rộng nếu cần nghiên cứu production-grade MCP client

---

# 118. Day 2 - Wrap-Up - Capabilities of Your Custom MCP Server

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `118. Day 2 - Wrap-Up - Capabilities of Your Custom MCP Server.txt`
- Slide: không có
- Code: Code được cung cấp trong session (`2_lab2.ipynb`, `accounts_server.py`, `accounts_client.py`, `accounts.py`) nhưng lesson này là phần wrap-up ngắn, không có code mới gắn trực tiếp
- Summary lịch sử: đã dùng — `day1_summary.md` và các lesson Day 2 phía trên như immediate context
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript rất ngắn, chủ yếu là lời kết và preview Day 3. Vì vậy section này tổng hợp ngắn, bám sát ngữ cảnh Day 2, không thêm suy diễn quá mức.

## 2. Executive Summary - Tóm tắt cốt lõi
- Bài wrap-up tổng kết rằng Day 2 vừa đi sâu vào plumbing và internals của MCP servers lẫn MCP clients.
- Instructor xác nhận trọng tâm chính là server; phần client thủ công chủ yếu để người học hiểu rõ cơ chế bên dưới.
- Day 3 sẽ quay trở lại đúng điểm hấp dẫn nhất của MCP: trang bị cho agent rất nhiều năng lực mới bằng các MCP servers có sẵn trong ecosystem.
- Từ Day 2, người học đã có cả hai góc nhìn: producer của MCP server và consumer của MCP ecosystem.
- Capabilities (năng lực) của custom MCP server không chỉ là tool calling; còn có thể có resources để chia sẻ context.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Cố định lại bức tranh lớn sau Day 2.
  - Nhấn mạnh giá trị học plumbing dù không phải lúc nào cũng cần viết thủ công.
  - Chuẩn bị tâm thế cho Day 3 tập trung vào khai thác ecosystem.
- Practical goals - mục tiêu thực hành:
  - Không có thực hành mới; mục tiêu là recap và định hướng tiếp.
- What learner should be able to explain - người học cần giải thích được:
  - Day 2 đã dạy những capability nào của custom MCP server.
  - Vì sao MCP client thủ công là bài tập hiểu nội bộ chứ không phải thao tác thường ngày.
  - Day 3 sẽ khác Day 2 ở điểm nào.

## 4. Previous Context - Liên hệ với bài trước
- Lesson 116 đã xây server, lesson 117 đã dùng server theo hai cách. Lesson 118 gói lại hai nửa đó thành một mental model thống nhất.
- Day 1 cho người học vai trò consumer của MCP ecosystem; Day 2 bổ sung vai trò builder/producer.
- Wrap-up này cũng nhấn mạnh đúng điểm instructor nói ở lesson 115: phần “nổi tiếng” của MCP là dùng nhiều servers có sẵn, điều sẽ quay lại ở Day 3.

## 5. Core Theory - Lý thuyết cốt lõi

### Plumbing literacy - hiểu biết về plumbing
- Term - thuật ngữ: Plumbing literacy - hiểu biết về đường ống tích hợp
- Meaning - nghĩa: Khả năng hiểu những gì diễn ra bên dưới khi host, client và server nói chuyện với nhau.
- Why it matters - vì sao quan trọng: Dù SDK che bớt chi tiết, hiểu plumbing giúp debug, thiết kế và chọn abstraction đúng hơn.
- Relationship - liên hệ với khái niệm khác: Là giá trị giáo dục chính của lesson 117.

### Custom MCP server capabilities - năng lực của MCP server tự viết
- Term - thuật ngữ: Custom MCP server capabilities - năng lực của MCP server tự viết
- Meaning - nghĩa: Một server tự viết có thể expose tools, resources, và về nguyên tắc là prompts theo chuẩn MCP.
- Why it matters - vì sao quan trọng: Cho thấy MCP không chỉ là cách gọi function mà là một protocol để công bố capability chuẩn hóa.
- Relationship - liên hệ với khái niệm khác: Day 2 mới dùng tools và resources; prompts được nhắc ở mức nền.

### Ecosystem leverage - tận dụng hệ sinh thái
- Term - thuật ngữ: Ecosystem leverage - tận dụng hệ sinh thái
- Meaning - nghĩa: Sau khi hiểu cách server vận hành, người học quay lại thế mạnh chính của MCP là tận dụng kho servers có sẵn.
- Why it matters - vì sao quan trọng: Giúp cân bằng giữa “tự xây” và “dùng cái cộng đồng đã có”.
- Relationship - liên hệ với khái niệm khác: Là cầu nối sang Day 3.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Khong co pipeline ro rang trong tai lieu nguon.

Luồng chủ đề của wrap-up:
1. Nhìn lại Day 2 như một hành trình vào internals của server và client.
2. Khẳng định phần tự viết client là để hiểu plumbing, không phải thao tác thường xuyên.
3. Chuyển kỳ vọng sang Day 3, nơi MCP được dùng đúng kiểu “equip agent with lots of capabilities”.

## 7. Techniques - Kỹ thuật sử dụng

### Learn internals once, abstract later - học nội bộ một lần rồi dùng abstraction
- Technique - kỹ thuật: Learn internals once, abstract later - học nội bộ một lần rồi dùng abstraction
- Purpose - mục đích: Đầu tư thời gian học plumbing để về sau dùng SDK abstraction tự tin hơn.
- When to use - dùng khi nào: Khi onboarding vào một protocol/framework mới như MCP.
- Trade-off - đánh đổi: Mất công học ban đầu nhưng giảm mù mờ khi hệ thống lỗi hoặc cần tùy biến.
- Common mistake - lỗi dễ gặp: Hoặc học quá hời hợt nên không hiểu gì, hoặc mắc kẹt ở internals mà không quay lại năng suất thực tế.

### Balance build vs buy - cân bằng tự xây và dùng sẵn
- Technique - kỹ thuật: Balance build vs buy - cân bằng tự xây và dùng sẵn
- Purpose - mục đích: Biết khi nào nên tự xây custom server, khi nào nên dùng community server.
- When to use - dùng khi nào: Mỗi khi mở rộng capability cho agent.
- Trade-off - đánh đổi: Tự xây cho kiểm soát cao hơn; dùng sẵn cho tốc độ nhanh hơn.
- Common mistake - lỗi dễ gặp: Cực đoan theo một hướng, hoặc tự xây mọi thứ, hoặc phụ thuộc hoàn toàn vào ecosystem.

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này. Bài 118 chỉ là wrap-up rất ngắn và preview Day 3, không giới thiệu file hay đoạn code mới nào.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Dùng community MCP servers
- Option: Ecosystem-first approach
- Pros: Nhanh mở rộng capability cho agent, tận dụng công sức cộng đồng.
- Cons: Phụ thuộc vào chất lượng, bảo mật và độ tương thích của server bên ngoài.
- When to choose: Khi nhu cầu phù hợp với server có sẵn trên marketplace.

### Option 2: Tự viết custom MCP server
- Option: Build-your-own approach
- Pros: Kiểm soát hoàn toàn logic, metadata, resources, lifecycle.
- Cons: Tốn công hơn, cần hiểu plumbing.
- When to choose: Khi logic đặc thù, cần chia sẻ nội bộ/ra ngoài, hoặc server có sẵn không đáp ứng.

### Option 3: Dùng abstraction cao của SDK sau khi đã hiểu internals
- Option: Abstraction-first after learning internals
- Pros: Vừa năng suất, vừa không mù mờ về cơ chế bên dưới.
- Cons: Cần đầu tư học lúc đầu.
- When to choose: Đây là đích đến hợp lý sau Day 2.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Học plumbing rồi nghĩ lúc nào cũng phải tự viết client
  - Root cause: Hiểu nhầm bài học internals là quy trình production chuẩn.
  - Symptom: Tốn công tái tạo những thứ SDK đã hỗ trợ native.
  - Fix / prevention: Xem handwritten client là công cụ học và custom integration, không phải mặc định.

- Failure mode: Sau khi học custom server lại quên tận dụng ecosystem
  - Root cause: Tập trung quá nhiều vào “tự xây”.
  - Symptom: Rebuild những tool phổ biến mà marketplace đã có sẵn.
  - Fix / prevention: Cân bằng build vs buy; dùng custom server cho logic đặc thù, dùng ecosystem cho capability phổ biến.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- Nhiều hệ sinh thái công nghệ trưởng thành đều có cùng quỹ đạo học tập: ban đầu phải hiểu internals, sau đó mới tận dụng abstraction một cách hiệu quả và an toàn.
- Với MCP, hiểu internals còn quan trọng về mặt security và observability, vì tool execution có thể xảy ra qua nhiều process hoặc nhiều server khác nhau.

## 12. Study Pack - Gói ôn tập
### Must remember
- Day 2 dạy cả custom MCP server lẫn MCP client internals.
- Phần client thủ công mang tính giáo dục nhiều hơn là thao tác thường nhật.
- MCP server tự viết có thể expose tools và resources.
- Sau Day 2, người học nên quay lại strength chính của MCP: ecosystem capabilities.
- Build vs buy là quyết định trung tâm khi làm việc với MCP.

### Self-check questions
- Giá trị lớn nhất của phần handwritten client trong Day 2 là gì?
- Sau Day 2, khi nào bạn nên tự viết MCP server?
- Vì sao Day 3 lại quay về ecosystem là hợp lý?
- Custom MCP server có thể expose những loại capability nào?

### Flashcards
- Q: Day 2 tập trung vào phần nào của MCP?
  A: Cách tự xây custom MCP server và hiểu plumbing của client/server interaction.

- Q: Phần nổi tiếng nhất của MCP mà Day 3 sẽ quay lại là gì?
  A: Trang bị cho agent rất nhiều capability mới bằng các MCP servers có sẵn trong ecosystem.

- Q: Handwritten MCP client có phải việc thường làm mỗi ngày không?
  A: Không; chủ yếu hữu ích để hiểu internals hoặc cho custom integration đặc biệt.

### Interview Q&A nếu phù hợp
- Q: Sau khi đã học cách tự viết MCP server và client, chiến lược thực tế nhất để áp dụng MCP trong dự án là gì?
  A: Hiểu internals một lần để có nền tảng debug và ra quyết định tốt, sau đó ưu tiên abstraction có sẵn của SDK để tăng tốc triển khai. Chỉ tự viết custom server khi có business logic đặc thù hoặc cần chia sẻ capability riêng; còn với nhu cầu phổ biến thì tận dụng community MCP servers sẽ hiệu quả hơn.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Transcript rất ngắn nên không có nhiều chi tiết beyond recap/preview
- Không có thêm yêu cầu review code hay bài tập thực hành tiếp nối trong session này
