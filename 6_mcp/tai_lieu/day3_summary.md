# 119. Day 3 - Exploring Types of MCP Servers and Agent Memory

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `119. Day 3 - Exploring Types of MCP Servers and Agent Memory.txt`
- Slide: không có
- Code: đã dùng — `3_lab3.ipynb` (đặc biệt các cell 2-7 và 13)
- Summary lịch sử: đã dùng — `day1_summary.md`, `day2_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript và notebook khớp nhau. Lesson này dùng notebook trực tiếp cho phần memory MCP; phần remote/hosted MCP chủ yếu là giải thích khái niệm và ví dụ docs, không có code chạy thực tế trong session.

## 2. Executive Summary - Tóm tắt cốt lõi
- Day 3 mở đầu bằng việc phân loại lại 3 kiến trúc chính của MCP server: local-only, local server gọi cloud API, và remote/hosted MCP server.
- Lesson 119 tập trung nhất vào loại đầu tiên: local MCP server làm việc hoàn toàn với dữ liệu local, cụ thể là một memory server dạng knowledge graph - đồ thị tri thức.
- Memory trong “MCP age” không được xem như một khối duy nhất; nó chỉ là một tập tools/resources giúp LLM truy xuất thêm context (ngữ cảnh).
- MCP memory server trong ví dụ này lưu entities (thực thể), observations (quan sát) và relationships (quan hệ), tức là một dạng structured memory - bộ nhớ có cấu trúc.
- Instructor dùng `mcp-memory-libsql`, cấu hình `LIBSQL_URL=file:./memory/ed.db`, để tạo persistent memory - bộ nhớ bền vững theo từng agent/user.
- Cùng một MCP server memory được gắn lại cho agent ở lượt sau để chứng minh agent có thể “nhớ” thông tin về Ed qua các tool như `search_nodes`.
- Lesson cũng nhắc rằng remote/hosted MCP server hiện chưa phổ biến, thường gắn với dịch vụ enterprise trả phí và cần SSE/authentication.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu 3 kiểu kiến trúc MCP server trong thực tế.
  - Hiểu memory như một dạng capability (năng lực) của MCP thay vì một abstraction duy nhất.
  - Hiểu vì sao knowledge-graph memory khác với việc chỉ nhồi raw chat history vào prompt.
- Practical goals - mục tiêu thực hành:
  - Biết cách cấu hình và dùng một local MCP memory server.
  - Biết cách kiểm tra tool list và trace để hiểu memory server đang làm gì bên dưới.
  - Biết cách giữ memory tách theo từng database/file riêng cho từng agent hoặc user.
- What learner should be able to explain - người học cần giải thích được:
  - 3 loại MCP server khác nhau ở đâu.
  - MCP memory server lưu những loại thông tin nào.
  - Vì sao remote MCP server chưa phải pattern phổ biến trong cộng đồng.

## 4. Previous Context - Liên hệ với bài trước
- Day 1 đã giới thiệu Host - Client - Server và 3 kiểu kiến trúc MCP ở mức sơ đồ; lesson 119 quay lại chính sơ đồ đó nhưng lần này gắn với ví dụ thực tế hơn.
- Day 2 giúp người học tự viết accounts MCP server và client, nên đến Day 3 người học đã sẵn sàng để tiêu thụ thêm nhiều MCP servers có sẵn từ ecosystem.
- `day2_summary.md` nhấn mạnh lesson 118 rằng Day 3 sẽ quay về điểm mạnh nhất của MCP là “equip agent with lots of capabilities”; lesson 119 mở màn đúng theo hướng đó.
- Dự án capstone trading floor ở tuần 6 cần cả memory và market intelligence; lesson này đặt nền phần memory cho các agent research hoặc agent có hội thoại kéo dài.

## 5. Core Theory - Lý thuyết cốt lõi

### Three MCP deployment patterns - ba kiểu triển khai MCP
- Term - thuật ngữ: Three MCP deployment patterns - ba kiểu triển khai MCP
- Meaning - nghĩa: (1) local server làm việc hoàn toàn local, (2) local server gọi cloud API, (3) hosted/managed remote server chạy trên máy khác.
- Why it matters - vì sao quan trọng: Nó giúp bạn hiểu “server” trong MCP không đồng nghĩa với “remote service”.
- Relationship - liên hệ với khái niệm khác: Lesson 119 demo trực tiếp kiểu (1), báo trước kiểu (2), và giải thích hạn chế của kiểu (3).

### Knowledge graph memory - bộ nhớ dạng đồ thị tri thức
- Term - thuật ngữ: Knowledge graph memory - bộ nhớ dạng đồ thị tri thức
- Meaning - nghĩa: Cách lưu nhớ dưới dạng entities, observations và relationships thay vì chỉ lưu text tuần tự.
- Why it matters - vì sao quan trọng: Nó cho phép agent truy vấn có cấu trúc hơn, đặc biệt khi cần nhớ facts (sự kiện), người, vai trò và mối liên hệ.
- Relationship - liên hệ với khái niệm khác: Được expose như MCP tools để LLM có thể tạo node, tìm node, tạo relation, đọc graph.

### Memory as tools/context - memory như tools và context
- Term - thuật ngữ: Memory as tools/context - memory như tools và context
- Meaning - nghĩa: Trong kỷ nguyên MCP, memory không phải “một thành phần thần kỳ” mà là thêm một bộ capability giúp agent lấy thêm context khi cần.
- Why it matters - vì sao quan trọng: Cách nhìn này thực dụng hơn và phù hợp với thiết kế agent modular - mô-đun.
- Relationship - liên hệ với khái niệm khác: Nối trực tiếp với ý tưởng “MCP equips agents with capabilities” từ Day 2 và Day 1.

### Persistent memory store - kho nhớ bền vững
- Term - thuật ngữ: Persistent memory store - kho nhớ bền vững
- Meaning - nghĩa: Bộ nhớ được lưu ra SQLite/libSQL file, sống qua nhiều lượt chạy agent.
- Why it matters - vì sao quan trọng: Nếu không persistent thì agent chỉ “nhớ” trong một run/session ngắn.
- Relationship - liên hệ với khái niệm khác: `LIBSQL_URL=file:./memory/ed.db` chính là cấu hình đảm bảo persistence.

### Remote MCP server - MCP server hosted/managed từ xa
- Term - thuật ngữ: Remote MCP server - MCP server hosted/managed từ xa
- Meaning - nghĩa: MCP server không chạy trên máy người dùng mà chạy ở cloud hoặc máy của provider.
- Why it matters - vì sao quan trọng: Đây là hướng gắn với authentication (xác thực), enterprise integrations và SSE transport.
- Relationship - liên hệ với khái niệm khác: Instructor nhấn mạnh đây chưa phải pattern phổ biến so với local/server-calling-API.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động

### Luồng memory MCP server
1. Input:
   - Agent instructions yêu cầu dùng “entity tools” như persistent memory.
   - User cung cấp facts như “My name's Ed. I'm an LLM engineer...”.
2. Processing steps:
   - `MCPServerStdio` spawn `mcp-memory-libsql`.
   - Agent được trang bị các tools như `create_entities`, `create_relations`, `search_nodes`, `read_graph`.
   - LLM quyết định khi nào ghi nhớ và khi nào truy xuất lại dữ liệu.
3. Output:
   - Lượt đầu: memory database được tạo/cập nhật.
   - Lượt sau: agent trả lời lại được thông tin đã lưu về Ed.
4. Control flow / data flow:
   - User request -> Agent -> MCP memory tools -> libSQL/SQLite memory file -> result -> Agent response.
5. Decision points:
   - Chọn model/agent instructions có khuyến khích dùng memory không.
   - Chọn memory file riêng cho từng identity/agent.
   - Chọn giữ hay xóa memory file để reset state.

### Luồng kiến trúc remote MCP
1. Input:
   - Nhu cầu truy cập capability ở dịch vụ trả phí/enterprise như Asana, PayPal, Zapier.
2. Processing steps:
   - Host/client kết nối tới remote server qua SSE.
   - Provider xử lý auth và capability ở phía cloud.
3. Output:
   - Tool/resource results từ hosted system.
4. Control flow / data flow:
   - Host -> remote MCP endpoint -> provider service -> response.
5. Decision points:
   - Có thật sự cần remote server không.
   - Có auth/business account phù hợp không.

## 7. Techniques - Kỹ thuật sử dụng

### Memory server per identity - tách memory theo từng định danh
- Technique - kỹ thuật: Memory server per identity - tách memory theo từng định danh
- Purpose - mục đích: Giữ memory store riêng cho từng agent/user để tránh lẫn kiến thức.
- When to use - dùng khi nào: Khi nhiều agent hoặc nhiều user cùng chia sẻ một app/host.
- Trade-off - đánh đổi: Quản lý nhiều file/database hơn nhưng tránh cross-contamination - lẫn ngữ cảnh.
- Common mistake - lỗi dễ gặp: Dùng chung một memory store cho mọi người rồi khiến agent nhớ nhầm thông tin.

### Instructional priming for memory use - định hướng dùng memory bằng instructions
- Technique - kỹ thuật: Instructional priming for memory use - định hướng dùng memory bằng instructions
- Purpose - mục đích: Dạy agent rằng các entity tools đóng vai trò persistent memory.
- When to use - dùng khi nào: Khi LLM chưa chắc tự phát hiện vì sao hoặc khi nào nên dùng memory tools.
- Trade-off - đánh đổi: Instructions dài hơn nhưng tăng xác suất agent gọi đúng tools.
- Common mistake - lỗi dễ gặp: Trang bị memory tools nhưng không nói rõ agent nên dùng chúng ra sao.

### Trace-based memory debugging - debug memory bằng trace
- Technique - kỹ thuật: Trace-based memory debugging - debug memory bằng trace
- Purpose - mục đích: Xem agent đã gọi `search_nodes`/`create_entities` như thế nào và dữ liệu gì được trả về.
- When to use - dùng khi nào: Khi agent nhớ sai, quên thông tin, hoặc tạo graph không như kỳ vọng.
- Trade-off - đánh đổi: Tốn thời gian xem trace nhưng rất hữu ích để hiểu reasoning + tool flow.
- Common mistake - lỗi dễ gặp: Đổ lỗi cho “model tệ” khi thật ra graph memory được ghi sai hoặc query chưa đúng.

### Architectural classification before adoption - phân loại kiến trúc trước khi dùng
- Technique - kỹ thuật: Architectural classification before adoption - phân loại kiến trúc trước khi dùng
- Purpose - mục đích: Hiểu server nào local, server nào local-call-cloud, server nào remote.
- When to use - dùng khi nào: Trước khi gắn MCP server mới vào dự án thật.
- Trade-off - đánh đổi: Cần đọc docs/config kỹ hơn nhưng tránh hiểu sai boundary bảo mật và vận hành.
- Common mistake - lỗi dễ gặp: Thấy “server” là mặc định nghĩ đang gọi remote.

## 8. Code Walkthrough - Phân tích code nếu có

### File / block: `3_lab3.ipynb` cell 3
- Purpose - mục đích: Khởi tạo một local MCP memory server với persistent store đặt ở `./memory/ed.db`.
- Key logic - logic chính:
  - Dùng `npx -y mcp-memory-libsql` để tải/chạy server Node-based.
  - Truyền `env={"LIBSQL_URL": "file:./memory/ed.db"}` để memory được lưu bền vững.
  - Gọi `await server.list_tools()` để xem các memory capabilities.
- Important lines / functions:
  - `params = {"command": "npx", "args": ["-y", "mcp-memory-libsql"], "env": {"LIBSQL_URL": "file:./memory/ed.db"}}`
  - `await server.list_tools()`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là local MCP server đúng nghĩa: chạy trên máy local và lưu dữ liệu local.
  - `LIBSQL_URL` giúp biến memory từ “tạm thời” thành “persistent”.

### File / block: `3_lab3.ipynb` cells 4-6
- Purpose - mục đích: Chứng minh agent có thể ghi nhớ rồi truy xuất thông tin về Ed qua MCP memory tools.
- Key logic - logic chính:
  - Instructions nói rõ “You use your entity tools as persistent memory...”.
  - Lượt 1 cho agent facts về Ed và MCP.
  - Lượt 2 hỏi lại “What do you know about me?” để buộc agent truy xuất memory.
- Important lines / functions:
  - `instructions = "You use your entity tools as persistent memory..."`
  - `Agent(..., mcp_servers=[mcp_server])`
  - `Runner.run(agent, request)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Bản thân memory không tự chạy; LLM vẫn phải được “gợi ý” dùng đúng tools.
  - Vì cùng memory database được reuse, agent có thể nhớ lại facts ở lượt sau.

