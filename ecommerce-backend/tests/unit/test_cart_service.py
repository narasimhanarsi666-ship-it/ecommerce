from src.services.cart_service import CartService

def test_add_and_price():
    svc = CartService()
    resp = svc.add_item("u1", "SKU-1", 2)
    assert resp.subtotal == 200.0
    assert any(i.sku == "SKU-1" and i.qty == 2 for i in resp.items)
