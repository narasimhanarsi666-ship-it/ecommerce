import httpx, time

# A thin E2E example chaining API calls; UI flow is in Playwright tests

def test_guest_checkout(api_base):
    user = 'guest'
    with httpx.Client(base_url=api_base) as c:
        r = c.post('/api/cart/item', json={"user_id":user,"sku":"SKU-1","qty":1})
        assert r.status_code == 200
        total = r.json()['total']
        r = c.post('/api/payment/pay', json={"user_id":user,"method":"creditcard","amount": total})
        assert r.status_code == 200
        assert r.json()['status'] == 'APPROVED'
