# 109. Day 1 - Intro to MCP - The USB-C of Agentic AI

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `109. Day 1 - Intro to MCP - The USB-C of Agentic AI.txt`
- Slide: không có
- Code: Code được cung cấp trong session (`1_lab1.ipynb`) nhưng chưa thấy code liên quan trực tiếp tới lesson này
- Summary lịch sử: không có (đây là Day 1 của section MCP)
- Ghi chú về độ tin cậy: Transcript rõ ràng, giảng viên giải thích trực tiếp. Không có mâu thuẫn.

## 2. Executive Summary - Tóm tắt cốt lõi
- MCP (Model Context Protocol) là một protocol (giao thức) do Anthropic công bố, không phải một agent framework.
- Anthropic gọi MCP là "USB-C of Agentic AI" — ý nhấn mạnh MCP là chuẩn kết nối chung (connectivity standard), giúp agent dễ dàng tích hợp tool từ bên ngoài.
- MCP không giúp bạn xây agent, không thay đổi cách tạo tool riêng. Nó chỉ giúp dùng tool của người khác một cách frictionless (không ma sát).
- Giá trị cốt lõi: ecosystem — hàng nghìn MCP server/tool do cộng đồng xây, sẵn sàng sử dụng.
- MCP bắt đầu nổi lên từ cuối 2024, bùng nổ vào đầu 2025.
- So sánh: tương tự HTML tạo nên World Wide Web, MCP tạo nên hệ sinh thái tool chia sẻ nhờ sự adoption (chấp nhận rộng rãi).
- Tuần 6 (finale week) kết hợp MCP với OpenAI Agents SDK để xây capstone project: equity trading floor.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu MCP là gì và không phải là gì
  - Phân biệt MCP với agent framework (OpenAI Agents SDK, CrewAI, LangGraph, Autogen)
  - Hiểu tại sao adoption (sự chấp nhận) của chuẩn giao thức quan trọng hơn bản thân kỹ thuật
- Practical goals - mục tiêu thực hành:
  - Chưa có code thực hành trong bài này (bài giới thiệu lý thuyết)
- What learner should be able to explain - người học cần giải thích được:
  - MCP là protocol, không phải framework — sự khác biệt cốt lõi
  - Tại sao MCP được gọi là USB-C of Agentic AI
  - Giá trị chính của MCP nằm ở ecosystem và tính dễ tích hợp

## 4. Previous Context - Liên hệ với bài trước
- Khóa học đã cover 4 agent framework trước đó: OpenAI Agents SDK (tuần 2), CrewAI (tuần 3), LangGraph (tuần 4), Autogen (tuần 5).
- MCP không phải framework mới mà là protocol bổ sung, dùng kết hợp với các framework đã học.
- Tuần 6 quay lại dùng OpenAI Agents SDK (framework yêu thích của giảng viên) kết hợp MCP.
- Concept tool và function tool decorator đã được giới thiệu từ tuần 2 với OpenAI Agents SDK.

## 5. Core Theory - Lý thuyết cốt lõi

### MCP - Model Context Protocol
- Term: Model Context Protocol (MCP)
- Meaning: Giao thức chuẩn hóa cách agent kết nối và sử dụng tool/resource/prompt từ bên ngoài
- Why it matters: Cho phép chia sẻ tool giữa các developer một cách frictionless, tạo ecosystem lớn
- Relationship: Bổ sung cho agent framework (OpenAI Agents SDK, CrewAI, etc.) — không thay thế chúng

### Protocol vs Framework
- Term: Protocol vs Framework
- Meaning: Protocol là chuẩn giao tiếp (như HTTP, HTML); Framework là bộ công cụ xây dựng (như SDK)
- Why it matters: MCP là protocol — nó không giúp xây agent, chỉ giúp kết nối agent với tool
- Relationship: Agent framework dùng protocol MCP để truy cập tool ecosystem

### USB-C Analogy
- Term: USB-C of Agentic AI
- Meaning: Giống USB-C là chuẩn kết nối phần cứng phổ quát, MCP là chuẩn kết nối tool cho AI agent
- Why it matters: Nhấn mạnh MCP là về connectivity (kết nối), không phải về capability (khả năng)
- Relationship: Analogy do Anthropic đưa ra, trở thành cách mô tả phổ biến nhất

### Ecosystem Value
- Term: Tool Ecosystem
- Meaning: Hệ sinh thái hàng nghìn MCP server/tool do cộng đồng xây dựng và chia sẻ
- Why it matters: Giá trị thực sự của MCP không nằm ở kỹ thuật mà ở sự adoption tạo ecosystem
- Relationship: Tương tự HTML tạo World Wide Web nhờ adoption

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Không có pipeline rõ ràng trong tài liệu nguồn.

Luồng tư duy bài học:
1. Giới thiệu tuần 6 là finale week, capstone project
2. Nhắc lại các framework đã học (OpenAI Agents SDK, CrewAI, LangGraph, Autogen)
3. Giải thích MCP không phải là gì (not a framework, not a new invention, not about coding agents)
4. Giải thích MCP là gì (protocol, standard, connectivity for tools)
5. Giải thích tại sao MCP quan trọng (ecosystem, adoption, frictionless integration)

## 7. Techniques - Kỹ thuật sử dụng

### Function Tool Decorator (nhắc lại)
- Technique: `@function_tool` decorator trong OpenAI Agents SDK
- Purpose: Biến bất kỳ Python function nào thành tool cho agent
- When to use: Khi tự viết tool riêng cho agent của mình
- Trade-off: Dễ dùng cho tool riêng, nhưng không giúp chia sẻ/tái sử dụng tool từ người khác
- Common mistake: Nhầm lẫn rằng MCP cần thiết cho mọi tool — thực tế MCP chỉ hữu ích khi dùng tool của người khác

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session (`1_lab1.ipynb`) nhưng chưa thấy code liên quan trực tiếp tới lesson này. Bài 109 là bài giới thiệu lý thuyết thuần.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Tự viết tool vs Dùng MCP tool
- Option: Tự viết tool riêng với `@function_tool`
  - Pros: Đơn giản, kiểm soát hoàn toàn, không phụ thuộc bên ngoài
  - Cons: Không tận dụng được ecosystem, phải tự implement mọi thứ
  - When to choose: Khi logic tool đặc thù cho ứng dụng của bạn

- Option: Dùng MCP server từ cộng đồng
  - Pros: Frictionless, ecosystem lớn, tool đã được tối ưu (bao gồm prompt engineering cho tool description)
  - Cons: Phụ thuộc bên ngoài, cần quản lý security
  - When to choose: Khi cần chức năng phổ biến (web search, file system, database access, etc.)

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Nhầm MCP là agent framework
  - Root cause: Tên gọi và hype xung quanh MCP dễ gây hiểu lầm
  - Symptom: Cố dùng MCP để xây toàn bộ agent thay vì chỉ để kết nối tool
  - Fix: MCP là protocol bổ sung, cần kết hợp với framework như OpenAI Agents SDK

- Failure mode: Nghĩ MCP giúp tạo tool dễ hơn
  - Root cause: Không phân biệt "tạo tool" vs "dùng tool người khác"
  - Symptom: Dùng MCP cho tool riêng, thấy phức tạp hơn decorator đơn giản
  - Fix: MCP thêm overhead, chỉ có giá trị khi chia sẻ hoặc dùng tool từ ecosystem

## 11. Knowledge Extension - Kiến thức mở rộng
> Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- MCP spec bao gồm 3 loại primitive (nguyên thủy): Tools, Resources, và Prompts. Trong thực tế, Tools chiếm phần lớn sự quan tâm. Resources cho phép cung cấp RAG-like context. Prompts cho phép chia sẻ template nhưng chưa phổ biến.
- MCP được Anthropic open-source, spec công khai tại `modelcontextprotocol.io`. Nhiều framework ngoài Anthropic (OpenAI Agents SDK, LangChain, etc.) đã hỗ trợ MCP.
- Sự bùng nổ MCP trong Q1 2025 một phần nhờ sự hỗ trợ native từ Claude Desktop, Cursor, và nhiều IDE khác.

## 12. Study Pack - Gói ôn tập
### Must remember
1. MCP là protocol, không phải framework
2. MCP = "USB-C of Agentic AI" — chuẩn kết nối tool
3. Giá trị MCP nằm ở ecosystem và adoption, không phải kỹ thuật mới
4. MCP giúp dùng tool người khác, không giúp tạo tool riêng dễ hơn
5. MCP hỗ trợ 3 primitive: Tools (chính), Resources, Prompts
6. Tuần 6 kết hợp MCP + OpenAI Agents SDK
7. Anthropic công bố MCP cuối 2024, bùng nổ đầu 2025

