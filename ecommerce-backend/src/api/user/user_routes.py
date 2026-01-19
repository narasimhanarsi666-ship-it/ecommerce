from fastapi import APIRouter

router = APIRouter()

@router.get('/profile')
def profile(user_id: str):
    return {"user_id": user_id, "tier": "standard"}
