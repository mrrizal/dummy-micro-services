from fastapi import FastAPI

app = FastAPI()

@app.post("/process_payment/{order_id}")
async def process_payment(order_id: int, amount: float):
    # Business logic for processing payment
    # ...

    # Simulate a delay for illustration purposes
    import time
    time.sleep(3)

    return {"payment_status": "success"}