### Self-check questions
1. MCP là framework hay protocol? Sự khác biệt là gì?
2. Tại sao Anthropic gọi MCP là "USB-C of Agentic AI"?
3. MCP có giúp bạn xây agent không? Tại sao?
4. Giá trị thực sự của MCP nằm ở đâu?
5. Khi nào nên dùng `@function_tool` và khi nào nên dùng MCP server?
6. Ba loại primitive của MCP là gì? Loại nào phổ biến nhất?
7. Tại sao adoption quan trọng đối với một protocol?

### Flashcards
- Q: MCP là viết tắt của gì?
  A: Model Context Protocol — giao thức ngữ cảnh mô hình, chuẩn hóa cách agent kết nối với tool/resource/prompt bên ngoài

- Q: MCP được công bố bởi ai và khi nào?
  A: Anthropic, công bố cuối 2024, bùng nổ đầu 2025

- Q: MCP được ví như gì?
  A: USB-C of Agentic AI — chuẩn kết nối phổ quát cho tool AI agent

- Q: Ba primitive của MCP là gì?
  A: Tools (công cụ), Resources (tài nguyên/RAG), Prompts (mẫu prompt)

- Q: MCP có phải agent framework không?
  A: Không. MCP là protocol (giao thức chuẩn), cần kết hợp với framework như OpenAI Agents SDK

### Interview Q&A
- Q: Giải thích sự khác biệt giữa MCP và một agent framework như LangGraph hoặc CrewAI.
  A: Agent framework cung cấp công cụ để xây dựng agent (orchestration, routing, memory, etc.). MCP là protocol chuẩn hóa cách agent kết nối với tool bên ngoài. MCP không xây agent mà bổ sung khả năng tích hợp tool từ ecosystem. Bạn dùng framework để xây agent, rồi dùng MCP để trang bị tool cho agent đó.

- Q: Tại sao adoption quan trọng hơn kỹ thuật đối với MCP?
  A: Tương tự HTML — kỹ thuật HTML đơn giản, nhưng adoption rộng rãi tạo ra World Wide Web. MCP cũng vậy: protocol đơn giản, nhưng adoption tạo ecosystem hàng nghìn tool sẵn dùng. Không có adoption, MCP chỉ là spec trên giấy.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Summary lịch sử các tuần trước (1-5): không được cung cấp, nhưng không ảnh hưởng nghiêm trọng vì bài này tự đứng được

---

# 110. Day 1 - Understanding MCP Hosts, Clients, and Servers

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `110. Day 1 - Understanding MCP Hosts, Clients, and Servers.txt`
- Slide: không có
- Code: Code được cung cấp trong session (`1_lab1.ipynb`) nhưng chưa thấy code liên quan trực tiếp tới lesson này
- Summary lịch sử: không có
- Ghi chú về độ tin cậy: Transcript rõ ràng, giảng viên nhấn mạnh nhiều lần kiến trúc MCP. Không có mâu thuẫn.

## 2. Executive Summary - Tóm tắt cốt lõi
- Kiến trúc MCP gồm 3 thành phần: Host, Client, Server.
- MCP Host là ứng dụng tổng thể (Claude Desktop, hoặc ứng dụng agent bạn viết bằng OpenAI Agents SDK).
- MCP Client là plugin nhỏ chạy bên trong Host, mỗi Client kết nối 1-1 với một MCP Server.
- MCP Server là code cung cấp tool/resource/prompt, chạy bên ngoài Host.
- Điểm quan trọng nhất: MCP Server hầu hết chạy locally trên máy bạn, không phải remote server. Đây là misconception (hiểu lầm) phổ biến nhất.
- Hai transport mechanism (cơ chế truyền tải): Stdio (standard input/output) — phổ biến nhất, và SSE (Server-Sent Events) — dùng cho remote server.
- Ví dụ cụ thể: fetch MCP server dùng Playwright chạy headless browser để thu thập web page.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu 3 thành phần kiến trúc MCP: Host, Client, Server
  - Phân biệt local MCP server vs remote/hosted/managed MCP server
  - Hiểu 2 transport mechanism: Stdio vs SSE
  - Nắm rõ misconception phổ biến về MCP server
- Practical goals - mục tiêu thực hành:
  - Chưa có code thực hành trong bài này
- What learner should be able to explain - người học cần giải thích được:
  - Vẽ architecture diagram MCP với Host, Client, Server
  - Giải thích tại sao MCP server chạy local chứ không phải remote
  - Phân biệt Stdio và SSE, khi nào dùng loại nào

## 4. Previous Context - Liên hệ với bài trước
- Bài 109 giới thiệu MCP là protocol và USB-C analogy. Bài 110 đi sâu vào kiến trúc kỹ thuật.
- Giảng viên nhắc lại fetch MCP server đã dùng trong tuần Autogen (tuần 5) để minh họa.
- Khái niệm Host liên hệ với concept ứng dụng agent đã xây trong các tuần trước.

## 5. Core Theory - Lý thuyết cốt lõi

### MCP Host
- Term: MCP Host
- Meaning: Ứng dụng tổng thể chứa agent và quản lý các MCP client. Ví dụ: Claude Desktop, hoặc app viết bằng OpenAI Agents SDK.
- Why it matters: Host là context tổng thể — mọi MCP client đều sống trong Host
- Relationship: Host chứa nhiều MCP Client, mỗi Client kết nối 1 MCP Server

### MCP Client
- Term: MCP Client
- Meaning: Plugin nhỏ chạy bên trong Host, kết nối 1-1 với một MCP Server
- Why it matters: Client là cầu nối giữa Host (agent) và Server (tool)
- Relationship: Mỗi MCP Server cần một MCP Client tương ứng trong Host

### MCP Server
- Term: MCP Server
- Meaning: Code chạy bên ngoài Host, cung cấp tool/resource/prompt cho agent
- Why it matters: Server là nơi chứa logic tool thực tế
- Relationship: Server kết nối với Client qua Stdio hoặc SSE

### Stdio Transport
- Term: Stdio (Standard Input/Output)
- Meaning: MCP Client spawn (tạo) một process mới trên máy local, giao tiếp qua standard input/output
- Why it matters: Cách triển khai phổ biến nhất, đơn giản nhất
- Relationship: Chỉ dùng cho local MCP server

### SSE Transport
- Term: SSE (Server-Sent Events)
- Meaning: Dùng HTTPS connection, stream kết quả về — tương tự cách LLM stream response
- Why it matters: Cần thiết cho remote/hosted MCP server
- Relationship: Có thể dùng cho cả local và remote, nhưng local thường dùng Stdio

### Local vs Remote MCP Server
- Term: Local vs Remote MCP Server
- Meaning: Local server chạy trên máy bạn (phổ biến nhất); Remote/hosted/managed server chạy trên máy khác
- Why it matters: Misconception lớn nhất — nghe "server" dễ nghĩ là remote, nhưng thực tế hầu hết MCP server chạy local
- Relationship: Local dùng Stdio hoặc SSE; Remote bắt buộc dùng SSE

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động

### Kiến trúc MCP (3 cấu hình)

**Cấu hình 1: Local MCP Server (phổ biến nhất)**
1. Input: User request đến agent trong Host
2. Processing: Host chứa MCP Client → Client kết nối MCP Server chạy local qua Stdio
3. Output: Server thực thi tool và trả kết quả về Client → Host → Agent
4. Data flow: Host (Agent) → MCP Client → MCP Server (local) → Tool execution → kết quả trả ngược

**Cấu hình 2: Remote MCP Server (ít phổ biến)**
1. Input: User request đến agent trong Host
2. Processing: Host chứa MCP Client → Client kết nối MCP Server chạy remote qua SSE
3. Output: Server thực thi tool trên remote machine và trả kết quả
4. Control flow: Cần SSE transport, không dùng Stdio được

**Cấu hình 3: Local MCP Server gọi internet (rất phổ biến)**
1. Input: User request đến agent
2. Processing: MCP Server chạy local nhưng gọi API/web service qua internet
3. Output: Server thu thập dữ liệu từ internet, trả về Client
4. Decision point: Phân biệt "server chạy local nhưng gọi internet" vs "server chạy remote"

## 7. Techniques - Kỹ thuật sử dụng

### Fetch MCP Server
- Technique: Dùng fetch MCP server để thu thập web page
- Purpose: Cho agent khả năng đọc nội dung web page
- When to use: Khi agent cần truy cập và đọc nội dung từ internet
- Trade-off: Dùng headless browser (Playwright) — mạnh nhưng tốn tài nguyên hơn HTTP request đơn giản
- Common mistake: Nhầm fetch MCP server chạy remote — thực tế nó chạy local trên máy bạn, chỉ gọi internet để lấy dữ liệu

