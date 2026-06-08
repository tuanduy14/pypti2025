import asyncio
import re
import os
from telethon import TelegramClient, events
from playwright.async_api import async_playwright

# --- CẤU HÌNH ---
api_id = 38194385
api_hash = 'f69dfab378e32218ea6aa05bb1a5e217'
bot_username = '@doncheck_bot'

# Đường dẫn Chrome của bạn
user_data_path = r"C:\Users\Laptop K1\AppData\Local\Google\Chrome\User Data"
profile_name = "Profile 1"

client = TelegramClient('session_bot_cmt', api_id, api_hash)
last_comment_text = ""


async def open_tiktok_and_cmt(link, content):
    async with async_playwright() as p:
        print(f"🚀 Đang truy cập TikTok: {link}")
        try:
            # Chạy trình duyệt với Profile 1
            browser_context = await p.chromium.launch_persistent_context(
                user_data_dir=user_data_path,
                headless=False,
                args=[f"--profile-directory={profile_name}", "--no-sandbox"]
            )
            page = await browser_context.new_page()
            await page.goto(link, wait_until="domcontentloaded")
            await asyncio.sleep(5)

            selector = 'div[data-e2e="comment-input"] div[contenteditable="true"]'
            await page.wait_for_selector(selector, timeout=15000)
            await page.click(selector)
            await page.fill(selector, content)
            await asyncio.sleep(1)
            await page.keyboard.press("Enter")

            print(f"✅ Đã cmt: {content}")
            await asyncio.sleep(3)
            await browser_context.close()
        except Exception as e:
            print(f"❌ Lỗi Playwright: {e}")


async def main():
    global last_comment_text
    try:
        await client.start()
        print(f"🤖 Bot đang trực đơn bằng Profile: {profile_name}...")
        await client.send_message(bot_username, '/cmt')

        @client.on(events.NewMessage(chats=bot_username))
        async def handler(event):
            global last_comment_text
            msg = event.raw_text

            # Kiểm tra xem có phải link không
            link_match = re.search(r'(https?://[^\s]+tiktok[^\s]+)', msg)

            if link_match:
                link_tt = link_match.group(1)

                # Nếu chưa có nội dung, đợi tối đa 3 giây xem tin nhắn chữ có đến không
                retry = 0
                while not last_comment_text and retry < 3:
                    print("⏳ Đang đợi nội dung cmt từ tin nhắn khác...")
                    await asyncio.sleep(1)
                    retry += 1

                if last_comment_text:
                    content_to_use = last_comment_text
                    last_comment_text = ""  # Reset ngay để tránh trùng đơn
                    await open_tiktok_and_cmt(link_tt, content_to_use)

                    print("⏳ Nghỉ 15s trước khi xin đơn mới...")
                    await asyncio.sleep(15)
                    await client.send_message(bot_username, '/cmt')
                else:
                    print("⚠️ Bỏ qua link vì không nhận được nội dung cmt kèm theo.")

            # Nếu là tin nhắn chữ (nội dung cmt)
            elif "/" not in msg and "http" not in msg and len(msg) > 2:
                if "ĐƠN #" not in msg and "Bấm vào link" not in msg:
                    last_comment_text = msg.strip()
                    print(f"📝 Đã ghi nhớ nội dung: {last_comment_text}")

        await client.run_until_disconnected()

    finally:
        # Giải phóng file .session-journal để tránh lỗi "Database is locked"
        await client.disconnect()
        print("🔌 Đã ngắt kết nối Telegram an toàn.")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass