import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.1.1/common/login.html")
    page.locator("#username").click()
    page.locator("#username").fill("admin")
    page.locator("#password").click()
    page.locator("#password").fill("admin")
    page.get_by_role("button", name="登录").click()
    page.locator("span").filter(has_text="移动网络").first.click()
    page.get_by_role("link", name="SIM卡管理").click()
    page.get_by_role("button", name="应用").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
