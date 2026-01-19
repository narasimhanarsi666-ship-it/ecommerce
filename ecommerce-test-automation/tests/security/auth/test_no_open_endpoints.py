import httpx

def test_health_open(api_base):
    r = httpx.get(f"{api_base}/health")
    assert r.status_code == 200
