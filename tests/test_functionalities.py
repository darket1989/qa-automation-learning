from pages.login import LoginPage
from pages.cart_page import CartPage
from pages.checkout import CheckoutPage
from playwright.sync_api import Page, expect

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    assert page.get_by_test_id("title").is_visible

def test_add_remove_products(page):
    #Login
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    assert page.get_by_test_id("title").is_visible

    #Add products to cart
    cart_page = CartPage(page)
    cart_page.add_product("sauce-labs-backpack")
    cart_page.add_product("sauce-labs-bike-light")
    expect(cart_page.cart_badge).to_contain_text("2")

    #Go to cart
    cart_page.go_to_cart()

    #Remove products from cart
    cart_page.remove_product("sauce-labs-backpack")
    cart_page.remove_product("sauce-labs-bike-light")

    #Assert cart_badge no longer exists
    expect(cart_page.cart_badge.locator(".shopping_cart_badge")).to_be_hidden()


def test_checkout_process(page):
    #Login
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    assert page.get_by_test_id("title").is_visible

    #Add products to cart
    cart_page = CartPage(page)
    cart_page.add_product("sauce-labs-backpack")
    cart_page.add_product("sauce-labs-bike-light")
    expect(cart_page.cart_badge).to_contain_text("2")

    #Go to cart
    cart_page.go_to_cart()

    checkout = CheckoutPage(page)
    checkout.go_to_checkout()

    expect(checkout.checkout_message).to_be_visible()


def test_with_testdata(page, users):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(users["validUser"]["username"], users["validUser"]["password"])

    assert page.get_by_test_id("title").is_visible

def test_login_with_env_vars(page, creds):
    
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(creds["valid_user"], creds["pwd"])

    assert page.get_by_test_id("title").is_visible

