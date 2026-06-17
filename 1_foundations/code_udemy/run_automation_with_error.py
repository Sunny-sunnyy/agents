import asyncio
import os
import sys
import re
from playwright.async_api import async_playwright

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# Path configuration - Thay đổi đường dẫn này tương ứng với chương cần chạy
TAI_LIEU_DIR = r"G:\Agent2026Win\agents\6_mcp\tai_lieu"
TEST_MODE = False  # Đổi thành True để test trước với 2 bài đầu trong dải được cấu hình

def get_file_map():
    """
    Scans the target directory and maps lesson numbers to file paths.
    E.g., 109 -> 'G:\\...\\109. Day 1 - ... .txt'
    """
    file_map = {}
    if not os.path.exists(TAI_LIEU_DIR):
        print(f"Error: Directory does not exist: {TAI_LIEU_DIR}")
        return file_map
        
    for filename in os.listdir(TAI_LIEU_DIR):
        if filename.endswith(".txt"):
            match = re.match(r"^(\d+)\.", filename)
            if match:
                lesson_num = int(match.group(1))
                filepath = os.path.join(TAI_LIEU_DIR, filename)
                file_map[lesson_num] = filepath
                
    return file_map

async def close_video_error_popup(page):
    """
    Checks if the video error popup is visible and clicks the 'Đóng' (Close) button.
    """
    print("Checking for video error popup...")
    try:
        # Tìm nút đóng popup bằng thuộc tính data-purpose, class prefix hoặc text
        close_btn = await page.query_selector('button[data-purpose="close-popup"], button[class*="error-display-module--close-button"], button:has-text("Đóng")')
        if close_btn:
            is_visible = await close_btn.is_visible()
            if is_visible:
                print("Found 'Lỗi video' popup. Clicking 'Đóng'...")
                await close_btn.click(force=True)
                await asyncio.sleep(1.5)
                return True
        else:
            # Fallback dùng text locator của Playwright
            close_btn_locator = page.locator('button:has-text("Đóng"), span:has-text("Đóng")').first
            if await close_btn_locator.is_visible():
                print("Found 'Lỗi video' popup via text locator. Clicking it...")
                await close_btn_locator.click(force=True)
                await asyncio.sleep(1.5)
                return True
    except Exception as e:
        print(f"Warning: Could not close popup: {e}")
    return False

