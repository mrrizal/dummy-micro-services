from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DeliveryRequest(BaseModel):
    order_id: int
    address: str

@app.post("/delivery/initiate_delivery/")
async def initiate_delivery(delivery_request: DeliveryRequest):
    order_id = delivery_request.order_id
    address = delivery_request.address

    # Business logic for initiating delivery
    # ...

    # Simulate a delay for illustration purposes
    import time
    time.sleep(4)

    return {
        "order_id": order_id,
        "delivery_status": "in_progress",
        "address": address
    }
