import re
from playwright.sync_api import Playwright, sync_playwright, expect
import sys



yacdProxyPath="http://192.168.31.1:9999/ui/#/proxies"
def run(playwright: Playwright,proxy,proxyemby,autoclose) -> None:
    print("params: ",proxy," ",proxyemby," ",autoclose)
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(yacdProxyPath)
    if autoclose == "1":
        page.locator("._btn_vsco8_4").first.click()
        page.locator("xpath=/html/body/div[4]/div/div/div[3]/div/div/div[2]").click()
        page.get_by_role("dialog").press("Escape")
        print("autoclose selected")
    page.get_by_role("button", name="科学上网Selector").click()
    page.get_by_text(proxy).first.click()
    page.get_by_role("button", name="emby_selSelector").click()
    page.get_by_text(proxyemby).nth(1).click()

    # ---------------------
    context.close()
    browser.close()



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <yacd_proxy_path> <selector_name> <autoclose:1/0>")
        sys.exit(1)
    
    proxy = sys.argv[1]
    proxyemby = sys.argv[2]
    autoclose = sys.argv[3]

    with sync_playwright() as playwright:
        run(playwright, proxy, proxyemby, autoclose)