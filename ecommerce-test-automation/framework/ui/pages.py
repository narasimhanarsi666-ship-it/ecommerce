from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
    def goto(self, base: str):
        self.page.goto(f"{base}/cart")
    def add_sku1(self):
        self.page.get_by_role("button", name="Add SKU-1").click()
