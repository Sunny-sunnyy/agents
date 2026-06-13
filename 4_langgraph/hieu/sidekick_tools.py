# === IMPORT THƯ VIỆN ===
# Playwright: điều khiển browser tự động
from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit

# File management, search, Wikipedia, Python REPL
from dotenv import load_dotenv
import os
import requests
from langchain.agents import Tool
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_experimental.tools import PythonREPLTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

# === LOAD BIẾN MÔI TRƯỜNG VÀ THÔNG TIN PUSHOVER ===
load_dotenv(override=True)
pushover_token = os.getenv("PUSHOVER_TOKEN")  # Token để gửi thông báo
pushover_user = os.getenv("PUSHOVER_USER")    # User ID nhận thông báo
pushover_url = "https://api.pushover.net/1/messages.json"  # API endpoint
serper = GoogleSerperAPIWrapper()  # Tool tìm kiếm Google

# === TOOL 1: TẠO CÁC PLAYWRIGHT BROWSER TOOLS ===
async def playwright_tools():
    """
    Khởi tạo browser automation tools cho AI:
    - Mở trình duyệt Chromium (headless=False để thấy giao diện)
    - Tạo các tools để AI có thể: navigate URL, click, type, extract data...
    - Trả về: (tools, browser, playwright) để dùng và cleanup sau
    """
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    return toolkit.get_tools(), browser, playwright


# === TOOL 2: GỬI THÔNG BÁO PUSHOVER ===
def push(text: str):
    """
    Gửi thông báo push tới điện thoại/máy tính qua Pushover API
    Dùng khi AI muốn báo cáo kết quả hoặc nhắc nhở user
    """
    requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})
    return "success"


# === TOOL 3: QUẢN LÝ FILE ===
def get_file_tools():
    """
    Tạo các tools quản lý file trong thư mục "sandbox":
    - Đọc, viết, copy, delete file
    - List các file trong folder
    """
    toolkit = FileManagementToolkit(root_dir="sandbox")
    return toolkit.get_tools()


# === TẬP HỢP TẤT CẢ CÁC TOOLS KHÁC ===
async def other_tools():
    """
    Kết hợp các tools không phải browser:
    1. Push notification tool
    2. File management tools (read/write/list files)
    3. Google Search tool (tìm kiếm trên mạng)
    4. Wikipedia tool (tra cứu Wikipedia)
    5. Python REPL (chạy code Python)
    """
    # 1. Push notification
    push_tool = Tool(name="send_push_notification", func=push, description="Use this tool when you want to send a push notification")
    
    # 2. File management
    file_tools = get_file_tools()

    # 3. Google Search
    tool_search =Tool(
        name="search",
        func=serper.run,
        description="Use this tool when you want to get the results of an online web search"
    )

    # 4. Wikipedia
    wikipedia = WikipediaAPIWrapper()
    wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)

    # 5. Python REPL (chạy code Python trong sandbox)
    python_repl = PythonREPLTool()
    
    return file_tools + [push_tool, tool_search, python_repl,  wiki_tool]