### File / block: `3_lab3.ipynb` cells 7 và 13
- Purpose - mục đích: Nhấn mạnh trace và docs như công cụ để hiểu memory behavior và remote MCP landscape.
- Key logic - logic chính:
  - Trace cho thấy agent dùng `search_nodes` và nhận về JSON graph structure.
  - Markdown cell 13 tổng hợp docs về remote MCP servers và Cloudflare deployment path.
- Important lines / functions:
  - URL `https://platform.openai.com/traces`
  - URL docs Anthropic remote MCP
  - URL docs Cloudflare remote MCP
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Dù không có code live cho remote MCP, cell markdown này là nguồn trực tiếp cho phần hosted/managed server trong transcript.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Local-only MCP server
- Option: Local-only memory/tool server
- Pros: Dễ hiểu, dễ kiểm soát dữ liệu, ít phụ thuộc bên ngoài, phù hợp cho prototyping.
- Cons: Capability bị giới hạn ở tài nguyên local.
- When to choose: Khi tool/memory chỉ cần thao tác trên máy local hoặc dữ liệu cục bộ.

### Option 2: Local MCP server gọi cloud API
- Option: Local server with remote API calls
- Pros: Vẫn giữ mô hình local process nhưng tận dụng dịch vụ mạnh từ bên ngoài.
- Cons: Cần API key, rate limits, phụ thuộc availability của provider.
- When to choose: Khi cần web search, market data, SaaS integrations nhưng vẫn muốn host/client spawn local.

### Option 3: Hosted/managed remote MCP server
- Option: Remote/managed MCP
- Pros: Provider vận hành server hộ, phù hợp enterprise integrations và centralized auth.
- Cons: Ít phổ biến, dễ flaky, thường cần paid account/business setup, phải dùng SSE.
- When to choose: Khi chính provider cung cấp capability dạng hosted và bạn đã ở trong ecosystem trả phí của họ.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Nghĩ memory là một khối abstraction cố định
  - Root cause: Ảnh hưởng từ một số framework cũ nơi “memory” bị đóng gói thành một khái niệm đơn.
  - Symptom: Thiết kế agent mơ hồ, không rõ memory thực ra là tools nào, context nào.
  - Fix / prevention: Xem memory như nhiều capabilities cụ thể: entities, observations, relationships, retrieval tools.

- Failure mode: Dùng chung một memory store cho nhiều agent/user
  - Root cause: Không tách file/db theo identity.
  - Symptom: Agent nhớ nhầm thông tin của người này sang người khác.
  - Fix / prevention: Tạo memory path riêng như `./memory/{name}.db`.

- Failure mode: Tưởng remote MCP server là mô hình mặc định
  - Root cause: Nghe chữ “server” rồi liên tưởng ngay tới cloud service.
  - Symptom: Thiết kế sai về security, auth, deployment, hoặc chọn nhầm transport.
  - Fix / prevention: Phân loại trước xem server đang chạy local hay remote.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- Knowledge-graph memory đặc biệt hữu ích khi agent cần suy luận về mối quan hệ giữa người, tổ chức, mục tiêu, vai trò và facts ổn định theo thời gian.
- Một số hệ thống production kết hợp nhiều dạng memory cùng lúc: short-term conversational memory, vector memory, structured entity memory, và external business records.
- Với remote MCP, authentication và authorization - xác thực và phân quyền - thường trở thành vấn đề trung tâm hơn cả tool design.

## 12. Study Pack - Gói ôn tập
### Must remember
- Day 3 quay lại 3 kiểu kiến trúc MCP: local-only, local-call-cloud, remote/managed.
- Lesson 119 demo thực tế một local MCP memory server.
- Memory trong MCP là một tập tools/context capabilities chứ không phải một “khối thần kỳ”.
- `mcp-memory-libsql` lưu entities, observations và relationships.
- `LIBSQL_URL=file:./memory/ed.db` tạo persistent memory cho riêng Ed.
- Remote MCP hiện chưa phổ biến như local MCP server hoặc local MCP server gọi API.

### Self-check questions
- 3 kiểu triển khai MCP server là gì?
- Tại sao instructor nói memory không phải chỉ là “một thứ”?
- Knowledge-graph memory lưu những loại thông tin nào?
- Vì sao cùng một memory file cho phép agent nhớ lại thông tin ở lượt sau?
- Tại sao remote/hosted MCP server chưa phải pattern phổ biến?

### Flashcards
- Q: `mcp-memory-libsql` là loại MCP server nào?
  A: Local-only MCP server chạy local và lưu memory local vào libSQL/SQLite file.

- Q: Knowledge-graph memory lưu gì?
  A: Entities, observations và relationships giữa các entities đó.

- Q: Tại sao cần `LIBSQL_URL`?
  A: Để chỉ định persistent memory store, giúp memory sống qua nhiều lượt chạy.

- Q: Remote MCP server thường dùng transport gì?
  A: SSE - Server-Sent Events.

