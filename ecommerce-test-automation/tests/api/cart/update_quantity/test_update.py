import httpx, pytest

@pytest.mark.asyncio
async def test_update_qty(api_base):
    async with httpx.AsyncClient(base_url=api_base) as c:
        await c.post('/api/cart/item', json={"user_id":"u1","sku":"SKU-1","qty":2})
        r = await c.patch('/api/cart/item', json={"user_id":"u1","sku":"SKU-1","qty":1})
        assert r.status_code == 200
