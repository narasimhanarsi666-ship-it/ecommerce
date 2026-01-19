import itertools, uuid, yaml

COMPONENTS = ["cart","checkout","payment","order","inventory","promotions","fraud","user"]
PRIORITIES = ["P1","P2","P3"]
USERS = ["guest","u1","u2","vip"]
SKUS = ["SKU-1","SKU-2","SKU-3"]
QTY = [0,1,2,10]
COUPONS = ["", "NEW10", "VIP20"]


def cases():
    for comp in COMPONENTS:
        for user, sku, qty, coupon, pr in itertools.product(USERS, SKUS, QTY, COUPONS, PRIORITIES):
            yield {
              "id": f"TC-{comp.upper()}-{uuid.uuid4().hex[:6]}",
              "component": comp,
              "user": user,
              "sku": sku,
              "qty": qty,
              "coupon": coupon,
              "priority": pr
            }

if __name__ == "__main__":
    data = list(itertools.islice(cases(), 1000))
    with open("mapping/test_metadata.yaml","w") as f:
        yaml.safe_dump(data, f, sort_keys=False)
    print({"generated": len(data)})
