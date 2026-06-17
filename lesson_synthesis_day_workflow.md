# Lesson Synthesis Day Workflow

Workflow này dùng cho một session xử lý đúng 1 day của khóa học.

Course domain: AI Agents  
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Prompt gửi agent trong session mới để tạo file summary day .md

Copy prompt dưới đây vào session mới, rồi gửi kèm:

- File workflow này.
- Các file transcript `.txt` của day hiện tại. Tên file chính là lesson topic.
- File code nếu có: `.ipynb`, `.py`, project folder, Docker/config, hoặc các file liên quan.
- File slide nếu có.
- File summary của các day trước, ví dụ `day1_summary.md`, `day2_summary.md`.
- Ghi chú riêng nếu có.

```text
Bạn là coding/learning agent làm việc trong workspace của tôi.

Nhiệm vụ: áp dụng Prompt S1 - Lesson synthesis cho toàn bộ transcript của 1 day học, theo đúng workflow trong file `lesson_synthesis_day_workflow.md` tôi gửi kèm.

Thông tin cố định:
- course_domain: AI Agents
- course_name: AI Engineer Agentic Track: The Complete Agent & MCP Course

Quy tắc làm việc:
1. Đọc file workflow `lesson_synthesis_day_workflow.md` ("G:\harness_template\codex_output_learn_udemy\lesson_synthesis_day_workflow.md") trước.
2. Đọc Prompt S1 gốc từ:
   `G:\harness_template\codex_output_learn_udemy\lesson_study_workflow_template.html`
   Nếu không truy cập được file gốc, dùng bản S1 schema được nhúng trong workflow.
3. Tự nhận diện day hiện tại từ tên transcript, ví dụ `9. Day 2 - ...txt` nghĩa là Day 2.
4. Tự sắp xếp transcript theo số thứ tự đầu filename: 9, 10, 11, ...
5. Với mỗi transcript, dùng filename không có `.txt` làm `lesson_topic`.
6. Đọc toàn bộ transcript, code được gửi, slide được gửi, và summary các day trước trước khi tổng hợp.
7. Nếu code/project context bị thiếu, dùng hybrid discovery:
   - Ưu tiên file/folder code tôi gửi.
   - Nếu vẫn thiếu context, scan targeted trong allowed project/chapter roots có liên quan.
   - Báo rõ đã scan thêm file/folder nào và vì sao.
8. Không mặc định rằng mọi transcript trong cùng một day đều có code liên quan:
   - Nếu một day có lesson 12, 13, 14 chỉ dạy lý thuyết và lesson 15, 16 mới có code, thì chỉ lesson 15, 16 được phân tích Code Walkthrough.
   - Với lesson lý thuyết, dù session có gửi file code, ghi rõ `Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này`.
   - Chỉ phân tích code khi transcript, filename, notebook heading, markdown cells, code comments, summary cũ hoặc project context cho thấy code đó thuộc lesson hiện tại.
   - Không tạo Code Walkthrough giả chỉ vì trong session có file code.
9. Không đọc, không in, không tóm tắt secrets: `.env`, API keys, tokens, credentials, private keys.
10. Tạo file `dayN_summary.md` nếu chưa có, trong cùng thư mục tài liệu/transcript nếu suy luận được. Nếu đã có thì append đúng thứ tự lesson.
11. Mỗi lesson phải là một section S1 đầy đủ, không gộp nhiều lesson thành một summary chung.
12. Sau khi hoàn thành, kiểm tra file output:
    - Có đủ các section S1.
    - Không còn placeholder dạng `[[...]]`.
    - Source Map ghi rõ transcript/code/slide/summary đã dùng.
    - Missing Inputs ghi rõ phần thiếu nếu có.


Bạn hãy dùng `brainstorming` làm quy trình chính để cùng tôi thảo luận, hỏi thêm, làm rõ yêu cầu.
   - Luôn bắt đầu bằng `using-superpowers`.
   - Dùng `brainstorming` làm quy trình chính. 
   - Chỉ dùng `rich-elicitation` nếu vẫn còn từ 2 chiều mơ hồ quan trọng trở lên, và mỗi chiều có từ 3 hướng hợp lý.
   - Hỏi tối đa 3 câu hỏi quan trọng mỗi lượt.
   - Ưu tiên câu hỏi multiple-choice có recommended option.
   - Không hỏi lan man. Mỗi câu hỏi phải làm thay đổi scope, design, test, hoặc implementation plan.
   - Đừng bắt đầu viết code cho đến khi chúng ta đã thống nhất yêu cầu.

Load các skills ở:
- Windows: `C:\Users\hieu\.agents\skills`
- WSL/Linux: `/home/hieu0606sunny/.codex/skills/`

Dừng lại trao đổi với tôi, tôi xác nhận mới tạo file

Hãy thực hiện luôn, không chỉ lập kế hoạch, trừ khi thiếu thông tin nghiêm trọng khiến không thể xác định day hoặc nơi ghi output.

transcript: 
code:
slide: 
Nội dung các bài trước: 

Bạn có thể tự khám phá các file, folder chứa code khác để hiểu rõ thêm về bài học nếu thấy cần thiết hoặc nếu tôi cung cấp thiếu ngữ cảnh
```

