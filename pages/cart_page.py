from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_badge = page.locator("[data-test=\"shopping-cart-link\"]")
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")

    
    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def add_product(self, product_name : str):
        add_button = self.page.locator(f"#add-to-cart-{product_name}")
        add_button.click()

    def remove_product(self, product_name: str):
        
        remove_button = self.page.locator(f"#remove-{product_name}")
        remove_button.click()

    def get_cart_count(self) -> int:
        
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.text_content())

    def get_cart_items(self):
        return self.cart_items.all_text_contents()




