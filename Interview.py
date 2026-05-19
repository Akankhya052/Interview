from playwright.sync_api import Page

def test_Interview(page:Page):
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").type("laptop")
    page.locator(".s-suggestion").filter(has_text = "stand metal").click()
    page.wait_for_timeout(3000)