### Process Spawning qua Stdio
- Technique: MCP Client spawn một process mới và giao tiếp qua stdin/stdout
- Purpose: Cách đơn giản nhất để chạy MCP server locally
- When to use: Mọi local MCP server (default choice)
- Trade-off: Đơn giản, nhanh nhưng chỉ hoạt động local
- Common mistake: Cố dùng Stdio cho remote server — không hoạt động

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session (`1_lab1.ipynb`) nhưng chưa thấy code liên quan trực tiếp tới lesson này. Bài 110 tập trung giải thích kiến trúc MCP, chưa đi vào code.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Stdio vs SSE Transport
- Option: Stdio
  - Pros: Đơn giản, nhanh, không cần setup network
  - Cons: Chỉ hoạt động local
  - When to choose: Default choice cho local MCP server (hầu hết trường hợp)

- Option: SSE (Server-Sent Events)
  - Pros: Hỗ trợ remote server, streaming response
  - Cons: Cần HTTPS, phức tạp hơn, latency cao hơn
  - When to choose: Khi kết nối remote/hosted MCP server, hoặc cần streaming

### Local vs Remote MCP Server
- Option: Local MCP Server
  - Pros: Nhanh, dễ setup, kiểm soát hoàn toàn
  - Cons: Chạy trên máy bạn, tốn tài nguyên local
  - When to choose: Hầu hết trường hợp (default)

- Option: Remote/Hosted MCP Server
  - Pros: Không tốn tài nguyên local, có thể scale
  - Cons: Phụ thuộc network, latency, ít phổ biến, khó tìm
  - When to choose: Khi cần server side processing hoặc enterprise deployment

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Nghĩ MCP server chạy remote
  - Root cause: Từ "server" gợi liên tưởng đến remote machine
  - Symptom: Cố tìm hosted MCP server thay vì install locally
  - Fix: Hiểu rằng hầu hết MCP server download về và chạy local, dù code từ repo công khai

- Failure mode: Nhầm "server chạy local gọi internet" với "remote server"
  - Root cause: Không phân biệt nơi server chạy vs nơi server gọi đến
  - Symptom: Tưởng fetch MCP server là remote server vì nó truy cập web
  - Fix: fetch chạy local (spawn process trên máy bạn), chỉ gọi internet để lấy data

- Failure mode: Dùng Stdio cho remote MCP server
  - Root cause: Không hiểu Stdio chỉ giao tiếp qua stdin/stdout local
  - Symptom: Kết nối fail khi cố spawn remote process
  - Fix: Remote server phải dùng SSE transport

## 11. Knowledge Extension - Kiến thức mở rộng
> Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- Trong MCP spec chính thức, ngoài Stdio và SSE còn có thảo luận về Streamable HTTP transport — một cải tiến của SSE cho phép bidirectional communication tốt hơn.
- MCP Client-Server tuân theo JSON-RPC 2.0 protocol cho message format.
- Một Host có thể chạy nhiều Client đồng thời, mỗi Client kết nối một Server khác nhau — đây là cách agent có thể dùng nhiều tool sources cùng lúc.

## 12. Study Pack - Gói ôn tập
### Must remember
1. MCP có 3 thành phần: Host (app tổng), Client (plugin trong Host), Server (tool provider bên ngoài)
2. MCP Server hầu hết chạy LOCAL trên máy bạn, không phải remote
3. Mỗi MCP Client kết nối 1-1 với một MCP Server
4. Stdio: transport phổ biến nhất, spawn local process, giao tiếp qua stdin/stdout
5. SSE: transport cho remote server, dùng HTTPS + streaming
6. Local MCP server có thể gọi internet (ví dụ: fetch) — khác với remote MCP server
7. Fetch MCP server: dùng Playwright headless browser để thu thập web page

### Self-check questions
1. Ba thành phần kiến trúc MCP là gì? Quan hệ giữa chúng?
2. MCP Server chạy ở đâu trong hầu hết trường hợp?
3. Stdio và SSE khác nhau thế nào? Khi nào dùng cái nào?
4. Fetch MCP server hoạt động như thế nào? Nó chạy ở đâu?
5. Tại sao "server chạy local gọi internet" khác "remote server"?
6. Vẽ architecture diagram cho cấu hình MCP local phổ biến nhất.

### Flashcards
- Q: MCP Host là gì?
  A: Ứng dụng tổng thể chứa agent và quản lý MCP client. Ví dụ: Claude Desktop, app OpenAI Agents SDK.

- Q: MCP Client là gì?
  A: Plugin nhỏ chạy trong Host, kết nối 1-1 với một MCP Server

- Q: MCP Server chạy ở đâu phổ biến nhất?
  A: Chạy locally trên máy bạn, không phải remote. Bạn download và chạy local.

- Q: Stdio transport hoạt động thế nào?
  A: MCP Client spawn một process local mới, giao tiếp qua standard input/output

- Q: Khi nào phải dùng SSE thay vì Stdio?
  A: Khi kết nối remote/hosted MCP server. Stdio chỉ hoạt động local.

### Interview Q&A
- Q: Giải thích kiến trúc MCP và phân biệt 3 cấu hình triển khai.
  A: MCP gồm Host (app tổng), Client (connector trong Host), Server (tool provider). Có 3 cấu hình: (1) Local server dùng Stdio — phổ biến nhất; (2) Remote server dùng SSE — ít gặp; (3) Local server gọi internet — phổ biến, cần phân biệt với remote server. Ví dụ: fetch MCP server chạy local nhưng dùng Playwright truy cập web.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp — giảng viên nhắc đến architecture diagram nhưng không có slide để xem
- Summary lịch sử tuần 5 (Autogen): không có, giảng viên nhắc đã dùng fetch MCP server trong Autogen

---

# 111. Day 1 - Using MCP Servers with OpenAI Agents SDK

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `111. Day 1 - Using MCP Servers with OpenAI Agents SDK.txt`
- Slide: không có
- Code: đã dùng — `1_lab1.ipynb` (cells 1-4: imports, load_dotenv, fetch_params, MCPServerStdio)
- Summary lịch sử: không có
- Ghi chú về độ tin cậy: Transcript và code khớp nhau. Giảng viên walk-through code trực tiếp.

## 2. Executive Summary - Tóm tắt cốt lõi
- Bài này bắt đầu lab thực hành MCP trong OpenAI Agents SDK (notebook `1_lab1.ipynb`).
- Giới thiệu `MCPServerStdio` — context manager trong OpenAI Agents SDK để tạo MCP client và spawn MCP server.
- Demo đầu tiên: dùng fetch MCP server (Python-based, install qua `uvx mcp-server-fetch`).
- `fetch_params` dictionary mô tả command + args để spawn MCP server process.
- `server.list_tools()` trả về danh sách tool mà server cung cấp.
- Timeout parameter quan trọng: default 5s hay timeout, nên set 30-60s.
- Lưu ý Windows: MCP không hoạt động trên Windows native, cần WSL (Windows Subsystem for Linux).
- Giảng viên nhấn mạnh code có thể thay đổi vì MCP evolving nhanh — cần pull latest code.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cấu trúc params dictionary cho MCP server
  - Hiểu MCPServerStdio context manager pattern
  - Hiểu flow: spawn server → create client → list tools
- Practical goals - mục tiêu thực hành:
  - Chạy notebook 1_lab1.ipynb
  - Tạo MCPServerStdio với fetch_params
  - Gọi list_tools() để xem tool descriptions
  - Cài WSL nếu dùng Windows
- What learner should be able to explain - người học cần giải thích được:
  - Params dictionary chứa gì và tại sao
  - MCPServerStdio làm gì behind the scenes
  - Tại sao timeout quan trọng

## 4. Previous Context - Liên hệ với bài trước
- Bài 109-110 giải thích lý thuyết MCP (protocol, Host/Client/Server, Stdio/SSE). Bài 111 áp dụng vào code.
- OpenAI Agents SDK đã được giới thiệu từ tuần 2. Bài này quay lại dùng SDK kết hợp MCP.
- Fetch MCP server đã được nhắc đến trong bài 110 và tuần Autogen.
- Concept kernel (Jupyter notebook) đã quen thuộc từ các tuần trước.

## 5. Core Theory - Lý thuyết cốt lõi

### MCP Server Parameters
- Term: MCP Server Parameters (params dictionary)
- Meaning: Dictionary chứa `command` và `args` — mô tả lệnh command line để spawn MCP server process
- Why it matters: Đây là cách duy nhất để mô tả cho MCPServerStdio biết cần chạy gì
- Relationship: params được truyền vào MCPServerStdio constructor

