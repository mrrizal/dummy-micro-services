from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import httpx

app = FastAPI()

# OAuth2 for securing the API
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dummy function to calculate total amount
def calculate_total(items: str):
    # Dummy logic
    return 100.0

async def create_order(user_id: int, items: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"http://order-service/create_order/{user_id}", json={"items": items})
        return response.json()

async def process_payment(order_id: int, amount: float):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"http://payment-service/process_payment/{order_id}", json={"amount": amount})
        return response.json()

async def initiate_delivery(order_id: int, address: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"http://delivery-service/initiate_delivery/{order_id}", json={"address": address})
        return response.json()

@app.post("/checkout/{user_id}")
async def checkout(user_id: int, items: str, address: str, token: str = Depends(oauth2_scheme)):
    # Dummy token validation
    if token != "fake-token":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Step 1: Create an order
    order_response = await create_order(user_id, items)
    order_id = order_response["order_id"]

    # Step 2: Process payment
    payment_status_response = await process_payment(order_id, calculate_total(items))
    payment_status = payment_status_response["payment_status"]

    # Step 3: Initiate delivery if payment successful
    if payment_status == "success":
        delivery_response = await initiate_delivery(order_id, address)
        delivery_status = delivery_response["delivery_status"]
        return {"message": f"Order placed successfully. {delivery_status}"}
    else:
        return {"message": "Payment failed. Please try again."}
