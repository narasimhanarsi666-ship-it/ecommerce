from playwright.sync_api import sync_playwright

def test_add_to_cart_ui(frontend_base):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{frontend_base}/cart")
        page.get_by_role("button", name="Add SKU-1").click()
        page.wait_for_selector("text=Subtotal:")
        browser.close()
