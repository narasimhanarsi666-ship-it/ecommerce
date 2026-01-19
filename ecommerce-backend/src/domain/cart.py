from dataclasses import dataclass, field

@dataclass
class Cart:
    user_id: str
    items: dict[str, int] = field(default_factory=dict)

    def add(self, sku: str, qty: int):
        self.items[sku] = self.items.get(sku, 0) + qty

    def update(self, sku: str, qty: int):
        if qty <= 0:
            self.items.pop(sku, None)
        else:
            self.items[sku] = qty
