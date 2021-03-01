from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext(storageState="wiki")

    # Open new page
    page = context.newPage()

    # Go to https://wiki.imgo.tv/
    page.goto("https://wiki.imgo.tv/")

    # Go to https://wiki.imgo.tv/#all-updates
    page.goto("https://wiki.imgo.tv/#all-updates")

    # Click text="最近访问"
    page.click("text=\"最近访问\"")
    # assert page.url == "https://wiki.imgo.tv/#recently-viewed"

    # Click text="剧本杀Pad端需求V0.1"
    page.click("text=\"剧本杀Pad端需求V0.1\"")
    print(page.text())
    # assert page.url == "https://wiki.imgo.tv/pages/viewpage.action?pageId=29130063"

    # Click //li[normalize-space(.)='t附件(67) 页面历史 限制 页面信息 已解决评论 (0) 以层级方式查看 查看页面源代码 导出为PDF 导出为Word Doc文件导入 复制 移动']/a/span/span
    page.click("//li[normalize-space(.)='t附件(67) 页面历史 限制 页面信息 已解决评论 (0) 以层级方式查看 查看页面源代码 导出为PDF 导出为Word Doc文件导入 复制 移动']/a/span/span")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)