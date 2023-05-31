import os
import stripe
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from environs import Env


env = Env()
env.read_env()


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

stripe.api_key = env.str("STRIPE_KEY")

app.state.stripe_customer_id = None


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "hasCustomer": app.state.stripe_customer_id is not None})



@app.post("/payment")
async def payment(request: Request):
    data = await request.json()
    




if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)