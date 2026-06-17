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

# Path configuration
TAI_LIEU_DIR = r"G:\Agent2026Win\agents\2_openai\tai_lieu"

def get_file_map():
    """
    Scans the target directory and maps lesson numbers to file paths.
    E.g., 29 -> 'G:\\...\\29. Day 1 - ... .txt'
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

async def scrape_lesson_transcript(page, lesson_num, filepath):
    print(f"\n--- Processing Lesson {lesson_num} ---")
    
    # 1. Ensure transcript panel is closed before searching for lesson
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
        
    # 2. Find the lesson item in the sidebar
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
        
    # 3. Click the lesson item to navigate
    print(f"Clicking lesson {lesson_num}...")
    clickable = await target_item.query_selector('div[class*="item-link"]')
    if clickable:
        await clickable.click(force=True)
    else:
        await target_item.click(force=True)
        
    print(f"Navigating to lesson {lesson_num}. Waiting 2.5 seconds for page load...")
    await asyncio.sleep(2.5)
    
    # 4. Open transcript panel
    print("Opening transcript panel...")
    toggle_btn = await page.query_selector('button[data-purpose="transcript-toggle"]')
    if not toggle_btn:
        toggle_btn = await page.query_selector("button[aria-label*='Phiên âm'], button[aria-label*='Transcript']")
    if toggle_btn:
        await toggle_btn.click(force=True)
        print("Clicked transcript toggle to open panel. Waiting 1.5 seconds...")
        await asyncio.sleep(1.5)
    else:
        print("Error: Could not find transcript toggle button to open panel.")
        return False
        
    # 5. Extract transcript text
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
        
    # 6. Save to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"Success: Saved {len(lines)} lines for Lesson {lesson_num} to:")
    print(f"  {filepath}")
    
    # 7. Close transcript panel to return to clean state
    print("Closing transcript panel to return to clean state...")
    if toggle_btn:
        await toggle_btn.click(force=True)
        print("Clicked transcript toggle to close panel. Waiting 1.5 seconds...")
        await asyncio.sleep(1.5)
        
    return True

async def main():
    file_map = get_file_map()
    if not file_map:
        print(f"No lesson files found in {TAI_LIEU_DIR}.")
        return
        
    # We want to process lessons 29 to 49
    lessons_to_process = [l for l in range(29, 50) if l in file_map]
    print(f"Lessons to process: {lessons_to_process}")
    
    async with async_playwright() as p:
        try:
            browser = await p.chromium.connect_over_cdp("http://localhost:9222")
            print("Connected to Thorium.")
            
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
                
            success_count = 0
            fail_count = 0
            
            for lesson_num in lessons_to_process:
                filepath = file_map[lesson_num]
                success = await scrape_lesson_transcript(page, lesson_num, filepath)
                if success:
                    success_count += 1
                else:
                    fail_count += 1
                
                # Small pause between lessons
                await asyncio.sleep(2)
                
            print(f"\n--- Automation Finished ---")
            print(f"Successfully processed: {success_count} lessons.")
            print(f"Failed: {fail_count} lessons.")
            
        except Exception as e:
            print(f"Automation stopped due to error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
