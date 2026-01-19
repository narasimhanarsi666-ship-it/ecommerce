from fastapi import APIRouter, Depends, HTTPException
from .cart_dto import AddItemRequest, UpdateQtyRequest, MergeCartRequest, CartResponse
from src.services.cart_service import CartService

router = APIRouter()

def get_service():
    return CartService()

@router.get("/", response_model=CartResponse)
def get_cart(user_id: str, svc: CartService = Depends(get_service)):
    return svc.get_cart(user_id)

@router.post("/item", response_model=CartResponse)
def add_item(req: AddItemRequest, svc: CartService = Depends(get_service)):
    try:
        return svc.add_item(req.user_id, req.sku, req.qty)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/item", response_model=CartResponse)
def update_qty(req: UpdateQtyRequest, svc: CartService = Depends(get_service)):
    return svc.update_qty(req.user_id, req.sku, req.qty)

@router.post('/merge', response_model=CartResponse)
def merge(req: MergeCartRequest, svc: CartService = Depends(get_service)):
    return svc.merge(req.from_user_id, req.to_user_id)