async def scrape_lesson_transcript(page, lesson_num, filepath):
    print(f"\n--- Processing Lesson {lesson_num} ---")
    
    # 0. Kiểm tra và đóng popup lỗi video (nếu có) trước khi bắt đầu chuyển bài
    await close_video_error_popup(page)
    
    # 1. Đảm bảo panel phiên âm đóng trước khi tìm bài học để hiển thị sidebar bài học
    header = await page.query_selector('[class*="sidebar--sidebar-header"]')
    is_transcript_open = False
    if header:
        header_text = await header.inner_text()
        if "Phiên âm" in header_text or "Transcript" in header_text:
            is_transcript_open = True
            
    if is_transcript_open:
        print("Transcript panel is open. Closing it to reveal 'Nội dung khóa học'...")
        toggle_btn = await page.query_selector('button[data-purpose="transcript-toggle"]')
        if not toggle_btn:
            toggle_btn = await page.query_selector("button[aria-label*='Phiên âm'], button[aria-label*='Transcript']")
        if toggle_btn:
            await toggle_btn.click(force=True)
            print("Clicked transcript toggle to close panel. Waiting 1.5 seconds...")
            await asyncio.sleep(1.5)
        else:
            print("Warning: Could not find transcript toggle button to close panel.")
    else:
        print("Transcript panel is already closed. 'Nội dung khóa học' should be visible.")
        
    # 2. Mở rộng tất cả các Section accordion đang đóng trong sidebar
    print("Expanding all sections in sidebar...")
    try:
        closed_sections = await page.query_selector_all('button[aria-expanded="false"]')
        for sec in closed_sections:
            sec_text = await sec.inner_text()
            if "Phần" in sec_text or "Section" in sec_text:
                await sec.click(force=True)
                await asyncio.sleep(0.5)
    except Exception as e:
        print(f"Warning: Error expanding sections: {e}")

    # 3. Tìm bài học tương ứng trong sidebar
    print("Searching for lesson item in sidebar...")
    lesson_items = await page.query_selector_all('li[class*="curriculum-item-link--curriculum-item"]')
    target_item = None
    
    for item in lesson_items:
        text = await item.inner_text()
        clean_text = " ".join(text.split()).strip()
        match = re.search(rf"\b{lesson_num}\.", clean_text)
        if match:
            target_item = item
            print(f"Found lesson item: '{clean_text[:60]}...'")
            break
            
    if not target_item:
        print(f"Error: Could not find lesson item {lesson_num} in the sidebar.")
        return False
        
    # 4. Click bài học để chuyển hướng
    print(f"Clicking lesson {lesson_num}...")
    clickable = await target_item.query_selector('div[class*="item-link"]')
    if clickable:
        await clickable.click(force=True)
    else:
        await target_item.click(force=True)
        
    print(f"Navigating to lesson {lesson_num}. Waiting 3 seconds for page load...")
    await asyncio.sleep(3)
    
    # 5. Xử lý popup lỗi video xuất hiện sau khi bài mới được tải
    await close_video_error_popup(page)
    
    # 6. Mở panel phiên âm
    print("Opening transcript panel...")
    toggle_btn = await page.query_selector('button[data-purpose="transcript-toggle"]')
    if not toggle_btn:
        toggle_btn = await page.query_selector("button[aria-label*='Phiên âm'], button[aria-label*='Transcript']")
    if toggle_btn:
        await toggle_btn.click(force=True)
        print("Clicked transcript toggle to open panel. Waiting 2 seconds...")
        await asyncio.sleep(2)
    else:
        print("Error: Could not find transcript toggle button to open panel.")
        return False
        
    # 7. Trích xuất text phiên âm
    print("Extracting transcript text...")
    cues = await page.query_selector_all('p[class*="transcript--underline-cue"]')
    if not cues:
        cues = await page.query_selector_all('section.sidebar--sidebar--paNd5 p')
        
    if not cues:
        print("Error: Failed to find any transcript lines.")
        return False
        
    lines = []
    for cue in cues:
        t = await cue.inner_text()
        t = t.strip()
        if t:
            lines.append(t)
            
    if not lines:
        print("Error: Transcript content is empty.")
        return False
        
    # 8. Lưu vào file txt
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"Success: Saved {len(lines)} lines for Lesson {lesson_num} to:")
    print(f"  {filepath}")
    
    # 9. Đóng panel phiên âm để chuẩn bị cho bài tiếp theo hiển thị sidebar bài học
    print("Closing transcript panel to return to clean state...")
    if toggle_btn:
        await toggle_btn.click(force=True)
        print("Clicked transcript toggle to close panel. Waiting 1.5 seconds...")
        await asyncio.sleep(1.5)
        
    return True

async def main():
    file_map = get_file_map()
    if not file_map:
        print("No lesson files found in target directory.")
        return
        
    # Cấu hình dải bài học cần chạy tại đây
    start_lesson = 109
    end_lesson = 131
    
    if TEST_MODE:
        # Chế độ test lấy 2 bài đầu trong dải cấu hình
        lessons_to_process = [start_lesson, start_lesson + 1]
        print(f"TEST MODE: Processing lessons: {lessons_to_process}")
    else:
        lessons_to_process = [l for l in range(start_lesson, end_lesson + 1) if l in file_map]
        print(f"FULL MODE: Processing lessons: {lessons_to_process}")
        
    async with async_playwright() as p:
        try:
            print("Connecting to Thorium at http://localhost:9222...")
            browser = await p.chromium.connect_over_cdp("http://localhost:9222")
            print("Connected successfully.")
            
            contexts = browser.contexts
            page = None
            for context in contexts:
                for pg in context.pages:
                    if "udemy.com/course" in pg.url:
                        page = pg
                        break
                if page:
                    break
                    
            if not page:
                print("Error: Could not find Udemy tab.")
                return
                
            print(f"Found Udemy tab: {page.url}")
            
            success_count = 0
            fail_count = 0
            
            for lesson_num in lessons_to_process:
                if lesson_num not in file_map:
                    print(f"Warning: File for lesson {lesson_num} does not exist in target directory.")
                    continue
                filepath = file_map[lesson_num]
                success = await scrape_lesson_transcript(page, lesson_num, filepath)
                if success:
                    success_count += 1
                else:
                    fail_count += 1
                
                await asyncio.sleep(2)
                
            print(f"\n--- Automation Finished ---")
            print(f"Successfully processed: {success_count} lessons.")
            print(f"Failed: {fail_count} lessons.")
            
        except Exception as e:
            print(f"Automation stopped due to error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
