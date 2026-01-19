from pydantic import BaseModel, Field

class AddItemRequest(BaseModel):
    user_id: str
    sku: str
    qty: int = Field(gt=0)

class UpdateQtyRequest(BaseModel):
    user_id: str
    sku: str
    qty: int = Field(ge=0)

class MergeCartRequest(BaseModel):
    from_user_id: str
    to_user_id: str

class CartItem(BaseModel):
    sku: str
    qty: int
    price: float

class CartResponse(BaseModel):
    user_id: str
    items: list[CartItem]
    subtotal: float
    total: float