## 2. Mục tiêu workflow

Agent cần biến nhiều transcript trong cùng một day thành một file `dayN_summary.md`.

Mỗi transcript được xử lý độc lập bằng Prompt S1 - Lesson synthesis. Kết quả của lesson đầu tiên được ghi vào file summary của day hiện tại; các lesson sau được append vào cùng file theo đúng thứ tự.

Ví dụ Day 2 trong `1_foundations` có 3 transcript:

1. `9. Day 2 - Building Effective Agents LLM Autonomy & Tool Integration Explained.txt`
2. `10. Day 2 - 5 Essential LLM Workflow Design Patterns for Building Robust AI Systems.txt`
3. `11. Day 2 - Understanding Agent vs Workflow Patterns in LLM Application Design.txt`

Output chuẩn:

```text
day2_summary.md
```

## 3. Input agent phải tự nhận diện

Agent không yêu cầu người dùng điền config. Agent tự nhận diện từ file được gửi trong session.

### Transcript

- File `.txt` là transcript bài học.
- Tên file là `lesson_topic`.
- Nếu filename có prefix số thứ tự, dùng prefix đó để sắp xếp.
- Nếu có nhiều day lẫn trong input, chỉ xử lý day được người dùng yêu cầu rõ. Nếu người dùng không nói rõ và input chứa nhiều day, hỏi lại.

### Code

Code có thể là:

- Không có code.
- Một hoặc nhiều notebook `.ipynb`.
- Một hoặc nhiều file `.py`.
- Cả project folder gồm `.py`, `.ipynb`, Dockerfile, config, docs, tests.
- Project kéo dài nhiều day hoặc nhiều tuần.

Agent phải đọc code như nguồn ngang hàng với transcript và summary cũ khi code được cung cấp hoặc cần thiết để hiểu lesson.

Không mặc định rằng mọi transcript trong cùng một day đều có code liên quan. Nếu một day có nhiều lesson, ví dụ lesson 12, 13, 14 là lý thuyết và lesson 15, 16 mới thực hành code, thì:

- Lesson 12, 13, 14: Source Map ghi `Code: không có code trực tiếp cho lesson này` nếu code được gửi nhưng transcript không liên quan trực tiếp tới code.
- Lesson 15, 16: phân tích Code Walkthrough đầy đủ nếu transcript dạy hoặc dùng code.
- Nếu chưa chắc code thuộc lesson nào, suy luận từ transcript, filename, notebook heading, markdown cells, code comments, summary cũ và folder structure.
- Không ép tạo Code Walkthrough giả cho lesson lý thuyết chỉ vì session có file code.

### Slide

- Nếu có slide, đọc như nguồn ngang hàng.
- Nếu không có, ghi `Slide: không có` trong Source Map.

### Summary các day trước

- Đọc tất cả summary cũ người dùng gửi.
- Nếu Day 5 phụ thuộc project từ Day 3 và Day 4, dùng summary Day 3 và Day 4 như previous context.
- Nếu thiếu summary quan trọng, vẫn xử lý nhưng ghi rõ trong `Missing Inputs`.

