from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class OrderCreate(BaseModel):
    user_id: str
    items: list[dict]

@router.post('/create')
def create(order: OrderCreate):
    return {"order_id": "ORD-1", "user_id": order.user_id, "items": order.items}

@router.get('/history')
def history(user_id: str):
    return {"user_id": user_id, "orders": []}
