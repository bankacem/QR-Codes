from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    # 1. Go to homepage
    page.goto("http://localhost:8000")
    page.wait_for_timeout(1000)
    page.screenshot(path="verification/screenshots/homepage.png")

    # 2. Scroll to articles
    page.locator("#articles").scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path="verification/screenshots/articles_section.py.png")

    # 3. Click the first article
    page.locator(".arc").first.click()
    page.wait_for_timeout(1000)

    # 4. Verify we are on an article page
    page.screenshot(path="verification/screenshots/article_page.png")

    # 5. Go back to homepage
    page.goto("http://localhost:8000")
    page.wait_for_timeout(500)

    # 6. Click the second article
    page.locator(".arc").nth(1).click()
    page.wait_for_timeout(1000)
    page.screenshot(path="verification/screenshots/article_page_2.png")

    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
