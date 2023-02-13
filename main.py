from fastapi import FastAPI, HTTPException

from model import Todo, crazy, price

from database1 import *
from Bitcoin import *
from ERC20_Balance import *
from moonbeam import *
# from database2 import (
#     # fetch_all_names,
#     # create_crazy,
#     )

# an HTTP-specific exception class  to generate exception information

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",
]

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/conversion")
async def get_conversion():
    response = await fetch_all_conversions()
    return response

@app.get("/api/conversion/{Address}", response_model=Todo)
async def get_conversion_by_title(Address):
    response = await fetch_one_conversion(Address)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {Address}")

# @app.post("/api/todo/", response_model=Todo)
# async def post_todo(todo: Todo):
#     response = await create_todo(todo.dict())
#     if response:
#         return response
#     raise HTTPException(400, "Something went wrong")

@app.post("/api/conversion/", response_model=price)
async def post_conversion(todo: Todo):
    print(todo)
    yo = todo.dict()
    print(yo)
    chain = yo["Chain"]
    address = yo["Address"]
    slug = yo["Coin"]
    print(chain)
    print(address)
    print(slug)
    if chain == "BTC":
        price = get_btc_price(address, slug)
        amount = get_btc_amount(address)
        ok = {
            'Price' : str(price),
            'Coin' : str(slug),
            'Amount' : str(amount)
        }
    elif chain == "ERC20":
        if slug == "Eth":
            price = get_eth_price(address, slug)
            amount = get_eth_amount(address, slug)
            ok = {
                'Price' : str(price),
                'Coin' : str(slug),
                'Amount' : str(amount)
            }
    elif chain == "Polkadot":
        if slug == "Polkadot":
            amount = get_polk_tokens(address)
            price = get_polk_price(address, slug)
            ok = {
                'Price' : str(price),
                'Coin' : str(slug),
                'Amount' : str(amount)
            }
        elif slug == "Moonbeam":
            amount = get_moonbeam_tokens(address)
            price = get_moonbeam_price(address)
            ok = {
                'Price' : str(price),
                'Coin' : str(slug),
                'Amount' : str(amount)
            }
    response = await create_conversion(ok)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/conversion/{title}/", response_model=Todo)
async def put_todo(title: str, addy: str):
    response = await update_conversion(title, addy)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.delete("/api/conversion/{title}")
async def delete_todo(title):
    response = await remove_conversion(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.post("/api/crazy/", response_model=crazy)
async def post_crazy(name: crazy):
    response = await create_conversion(name.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.get("/api/crazy")
async def get_crazy():
    response = await fetch_all_conversions()
    return response
print("")
# @app.post("/api/todo/", response_model=price)
# async def post_todo(todo: Todo):
#     response = todo.dict()
#     print(response)
#     chain = response["Chain"]
#     address = response["Address"]
#     slug = response["Coin"]
#     print(chain)
#     print(address)
#     print(slug)
#     if chain == "BTC":
#         price = get_btc_price(address, slug)
#         print(price)
#         return price
#     yes = await create_todo(price)
#     if yes:
#         return yes
#     raise HTTPException(400, "Something went wrong")