## 4. Hybrid Code Context Rules

Agent đọc code theo thứ tự:

1. Đọc code manifest/file/folder người dùng gửi trong session.
2. Đọc summary các day trước để xác định project context.
3. Nếu còn thiếu context, scan targeted trong folder/chapter/project root liên quan.
4. Trước hoặc sau khi scan thêm, báo ngắn gọn:
   - Vì sao cần scan thêm.
   - Đã scan folder nào.
   - Đã đọc thêm file nào.

### Targeted scan mặc định

Được scan:

- `*.py`
- `*.ipynb`
- `*.md`
- `*.yaml`, `*.yml`
- `*.toml`
- `*.json` nếu là config hoặc notebook metadata cần thiết
- `Dockerfile`, `docker-compose*.yml`
- `requirements*.txt`, `pyproject.toml`, `uv.lock`
- Files/folders tên `src`, `app`, `tests`, `notebooks`, `examples`, `guides`, `docs`

Không đọc hoặc không tóm tắt:

- `.env`, `.env.*`
- API keys, tokens, credentials, private keys
- `.git`
- `.venv`, `venv`, `env`
- `node_modules`
- cache/build folders: `__pycache__`, `.pytest_cache`, `.mypy_cache`, `dist`, `build`
- data lớn, binary files, model weights, logs lớn

Nếu scan rộng có nguy cơ tốn context, agent chỉ đọc danh sách file trước, sau đó chọn file quan trọng nhất.

## 5. Execution Order

1. Đọc workflow này.
2. Đọc Prompt S1 gốc từ HTML template nếu có thể.
3. Xác định day number từ transcript filenames.
4. Xác định output file: `dayN_summary.md`.
5. Đọc previous summaries.
6. Đọc code/slides được gửi.
7. Nếu thiếu context code/project, dùng Hybrid Code Context Rules.
8. Sắp xếp transcript theo số đầu filename.
9. Với từng transcript:
   - Set `lesson_topic` bằng filename không có `.txt`.
   - Áp dụng Prompt S1.
   - Lesson đầu: tạo file `dayN_summary.md` nếu chưa có.
   - Lesson sau: append vào cuối file.
10. Sau mỗi lesson, đảm bảo section đó tự đứng được và có Source Map rõ.
11. Sau toàn bộ day, chạy quality gate.

## 6. Output Rules

### File naming

Output summary phải dùng pattern:

```text
dayN_summary.md
```

Ví dụ:

- `day1_summary.md`
- `day2_summary.md`
- `day3_summary.md`

Không dùng dấu phẩy trong extension, ví dụ không dùng `day1_summary,md`.

### File location

Ưu tiên ghi output trong cùng thư mục chứa transcript của day hiện tại.

Ví dụ:

```text
G:\Agent2026Win\agents\1_foundations\tai lieu\day2_summary.md
```

Nếu không suy luận được thư mục output, hỏi người dùng trước khi ghi file.

### Append behavior

- Nếu `dayN_summary.md` chưa tồn tại: tạo file mới.
- Nếu đã tồn tại:
  - Nếu file chưa có lesson đang xử lý: append.
  - Nếu file đã có lesson đang xử lý: hỏi người dùng trước khi ghi đè hoặc append bản mới.

## 7. Prompt S1 - Lesson Synthesis Schema

Source of truth là Prompt S1 trong:

```text
G:\harness_template\codex_output_learn_udemy\lesson_study_workflow_template.html
```

Nếu agent đọc được file HTML gốc, dùng prompt trong đó. Nếu không, dùng schema dưới đây.

### S1 role

Bạn là một chuyên gia và giảng viên về AI Agents.

Nhiệm vụ: đọc toàn bộ tài nguyên được cung cấp và tạo một bản tổng hợp buổi học chính xác, có cấu trúc, dùng để thêm vào summary history và đưa tiếp cho coding agent tạo HTML ôn tập nếu cần.

Thông tin cố định:

- Tên khóa học: AI Engineer Agentic Track: The Complete Agent & MCP Course
- Chủ đề bài học: lấy từ filename transcript hiện tại.

