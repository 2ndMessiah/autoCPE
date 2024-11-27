import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True,slow_mo=4000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://akile.io/login")
    page.get_by_placeholder("请输入邮箱").click()
    page.get_by_placeholder("请输入邮箱").fill("lym.0072003@gmail.com")
    page.get_by_placeholder("请输入密码").click()
    page.get_by_placeholder("请输入密码").fill("trillion-savings5-variable")
    page.get_by_role("button", name="登录").click()
    page.goto("https://akile.io/console")
    page.get_by_role("button", name="每日签到").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
