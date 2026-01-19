from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Address(BaseModel):
    line1: str
    city: str
    postal: str

@router.post('/address')
def set_address(user_id: str, addr: Address):
    return {"user_id": user_id, "address": addr.model_dump()}

@router.get('/price')
def price(user_id: str):
    # Placeholder pricing breakdown
    return {"user_id": user_id, "subtotal": 100, "shipping": 0, "tax": 0, "total": 100}
