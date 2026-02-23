from playwright.sync_api import Page
import pytest

URL = "https://www.saucedemo.com/"
login_dashboard = "https://www.saucedemo.com/inventory.html"

def test_valid_login(page: Page):
    page.goto(URL)
    
    username_input = page.get_by_placeholder("Username")
    username_input.fill("standard_user")

    password_input = page.get_by_placeholder("Password")
    password_input.fill("secret_sauce")

    login_button = page.locator("input#login-button")
    login_button.click()

    page.screenshot(path="login.png")
    assert page.get_by_test_id("title").is_visible
    assert page.url == login_dashboard

def test_invalid_login(page: Page):
    page.goto(URL)
    
    username_input = page.get_by_placeholder("Username")
    username_input.fill("standard_user")

    password_input = page.get_by_placeholder("Password")
    password_input.fill("secret")

    login_button = page.locator("input#login-button")
    login_button.click()

    error_message = page.get_by_text("Epic sadface: Username and password do not match any user in this service")
    assert error_message.is_visible
    page.screenshot(path= "error_message_login.png")

def test_logout_session(page: Page):
    page.goto(URL)
    
    username_input = page.get_by_placeholder("Username")
    username_input.fill("standard_user")

    password_input = page.get_by_placeholder("Password")
    password_input.fill("secret_sauce")

    login_button = page.locator("input#login-button")
    login_button.click()

    open_menu_button = page.locator("button#react-burger-menu-btn")
    open_menu_button.click()

    logout_option = page.locator("a#logout_sidebar_link")
    logout_option.click()

    assert login_button.is_visible()
    page.screenshot(path="successfull_login.png")


@pytest.mark.parametrize("username, password",[
    ("error_user","secret_sauce"),
    ("performance_glitch_user","secret_sauce"),
    ("visual_user","secret_sauce")])

def test_multiple_users(page: Page, username, password):
    page.goto(URL)
    
    username_input = page.get_by_placeholder("Username")
    username_input.fill(username)

    password_input = page.get_by_placeholder("Password")
    password_input.fill(password)

    login_button = page.locator("input#login-button")
    login_button.click()

    assert page.get_by_test_id("title").is_visible
    assert page.url == login_dashboard