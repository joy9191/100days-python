import time
from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext(storageState="jd")

    # Open new page
    page = context.newPage()

    # Go to https://www.jd.com/
    page.goto("https://www.jd.com/")

    # Click text="Hi，" >> text="jd星心"
    with page.expect_popup() as popup_info:
        page.click("text=\"Hi，\" >> text=\"jd星心\"")
    page1 = popup_info.value

    # 0× click
    page1.click("dd[id=\"_MYJD_bean\"]")

    # Click text="我的预约"
    page1.click("text=\"我的预约\"")

    # Click text="立即抢购"
    page1.click("text=\"立即抢购\"")
    # assert page1.url == "https://item.jd.com/100012043978.html"

    # Click text="抢购"
    page1.click("text=\"抢购\"")
    # assert page1.url == "https://marathon.jd.com/seckill/seckill.action?skuId=100012043978&num=1&rid=1608861619"

    # Go to https://marathon.jd.com/koFail.html
    page1.goto("https://marathon.jd.com/koFail.html")

    time.sleep(100)

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)