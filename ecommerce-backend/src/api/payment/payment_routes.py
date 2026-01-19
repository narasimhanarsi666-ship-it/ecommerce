from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PayRequest(BaseModel):
    user_id: str
    method: str
    amount: float

@router.post('/pay')
def pay(req: PayRequest):
    # Mock approval
    return {"status": "APPROVED", "txn_id": f"TXN-{req.user_id}-{req.method}", "amount": req.amount}

@router.post('/refund')
def refund(txn_id: str, amount: float):
    return {"status": "REFUNDED", "txn_id": txn_id, "amount": amount}
