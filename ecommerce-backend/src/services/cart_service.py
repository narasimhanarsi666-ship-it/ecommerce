from src.domain.cart import Cart
from src.services.pricing_service import PricingService

class CartService:
    def __init__(self):
        self._store: dict[str, Cart] = {}
        self._pricing = PricingService()

    def _get(self, user_id: str) -> Cart:
        return self._store.setdefault(user_id, Cart(user_id=user_id, items={}))

    def get_cart(self, user_id: str):
        cart = self._get(user_id)
        return self._pricing.price_cart(cart)

    def add_item(self, user_id: str, sku: str, qty: int):
        if qty <= 0:
            raise ValueError("qty must be > 0")
        cart = self._get(user_id)
        cart.add(sku, qty)
        return self._pricing.price_cart(cart)

    def update_qty(self, user_id: str, sku: str, qty: int):
        cart = self._get(user_id)
        cart.update(sku, qty)
        return self._pricing.price_cart(cart)

    def merge(self, from_user_id: str, to_user_id: str):
        src = self._get(from_user_id)
        dst = self._get(to_user_id)
        for sku, qty in src.items.items():
            dst.items[sku] = dst.items.get(sku, 0) + qty
        self._store[from_user_id] = Cart(user_id=from_user_id, items={})
        return self._pricing.price_cart(dst)
