from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class OrderRequest(BaseModel):
    user_id: int
    order_id: int
    items: list

@app.post("/order/create_order/")
async def create_order(order_request: OrderRequest):
    # Business logic for creating an order
    # ...

    # Simulate a delay for illustration purposes
    import time
    time.sleep(2)

    return {
        "user_id": order_request.user_id,
        "order_id": order_request.order_id,
        "items": order_request.items,
        "order_status": "in_progress",
        "total_amount": 10000
    }
