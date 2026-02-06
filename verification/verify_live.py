from playwright.sync_api import sync_playwright, expect
import time

def verify_live():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto("http://localhost:3000")
            expect(page.locator(".magic-title")).to_be_visible(timeout=10000)
            time.sleep(1)
            page.screenshot(path="verification/live_preview.png", full_page=True)
            print("Screenshot taken.")
        except Exception as e:
            print(f"Failed: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_live()
