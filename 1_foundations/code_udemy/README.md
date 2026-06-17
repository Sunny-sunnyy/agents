# Udemy Transcript Scraper

Công cụ tự động hóa sử dụng Python Playwright kết nối qua Chrome DevTools Protocol (CDP) để cào phiên âm (transcripts) các bài học trên Udemy từ một trình duyệt đang chạy sẵn.

---

## Cấu trúc thư mục

*   [create_files.py](file:///G:/Agent2026Win/agents/1_foundations/code_udemy/create_files.py): Script khởi tạo các file văn bản rỗng `.txt` tương ứng với tiêu đề các bài học. Tự động chuyển đổi các ký tự không hợp lệ trên Windows (ví dụ `:` thành ` -`).
*   [run_automation_normal.py](file:///G:/Agent2026Win/agents/1_foundations/code_udemy/run_automation_normal.py): **Phiên bản chạy bình thường (Bản cũ)**. Dùng khi Udemy hoạt động bình thường, trình phát video không bị lỗi hiển thị.
*   [run_automation_with_error.py](file:///G:/Agent2026Win/agents/1_foundations/code_udemy/run_automation_with_error.py): **Phiên bản xử lý lỗi video (Bản mới)**. Dùng khi trình phát video của Udemy bị lỗi và hiển thị popup thông báo lỗi chặn màn hình.
*   [README.md](file:///G:/Agent2026Win/agents/1_foundations/code_udemy/README.md): Hướng dẫn sử dụng và tài liệu xử lý lỗi này.

---

## Các Tình Huống và Cách Xử Lý

### Tình huống 1: Udemy chạy bình thường (Không lỗi trình phát video)
*   **Mô tả**: Trình phát video trên Udemy chạy bình thường. Khi tải trang bài học mới, không có popup lỗi nào che khuất giao diện.
*   **Giải pháp**: Sử dụng script [run_automation_normal.py](file:///G:/Agent2026Win/agents/1_foundations/code_udemy/run_automation_normal.py). 
*   **Quy trình chạy**:
    1. Click bài học trên sidebar.
    2. Chờ tải trang.
    3. Mở panel phiên âm.
    4. Cào dữ liệu lưu file.
    5. Đóng panel phiên âm để hiển thị lại sidebar bài học.

### Tình huống 2: Udemy bị lỗi trình phát video (Có popup chặn)
*   **Mô tả**: Trình phát video của Udemy gặp lỗi kỹ thuật và liên tục hiển thị một hộp thoại thông báo màu trắng ở giữa màn hình:
    > **Lỗi video**
    > Chúng tôi thử phát video của bạn nhiều lần nhưng đã xảy ra lỗi ngoài dự kiến. Chúng tôi đã thông báo cho các kỹ sư. **Đóng**
    
    Popup này che khuất màn hình và có thể cản trở một số thao tác với thanh điều khiển hoặc panel phiên âm.
*   **Giải pháp**: Sử dụng script [run_automation_with_error.py](file:///G:/Agent2026Win/agents/1_foundations/code_udemy/run_automation_with_error.py).
*   **Cơ chế xử lý lỗi**:
    - **Tự động đóng popup**: Script bổ sung hàm `close_video_error_popup` để tìm kiếm nút **Đóng** có mã HTML:
      ```html
      <button type="button" class="... error-display-module--close-button--..." data-purpose="close-popup"><span class="ud-btn-label">Đóng</span></button>
      ```
      Nó định vị nút này qua selector `button[data-purpose="close-popup"]` hoặc tìm văn bản `"Đóng"` và click vào đó trước khi thực hiện các bước khác.
    - **Thời điểm đóng**: Gọi kiểm tra đóng popup tại 2 thời điểm quan trọng:
      1. Trước khi click bài học mới trong sidebar (đảm bảo sidebar không bị mờ/khóa bởi popup cũ).
      2. Ngay sau khi bài học mới được tải xong (đảm bảo đóng popup mới hiển thị trước khi click nút "Phiên âm").
    - **Tự động mở rộng Sidebar**: Script quét và tự động bấm vào tất cả các Section accordion đang đóng trong sidebar (`button[aria-expanded="false"]`) để đảm bảo bài học tiếp theo luôn hiện diện trong DOM và có thể click.

---

## Hướng dẫn tùy biến cho chương mới (Chapters khác)

Khi cấu hình script cho một chương mới hoặc phạm vi bài học khác, các coding agent tiếp theo cần thực hiện:

### Bước 1: Khởi tạo các file rỗng cho chương mới
1. Mở file [create_files.py](file:///G:/Agent2026Win/agents/1_foundations/code_udemy/create_files.py).
2. Thay đổi đường dẫn thư mục đích `target_dir`:
    ```python
    target_dir = r"G:\Agent2026Win\agents\<chapter_folder>\tai_lieu"
    ```
3. Cập nhật danh sách tiêu đề bài học trong biến `titles` tương ứng với chương mới.
4. Chạy script để tạo hàng loạt file `.txt` rỗng:
    ```bash
    uv run 1_foundations/code_udemy/create_files.py
    ```

### Bước 2: Cấu hình Script tự động hóa
Tùy vào trạng thái Udemy có bị lỗi video hay không, mở file tương ứng:
- Bình thường: [run_automation_normal.py](file:///G:/Agent2026Win/agents/1_foundations/code_udemy/run_automation_normal.py)
- Có lỗi video: [run_automation_with_error.py](file:///G:/Agent2026Win/agents/1_foundations/code_udemy/run_automation_with_error.py)

Sau đó cập nhật các cấu hình sau ở đầu file:
1. **Thư mục lưu trữ tài liệu**:
    ```python
    TAI_LIEU_DIR = r"G:\Agent2026Win\agents\<chapter_folder>\tai_lieu"
    ```
2. **Khoảng số bài học cần chạy** (chỉ có trong file script):
    - Trong file `run_automation_normal.py` (hàm `main`):
      ```python
      lessons_to_process = [l for l in range(start_num, end_num + 1) if l in file_map]
      ```
    - Trong file `run_automation_with_error.py` (hàm `main`):
      ```python
      start_lesson = 109
      end_lesson = 131
      ```
3. **Biến chạy thử nghiệm (`TEST_MODE`)** (chỉ có trong bản xử lý lỗi):
    - Đặt `TEST_MODE = True` để chạy thử nghiệm trước với 2 bài đầu tiên xem độ ổn định và cách đóng popup lỗi.
    - Đặt `TEST_MODE = False` sau khi xác nhận chạy thử thành công để cào toàn bộ danh sách bài học.

### Bước 3: Chuẩn bị Trình duyệt
1. Khởi chạy trình duyệt Thorium ở chế độ debug port `9222`:
    ```powershell
    & "C:\Users\hieu\AppData\Local\Thorium\Application\thorium.exe" --remote-debugging-port=9222 --profile-directory="Profile 1"
    ```
2. Đăng nhập Udemy, chuyển tới tab khóa học.
3. Đảm bảo bạn đang ở bài học bắt đầu của dải cần cào.

### Bước 4: Chạy cào dữ liệu tự động
Chạy lệnh tương ứng trên terminal để khởi động:
- Đối với bản bình thường:
  ```bash
  uv run 1_foundations/code_udemy/run_automation_normal.py
  ```
- Đối với bản lỗi video:
  ```bash
  uv run 1_foundations/code_udemy/run_automation_with_error.py
  ```
*Lưu ý: Không tương tác chuột/bàn phím vào cửa sổ trình duyệt Thorium trong quá trình script đang chạy để tránh làm mất tiêu điểm (focus).*

---

## Chỉ dẫn dành cho AI Coding Agents (AI Agent Instructions)
> [!IMPORTANT]
> **Nếu bạn (coding agents) gặp lỗi không mong muốn hoặc quá trình tự động hóa bị kẹt** mà không thể tự giải quyết:
> 1. Hãy lập tức dừng việc thực thi script.
> 2. Khai báo rõ ràng tình huống lỗi (mô tả hành vi hiện tại, bước đang bị kẹt).
> 3. Yêu cầu người dùng hỗ trợ cung cấp **ảnh chụp màn hình (screenshot)** hoặc **mã nguồn HTML** của phần tử UI đang bị lỗi để cùng giải quyết.