Nguồn có thể có:

1. Transcript / phiên âm bài học hiện tại.
2. Slide bài học nếu có.
3. Code bài học nếu có.
4. Summary lịch sử: nội dung các day trước đã được LLM tóm tắt.

Quy tắc bắt buộc:

- Đọc toàn bộ nguồn được cung cấp trước khi tổng hợp.
- Xem transcript, slide, code và summary lịch sử là các nguồn quan trọng ngang nhau.
- Nếu các nguồn mâu thuẫn, nêu rõ mâu thuẫn và ưu tiên cách diễn giải hợp lý nhất dựa trên toàn bộ ngữ cảnh.
- Không bịa nội dung. Nếu thiếu dữ kiện, ghi rõ là chưa thấy trong tài liệu.
- Tách riêng `Nội dung từ nguồn` và `Knowledge Extension - Kiến thức mở rộng`.
- Technical term phrase dùng dạng `English - nghĩa tiếng Việt`.
- Từ đơn phổ biến dùng dạng `cost (chi phí)`.
- Viết bằng tiếng Việt. Giữ technical terms tiếng Anh khi rõ nghĩa hơn.
- Không yêu cầu hoặc lộ secrets, tokens, API keys.

### Required S1 output structure

```markdown
# [lesson_topic]

Course domain: AI Agents
Course name: AI Engineer Agentic Track: The Complete Agent & MCP Course

## 1. Source Map - Bản đồ nguồn
- Transcript: [đã dùng / không có / không đủ rõ]
- Slide: [đã dùng / không có]
- Code: [đã dùng / không có]
- Summary lịch sử: [đã dùng / không có]
- Ghi chú về độ tin cậy hoặc mâu thuẫn giữa nguồn: [nếu có]

## 2. Executive Summary - Tóm tắt cốt lõi
Viết 5-8 bullet về những điểm quan trọng nhất của buổi học.

## 3. Lesson Goals - Mục tiêu bài học
- Concept goals - mục tiêu kiến thức:
- Practical goals - mục tiêu thực hành:
- What learner should be able to explain - người học cần giải thích được:

## 4. Previous Context - Liên hệ với bài trước
Nêu bài học này nối tiếp, sửa, mở rộng hoặc phụ thuộc vào nội dung nào trong summary lịch sử.

## 5. Core Theory - Lý thuyết cốt lõi
Với mỗi khái niệm quan trọng:
- Term - thuật ngữ:
- Meaning - nghĩa:
- Why it matters - vì sao quan trọng:
- Relationship - liên hệ với khái niệm khác:

## 6. Workflow / Pipeline - Quy trình / luồng hoạt động
Nếu bài học có pipeline:
1. Input:
2. Processing steps:
3. Output:
4. Control flow / data flow:
5. Decision points:

Nếu không có pipeline rõ ràng, ghi:
`Không có pipeline rõ ràng trong tài liệu nguồn`
và thay bằng luồng tư duy/chủ đề.

## 7. Techniques - Kỹ thuật sử dụng
Với mỗi kỹ thuật:
- Technique - kỹ thuật:
- Purpose - mục đích:
- When to use - dùng khi nào:
- Trade-off - đánh đổi:
- Common mistake - lỗi dễ gặp:

## 8. Code Walkthrough - Phân tích code nếu có
Nếu có code liên quan trực tiếp tới lesson hiện tại, phân tích từng file hoặc khối code quan trọng:
- File / block:
- Purpose - mục đích:
- Key logic - logic chính:
- Important lines / functions:
- Vietnamese inline notes - ghi chú tiếng Việt để giải thích snippet:

Nếu session có code nhưng transcript hiện tại là bài lý thuyết hoặc không dùng code trực tiếp, ghi rõ:
`Code được cung cấp trong session nhưng chưa thấy code liên quan trực tiếp tới lesson này`.

Nếu không có code nào được cung cấp, ghi rõ:
`Buổi học này không có code được cung cấp`.

## 9. Options / Trade-offs - Bản đồ lựa chọn
Nếu bài học có nhiều cách làm:
- Option:
- Pros:
- Cons:
- When to choose:

## 10. Pitfalls - Lỗi / bẫy thường gặp
- Failure mode:
- Root cause:
- Symptom:
- Fix / prevention:

## 11. Knowledge Extension - Kiến thức mở rộng
Chỉ thêm kiến thức thật sự hữu ích để hiểu bài sâu hơn. Mỗi ý phải ghi rõ là mở rộng, không phải nội dung chắc chắn có trong buổi học.

## 12. Study Pack - Gói ôn tập
### Must remember
5-10 ý phải nhớ.

### Self-check questions
5-10 câu tự kiểm tra.

### Flashcards
- Q:
  A:

### Interview Q&A nếu phù hợp
- Q:
  A:

## 13. Missing Inputs - Còn thiếu gì
Liệt kê file, slide, code, log hoặc ngữ cảnh còn thiếu nếu có. Không yêu cầu secrets.
```

