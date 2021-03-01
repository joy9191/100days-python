from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://wiki.imgo.tv/login.action?os_destination=%2Fpages%2Fviewpage.action%3FpageId%3D23480453&permissionViolation=true
    page.goto("https://wiki.imgo.tv/login.action?os_destination=%2Fpages%2Fviewpage.action%3FpageId%3D23480453&permissionViolation=true")

    # Click input[name="os_username"]
    page.click("input[name=\"os_username\"]")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)