### MCPServerStdio Context Manager
- Term: MCPServerStdio (async context manager)
- Meaning: Class trong OpenAI Agents SDK, dùng `async with` để spawn MCP server, tạo client, và quản lý lifecycle
- Why it matters: Abstraction chính để tích hợp MCP vào OpenAI Agents SDK — chỉ 1 dòng code
- Relationship: Nhận params, trả về server object có thể gọi list_tools()

### list_tools()
- Term: `server.list_tools()`
- Meaning: Gọi MCP server để hỏi nó cung cấp những tool nào, trả về danh sách tool với name, description, parameters
- Why it matters: Đây là bước discovery — agent biết được server có thể làm gì
- Relationship: Kết quả này sẽ được truyền cho Agent để LLM biết tool nào khả dụng

### Tool Description Quality
- Term: Tool Description trong MCP
- Meaning: Mô tả chi tiết của tool, bao gồm cả prompt hints cho LLM (ví dụ: "you now have internet access")
- Why it matters: Description tốt giúp LLM dùng tool đúng cách — đây là giá trị ẩn của MCP ecosystem
- Relationship: Người tạo MCP server đã prompt-engineer description, bạn được hưởng miễn phí

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động

### Pipeline sử dụng MCP Server trong OpenAI Agents SDK
1. Input: params dictionary (`{"command": "uvx", "args": ["mcp-server-fetch"]}`)
2. Processing steps:
   - `async with MCPServerStdio(params=fetch_params, client_session_timeout_seconds=60) as server:` → spawn process, tạo client
   - `await server.list_tools()` → client hỏi server có những tool nào
3. Output: Danh sách tool objects (name, description, input_schema)
4. Control flow: Context manager đảm bảo cleanup process khi exit
5. Decision points: Timeout (default 5s) — nếu quá ngắn, server chưa kịp start → fail

## 7. Techniques - Kỹ thuật sử dụng

### uvx để chạy Python MCP Server
- Technique: Dùng `uvx` (uv execute) trong params command để install và chạy MCP server package
- Purpose: Một lệnh vừa install vừa run package từ PyPI
- When to use: Với Python-based MCP server (ví dụ: `mcp-server-fetch`)
- Trade-off: Tiện nhưng lần đầu chạy có thể chậm (cần download)
- Common mistake: Quên rằng `uvx` cần `uv` đã cài trước đó

### Timeout Configuration
- Technique: Set `client_session_timeout_seconds=60` thay vì default 5s
- Purpose: Tránh timeout khi server cần thời gian để start (đặc biệt lần đầu download)
- When to use: Luôn luôn — giảng viên khuyến cáo luôn set timeout cao
- Trade-off: Chờ lâu hơn nếu server thực sự fail, nhưng tránh false timeout
- Common mistake: Dùng default 5s → fail ngẫu nhiên → tưởng code sai

## 8. Code Walkthrough - Phân tích code nếu có

### File: `1_lab1.ipynb` — Phần đầu (cells 1-4)

#### Cell 1: Imports
```python
from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
import os
```
- Purpose: Import các thành phần cốt lõi
- Key logic: `MCPServerStdio` từ `agents.mcp` — đây là class chính để tích hợp MCP
- Ghi chú: `Agent, Runner, trace` đã quen từ tuần 2 OpenAI Agents SDK

#### Cell 2: Load Environment
```python
load_dotenv(override=True)
```
- Purpose: Load API keys từ file `.env`
- Ghi chú: `override=True` đảm bảo giá trị mới trong `.env` ghi đè biến môi trường hiện tại

#### Cell 3: Fetch MCP Server — Params và List Tools
```python
fetch_params = {"command": "uvx", "args": ["mcp-server-fetch"]}

async with MCPServerStdio(params=fetch_params, client_session_timeout_seconds=60) as server:
    fetch_tools = await server.list_tools()

fetch_tools
```
- Purpose: Spawn fetch MCP server và lấy danh sách tool
- Key logic:
  - `fetch_params`: dictionary mô tả command line `uvx mcp-server-fetch`
  - `MCPServerStdio(params=..., client_session_timeout_seconds=60)`: tạo context manager, spawn process, tạo client
  - `server.list_tools()`: hỏi server có tool nào → trả về 1 tool "fetch" với description chi tiết
- Important lines: `client_session_timeout_seconds=60` — quan trọng, default 5s hay fail
- Ghi chú: Tool description bao gồm prompt hint "this tool now grants you internet access" — prompt engineering từ Anthropic

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Python MCP Server (uvx) vs Node MCP Server (npx)
- Option: Python-based MCP Server (uvx)
  - Pros: Quen thuộc với Python developer, dùng PyPI ecosystem
  - Cons: Cần có `uv` cài sẵn
  - When to choose: Khi MCP server viết bằng Python (ví dụ: fetch)

- Option: Node-based MCP Server (npx)
  - Pros: Nhiều MCP server viết bằng Node (ví dụ: Playwright, filesystem)
  - Cons: Cần có Node.js và npx cài sẵn
  - When to choose: Khi MCP server viết bằng JavaScript (sẽ thấy ở bài sau)

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Timeout khi spawn MCP server
  - Root cause: Default timeout 5s quá ngắn, server chưa kịp start
  - Symptom: Exception timeout sau 5 giây
  - Fix: Set `client_session_timeout_seconds=30` hoặc `60`

- Failure mode: MCP không hoạt động trên Windows
  - Root cause: Production bug trong MCP với Windows (confirmed issue)
  - Symptom: MCP server không spawn được hoặc lỗi không rõ nguyên nhân
  - Fix: Cài WSL (Windows Subsystem for Linux) và chạy trong môi trường Linux

- Failure mode: Breaking change khi update OpenAI Agents SDK
  - Root cause: SDK đang evolve nhanh, API thay đổi
  - Symptom: `server.list_tools()` không hoạt động sau update
  - Fix: Có thể cần đổi thành `server.session.list_tools()` và kết quả thành `.tools`

## 11. Knowledge Extension - Kiến thức mở rộng
> Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- `uvx` là shorthand của `uv tool run` — nó tạo temporary virtual environment, install package, chạy rồi cleanup. Tương đương `pipx run`.
- MCPServerStdio internally sử dụng `subprocess` để spawn process và communicate qua stdin/stdout pipes.
- Fetch MCP server dùng Playwright headless Chrome — có thể render JavaScript pages, không chỉ static HTML.

## 12. Study Pack - Gói ôn tập
### Must remember
1. `fetch_params = {"command": "uvx", "args": ["mcp-server-fetch"]}` — cấu trúc params
2. `MCPServerStdio` là context manager chính để dùng MCP trong OpenAI Agents SDK
3. Luôn set `client_session_timeout_seconds=30` trở lên
4. `server.list_tools()` trả về danh sách tool với name + description
5. Tool description đã được prompt-engineered bởi tác giả MCP server
6. Windows cần WSL để chạy MCP
7. Code MCP đang evolve nhanh — luôn pull latest

### Self-check questions
1. params dictionary chứa những key nào? Chúng mô tả cái gì?
2. MCPServerStdio làm gì khi bạn dùng `async with`?
3. Tại sao cần set timeout cao hơn default?
4. list_tools() trả về thông tin gì?
5. Tại sao Windows cần WSL cho MCP?
6. Nếu update OpenAI Agents SDK và code break, cần thay đổi gì?

### Flashcards
- Q: Cấu trúc params dictionary cho MCP server?
  A: `{"command": "uvx", "args": ["mcp-server-fetch"]}` — command là lệnh chạy, args là tham số

- Q: MCPServerStdio là gì?
  A: Async context manager trong OpenAI Agents SDK, spawn MCP server process và tạo client kết nối

- Q: Default timeout của MCPServerStdio là bao nhiêu? Nên set bao nhiêu?
  A: Default 5 giây — hay fail. Nên set 30-60 giây.

- Q: server.list_tools() trả về gì?
  A: Danh sách tool objects với name, description, và input schema

### Interview Q&A
- Q: Mô tả flow tích hợp MCP server vào OpenAI Agents SDK.
  A: Tạo params dictionary chứa command + args. Dùng `async with MCPServerStdio(params=...)` để spawn server process và tạo client. Gọi `server.list_tools()` để discovery tools. Sau đó truyền server vào `Agent(mcp_servers=[...])` để agent có thể dùng tools. SDK tự xử lý communication giữa client và server qua Stdio.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Setup guide WSL (SETUP-WSL.md): giảng viên nhắc đến nhưng không được gửi trong session

---

# 112. Day 1 - Exploring Node-Based MCP Servers & Tool Access

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `112. Day 1 - Exploring Node-Based MCP Servers & Tool Access.txt`
- Slide: không có
- Code: đã dùng — `1_lab1.ipynb` (cells: playwright_params, files_params, MCPServerStdio cho cả hai)
- Summary lịch sử: không có
- Ghi chú về độ tin cậy: Transcript và code khớp nhau. Giảng viên walk-through code trực tiếp.

