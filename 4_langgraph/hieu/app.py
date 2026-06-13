# Import thư viện Gradio để xây dựng giao diện web và class Sidekick (AI assistant)
import gradio as gr
from sidekick import Sidekick

# Hàm khởi tạo Sidekick khi load app
async def setup():
    """Tạo instance Sidekick mới và setup các tools (browser, search, file management...)"""
    sidekick = Sidekick()
    await sidekick.setup()
    return sidekick


# Hàm xử lý tin nhắn từ user
async def process_message(sidekick, message, success_criteria, history):
    """Gửi message và success criteria tới Sidekick, nhận về kết quả và cập nhật lịch sử chat"""
    results = await sidekick.run_superstep(message, success_criteria, history)
    return results, sidekick


# Hàm reset toàn bộ hội thoại
async def reset():
    """Tạo Sidekick mới, xóa sạch message và success_criteria, reset lịch sử chat"""
    new_sidekick = Sidekick()
    await new_sidekick.setup()
    return "", "", None, new_sidekick


# Hàm giải phóng tài nguyên khi đóng app
def free_resources(sidekick):
    """Đóng browser và các tài nguyên khi user thoát app để tránh memory leak"""
    print("Cleaning up")
    try:
        if sidekick:
            sidekick.cleanup()
    except Exception as e:
        print(f"Exception during cleanup: {e}")


# === XÂY DỰNG GIAO DIỆN GRADIO ===
with gr.Blocks(title="Sidekick", theme=gr.themes.Default(primary_hue="emerald")) as ui:
    gr.Markdown("## Sidekick Personal Co-Worker")
    # State lưu trữ instance Sidekick, tự động gọi free_resources khi đóng app
    sidekick = gr.State(delete_callback=free_resources)

    # Chatbot hiển thị lịch sử hội thoại
    with gr.Row():
        chatbot = gr.Chatbot(label="Sidekick", height=300, type="messages")
    
    # Ô nhập liệu cho user
    with gr.Group():
        with gr.Row():
            message = gr.Textbox(show_label=False, placeholder="Your request to the Sidekick")
        with gr.Row():
            success_criteria = gr.Textbox(
                show_label=False, placeholder="What are your success critiera?"
            )
    
    # Nút Reset và Go
    with gr.Row():
        reset_button = gr.Button("Reset", variant="stop")
        go_button = gr.Button("Go!", variant="primary")

    # === KẾT NỐI CÁC SỰ KIỆN ===
    # Khi load app, khởi tạo Sidekick
    ui.load(setup, [], [sidekick])
    
    # Khi user nhấn Enter ở ô message hoặc success_criteria -> xử lý
    message.submit(
        process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick]
    )
    success_criteria.submit(
        process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick]
    )
    
    # Khi click nút Go -> xử lý
    go_button.click(
        process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick]
    )
    
    # Khi click Reset -> xóa hết và tạo Sidekick mới
    reset_button.click(reset, [], [message, success_criteria, chatbot, sidekick])

# Khởi chạy app và tự động mở browser
ui.launch(inbrowser=True)
