from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.checkout_message = page.locator("[data-test=\"title\"]")

    def go_to_checkout(self):
        self.checkout_button.click()