## 2. Executive Summary - Tóm tắt cốt lõi
- Chuyển sang Node-based MCP server (JavaScript), dùng `npx` thay vì `uvx`.
- Demo Playwright MCP server (`@playwright/mcp@latest`): cung cấp hàng chục tool chi tiết cho browser automation (navigate, click, type, screenshot, drag, hover, etc.).
- So sánh: fetch server chỉ có 1 tool đơn giản, Playwright server cho fine-grained control (kiểm soát chi tiết).
- Demo File System MCP server (`@modelcontextprotocol/server-filesystem`): tool đọc/ghi file, giới hạn trong sandbox directory.
- Pattern code giống hệt fetch: params → MCPServerStdio → list_tools(). Chỉ thay đổi params.
- Playwright MCP server do Microsoft tạo. File System server là reference implementation từ Anthropic.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu MCP server có thể viết bằng JavaScript/Node, không chỉ Python
  - So sánh granularity (độ chi tiết) giữa các MCP server khác nhau
  - Hiểu file system MCP server giới hạn trong sandbox path
- Practical goals - mục tiêu thực hành:
  - Chạy Playwright MCP server với npx
  - Chạy File System MCP server với npx
  - Liệt kê tools của cả hai server
- What learner should be able to explain - người học cần giải thích được:
  - Sự khác biệt giữa fetch (1 tool) và Playwright (nhiều tool chi tiết)
  - Tại sao sandbox path quan trọng cho file system server
  - Cách dùng npx trong params thay vì uvx

## 4. Previous Context - Liên hệ với bài trước
- Bài 111 giới thiệu MCPServerStdio với Python-based fetch server. Bài 112 mở rộng sang Node-based server.
- Pattern code hoàn toàn giống: chỉ thay params dictionary.
- Giảng viên nhắc Playwright đã dùng trong tuần 4 (week 4 sidekick agent).
- Fetch server từ bài trước cũng dùng Playwright nhưng chỉ expose 1 tool đơn giản.

## 5. Core Theory - Lý thuyết cốt lõi

### Node-based MCP Server
- Term: Node-based MCP Server
- Meaning: MCP server viết bằng JavaScript, chạy bằng Node.js qua lệnh `npx`
- Why it matters: Nhiều MCP server phổ biến viết bằng Node (Playwright, file system, etc.)
- Relationship: Tương đương Python-based server nhưng dùng npm ecosystem thay vì PyPI

### Playwright MCP Server
- Term: Playwright MCP Server (`@playwright/mcp@latest`)
- Meaning: MCP server do Microsoft tạo, cung cấp fine-grained browser automation tools
- Why it matters: Cho agent khả năng điều khiển browser chi tiết (click, type, screenshot, navigate, etc.)
- Relationship: So với fetch server (1 tool đơn giản), Playwright cho nhiều tool granular hơn

### File System MCP Server
- Term: File System MCP Server (`@modelcontextprotocol/server-filesystem`)
- Meaning: MCP server cho phép đọc/ghi file trên local file system, giới hạn trong sandbox directory
- Why it matters: Cho agent khả năng tương tác với file system nhưng có sandboxing an toàn
- Relationship: Reference implementation từ Anthropic, dùng sandbox_path để giới hạn quyền truy cập

### Tool Granularity
- Term: Tool Granularity (độ chi tiết của tool)
- Meaning: Mức độ chi tiết mà MCP server expose qua tools — từ 1 tool tổng hợp (fetch) đến hàng chục tool chi tiết (Playwright)
- Why it matters: Granularity cao cho agent linh hoạt hơn nhưng cũng phức tạp hơn
- Relationship: Trade-off giữa simplicity (fetch) và flexibility (Playwright)

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động

### Pipeline chung cho mọi MCP Server
1. Input: params dictionary với command (`npx` hoặc `uvx`) và args (package name + options)
2. Processing: `MCPServerStdio(params=..., client_session_timeout_seconds=60)` → spawn process
3. Output: `server.list_tools()` → danh sách tool objects
4. Control flow: Pattern giống hệt nhau cho mọi loại MCP server, chỉ thay params
5. Decision points: Chọn server nào tùy nhu cầu (browser automation, file system, etc.)

## 7. Techniques - Kỹ thuật sử dụng

### npx để chạy Node MCP Server
- Technique: Dùng `npx` trong params command để install và chạy Node-based MCP server
- Purpose: Tương đương `uvx` cho Python, nhưng dùng npm ecosystem
- When to use: Với JavaScript/Node-based MCP server
- Trade-off: Cần Node.js cài sẵn, version phải đủ mới
- Common mistake: Dùng Node version cũ → lỗi không rõ ràng. Cần cập nhật qua nvm.

### Sandbox Path cho File System
- Technique: Truyền sandbox path vào args của file system MCP server
- Purpose: Giới hạn quyền truy cập file system trong một directory cụ thể
- When to use: Khi dùng file system MCP server — luôn cần sandbox
- Trade-off: An toàn nhưng giới hạn scope hoạt động
- Common mistake: Quên tạo sandbox directory trước khi chạy

## 8. Code Walkthrough - Phân tích code nếu có

### File: `1_lab1.ipynb` — Playwright MCP Server

```python
playwright_params = {"command": "npx", "args": ["@playwright/mcp@latest"]}

async with MCPServerStdio(params=playwright_params, client_session_timeout_seconds=60) as server:
    playwright_tools = await server.list_tools()

playwright_tools
```
- Purpose: Spawn Playwright MCP server và liệt kê tools
- Key logic:
  - `"command": "npx"` — chạy Node package manager
  - `"args": ["@playwright/mcp@latest"]` — install và chạy Playwright MCP server bản mới nhất
  - Pattern code giống hệt fetch, chỉ thay params
- Important lines: `@playwright/mcp@latest` — chỉ định lấy version mới nhất
- Ghi chú: Kết quả trả về nhiều tool: browser_navigate, browser_click, browser_type, browser_screenshot, browser_close, browser_resize, browser_console_messages, browser_file_upload, browser_press_key, browser_drag, browser_hover, browser_select, etc.

### File: `1_lab1.ipynb` — File System MCP Server

```python
sandbox_path = os.path.abspath(os.path.join(os.getcwd(), "sandbox"))
files_params = {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", sandbox_path]}

async with MCPServerStdio(params=files_params, client_session_timeout_seconds=60) as server:
    file_tools = await server.list_tools()

file_tools
```
- Purpose: Spawn File System MCP server giới hạn trong sandbox directory
- Key logic:
  - `os.path.abspath(os.path.join(os.getcwd(), "sandbox"))` — tạo absolute path tới sandbox dir
  - `"-y"` flag trong args — auto-confirm npm install prompt
  - `sandbox_path` được truyền làm argument cuối — server chỉ access files trong path này
- Important lines: `sandbox_path` — đây là sandboxing mechanism
- Ghi chú: Tools trả về: read_file, read_multiple_files, write_file, create_directory, list_directory, move_file, search_files, get_file_info — tất cả giới hạn trong sandbox

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Fetch vs Playwright cho Browser Automation
- Option: Fetch MCP Server
  - Pros: Đơn giản, 1 tool duy nhất, nhanh
  - Cons: Chỉ lấy nội dung page, không tương tác được
  - When to choose: Khi chỉ cần đọc nội dung web page

- Option: Playwright MCP Server
  - Pros: Fine-grained control, click/type/screenshot/navigate, tương tác đầy đủ
  - Cons: Phức tạp hơn, nhiều tool hơn, tốn tài nguyên hơn
  - When to choose: Khi agent cần tương tác với web page (click button, fill form, etc.)

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Node version quá cũ
  - Root cause: MCP server cần Node version mới
  - Symptom: npx fail hoặc lỗi runtime
  - Fix: Dùng nvm (Node Version Manager) để update Node

- Failure mode: Sandbox directory chưa tồn tại
  - Root cause: `os.path.abspath(os.path.join(os.getcwd(), "sandbox"))` tạo path nhưng không tạo folder
  - Symptom: File system server không hoạt động đúng
  - Fix: Tạo folder `sandbox` trước khi chạy

- Failure mode: Nhầm fetch và Playwright
  - Root cause: Cả hai đều liên quan browser, nhưng granularity khác nhau hoàn toàn
  - Symptom: Dùng fetch khi cần click/interact → không được
  - Fix: Fetch = đọc page. Playwright = điều khiển browser.

