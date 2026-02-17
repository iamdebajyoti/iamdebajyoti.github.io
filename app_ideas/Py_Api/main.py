from subprocess import BELOW_NORMAL_PRIORITY_CLASS
from types import ClassMethodDescriptorType
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from pprint import pprint
import json

app = FastAPI()

# Define a pydantic model for data validation (e.g., for POST requests)


class Item(BaseModel):
    name: str
    model: Optional[str] = None
    description: str | None = None
    price: float
    tax: float | None = None

All_Items = []

# Get endpoints

@app.get("/allitems/")
async def see_all_items():
    print(All_Items)
    return All_Items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # return {"Showing Data Fields of :": item_id,  "~~~": json.dumps(All_Items[item_id], indent=4)}
    return {"Showing Data Fields of :": item_id,  "~~~": f"All_Items[item_id]"}

# Post endpoint
@app.post("/items/")
async def create_item(item: Item):
    All_Items.append(item)
    return {"The items details are - ": item}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the first API!"}










"""
How to run and test the api urls locally:

python -m fastapi dev main.py
python -m fastapi run main.py

Go to the bash shell prompt and enter like below-

curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Laptop",
    "description": "Powerful computing device",
    "price": 1200.00,
    "tax": 96.00
}' http://127.0.0.1:8000/items/

curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Desktop1",
    "description": "Powerful computing device",
    "price": 2900.00,
    "tax": 41.00
}' http://127.0.0.1:8000/items/

curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Laptop3",
    "description": "Powerful computing device",
    "price": 2400.00,
    "tax": 91.00
}' http://127.0.0.1:8000/items/

curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Laptop2",
    "description": "Powerful computing device",
    "price": 1400.00,
    "tax": 91.00
}' http://127.0.0.1:8000/items/

curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Desktop2",
    "description": "Powerful computing device",
    "price": 4900.00,
    "tax": 51.00
}' http://127.0.0.1:8000/items/


To view all the items ---

curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8000/allitems/ | python -m json.tool


"""