### Interview Q&A nếu phù hợp
- Q: Hãy giải thích sự khác nhau giữa “memory as MCP capability” và “memory as one monolithic component”.
  A: “Memory as MCP capability” coi bộ nhớ là các tools/resources cụ thể mà agent gọi khi cần, ví dụ tạo entity, truy vấn graph, đọc observations. Cách này module hóa và minh bạch hơn. Ngược lại, “memory as one monolithic component” khiến thiết kế mơ hồ và khó kiểm soát: bạn không rõ model đang ghi gì, đọc gì, và bằng công cụ nào. Trong MCP, cách nhìn capability-based thực tế hơn và dễ debug hơn.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Không có screenshot trace hay memory file contents cụ thể trong session
- Không có một remote MCP server public ổn định để demo live, nên phần remote chủ yếu dừng ở docs và giải thích khái niệm

---

# 120. Day 3 - Brave Search API - MCP Server Calling the Web

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `120. Day 3 - Brave Search API - MCP Server Calling the Web.txt`
- Slide: không có
- Code: đã dùng — `3_lab3.ipynb` (đặc biệt các cell 8-13)
- Summary lịch sử: đã dùng — `day1_summary.md`, `day2_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript và notebook trùng khớp. Lesson này không dùng file Python nội bộ riêng; logic chính nằm ở params env, MCP server spawn và agent query trong notebook.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson 120 minh họa kiểu MCP server phổ biến nhất trong thực tế: server chạy local nhưng gọi remote web service.
- MCP server được dùng là Brave Search reference implementation của Anthropic, chạy local qua `npx` nhưng gọi Brave Search API bằng `BRAVE_API_KEY`.
- Đây là ví dụ rất rõ cho “architecture type 2”: code tải từ online, chạy trên máy local, rồi chính code đó gọi cloud API.
- Server expose các tools như `brave_web_search` và, với plan phù hợp, `local_search`.
- Instructor so sánh Brave Search với các công cụ tìm web trước đó như OpenAI hosted web search, Tavily, SerpAPI/Serp, nhấn mạnh Brave có free tier khá rộng.
- Agent được yêu cầu nghiên cứu tin tức mới nhất về Amazon stock price, đồng thời được cung cấp current date (ngày hiện tại) trong prompt để định khung thời gian.
- Lesson cũng củng cố thói quen xem trace để xác nhận query thực tế mà agent đã gửi đến Brave Search MCP server.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu local MCP server có thể làm proxy - cầu nối cho cloud API.
  - Hiểu sự khác nhau giữa browsing bằng browser/fetch và web search bằng search API.
  - Hiểu vai trò của environment variables khi MCP server cần credentials.
- Practical goals - mục tiêu thực hành:
  - Biết cấu hình Brave Search MCP server với `BRAVE_API_KEY`.
  - Biết list tools và gắn Brave Search server vào agent.
  - Biết viết request có current date để giảm ambiguity - mơ hồ về thời gian.
- What learner should be able to explain - người học cần giải thích được:
  - Tại sao Brave Search thuộc kiến trúc loại 2 chứ không phải remote MCP server.
  - MCP server local + cloud API hoạt động theo luồng nào.
  - Khi nào web search API tốt hơn browser automation/fetch.

## 4. Previous Context - Liên hệ với bài trước
- Lesson 119 vừa giới thiệu kiến trúc loại 2 như local server gọi remote service; lesson 120 là ví dụ code cụ thể đầu tiên của loại này trong Day 3.
- Day 1 từng dùng fetch và Playwright, cũng là local MCP servers gọi/đụng tới web. Lesson 120 mở rộng sang search API chuyên dụng thay vì browser/webpage retrieval.
- Day 2 đã dạy cách tự viết MCP server; giờ Day 3 chuyển sang tận dụng community/reference MCP servers để tăng capability cho agent nhanh hơn.
- Trong capstone trading floor, web search kiểu Brave có thể bổ sung tin tức thị trường bên cạnh market price tools sẽ xuất hiện ở lesson 121-122.

## 5. Core Theory - Lý thuyết cốt lõi

### Local MCP server calling cloud API - local server gọi API đám mây
- Term - thuật ngữ: Local MCP server calling cloud API - local server gọi API đám mây
- Meaning - nghĩa: MCP server được spawn trên máy local nhưng bản thân nó lại gọi ra internet để lấy kết quả từ provider.
- Why it matters - vì sao quan trọng: Đây là pattern rất phổ biến vì vừa giữ trải nghiệm MCP local, vừa tận dụng sức mạnh của dịch vụ bên ngoài.
- Relationship - liên hệ với khái niệm khác: Brave Search, Polygon, và nhiều SaaS MCP servers nằm trong nhóm này.

### Search API vs browser fetching - API tìm kiếm vs duyệt trang
- Term - thuật ngữ: Search API vs browser fetching - API tìm kiếm vs duyệt trang
- Meaning - nghĩa: Search API trả kết quả tìm kiếm đã được xếp hạng; browser/fetch lấy nội dung của một URL cụ thể hoặc thao tác trên giao diện web.
- Why it matters - vì sao quan trọng: Chúng phục vụ nhu cầu khác nhau; tin tức/thị trường mới nhất thường hợp với search API hơn.
- Relationship - liên hệ với khái niệm khác: Day 1 đã dùng Playwright/fetch; lesson này dùng Brave Search.

### Environment-backed MCP configuration - cấu hình MCP qua biến môi trường
- Term - thuật ngữ: Environment-backed MCP configuration - cấu hình MCP qua biến môi trường
- Meaning - nghĩa: Truyền API key và settings vào MCP server qua `env` trong params.
- Why it matters - vì sao quan trọng: Đây là cách phổ biến để giữ secrets tách khỏi code và để MCP server dùng được credentials khi spawn.
- Relationship - liên hệ với khái niệm khác: `BRAVE_API_KEY` là ví dụ trực tiếp; lesson 121-122 sẽ dùng `POLYGON_API_KEY`.

### Time grounding in prompts - neo thời gian trong prompt
- Term - thuật ngữ: Time grounding in prompts - neo thời gian trong prompt
- Meaning - nghĩa: Ghi current date (ngày hiện tại) ngay trong request để truy vấn “latest news” có mốc thời gian cụ thể.
- Why it matters - vì sao quan trọng: Giảm nguy cơ agent trả kết quả cũ hoặc query mơ hồ.
- Relationship - liên hệ với khái niệm khác: Quan trọng đặc biệt cho market/news use case.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - `BRAVE_API_KEY` từ `.env`
   - Query như “latest news on Amazon stock price”
   - Current date được chèn vào prompt
2. Processing steps:
   - Notebook tạo `env = {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}`.
   - `MCPServerStdio` spawn `@modelcontextprotocol/server-brave-search` qua `npx`.
   - Agent được gắn với MCP server và chọn tool web search phù hợp.
   - MCP server gọi Brave Search cloud API bằng key đã cấp.
3. Output:
   - Kết quả web search và phần tóm tắt outlook - triển vọng ngắn gọn cho Amazon stock.
4. Control flow / data flow:
   - User request -> Agent -> Brave Search MCP tool -> Brave API -> search results -> Agent summary.
5. Decision points:
   - Có API key hợp lệ hay không.
   - Chọn search API thay vì fetch/browser.
   - Chọn free vs paid plan ảnh hưởng tool surface như `local_search`.

## 7. Techniques - Kỹ thuật sử dụng

### API-key injection through MCP params - truyền API key qua MCP params
- Technique - kỹ thuật: API-key injection through MCP params - truyền API key qua MCP params
- Purpose - mục đích: Cho phép server local truy cập cloud API có xác thực.
- When to use - dùng khi nào: Với mọi MCP server cần credentials để gọi provider bên ngoài.
- Trade-off - đánh đổi: Dễ cấu hình nhưng phải quản lý env cẩn thận.
- Common mistake - lỗi dễ gặp: Quên reload `.env` hoặc truyền nhầm key name khiến server spawn được nhưng tool call fail.

### Search-specific prompting - viết prompt phù hợp cho search
- Technique - kỹ thuật: Search-specific prompting - viết prompt phù hợp cho search
- Purpose - mục đích: Làm rõ agent cần “research latest news” chứ không chỉ trả giá cổ phiếu đơn lẻ.
- When to use - dùng khi nào: Khi dùng search tool cho market/news intelligence.
- Trade-off - đánh đổi: Prompt dài hơn một chút nhưng hướng agent đúng hơn.
- Common mistake - lỗi dễ gặp: Query quá ngắn khiến kết quả search không tập trung.

### Trace validation for search queries - xác thực query bằng trace
- Technique - kỹ thuật: Trace validation for search queries - xác thực query bằng trace
- Purpose - mục đích: Kiểm tra agent thật sự đã hỏi Brave điều gì.
- When to use - dùng khi nào: Khi kết quả search không liên quan, quá cũ, hoặc bias do query formulation.
- Trade-off - đánh đổi: Thêm bước kiểm tra nhưng giúp tune prompt tốt hơn.
- Common mistake - lỗi dễ gặp: Chỉ nhìn final answer mà không xem query gốc agent đã gửi đi.

## 8. Code Walkthrough - Phân tích code nếu có

### File / block: `3_lab3.ipynb` cell 9
- Purpose - mục đích: Cấu hình Brave Search MCP server bằng Node và environment variable cho API key.
- Key logic - logic chính:
  - Đọc `BRAVE_API_KEY` từ `.env`.
  - Truyền `env` vào params của MCP server.
  - List tools để xác nhận server đã expose `brave_web_search`.
- Important lines / functions:
  - `env = {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}`
  - `params = {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-brave-search"], "env": env}`
  - `await server.list_tools()`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là pattern chuẩn khi MCP server local cần credentials cho cloud API.
  - Từ phía host, bạn vẫn chỉ đang nói chuyện với local process.

### File / block: `3_lab3.ipynb` cells 10-11
- Purpose - mục đích: Cho agent dùng Brave Search MCP tool để nghiên cứu tin tức mới nhất về Amazon stock.
- Key logic - logic chính:
  - Request chèn `datetime.now().strftime('%Y-%m-%d')` để neo mốc thời gian.
  - Agent dùng MCP server qua `mcp_servers=[mcp_server]`.
  - Final output là một brief summary - tóm tắt ngắn gọn.
- Important lines / functions:
  - `request = f"Please research the latest news on Amazon stock price... {datetime.now().strftime('%Y-%m-%d')}"`
  - `Agent(..., mcp_servers=[mcp_server])`
  - `Runner.run(agent, request)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Việc truyền current date trực tiếp vào prompt rất hợp lý cho bài toán “latest news”.
  - Tool này khác fetch ở chỗ nó trả search results, không phải đi mở từng website bằng browser.

### File / block: `3_lab3.ipynb` cell 12
- Purpose - mục đích: Nhắc người học dùng trace để xác minh query và tool usage.
- Key logic - logic chính:
  - Trace cho thấy agent đã gọi `brave_web_search` với query nào.
  - Đây là nguồn quan trọng để debug prompt và độ chính xác thông tin.
- Important lines / functions:
  - URL `https://platform.openai.com/traces`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Với search tools, trace gần như là nơi tốt nhất để xem agent “nghĩ” gì khi tạo query.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Brave Search MCP server
- Option: Brave Search MCP
- Pros: Free tier hào phóng, tích hợp chuẩn MCP, phù hợp news/web search cho AI workflows.
- Cons: Cần API key, phụ thuộc provider bên ngoài, local business search có thể giới hạn theo plan.
- When to choose: Khi cần market/news research nhanh và không muốn browser automation.

### Option 2: Fetch/Playwright MCP servers
- Option: Browser/fetch style retrieval
- Pros: Truy cập trực tiếp webpage, phù hợp khi cần nội dung cụ thể hoặc tương tác giao diện.
- Cons: Chậm hơn, dễ vướng cookies/popups, không tối ưu cho “search broad landscape”.
- When to choose: Khi đã biết site/URL hoặc cần thao tác web chi tiết.

### Option 3: Hosted search tool từ provider framework
- Option: Framework-hosted web search
- Pros: Dùng nhanh, ít config local.
- Cons: Có thể đắt hơn hoặc ít kiểm soát hơn.
- When to choose: Khi framework bạn dùng đã có hosted search tool đủ tốt và chi phí chấp nhận được.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Nhầm Brave Search là remote MCP server
  - Root cause: Vì nó gọi web nên người học tưởng server cũng chạy remote.
  - Symptom: Hiểu sai mô hình bảo mật/deployment.
  - Fix / prevention: Nhớ rằng code MCP server vẫn được tải về và chạy local qua `npx`.

- Failure mode: Quên truyền `BRAVE_API_KEY`
  - Root cause: `.env` chưa có key, hoặc `load_dotenv()` chưa reload.
  - Symptom: Server có thể spawn nhưng tool call thất bại hoặc trả lỗi auth.
  - Fix / prevention: Kiểm tra env trước khi chạy và list tools/trace sau khi chạy.

- Failure mode: Dùng search API cho bài toán cần content extraction cụ thể
  - Root cause: Chọn sai công cụ.
  - Symptom: Kết quả tổng quan nhưng thiếu chi tiết nội dung từ site cụ thể.
  - Fix / prevention: Dùng search để discovery, fetch/browser để deep dive.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- Search MCP servers rất hữu ích khi ghép với memory MCP server: agent có thể vừa tìm tin tức mới vừa lưu facts bền vững về user hoặc project.
- Trong production, search results còn thường cần thêm reranking - xếp hạng lại, source filtering - lọc nguồn, hoặc grounding rules - quy tắc bám nguồn.
- Việc truyền current date trong prompt là một soft grounding - neo mềm, còn một số hệ thống nâng cao sẽ tạo dedicated date/time tool riêng.

## 12. Study Pack - Gói ôn tập
### Must remember
- Brave Search là ví dụ điển hình của MCP server local gọi cloud API.
- Server chạy local qua `npx`, nhưng dùng `BRAVE_API_KEY` để gọi Brave Search service.
- Search API khác browser automation/fetch.
- Chèn current date vào prompt giúp query “latest” rõ ràng hơn.
- Trace rất quan trọng để kiểm tra query thực mà agent gửi.

### Self-check questions
- Vì sao Brave Search thuộc kiến trúc MCP loại 2?
- Sự khác nhau giữa Brave Search và fetch/Playwright là gì?
- Tại sao cần `BRAVE_API_KEY` trong `env`?
- Vì sao nên cho current date vào prompt?
- Khi nào search API không phải lựa chọn tốt nhất?

### Flashcards
- Q: `@modelcontextprotocol/server-brave-search` chạy ở đâu?
  A: Chạy local trên máy bạn qua `npx`, rồi từ đó gọi Brave Search cloud API.

- Q: Brave Search MCP cần biến môi trường nào?
  A: `BRAVE_API_KEY`.

- Q: Tool chính từ server này là gì?
  A: `brave_web_search`; với plan phù hợp còn có thể có `local_search`.

- Q: Tại sao nên xem trace sau khi search?
  A: Để kiểm tra query thực tế mà agent đã gửi và debug chất lượng kết quả.

### Interview Q&A nếu phù hợp
- Q: So sánh một MCP search server như Brave Search với browser-based MCP servers như Playwright hoặc fetch.
  A: Brave Search phù hợp cho discovery - khám phá và tổng hợp nhanh từ web vì nó dùng search API chuyên biệt. Playwright/fetch phù hợp khi đã biết site hoặc cần lấy nội dung trực tiếp từ webpage, thao tác tương tác, hoặc xử lý UI. Search API thường nhanh và gọn hơn cho market/news intelligence, còn browser tools sâu hơn nhưng nặng hơn và dễ vướng lỗi giao diện.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Không có trace screenshot hoặc raw Brave API response trong session
- Không có chi tiết pricing/plan đầy đủ từ website Brave, chỉ có mô tả từ transcript

---

# 121. Day 3 - Integrating Polygon API for Stock Market Data

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `121. Day 3 - Integrating Polygon API for Stock Market Data.txt`
- Slide: không có
- Code: đã dùng — `3_lab3.ipynb`, `market.py`, `market_server.py`
- Summary lịch sử: đã dùng — `day1_summary.md`, `day2_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript khớp với notebook và code. Đã scan thêm `database.py` trong `G:\Agent2026Win\agents\6_mcp` vì lesson này nói rõ market data được cache vào database để né rate limiting của free plan.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson 121 đưa capstone tiến gần trading floor thật hơn bằng cách trang bị market data thực từ Polygon.io cho các agent.
- Polygon.io được chọn vì vừa có free plan vừa có paid plan, nên cùng một provider có thể phục vụ cả học tập lẫn nâng cấp.
- Free plan của Polygon chỉ cho dữ liệu end-of-day - giá đóng cửa ngày trước và bị rate limited khá gắt.
- Để giải quyết rate limit, `market.py` không gọi giá từng mã lẻ lặp đi lặp lại; thay vào đó nó tải toàn bộ grouped daily market snapshot cho ngày close gần nhất rồi cache vào database.
- `get_share_price(symbol)` là hàm façade - điểm vào gọn, tự quyết định dùng free-plan EOD hay paid-plan minute snapshot.
- `market_server.py` tiếp tục áp dụng pattern Day 2: bọc business logic thành MCP server mỏng, chỉ expose một tool `lookup_share_price`.
- Agent sau đó có thể trả lời câu hỏi như “What’s the share price of Apple?” thông qua market MCP server riêng của dự án.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu cách tích hợp market data provider vào kiến trúc MCP cho capstone.
  - Hiểu vì sao free API constraints - giới hạn API miễn phí ảnh hưởng trực tiếp tới thiết kế tool.
  - Hiểu pattern cache toàn thị trường để vượt rate limit hợp lý.
- Practical goals - mục tiêu thực hành:
  - Biết cấu hình `POLYGON_API_KEY`.
  - Biết dùng trực tiếp `RESTClient` của Polygon để gọi previous close.
  - Biết gói `market.py` thành MCP server qua `market_server.py`.
- What learner should be able to explain - người học cần giải thích được:
  - `market.py` tối ưu free plan như thế nào.
  - `market_server.py` mỏng ở đâu và vì sao đó là pattern tốt.
  - Vì sao AAPL query trong agent có thể được giải quyết qua custom market MCP server.

## 4. Previous Context - Liên hệ với bài trước
- Day 2 đã dạy cách bọc business logic thành custom MCP server với `accounts_server.py`; lesson 121 áp dụng lại đúng pattern đó cho domain market data.
- Day 3 lesson 120 vừa giới thiệu loại MCP server local gọi cloud API; Polygon free-plan flow chính là ví dụ thứ hai của loại đó.
- `day2_summary.md` cho thấy accounts server quản lý simulated portfolio. Lesson 121 bổ sung nguồn dữ liệu thị trường thật để capstone có simulated execution nhưng real market context.
- Đây là điểm nối trực tiếp giữa “account management” của Day 2 và “market intelligence” cần cho trading floor ở các ngày tiếp theo.

## 5. Core Theory - Lý thuyết cốt lõi

### Rate limiting aware design - thiết kế có ý thức về rate limit
- Term - thuật ngữ: Rate limiting aware design - thiết kế có ý thức về giới hạn tần suất gọi API
- Meaning - nghĩa: Thiết kế tool/business logic dựa trên giới hạn thực tế của provider thay vì giả định API được gọi tự do.
- Why it matters - vì sao quan trọng: Với free plan của Polygon, gọi từng ticker nhiều lần sẽ nhanh chóng chạm ngưỡng.
- Relationship - liên hệ với khái niệm khác: Dẫn trực tiếp tới grouped snapshot caching trong `market.py`.

### Market snapshot caching - cache snapshot toàn thị trường
- Term - thuật ngữ: Market snapshot caching - lưu đệm snapshot toàn thị trường
- Meaning - nghĩa: Tải toàn bộ giá đóng cửa của thị trường cho ngày trước đó một lần, sau đó tra từng symbol từ cache/database.
- Why it matters - vì sao quan trọng: Một lần gọi API phục vụ được rất nhiều truy vấn symbol mà không bị rate limit.
- Relationship - liên hệ với khái niệm khác: `get_market_for_prior_date()` dùng `lru_cache` + SQLite persistence.

### Free-plan EOD fallback - cơ chế fallback dữ liệu đóng cửa ngày trước
- Term - thuật ngữ: Free-plan EOD fallback - cơ chế fallback dữ liệu đóng cửa ngày trước
- Meaning - nghĩa: Nếu không phải paid plan thì trả giá từ previous business day close thay vì minute-level near realtime.
- Why it matters - vì sao quan trọng: Đảm bảo hệ thống vẫn hoạt động ổn trên free tier.
- Relationship - liên hệ với khái niệm khác: `get_share_price_polygon()` chọn giữa EOD và minute snapshot.

### Thin MCP wrapper for market data - wrapper MCP mỏng cho dữ liệu thị trường
- Term - thuật ngữ: Thin MCP wrapper for market data - wrapper MCP mỏng cho dữ liệu thị trường
- Meaning - nghĩa: `market_server.py` chỉ công bố tool `lookup_share_price` và delegate toàn bộ logic xuống `market.py`.
- Why it matters - vì sao quan trọng: Giữ protocol layer đơn giản, để policy/caching/API logic ở module domain.
- Relationship - liên hệ với khái niệm khác: Lặp lại design tốt đã thấy ở `accounts_server.py`.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - `POLYGON_API_KEY`
   - Stock symbol như `AAPL`
   - Plan state: free hoặc paid
2. Processing steps:
   - `market.py` kiểm tra plan.
   - Nếu free: lấy previous close grouped market data, cache vào DB và `lru_cache`.
   - Nếu paid: lấy minute snapshot cho ticker cụ thể.
   - `market_server.py` expose `lookup_share_price` làm MCP tool.
   - Agent gọi MCP tool để trả lời câu hỏi giá cổ phiếu.
3. Output:
   - Giá cổ phiếu của symbol yêu cầu, ví dụ Apple.
4. Control flow / data flow:
   - User request -> Agent -> `lookup_share_price` -> `get_share_price` -> Polygon API / DB cache -> result -> Agent response.
5. Decision points:
   - Chọn free plan hay paid plan.
   - Dùng cache grouped market hay ticker snapshot.
   - Có MCP wrap tool này riêng hay gọi library trực tiếp.

## 7. Techniques - Kỹ thuật sử dụng

### Full-market fetch to amortize API limits - gọi toàn thị trường để dàn mỏng chi phí API
- Technique - kỹ thuật: Full-market fetch to amortize API limits - gọi toàn thị trường để dàn mỏng chi phí API
- Purpose - mục đích: Tránh việc mỗi ticker query lại tốn một API call riêng.
- When to use - dùng khi nào: Khi provider cho phép snapshot bulk và free plan bị giới hạn mạnh.
- Trade-off - đánh đổi: Tải nhiều dữ liệu hơn mức truy vấn hiện tại nhưng giảm mạnh số lần gọi API.
- Common mistake - lỗi dễ gặp: Chỉ tối ưu cho truy vấn “một ticker” mà quên rằng agent sẽ hỏi nhiều ticker khác nhau trong cùng ngày.

### Dual-layer caching - cache hai lớp
- Technique - kỹ thuật: Dual-layer caching - cache hai lớp
- Purpose - mục đích: Kết hợp `lru_cache` trong process với SQLite persistence trong DB.
- When to use - dùng khi nào: Khi muốn vừa nhanh trong cùng process, vừa giữ kết quả qua nhiều lần chạy.
- Trade-off - đánh đổi: Logic cache phức tạp hơn một chút nhưng hiệu quả hơn.
- Common mistake - lỗi dễ gặp: Chỉ dùng memory cache nên restart process là mất lợi ích.

### Tool abstraction over raw SDK client - trừu tượng hóa tool trên client thô
- Technique - kỹ thuật: Tool abstraction over raw SDK client - trừu tượng hóa tool trên client thô
- Purpose - mục đích: Đưa một API library như Polygon thành capability mà agent có thể tự gọi.
- When to use - dùng khi nào: Khi logic cần được agent-driven thay vì coder-driven.
- Trade-off - đánh đổi: Cần thêm một lớp server/tool wrapper.
- Common mistake - lỗi dễ gặp: Để agent phụ thuộc vào raw code snippets thay vì capability đóng gói rõ ràng.

## 8. Code Walkthrough - Phân tích code nếu có

### File / block: `3_lab3.ipynb` cells 17-18
- Purpose - mục đích: Xác thực `POLYGON_API_KEY` và demo cách dùng Polygon client trực tiếp.
- Key logic - logic chính:
  - Đọc `POLYGON_API_KEY` từ `.env`.
  - Dùng `RESTClient` và gọi `get_previous_close_agg("AAPL")[0]`.
- Important lines / functions:
  - `polygon_api_key = os.getenv("POLYGON_API_KEY")`
  - `client = RESTClient(polygon_api_key)`
  - `client.get_previous_close_agg("AAPL")[0]`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là baseline trực tiếp trước khi instructor bọc nó vào module và MCP server.
  - Rất quan trọng để thấy custom wrapper không “phát minh lại” provider, chỉ tổ chức cách dùng provider hợp với agent system.

### File / block: [market.py](G:\Agent2026Win\agents\6_mcp\market.py)
- Purpose - mục đích: Gói logic truy xuất market data, chọn plan, cache dữ liệu và cung cấp API gọn cho phần còn lại của dự án.
- Key logic - logic chính:
  - `get_all_share_prices_polygon_eod()` lấy grouped daily market close cho ngày close gần nhất.
  - `get_market_for_prior_date(today)` dùng `lru_cache` và `read_market`/`write_market` để cache/persist snapshot.
  - `get_share_price_polygon_eod(symbol)` tra giá symbol từ market snapshot đã cache.
  - `get_share_price_polygon_min(symbol)` dùng `get_snapshot_ticker` cho paid plan.
  - `get_share_price(symbol)` là façade cuối cùng, fallback sang random nếu không dùng được Polygon API.
- Important lines / functions:
  - `is_paid_polygon`, `is_realtime_polygon`
  - `def get_all_share_prices_polygon_eod()`
  - `@lru_cache(maxsize=2)`
  - `def get_market_for_prior_date(today)`
  - `def get_share_price_polygon(symbol)`
  - `def get_share_price(symbol)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Thiết kế hay nhất ở đây là không để rate limit quyết định UI/agent behavior; thay vào đó module xử lý chuyện đó bên trong.
  - Fallback random number chỉ là safety net cho demo, không phải dữ liệu production-grade.
  - Comment “thanks to student Reema...” cho thấy code đã được tinh chỉnh vì timezone issue thực tế.

### File / block: [database.py](G:\Agent2026Win\agents\6_mcp\database.py)
- Purpose - mục đích: Lưu snapshot market theo date để lần sau không cần gọi lại API miễn phí.
- Key logic - logic chính:
  - Bảng `market(date, data)` lưu JSON snapshot theo ngày.
  - `write_market()` upsert snapshot.
  - `read_market()` khôi phục snapshot cũ.
- Important lines / functions:
  - `CREATE TABLE IF NOT EXISTS market`
  - `def write_market(date: str, data: dict)`
  - `def read_market(date: str) -> dict | None`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là persistence companion cho `market.py`, biến cache từ “trong RAM” thành “sống qua nhiều lần chạy”.

### File / block: [market_server.py](G:\Agent2026Win\agents\6_mcp\market_server.py)
- Purpose - mục đích: Expose một MCP tool gọn để agent hỏi giá cổ phiếu.
- Key logic - logic chính:
  - Tạo `FastMCP("market_server")`.
  - Định nghĩa `lookup_share_price(symbol: str)` và delegate sang `get_share_price(symbol)`.
  - Chạy server qua `stdio`.
- Important lines / functions:
  - `mcp = FastMCP("market_server")`
  - `@mcp.tool()`
  - `async def lookup_share_price(symbol: str) -> float`
  - `mcp.run(transport='stdio')`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là “thin wrapper” rất đẹp: tất cả logic khó nằm ở `market.py`, còn server chỉ làm giao diện MCP.

### File / block: `3_lab3.ipynb` cells 23-25
- Purpose - mục đích: Kiểm tra custom market MCP server và cho agent dùng nó để trả lời giá cổ phiếu Apple.
- Key logic - logic chính:
  - Spawn `market_server.py` qua `uv run`.
  - List tools để xác nhận `lookup_share_price`.
  - Gắn server vào `Agent` và hỏi “What's the share price of Apple?”
- Important lines / functions:
  - `params = {"command": "uv", "args": ["run", "market_server.py"]}`
  - `await server.list_tools()`
  - `Runner.run(agent, request)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Instructor kỳ vọng model biết Apple -> `AAPL`, tức là có thêm một chút reasoning ở phía LLM trước khi gọi tool.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Dùng free Polygon plan + custom cached MCP server
- Option: Free-plan cached market server
- Pros: Chi phí thấp, vẫn dùng được trong capstone, né rate limit bằng grouped snapshot cache.
- Cons: Chỉ có end-of-day prices, không đủ real-time.
- When to choose: Khi học tập, demo, hoặc làm simulated trading không cần dữ liệu phút gần thời gian thực.

### Option 2: Dùng paid Polygon plan cho minute-level snapshot
- Option: Paid-plan near-realtime market access
- Pros: Dữ liệu mới hơn, ít bị hạn chế hơn.
- Cons: Tốn phí hàng tháng.
- When to choose: Khi cần trading agent có dữ liệu mới hơn EOD và query nhiều hơn.

### Option 3: Gọi Polygon SDK trực tiếp thay vì qua MCP
- Option: Direct code integration
- Pros: Ít lớp hơn, nhanh cho script truyền thống.
- Cons: Agent không tự gọi được như một capability chuẩn hóa.
- When to choose: Khi không cần tool-calling từ LLM hoặc không dùng MCP/agent framework.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Gọi previous close cho từng symbol liên tục trên free plan
  - Root cause: Bỏ qua rate limit.
  - Symptom: Nhanh chóng bị API từ chối hoặc hệ thống chậm/chập chờn.
  - Fix / prevention: Dùng grouped market snapshot + cache như `market.py`.

- Failure mode: Trộn business logic, API access và MCP server vào một file
  - Root cause: Tối ưu cho code ngắn hạn.
  - Symptom: File khó đọc, khó test, khó nâng cấp plan logic.
  - Fix / prevention: Tách `market.py`, `database.py`, `market_server.py`.

- Failure mode: Dùng fallback random price mà quên đó chỉ là demo fallback
  - Root cause: Không chú ý phần exception handling trong `get_share_price`.
  - Symptom: Hệ thống tưởng đang dùng real market data nhưng thực ra đang random.
  - Fix / prevention: Với ứng dụng nghiêm túc, thay fallback này bằng lỗi rõ ràng hoặc mock minh bạch hơn.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- Pattern “bulk fetch + local cache + MCP wrapper” là một mẫu rất mạnh cho nhiều external APIs chứ không chỉ market data.
- Với market systems thật, bạn còn cần xác định freshness policy - chính sách độ mới của dữ liệu, staleness detection - phát hiện dữ liệu cũ, và auditability - khả năng kiểm toán dữ liệu đã dùng.
- Việc tách plan logic trong `market.py` giúp hệ thống mở đường cho upgrade path từ free sang paid mà không cần đổi interface của agent.

## 12. Study Pack - Gói ôn tập
### Must remember
- Polygon.io được chọn vì có cả free plan và paid plan.
- Free plan bị rate limited và chỉ cho end-of-day prices.
- `market.py` giải bài toán đó bằng cách tải full market snapshot rồi cache.
- `database.py` lưu market snapshot theo ngày.
- `market_server.py` chỉ expose `lookup_share_price`.
- Agent có thể dùng custom market MCP server để trả lời giá Apple/AAPL.

### Self-check questions
- Tại sao `market.py` không gọi từng ticker một trên free plan?
- `get_market_for_prior_date()` giải quyết vấn đề gì?
- Vì sao `market_server.py` được xem là thin wrapper?
- Sự khác nhau giữa `get_share_price_polygon_eod()` và `get_share_price_polygon_min()` là gì?
- Nếu `POLYGON_API_KEY` không dùng được thì `get_share_price()` làm gì?

### Flashcards
- Q: Free Polygon plan cho loại dữ liệu giá nào?
  A: End-of-day / previous business day close prices.

- Q: Hàm nào cache snapshot toàn thị trường?
  A: `get_market_for_prior_date(today)`.

- Q: MCP tool của `market_server.py` tên là gì?
  A: `lookup_share_price`.

- Q: File nào giữ plan logic và provider logic?
  A: `market.py`.

### Interview Q&A nếu phù hợp
- Q: Bạn sẽ thiết kế một market data tool cho agent như thế nào khi provider miễn phí bị rate limited rất mạnh?
  A: Tôi sẽ tránh thiết kế naïve kiểu gọi API cho từng ticker riêng lẻ. Thay vào đó, nếu provider hỗ trợ bulk snapshot, tôi sẽ tải toàn bộ snapshot theo chu kỳ phù hợp, cache nó trong memory và/hoặc database, rồi expose cho agent một tool gọn như `lookup_share_price`. Như vậy agent vẫn có interface đơn giản, còn hệ thống bên dưới tối ưu số API calls, giảm rate limit và dễ nâng cấp từ free plan sang paid plan.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Không có raw response mẫu của grouped market snapshot trong session
- Không có benchmark so sánh số lần gọi API trước/sau cache, dù transcript đã giải thích mục tiêu rất rõ

---

# 122. Day 3 - Advanced Market Tools Using Paid Polygon Plan

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: đã dùng — `122. Day 3 - Advanced Market Tools Using Paid Polygon Plan.txt`
- Slide: không có
- Code: đã dùng — `3_lab3.ipynb`
- Summary lịch sử: đã dùng — `day1_summary.md`, `day2_summary.md`
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: Transcript và notebook khớp nhau. Đã scan thêm `mcp_params.py` như project context trong `G:\Agent2026Win\agents\6_mcp` để xác nhận capstone sẽ chọn official Polygon MCP server khi plan là `paid` hoặc `realtime`, còn free plan dùng `market_server.py`.

## 2. Executive Summary - Tóm tắt cốt lõi
- Lesson 122 mở rộng từ custom free-plan market server sang official Polygon MCP server đầy đủ tính năng dành cho người dùng paid plan.
- MCP server này được chạy bằng `uvx --from git+https://github.com/polygon-io/mcp_polygon@v0.1.0 mcp_polygon`, tức là lấy trực tiếp từ GitHub repo chính thức thay vì từ package đã publish.
- Instructor nhấn mạnh due diligence - thẩm định nguồn gốc mã: phải xác nhận đây là official repo của Polygon, xem community traction, stars và mức độ tin cậy như khi clone repo người khác.
- Official Polygon MCP server expose rất nhiều tools: market status, last trade, snapshot ticker, dividends, financials, crypto data và nhiều capability khác.
- Dù free user vẫn có thể thấy tool list, nhiều tools sẽ không usable - dùng được nếu plan không đủ quyền; vì vậy prompt hoặc tool selection phải tương thích plan thực tế.
- Instructor minh họa hành vi agent không ổn định: dù đã yêu cầu dùng `get_snapshot_ticker`, model vẫn có thể chọn sai tool ở lần đầu, và việc nâng model giúp cải thiện nhưng không bảo đảm tuyệt đối.
- Lesson kết lại bằng cơ chế `POLYGON_PLAN=paid|realtime` trong `.env`, chuẩn bị cho capstone chọn đúng market toolchain theo gói sử dụng.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
  - Hiểu khác biệt giữa custom MCP wrapper tối giản và official MCP server full-featured của provider.
  - Hiểu plan gating - giới hạn theo gói sử dụng ảnh hưởng trực tiếp tới tool availability.
  - Hiểu vì sao nhiều tools hơn không đồng nghĩa agent luôn dùng đúng hơn.
- Practical goals - mục tiêu thực hành:
  - Biết cấu hình params chạy official Polygon MCP server từ GitHub repo.
  - Biết cho agent dùng các advanced market tools với prompt constraints rõ ràng.
  - Biết dùng `POLYGON_PLAN` để đồng bộ code dự án với plan đã đăng ký.
- What learner should be able to explain - người học cần giải thích được:
  - Vì sao official Polygon MCP server hữu ích hơn khi đã có paid plan.
  - Tại sao prompt vẫn phải ràng buộc tool choice trên plan thấp hơn.
  - Cách dự án capstone chọn market MCP path theo plan.

## 4. Previous Context - Liên hệ với bài trước
- Lesson 121 xây custom market MCP server cho free plan. Lesson 122 cho thấy khi có paid plan thì “đi full provider integration” mới tận dụng được breadth - độ rộng của APIs.
- Day 1 và Day 3 đầu buổi đã nhấn mạnh rằng ecosystem MCP cho phép tái dùng tool người khác. Official Polygon MCP server là ví dụ rất rõ của ecosystem leverage - tận dụng hệ sinh thái.
- `day2_summary.md` cũng đã nói về build vs buy. Lesson 122 chính là bài toán build-vs-buy rất thực tế: free plan thì build wrapper tối giản; paid plan thì buy/use official provider MCP server.
- Từ `mcp_params.py`, có thể thấy bài học này đã nối trực tiếp vào capstone architecture: trader agent sẽ dùng official Polygon MCP nếu plan đủ, ngược lại dùng local `market_server.py`.

## 5. Core Theory - Lý thuyết cốt lõi

### Provider-native MCP server - MCP server chính chủ từ provider
- Term - thuật ngữ: Provider-native MCP server - MCP server chính chủ từ provider
- Meaning - nghĩa: MCP server do chính provider dữ liệu cung cấp, expose trực tiếp nhiều APIs chuyên sâu của họ.
- Why it matters - vì sao quan trọng: Khi đã trả phí cho dữ liệu/plan tốt hơn, provider-native MCP thường mang lại breadth và freshness vượt xa wrapper tự viết tối giản.
- Relationship - liên hệ với khái niệm khác: Đối lập với custom local `market_server.py` ở lesson 121.

### Plan-aware tool surface - bề mặt tool phụ thuộc gói sử dụng
- Term - thuật ngữ: Plan-aware tool surface - bề mặt tool phụ thuộc gói sử dụng
- Meaning - nghĩa: Cùng một MCP server có thể expose nhiều tools, nhưng hiệu lực thực tế của từng tool còn phụ thuộc plan API mà key hiện tại được cấp.
- Why it matters - vì sao quan trọng: Nếu không hiểu điều này, agent có thể liên tục gọi tools mà plan của bạn không đủ quyền.
- Relationship - liên hệ với khái niệm khác: Là lý do instructor phải hướng model dùng `get_snapshot_ticker`.

### Tool overload risk - rủi ro quá tải tool
- Term - thuật ngữ: Tool overload risk - rủi ro quá tải tool
- Meaning - nghĩa: Khi agent được cung cấp quá nhiều tools, xác suất chọn tool không tối ưu có thể tăng.
- Why it matters - vì sao quan trọng: “More capabilities” không luôn đồng nghĩa “better behavior”.
- Relationship - liên hệ với khái niệm khác: Instructor cho thấy model chọn sai tool ở lần chạy đầu.

### GitHub-sourced MCP execution - chạy MCP từ GitHub repo
- Term - thuật ngữ: GitHub-sourced MCP execution - chạy MCP từ GitHub repo
- Meaning - nghĩa: Dùng `uvx --from git+https://...` để chạy MCP server trực tiếp từ source repo.
- Why it matters - vì sao quan trọng: Đây là một cách phân phối MCP server linh hoạt, nhưng đòi hỏi review/reputation checks kỹ hơn.
- Relationship - liên hệ với khái niệm khác: Gắn trực tiếp với due diligence và security review của Day 1.

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
1. Input:
   - `POLYGON_API_KEY`
   - `POLYGON_PLAN=paid` hoặc `realtime` nếu có
   - User request về market data, ví dụ giá Apple
2. Processing steps:
   - Notebook cấu hình `uvx --from git+https://github.com/polygon-io/mcp_polygon@v0.1.0 mcp_polygon`.
   - `MCPServerStdio` spawn official Polygon MCP server local.
   - Agent được trang bị rất nhiều tools từ provider.
   - Prompt có thể cần ràng buộc rõ tool nên dùng theo plan, như `get_snapshot_ticker`.
   - Code dự án/capstone đọc `POLYGON_PLAN` để chọn official server hay local wrapper.
3. Output:
   - Giá cổ phiếu mới hơn EOD và/hoặc nhiều market capabilities nâng cao hơn.
4. Control flow / data flow:
   - User request -> Agent -> official Polygon MCP tool -> Polygon APIs -> result -> Agent response.
5. Decision points:
   - Chọn free, paid, hay realtime plan.
   - Chọn custom minimal server hay official provider server.
   - Chọn model/prompt đủ tốt để không lạc tool.

## 7. Techniques - Kỹ thuật sử dụng

### Progressive capability upgrade by plan - nâng cấp capability theo plan
- Technique - kỹ thuật: Progressive capability upgrade by plan - nâng cấp capability theo plan
- Purpose - mục đích: Giữ cùng một project architecture nhưng scale market capabilities theo budget/plan.
- When to use - dùng khi nào: Khi provider có nhiều tiers và bạn muốn codebase thích nghi dần.
- Trade-off - đánh đổi: Phải có plan-selection logic nhưng đổi lại upgrade path rất mượt.
- Common mistake - lỗi dễ gặp: Viết riêng hai hệ thống không tương thích cho free và paid plan.

### Prompt-constrained tool selection - ràng buộc chọn tool qua prompt
- Technique - kỹ thuật: Prompt-constrained tool selection - ràng buộc chọn tool qua prompt
- Purpose - mục đích: Hướng agent dùng tool phù hợp với plan hoặc mục tiêu.
- When to use - dùng khi nào: Khi tool surface quá rộng hoặc có tools plan-locked.
- Trade-off - đánh đổi: Prompt phức tạp hơn và vẫn không bảo đảm 100%.
- Common mistake - lỗi dễ gặp: Tưởng chỉ cần liệt kê tools là model sẽ luôn chọn đúng.

### Due diligence on source repos - thẩm định repo nguồn
- Technique - kỹ thuật: Due diligence on source repos - thẩm định repo nguồn
- Purpose - mục đích: Giảm rủi ro khi chạy MCP server trực tiếp từ repo GitHub.
- When to use - dùng khi nào: Bất cứ khi nào MCP server không phải package chính thức đã được xác minh sẵn.
- Trade-off - đánh đổi: Tốn thời gian review nhưng giảm risk chạy code bên thứ ba không đáng tin.
- Common mistake - lỗi dễ gặp: Thấy repo trông “official” là chạy ngay, bỏ qua check publisher/stars/community/support.

### Model upgrade as behavioral mitigation - nâng model để giảm lỗi hành vi
- Technique - kỹ thuật: Model upgrade as behavioral mitigation - nâng model để giảm lỗi hành vi
- Purpose - mục đích: Giảm xác suất model chọn sai tool trong môi trường nhiều công cụ.
- When to use - dùng khi nào: Khi tool routing của model ở plan/tool surface hiện tại chưa ổn định.
- Trade-off - đánh đổi: Tăng chi phí và không loại bỏ hoàn toàn unpredictability - tính khó đoán.
- Common mistake - lỗi dễ gặp: Tưởng đổi model là đủ, không cần thêm prompt constraints hay guardrails.

## 8. Code Walkthrough - Phân tích code nếu có

### File / block: `3_lab3.ipynb` cell 27
- Purpose - mục đích: Cấu hình official Polygon MCP server từ GitHub repo với `uvx`.
- Key logic - logic chính:
  - Dùng `uvx` với `--from git+https://github.com/polygon-io/mcp_polygon@v0.1.0`.
  - Truyền `POLYGON_API_KEY` qua env.
  - List tools để khám phá toàn bộ capability surface.
- Important lines / functions:
  - `params = {"command": "uvx", "args": ["--from", "git+https://github.com/polygon-io/mcp_polygon@v0.1.0", "mcp_polygon"], "env": {"POLYGON_API_KEY": polygon_api_key}}`
  - `await server.list_tools()`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là ví dụ rõ ràng cho việc MCP server có thể được phân phối trực tiếp từ repo chứ không cần package registry riêng.
  - Vì chạy code trực tiếp từ repo, phần due diligence là bắt buộc.

### File / block: `3_lab3.ipynb` cells 28-29
- Purpose - mục đích: Cho agent dùng official Polygon MCP server và thử lấy giá Apple với tool constraint phù hợp plan.
- Key logic - logic chính:
  - Prompt ghi rõ “Use your get_snapshot_ticker tool to get the latest price.”
  - Agent vẫn có thể chọn sai tool ở lần đầu, cho thấy tool overload và model unpredictability là thật.
  - Instructor nâng model và thử lại để cải thiện.
- Important lines / functions:
  - `request = "What's the share price of Apple? Use your get_snapshot_ticker tool to get the latest price."`
  - `Agent(..., mcp_servers=[mcp_server])`
  - `Runner.run(agent, request)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là đoạn rất đáng học vì nó không tô hồng behavior của agent; model vẫn có thể làm sai dù prompt đã rõ.
  - Khi tool surface lớn, prompt engineering và model choice càng quan trọng.

### File / block: `3_lab3.ipynb` cells 30-31
- Purpose - mục đích: Chuẩn hóa cách dự án biết bạn đang dùng free, paid hay realtime Polygon plan.
- Key logic - logic chính:
  - `.env` nhận `POLYGON_PLAN=paid` hoặc `realtime`.
  - Notebook đọc plan để in ra semantic mode - chế độ ngữ nghĩa dữ liệu hiện tại.
- Important lines / functions:
  - ``POLYGON_PLAN=paid``
  - ``POLYGON_PLAN=realtime``
  - `is_paid_polygon = polygon_plan == "paid"`
  - `is_realtime_polygon = polygon_plan == "realtime"`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - Đây là một feature flag rất thực tế cho project kéo dài nhiều ngày.
  - Nó giúp cùng codebase thích nghi với nhiều mức capability của market data provider.

### File / block: [mcp_params.py](G:\Agent2026Win\agents\6_mcp\mcp_params.py)
- Purpose - mục đích: Xác nhận Day 3 paid-plan logic đã đi vào project context của capstone, không chỉ dừng ở notebook demo.
- Key logic - logic chính:
  - Nếu `is_paid_polygon` hoặc `is_realtime_polygon`, `market_mcp` sẽ dùng official `mcp_polygon` từ GitHub.
  - Nếu không, trader sẽ dùng local `market_server.py`.
  - Researcher agent thì song song dùng fetch, Brave Search và memory MCP.
- Important lines / functions:
  - `if is_paid_polygon or is_realtime_polygon:`
  - `market_mcp = {"command": "uvx", ... "mcp_polygon"}`
  - `else: market_mcp = {"command": "uv", "args": ["run", "market_server.py"]}`
  - `researcher_mcp_server_params(name: str)`
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:
  - File này rất giá trị để thấy lesson 122 không phải kiến thức rời rạc; nó trở thành hạ tầng thật cho trading floor multi-agent ở các ngày sau.

## 9. Options / Trade-offs - Bản đồ lựa chọn

### Option 1: Free plan + custom minimal market MCP
- Option: Minimal custom server
- Pros: Rẻ, đủ cho học tập, tránh tool overload, kiểm soát behavior tốt hơn.
- Cons: Dữ liệu cũ hơn, ít APIs, ít capability phân tích thị trường.
- When to choose: Khi budget thấp hoặc chỉ cần trading simulation cơ bản.

### Option 2: Paid plan + official Polygon MCP server
- Option: Full provider MCP server
- Pros: Nhiều tools, dữ liệu mới hơn, capability rộng cho market intelligence.
- Cons: Tốn phí, dễ quá tải tool selection, cần due diligence tốt.
- When to choose: Khi muốn trader/researcher agents có năng lực market data mạnh hơn và plan cho phép.

### Option 3: Realtime plan
- Option: Realtime market plan
- Pros: Dữ liệu tươi nhất, gần production hơn cho trading use cases.
- Cons: Chi phí cao hơn nhiều, có thể overkill cho course project.
- When to choose: Khi dự án thật cần latency thấp và bạn sẵn sàng trả phí tương ứng.

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode: Cho agent quá nhiều tools rồi kỳ vọng nó luôn chọn đúng
  - Root cause: Nhầm lẫn giữa “more tools” và “better tool routing”.
  - Symptom: Agent gọi sai tool hoặc chọn tool không phù hợp plan.
  - Fix / prevention: Dùng prompt constraints, model tốt hơn, hoặc thu hẹp tool surface khi cần.

- Failure mode: Tin rằng official GitHub repo là auto-safe
  - Root cause: Bỏ qua security review vì thấy repo mang tên provider.
  - Symptom: Chạy code từ repo chưa kiểm chứng kỹ.
  - Fix / prevention: Kiểm tra repo, publisher, stars, community traction, docs, issues và release history.

- Failure mode: Không đồng bộ `.env` plan với code dự án
  - Root cause: Có key paid nhưng không set `POLYGON_PLAN`, hoặc set sai giá trị.
  - Symptom: Hệ thống vẫn chọn free-path hoặc dùng nhầm API assumptions.
  - Fix / prevention: Dùng feature flag plan rõ ràng như notebook và `mcp_params.py`.

- Failure mode: Coi model upgrade là cách sửa duy nhất cho tool mis-selection
  - Root cause: Đánh giá thấp vai trò của prompt/tool constraints.
  - Symptom: Tốn chi phí model hơn nhưng vẫn gặp lỗi routing khó đoán.
  - Fix / prevention: Kết hợp model choice, prompt constraints và giảm tool surface khi cần.

## 11. Knowledge Extension - Kiến thức mở rộng
Đây là kiến thức mở rộng, không phải nội dung chắc chắn có trong buổi học.

- Trong agent systems thật, một pattern phổ biến là “capability tiering”: free/basic agents dùng toolset tối giản, advanced agents mới được mở nhiều tool hơn.
- Tool routing trong môi trường có hàng chục tools thường cần thêm guardrails như tool whitelists theo task, ranking heuristics hoặc explicit routers, chứ không chỉ trông cậy vào model.
- Provider-native MCP servers có thể rất mạnh, nhưng đồng thời cũng khiến observability, policy enforcement và cost control trở nên quan trọng hơn.

## 12. Study Pack - Gói ôn tập
### Must remember
- Official Polygon MCP server phù hợp nhất khi đã có paid plan.
- Server này có rất nhiều tools hơn custom `market_server.py`.
- Nhiều tools hơn cũng kéo theo rủi ro model chọn sai tool.
- `uvx --from git+https://...` cho phép chạy MCP server trực tiếp từ GitHub repo.
- `POLYGON_PLAN=paid|realtime` là feature flag để dự án chọn market MCP path đúng.
- `mcp_params.py` xác nhận Day 3 logic đã nối vào capstone trading floor.

### Self-check questions
- Vì sao paid plan lại hợp với official provider MCP server hơn custom wrapper?
- Tool overload là gì và nó xuất hiện thế nào trong lesson này?
- Tại sao cần due diligence khi chạy MCP server từ GitHub repo?
- `POLYGON_PLAN` ảnh hưởng gì tới capstone project?
- Khi nào nên giữ custom minimal server thay vì dùng official full server?

### Flashcards
- Q: Official Polygon MCP server được chạy như thế nào trong notebook?
  A: Qua `uvx --from git+https://github.com/polygon-io/mcp_polygon@v0.1.0 mcp_polygon`.

- Q: Biến môi trường nào biểu thị plan Polygon?
  A: `POLYGON_PLAN`.

- Q: Nếu plan là paid hoặc realtime thì project context chọn market MCP nào?
  A: Official `mcp_polygon` server; nếu free thì dùng local `market_server.py`.

- Q: Tại sao agent có thể gọi sai tool dù prompt đã gợi ý?
  A: Vì tool routing của LLM vẫn có unpredictability, đặc biệt khi tool surface quá rộng.

### Interview Q&A nếu phù hợp
- Q: Khi nào bạn sẽ chọn official provider MCP server thay vì custom MCP wrapper tối giản?
  A: Tôi chọn official provider MCP server khi đã có plan đủ mạnh và cần breadth of capabilities - độ rộng capability mà wrapper tối giản không đáng công tự xây lại, ví dụ market status, snapshots, financials, dividends, crypto, nhiều endpoints khác nhau. Tuy nhiên tôi vẫn cân nhắc tool overload, cost và security review. Nếu chỉ cần một capability nhỏ, hoặc free plan bị giới hạn mạnh, custom wrapper tối giản thường dễ kiểm soát hơn và giúp agent chọn tool ổn định hơn.

## 13. Missing Inputs - Còn thiếu gì
- Slide: không được cung cấp
- Không có ảnh chụp tool list đầy đủ của official Polygon MCP server trong session
- Không có raw examples cho các paid-only tools ngoài `get_snapshot_ticker`
- Không có repo audit notes chi tiết; transcript chỉ nêu nguyên tắc due diligence chứ không cung cấp checklist cụ thể