## 11. Knowledge Extension - Kiến thức mở rộng
> Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- Playwright MCP server của Microsoft hỗ trợ cả headless mode (không hiện browser) và headed mode (hiện browser để debug). Mặc định là headless.
- `@modelcontextprotocol/server-filesystem` là một trong các reference server chính thức của Anthropic, nằm trong repo `modelcontextprotocol/servers` trên GitHub.
- npx flag `-y` tương đương `--yes` — tự động chấp nhận install prompt mà không cần user confirm.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Node-based MCP server dùng `npx` thay vì `uvx`
2. Playwright MCP server: `{"command": "npx", "args": ["@playwright/mcp@latest"]}` — nhiều tool chi tiết
3. File System server: `{"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", sandbox_path]}` — giới hạn trong sandbox
4. Pattern code giống hệt cho mọi MCP server: params → MCPServerStdio → list_tools()
5. Fetch = 1 tool đơn giản. Playwright = nhiều tool granular.
6. Cần Node.js version mới và npx hoạt động

### Self-check questions
1. Sự khác biệt giữa params cho Python MCP server và Node MCP server?
2. Playwright MCP server cung cấp những loại tool nào?
3. Tại sao file system MCP server cần sandbox path?
4. So sánh fetch vs Playwright về tool granularity.
5. Flag `-y` trong npm/npx có tác dụng gì?

### Flashcards
- Q: Params cho Playwright MCP server?
  A: `{"command": "npx", "args": ["@playwright/mcp@latest"]}`

- Q: Params cho File System MCP server?
  A: `{"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", sandbox_path]}`

- Q: Fetch vs Playwright — khác nhau thế nào?
  A: Fetch: 1 tool đơn giản (lấy nội dung page). Playwright: nhiều tool chi tiết (click, type, screenshot, navigate, etc.)

- Q: Sandbox path dùng để làm gì?
  A: Giới hạn file system MCP server chỉ truy cập files trong directory chỉ định, đảm bảo an toàn

### Interview Q&A
- Q: So sánh các loại MCP server bạn đã học (fetch, Playwright, file system) về use case và granularity.
  A: Fetch (Python-based, 1 tool): đọc nội dung web page đơn giản. Playwright (Node-based, 20+ tools): điều khiển browser chi tiết (click, type, navigate, screenshot). File System (Node-based, 8+ tools): đọc/ghi file local, sandboxed trong directory cụ thể. Trade-off chung: granularity cao = linh hoạt hơn nhưng phức tạp hơn cho LLM reasoning.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Node/Playwright setup guide (SETUP-node.md): giảng viên nhắc đến nhưng không được gửi

---

# 113. Day 1 - Building an Agent That Uses Multiple MCP Servers

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `113. Day 1 - Building an Agent That Uses Multiple MCP Servers.txt`
- Slide: không có
- Code: đã dùng — `1_lab1.ipynb` (cell: agent creation with mcp_servers, Runner.run, trace; markdown cell with marketplace links)
- Summary lịch sử: không có
- Ghi chú về độ tin cậy: Transcript và code khớp nhau. Bài dài, cover cả agent code lẫn MCP marketplace/security.

## 2. Executive Summary - Tóm tắt cốt lõi
- Tạo agent sử dụng nhiều MCP server cùng lúc: Playwright (browser) + File System (file I/O).
- Pattern: nested `async with MCPServerStdio` → tạo `Agent(mcp_servers=[...])` → `Runner.run(agent, task)`.
- Demo task: agent tìm recipe banoffee pie trên web → ghi file markdown vào sandbox.
- Agent instructions prompt: hướng dẫn agent browse web tự chủ, accept cookies, persistent until solved.
- Tracing: dùng `trace("investigate")` context manager để xem execution trong OpenAI platform.
- Giới thiệu MCP Marketplaces: mcp.so (4000+ research tools, 7344 developer tools), glama.ai (có security ratings), smithery.ai.
- Security: MCP server = chạy code người khác trên máy bạn ≈ pip install — cần due diligence (kiểm tra GitHub stars, community, publisher).
- End users (không phải developer) dùng MCP server nguy hiểm hơn vì không biết cách vet packages.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách kết hợp nhiều MCP server trong một agent
  - Hiểu MCP marketplace ecosystem
  - Hiểu security implications khi dùng MCP server
- Practical goals - mục tiêu thực hành:
  - Tạo agent với nhiều MCP server (browser + file system)
  - Chạy agent task end-to-end: web search → file write
  - Xem trace trong OpenAI platform
  - Khám phá MCP marketplaces
- What learner should be able to explain - người học cần giải thích được:
  - Cách truyền nhiều MCP server vào Agent constructor
  - Tại sao MCP security tương đương pip install security
  - Cách đánh giá MCP server an toàn

## 4. Previous Context - Liên hệ với bài trước
- Bài 111-112 giới thiệu từng MCP server riêng lẻ. Bài 113 kết hợp chúng trong một agent.
- OpenAI Agents SDK patterns (Agent, Runner, trace) đã học từ tuần 2.
- Playwright MCP server và File System server từ bài 112.
- Fetch MCP server từ bài 111.

## 5. Core Theory - Lý thuyết cốt lõi

### Multi-MCP-Server Agent
- Term: Multi-MCP-Server Agent
- Meaning: Agent được trang bị nhiều MCP server cùng lúc, mỗi server cung cấp toolset khác nhau
- Why it matters: Agent có thể kết hợp nhiều khả năng (browse web + write file + query database, etc.)
- Relationship: Dùng `Agent(mcp_servers=[server1, server2])` — SDK tự aggregate tools từ tất cả server

### MCP Marketplace
- Term: MCP Marketplace
- Meaning: Website liệt kê và phân loại MCP server có sẵn cho cộng đồng
- Why it matters: Đây là nơi discovery tools — thấy được ecosystem lớn của MCP
- Relationship: mcp.so, glama.ai/mcp, smithery.ai là 3 marketplace phổ biến nhất

### MCP Security Model
- Term: MCP Security Model
- Meaning: Running MCP server = running someone else's code on your machine ≈ pip install risk
- Why it matters: Cần vet MCP server như vet bất kỳ open source package nào
- Relationship: Glama.ai cung cấp security ratings (A/B/C) để đánh giá

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động

### Pipeline: Agent với nhiều MCP Server
1. Input: Agent instructions + task prompt ("Find banoffee pie recipe → write to markdown")
2. Processing steps:
   - Spawn MCP server 1 (file system) với `MCPServerStdio`
   - Spawn MCP server 2 (Playwright browser) với `MCPServerStdio`
   - Tạo Agent với `mcp_servers=[mcp_server_files, mcp_server_browser]`
   - SDK liệt kê tools từ cả 2 server → LLM biết tất cả tools
   - `Runner.run(agent, task)` → LLM tự chọn tool phù hợp → execute
3. Output: Agent browse web tìm recipe → ghi file markdown vào sandbox
4. Control flow: LLM tự quyết định tool nào dùng, thứ tự nào
5. Decision points: LLM chọn browser_navigate → browser_click → write_file tùy theo context

### Pipeline: Evaluating MCP Server Security
1. Check publisher (Microsoft, Anthropic = trusted)
2. Check GitHub repo (stars, community, activity)
3. Check marketplace ratings (Glama security score)
4. Consider Docker containerization cho extra isolation
5. Không dùng server không rõ nguồn gốc cho production

## 7. Techniques - Kỹ thuật sử dụng

### Nested Context Manager cho Multi-Server
- Technique: Nested `async with` để spawn nhiều MCP server
- Purpose: Mỗi server cần lifecycle management riêng
- When to use: Khi agent cần nhiều loại tool từ nhiều MCP server
- Trade-off: Code indent sâu hơn, nhưng đảm bảo cleanup đúng
- Common mistake: Đặt Agent creation ngoài context manager → server đã shutdown

### Agent Instructions Prompt
- Technique: Viết instructions cho agent biết cách browse web tự chủ
- Purpose: Hướng dẫn agent xử lý tình huống (cookies, popups, retry)
- When to use: Khi dùng browser automation MCP server
- Trade-off: Instructions chi tiết = behavior tốt hơn, nhưng dài hơn
- Common mistake: Không nói agent "be persistent" → agent bỏ cuộc sau 1 lần fail

### OpenAI Tracing
- Technique: `with trace("investigate"):` để wrap Runner.run
- Purpose: Xem execution trace trong OpenAI platform (tools called, order, responses)
- When to use: Luôn — đặc biệt khi debug agent behavior
- Trade-off: Nhỏ overhead nhưng rất hữu ích cho debugging
- Common mistake: Quên xem trace → không hiểu tại sao agent hành xử lạ

## 8. Code Walkthrough - Phân tích code nếu có

