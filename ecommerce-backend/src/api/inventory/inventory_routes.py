from fastapi import APIRouter

router = APIRouter()

@router.get('/stock')
def stock(sku: str):
    return {"sku": sku, "available": 100}