## 8. Quality Gate

Trước khi kết thúc, agent phải kiểm tra:

- Output file `dayN_summary.md` đã được tạo hoặc append đúng.
- Transcript đã được xử lý theo đúng thứ tự số filename.
- Mỗi lesson có đủ 13 section S1.
- Không còn placeholder dạng `[[...]]`.
- Source Map của từng lesson ghi rõ transcript/code/slide/summary đã dùng.
- Code Walkthrough chỉ áp dụng cho lesson có code liên quan trực tiếp.
- Nếu session có code nhưng lesson là lý thuyết, output phải ghi rõ code không liên quan trực tiếp thay vì phân tích giả.
- Knowledge Extension được tách khỏi nội dung từ nguồn.
- Missing Inputs ghi rõ phần thiếu.
- Không có secrets, API keys, tokens hoặc credentials trong output.

## 9. Example Day 2

Ví dụ nếu session mới gửi các file trong:

```text
G:\Agent2026Win\agents\1_foundations\tai lieu
```

Transcript Day 2 gồm:

```text
9. Day 2 - Building Effective Agents LLM Autonomy & Tool Integration Explained.txt
10. Day 2 - 5 Essential LLM Workflow Design Patterns for Building Robust AI Systems.txt
11. Day 2 - Understanding Agent vs Workflow Patterns in LLM Application Design.txt
```

Summary lịch sử:

```text
day1_summary.md
```

Code có thể là:

```text
G:\Agent2026Win\agents\1_foundations\2_lab2.ipynb
```

Output:

```text
G:\Agent2026Win\agents\1_foundations\tai lieu\day2_summary.md
```

Execution:

1. Đọc `day1_summary.md`.
2. Đọc `2_lab2.ipynb` nếu có.
3. Xử lý transcript `9...txt` bằng S1, tạo `day2_summary.md`.
4. Xử lý transcript `10...txt` bằng S1, append vào `day2_summary.md`.
5. Xử lý transcript `11...txt` bằng S1, append vào `day2_summary.md`.
6. Chạy Quality Gate.

## 10. Notes for Long Projects

Nếu một project kéo dài nhiều day hoặc nhiều tuần:

- Dùng summary các day trước để hiểu project evolution - tiến hóa dự án.
- Dùng code hiện tại để hiểu trạng thái mới nhất.
- Nếu day hiện tại phụ thuộc code cũ nhưng người dùng không gửi đủ, scan targeted trong project/chapter root liên quan.
- Không cần đọc toàn bộ project nếu summary và file chính đã đủ.
- Không gán code project cho mọi lesson trong day. Với day có cả lesson lý thuyết và lesson code, chỉ phân tích code ở lesson thực sự dạy, sửa, chạy hoặc giải thích code.
- Ví dụ: nếu lesson 12, 13, 14 chỉ dạy lý thuyết và lesson 15, 16 mới có code, thì lesson 12-14 ghi rõ không có code trực tiếp; lesson 15-16 mới có Code Walkthrough.
- Khi output Code Walkthrough, phân biệt:
  - Code mới trong day hiện tại.
  - Code từ day trước được reuse - tái sử dụng.
  - Code project nền cần biết để hiểu bài.