### File: `1_lab1.ipynb` — Agent với Multiple MCP Servers

```python
instructions = """
You browse the internet to accomplish your instructions.
You are highly capable at browsing the internet independently to accomplish your task, 
including accepting all cookies and clicking 'not now' as
appropriate to get to the content you need. If one website isn't fruitful, try another. 
Be persistent until you have solved your assignment,
trying different options and sites as needed.
"""

async with MCPServerStdio(params=files_params, client_session_timeout_seconds=60) as mcp_server_files:
    async with MCPServerStdio(params=playwright_params, client_session_timeout_seconds=60) as mcp_server_browser:
        agent = Agent(
            name="investigator", 
            instructions=instructions, 
            model="gpt-4.1-mini",
            mcp_servers=[mcp_server_files, mcp_server_browser]
            )
        with trace("investigate"):
            result = await Runner.run(agent, "Find a great recipe for Banoffee Pie, then summarize it in markdown to banoffee.md")
            print(result.final_output)
```
- Purpose: Tạo agent kết hợp 2 MCP server (file system + Playwright) để thực hiện task end-to-end
- Key logic:
  - Nested `async with` — mỗi MCPServerStdio spawn một server process riêng
  - `Agent(mcp_servers=[mcp_server_files, mcp_server_browser])` — truyền danh sách MCP server thay vì tools trực tiếp
  - `Runner.run(agent, task)` — SDK tự chạy agent loop: LLM → tool call → result → LLM → ...
  - `trace("investigate")` — wrap execution để xem trace trên OpenAI platform
- Important functions:
  - `Agent()`: tạo agent với name, instructions, model, mcp_servers
  - `Runner.run()`: chạy agent loop cho đến khi task hoàn thành
  - `trace()`: context manager cho OpenAI tracing
- Ghi chú:
  - Model `gpt-4.1-mini` — giảng viên chọn model mới nhất thời điểm quay
  - Instructions rất quan trọng: dạy agent cách handle cookies, popups, retry
  - Agent tự quyết định dùng Playwright tools (navigate, click) rồi file tools (write_file)
  - Kết quả: file `banoffee.md` được tạo trong sandbox directory

### Markdown cell: Marketplace Links
```markdown
https://mcp.so
https://glama.ai/mcp
https://smithery.ai/
https://huggingface.co/blog/LLMhacker/top-11-essential-mcp-libraries
https://huggingface.co/blog/Kseniase/mcp
```
- Purpose: Danh sách MCP marketplace và tài liệu tham khảo
- Ghi chú: mcp.so có 7344+ developer tools. Glama có security ratings. Smithery phổ biến với cộng đồng.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Đánh giá Security MCP Server
- Option: Chỉ dùng server từ publisher tin cậy (Microsoft, Anthropic)
  - Pros: An toàn nhất
  - Cons: Hạn chế lựa chọn
  - When to choose: Production environment

- Option: Dùng marketplace ratings (Glama A-grade)
  - Pros: Có đánh giá từ bên thứ ba
  - Cons: Rating có thể không cập nhật, false sense of security
  - When to choose: Khi cần thêm tool ngoài trusted publishers

- Option: Tự review code trên GitHub
  - Pros: Kiểm soát tối đa
  - Cons: Tốn thời gian, cần kỹ năng security review
  - When to choose: Khi dùng server ít phổ biến hoặc cho critical application

### Docker Isolation cho MCP Server
- Option: Chạy MCP server trực tiếp
  - Pros: Đơn giản, nhanh
  - Cons: Server có full access tới hệ thống (tùy thuộc tool)
  - When to choose: Development, trusted servers

- Option: Chạy trong Docker container
  - Pros: Isolation, giới hạn quyền truy cập
  - Cons: Setup phức tạp hơn, một số server không hỗ trợ
  - When to choose: Production, untrusted servers

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Agent creation ngoài MCP server context
  - Root cause: MCP server đã shutdown khi agent cần dùng tool
  - Symptom: Tool call fail, connection error
  - Fix: Đặt Agent creation và Runner.run bên trong nested `async with` blocks

- Failure mode: Agent không persistent khi browse web
  - Root cause: Instructions không dặn agent retry
  - Symptom: Agent bỏ cuộc sau 1 website fail
  - Fix: Thêm "be persistent", "try different options and sites" vào instructions

- Failure mode: Tin tưởng mọi MCP server trên marketplace
  - Root cause: Marketplace liệt kê nhưng không đảm bảo security
  - Symptom: Chạy malicious code trên máy
  - Fix: Due diligence: check publisher, GitHub stars, community, Glama ratings

## 11. Knowledge Extension - Kiến thức mở rộng
> Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- OpenAI Agents SDK internally liệt kê tools từ tất cả MCP server, merge chúng lại và gửi tool definitions tới LLM trong mỗi request. LLM không biết tool đến từ server nào — nó chỉ thấy flat list of tools.
- MCP server authentication (OAuth, API keys) đang được phát triển trong spec. Tính đến thời điểm bài học, remote/hosted server authentication vẫn chưa hoàn thiện.
- Banoffee pie là món tráng miệng Anh, gồm banana, toffee, cream trên base bánh quy. Giảng viên (người Anh) chọn ví dụ này có chủ đích để showcase agent browsing.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Nested `async with MCPServerStdio(...)` để spawn nhiều server
2. `Agent(mcp_servers=[server1, server2])` — truyền list MCP server
3. SDK tự aggregate tools từ tất cả server
4. Agent instructions cần chi tiết cho browser automation: cookies, retry, persistence
5. `trace()` để xem execution trên OpenAI platform
6. MCP Marketplaces: mcp.so, glama.ai/mcp, smithery.ai
7. MCP security ≈ pip install security — cần due diligence
8. Glama có security ratings A/B/C
9. End users không có kỹ năng vet packages — concern lớn hơn cho developer

### Self-check questions
1. Cách kết hợp nhiều MCP server trong một agent?
2. Tại sao agent instructions quan trọng cho browser automation?
3. trace() dùng để làm gì? Xem ở đâu?
4. 3 MCP marketplace phổ biến nhất?
5. MCP security risk tương đương với hành động nào?
6. Glama cung cấp thông tin bảo mật nào?
7. Tại sao end users dùng MCP nguy hiểm hơn developer?

### Flashcards
- Q: Cách truyền MCP server vào Agent?
  A: `Agent(mcp_servers=[mcp_server_files, mcp_server_browser])` — truyền list server objects

- Q: 3 MCP marketplace phổ biến?
  A: mcp.so, glama.ai/mcp, smithery.ai

- Q: MCP security risk tương đương gì?
  A: Tương đương pip install — bạn chạy code người khác trên máy mình, cần due diligence

- Q: Glama cung cấp gì đặc biệt?
  A: Security ratings (A/B/C) cho MCP server, đánh giá licensing và quality

- Q: Cách xem agent execution trace?
  A: Dùng `with trace("name"):` rồi vào https://platform.openai.com/traces

### Interview Q&A
- Q: Mô tả cách tạo một agent sử dụng nhiều MCP server và các bước security review cần thực hiện.
  A: (1) Spawn mỗi MCP server bằng MCPServerStdio trong nested context managers. (2) Tạo Agent với `mcp_servers=[...]` chứa tất cả server. (3) SDK tự liệt kê và aggregate tools. (4) Chạy Runner.run(agent, task). Security review: check publisher, GitHub stars, community activity, Glama security rating. Nếu critical: review source code. Nếu untrusted: chạy trong Docker container.

- Q: So sánh security risks giữa MCP server và pip install package.
  A: Tương đương nhau — cả hai đều là running third-party code on your machine. Khác biệt: MCP server tools có thể được LLM gọi tự động (agent autonomy), nên impact có thể lớn hơn vì developer không trực tiếp quyết định khi nào gọi tool. Mitigation: sandboxing (Docker, file path restrictions), trusted publishers, marketplace ratings.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- OpenAI trace UI screenshot: giảng viên nhắc đến nhưng không cung cấp
- Marketplace UI screenshots: giảng viên demo live nhưng không có screenshot

---

# 114. Day 1 - MCP Marketplaces & Security Considerations

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `114. Day 1 - MCP Marketplaces & Security Considerations.txt`
- Slide: không có
- Code: Code được cung cấp trong session (`1_lab1.ipynb`) nhưng chưa thấy code liên quan trực tiếp tới lesson này
- Summary lịch sử: không có
- Ghi chú về độ tin cậy: Transcript ngắn (46 dòng), tiếp nối trực tiếp bài 113. Nội dung rõ ràng, không mâu thuẫn.

