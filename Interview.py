from playwright.sync_api import Page,expect


def test_loginSuccess(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("rahulshettyacademy")
    page.locator("#password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("Consultant")
    page.get_by_role("button",name="Sign In").click()