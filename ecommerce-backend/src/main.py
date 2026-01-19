from fastapi import FastAPI
from src.api.cart.cart_routes import router as cart_router
from src.api.checkout.checkout_routes import router as checkout_router
from src.api.payment.payment_routes import router as payment_router
from src.api.order.order_routes import router as order_router
from src.api.user.user_routes import router as user_router
from src.api.inventory.inventory_routes import router as inventory_router

app = FastAPI(title="Ecommerce API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(cart_router, prefix="/api/cart", tags=["cart"])
app.include_router(checkout_router, prefix="/api/checkout", tags=["checkout"])
app.include_router(payment_router, prefix="/api/payment", tags=["payment"])
app.include_router(order_router, prefix="/api/order", tags=["order"])
app.include_router(user_router, prefix="/api/user", tags=["user"])
app.include_router(inventory_router, prefix="/api/inventory", tags=["inventory"])
