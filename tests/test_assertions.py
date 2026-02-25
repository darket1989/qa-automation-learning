from pages.login import LoginPage
from playwright.sync_api import Page, expect

def test_basic_assertions(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")

    #Basic assertions after login
    assert page.locator('[data-test="title"]')
    assert page.locator('[data-test="shopping-cart-link"]')
    assert page.locator('[data-test="inventory-list"]')
    
    expect(page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')).to_have_css("color","rgb(19, 35, 34)")
    expect(page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')).to_have_css("background-color","rgb(255, 255, 255)")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    
    expect(page.locator('[data-test="remove-sauce-labs-backpack"]')).to_have_css("color","rgb(226, 35, 26)")
    