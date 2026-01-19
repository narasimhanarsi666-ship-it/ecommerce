import httpx

class ApiClient:
    def __init__(self, base_url: str):
        self.client = httpx.Client(base_url=base_url)

    def add_item(self, user_id: str, sku: str, qty: int):
        r = self.client.post('/api/cart/item', json={"user_id": user_id, "sku": sku, "qty": qty})
        r.raise_for_status()
        return r.json()
