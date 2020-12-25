from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext(storageState="jd")

    # Open new page
    page = context.newPage()

    # Go to https://www.jd.com/
    page.goto("https://www.jd.com/")

    # Click input[aria-label="搜索"]
    page.click("input[aria-label=\"搜索\"]")

    # Fill input[aria-label="搜索"]
    # with page.expect_navigation(url="https://search.jd.com/Search?keyword=%E8%8C%85%E5%8F%B0&enc=utf-8&wq=%E8%8C%85%E5%8F%B0&pvid=73d73c9b822748e5be05d10c309ce257"):
    with page.expect_navigation():
        page.fill("input[aria-label=\"搜索\"]", "茅台")

    # Click //a[normalize-space(@title)='仅限正式PLUS会员预约享抢购资格，12月24日10:30开启预约，12月25日10:00开始抢购（京东APP需升级至8.5.6版本及以上）']/img
    with page.expect_popup() as popup_info:
        page.click("//a[normalize-space(@title)='仅限正式PLUS会员预约享抢购资格，12月24日10:30开启预约，12月25日10:00开始抢购（京东APP需升级至8.5.6版本及以上）']/img")
    page1 = popup_info.value

    # Click text="开始预约"
    page1.click("text=\"开始预约\"")
    # assert page1.url == "https://yushou.jd.com/toYuyue.action?sku=100012043978&key=6873604fdcdd146e64f79612425f9d03&shopId=1000085463&isPlusLimit=0"

    # Click text="查看我的预约"
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("text=\"查看我的预约\"")

    # 0× click
    page1.click("//p[normalize-space(.)='查看我的预约']")

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)