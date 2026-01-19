import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.mark.parametrize("user, sku, qty", [("u1","SKU-1",1),("u1","SKU-2",2)])
def test_cart_add(user, sku, qty):
    r = client.post("/api/cart/item", json={"user_id": user, "sku": sku, "qty": qty})
    assert r.status_code == 200
    data = r.json()
    assert any(i["sku"] == sku and i["qty"] == qty for i in data["items"])
