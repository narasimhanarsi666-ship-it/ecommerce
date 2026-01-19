from src.api.cart.cart_dto import CartItem, CartResponse
from src.domain.cart import Cart

CATALOG = {
    "SKU-1": 100.0,
    "SKU-2": 250.0,
    "SKU-3": 999.0
}

class PricingService:
    def price_cart(self, cart: Cart) -> CartResponse:
        items = []
        subtotal = 0.0
        for sku, qty in cart.items.items():
            price = CATALOG.get(sku, 0.0)
            subtotal += price * qty
            items.append(CartItem(sku=sku, qty=qty, price=price))
        total = round(subtotal, 2)
        return CartResponse(user_id=cart.user_id, items=items, subtotal=subtotal, total=total)