## 2. Executive Summary - Tóm tắt cốt lõi
- Giới thiệu Smithery — MCP marketplace phổ biến thứ ba (sau mcp.so và Glama).
- Smithery cho phép xem MCP server details, tools, và lấy params trực tiếp (cần login).
- Giảng viên giới thiệu 2 bài viết HuggingFace hữu ích:
  - Top 11 Essential MCP Libraries (danh sách marketplace/resource)
  - Community article phân tích reality check cho MCP hype
- Tổng kết Day 1: Host/Client/Server, Python (uvx) vs JavaScript (npx), Stdio vs SSE, ecosystem giá trị.
- Preview Day 2: xây MCP server và client riêng để đóng góp vào ecosystem.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Biết thêm Smithery marketplace
  - Biết các tài liệu tham khảo chất lượng trên HuggingFace
  - Tổng kết kiến thức Day 1
- Practical goals - mục tiêu thực hành:
  - Khám phá Smithery marketplace
  - Đọc bài viết HuggingFace
- What learner should be able to explain - người học cần giải thích được:
  - Sự khác biệt giữa 3 marketplace (mcp.so, Glama, Smithery)
  - Tổng kết các kiến thức chính Day 1

## 4. Previous Context - Liên hệ với bài trước
- Bài 113 đã giới thiệu mcp.so và Glama. Bài 114 bổ sung Smithery và tài liệu HuggingFace.
- Bài 113 đã cover security. Bài 114 nhắc lại nhẹ qua Smithery context.
- Toàn bộ Day 1 (109-114) kết thúc ở đây, preview Day 2.

## 5. Core Theory - Lý thuyết cốt lõi

### Smithery Marketplace
- Term: Smithery (smithery.ai)
- Meaning: MCP marketplace phổ biến, cho phép browse/search MCP server, xem tools, lấy params
- Why it matters: Một trong 3 marketplace chính để discovery MCP server
- Relationship: Cùng loại với mcp.so và Glama, nhưng có UI khác và community riêng

### HuggingFace MCP Resources
- Term: HuggingFace MCP Blog Posts
- Meaning: Bài viết cộng đồng trên HuggingFace về MCP libraries, marketplace, và reality check
- Why it matters: Cung cấp curated list và phân tích objective về MCP hype vs reality
- Relationship: Bổ sung cho marketplace — giúp hiểu landscape tổng thể

### Day 1 Knowledge Synthesis
- Term: MCP Day 1 Core Concepts
- Meaning: Tổng hợp: Protocol (không phải framework), Host/Client/Server, Stdio/SSE, Python/Node, Ecosystem
- Why it matters: Foundation cho Day 2 trở đi (xây MCP server riêng)
- Relationship: Day 2 sẽ xây trên nền tảng này

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Không có pipeline rõ ràng trong tài liệu nguồn.

Luồng tổng kết Day 1:
1. MCP = protocol = USB-C of AI (bài 109)
2. Kiến trúc: Host → Client → Server, Stdio/SSE (bài 110)
3. Code: MCPServerStdio + params + list_tools (bài 111)
4. Node servers: Playwright + File System (bài 112)
5. Multi-server agent + marketplaces + security (bài 113)
6. Thêm marketplace (Smithery) + resources + recap (bài 114)

## 7. Techniques - Kỹ thuật sử dụng

### MCP Server Discovery qua Marketplace
- Technique: Dùng marketplace để tìm MCP server phù hợp
- Purpose: Discovery tools mới cho agent
- When to use: Khi cần mở rộng khả năng agent
- Trade-off: Nhiều lựa chọn nhưng cần vetting
- Common mistake: Chọn server không phổ biến hoặc không maintained

### Reality Check MCP Hype
- Technique: Đọc bài phân tích objective (HuggingFace community articles) để phân biệt hype vs reality
- Purpose: Tránh overestimate hoặc underestimate giá trị MCP
- When to use: Trước khi adopt MCP vào production
- Trade-off: Tốn thời gian đọc nhưng tránh sai lầm
- Common mistake: Tin hoàn toàn vào hype hoặc bác bỏ hoàn toàn — cần balanced view

## 8. Code Walkthrough - Phân tích code nếu có
Code được cung cấp trong session (`1_lab1.ipynb`) nhưng chưa thấy code liên quan trực tiếp tới lesson này. Bài 114 là bài recap/marketplace overview, không có code mới.

Notebook có markdown cell chứa links marketplace liên quan:
- https://mcp.so
- https://glama.ai/mcp
- https://smithery.ai/
- https://huggingface.co/blog/LLMhacker/top-11-essential-mcp-libraries
- https://huggingface.co/blog/Kseniase/mcp

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Chọn MCP Marketplace
- Option: mcp.so
  - Pros: Lớn nhất, nhiều category, search mạnh
  - Cons: Volume lớn có thể overwhelming
  - When to choose: Khi cần tìm server trong category cụ thể

- Option: Glama (glama.ai/mcp)
  - Pros: Có security ratings, licensing info, quality scores
  - Cons: Ít server hơn mcp.so
  - When to choose: Khi security là ưu tiên hàng đầu

- Option: Smithery (smithery.ai)
  - Pros: Phổ biến, dễ dùng, có thể lấy params trực tiếp
  - Cons: Cần login cho một số tính năng
  - When to choose: Khi cần nhanh chóng lấy params cho server phổ biến

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Chỉ dùng một marketplace
  - Root cause: Nghĩ một marketplace đã đủ
  - Symptom: Bỏ lỡ server tốt hoặc thiếu security info
  - Fix: Cross-reference giữa ít nhất 2 marketplace (Glama cho security, mcp.so cho volume)

- Failure mode: Bị cuốn vào MCP hype
  - Root cause: Không đọc balanced analysis
  - Symptom: Overengineer giải pháp với MCP khi đơn giản hơn có thể dùng function_tool
  - Fix: Đọc HuggingFace reality check articles, nhớ MCP chỉ hữu ích cho third-party tools

## 11. Knowledge Extension - Kiến thức mở rộng
> Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- Smithery cung cấp tính năng "one-click deploy" cho một số MCP server — đơn giản hóa việc setup.
- Cursor IDE có built-in MCP server support — có thể thêm MCP server trực tiếp vào cursor settings để arm coding assistant với tools.
- Anthropic duy trì repo `modelcontextprotocol/servers` trên GitHub chứa reference implementations — đây là nguồn server đáng tin cậy nhất.
- Awesome MCP Servers (awesome-mcp-servers trên GitHub) là curated list cộng đồng phổ biến nhất.

## 12. Study Pack - Gói ôn tập
### Must remember
1. Smithery (smithery.ai) — marketplace phổ biến thứ ba
2. HuggingFace có bài viết chất lượng về MCP landscape
3. Day 1 recap: MCP = protocol, Host/Client/Server, Stdio/SSE, Python(uvx)/Node(npx), Ecosystem
4. Day 2 preview: xây MCP server và client riêng
5. Cross-reference nhiều marketplace khi chọn MCP server

### Self-check questions
1. Smithery khác gì so với mcp.so và Glama?
2. 2 bài HuggingFace nào được giảng viên recommend?
3. Tóm tắt 5 kiến thức chính của Day 1 MCP.
4. Day 2 sẽ làm gì tiếp theo?
5. Tại sao cần cross-reference nhiều marketplace?

### Flashcards
- Q: 3 MCP marketplace chính?
  A: mcp.so (lớn nhất), glama.ai/mcp (có security ratings), smithery.ai (phổ biến, dễ dùng)

- Q: Tóm tắt Day 1 MCP trong 1 câu?
  A: MCP là protocol chuẩn hóa kết nối tool cho AI agent, kiến trúc Host/Client/Server, transport Stdio/SSE, ecosystem hàng nghìn tool qua marketplace.

- Q: Day 2 sẽ làm gì?
  A: Xây MCP server và client riêng để đóng góp vào ecosystem

- Q: Nguồn tham khảo MCP nào đáng tin nhất?
  A: Anthropic reference servers trên GitHub (modelcontextprotocol/servers), bài viết HuggingFace, và marketplace có security ratings (Glama)

### Interview Q&A
- Q: Bạn sẽ đánh giá và chọn MCP server từ marketplace như thế nào cho production?
  A: (1) Tìm trên nhiều marketplace (mcp.so, Glama, Smithery). (2) Check Glama security rating — chỉ dùng A-grade. (3) Xem publisher — ưu tiên Microsoft, Anthropic, hoặc org lớn. (4) Check GitHub repo: stars, active community, recent commits. (5) Đọc code/documentation. (6) Test trong sandbox trước khi deploy. (7) Cân nhắc Docker isolation cho untrusted server.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- HuggingFace blog posts: giảng viên nhắc nhưng nội dung bài viết không được gửi trong session
- Smithery UI screenshots: giảng viên demo live nhưng không cung cấp
