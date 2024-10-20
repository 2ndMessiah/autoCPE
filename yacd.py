import re
from playwright.sync_api import Playwright, sync_playwright, expect
import sys



yacdProxyPath="http://192.168.31.1:9999/ui/#/proxies"
def run(playwright: Playwright,proxy,proxyemby) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(yacdProxyPath)
    page.get_by_role("button", name="科学上网Selector").click()
    page.get_by_text(proxy).first.click()
    page.get_by_role("button", name="emby_selSelector").click()
    page.get_by_text(proxyemby).nth(1).click()

    # ---------------------
    context.close()
    browser.close()



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <yacd_proxy_path> <selector_name>")
        sys.exit(1)
    
    proxy = sys.argv[1]
    proxyemby = sys.argv[2]

    with sync_playwright() as playwright:
        run(playwright, proxy, proxyemby)