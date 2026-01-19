import pytest, httpx

CASES = [
    ("u1", "SKU-1", 1, None),
    ("u1", "SKU-1", 2, None),
    ("u2", "SKU-2", 3, None),
]

@pytest.mark.parametrize("user,sku,qty,expected_total", CASES)
@pytest.mark.asyncio
async def test_add_variants(api_base, user, sku, qty, expected_total):
    async with httpx.AsyncClient(base_url=api_base) as c:
        r = await c.post("/api/cart/item", json={"user_id": user, "sku": sku, "qty": qty})
        assert r.status_code == 200
        data = r.json()
        assert any(i["sku"] == sku and i["qty"] == qty for i in data["items"])
