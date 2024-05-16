import requests
from models import Item
from fastapi import FastAPI, HTTPException
import json
from typing import List

app = FastAPI()

with open ("store_items.json", "r") as f:
    item_data = json.load(f)

@app.get("/items", response_model=List[Item])
async def get_items() -> List[Item]:
    return item_data

@app.post("/items/new", response_model=List[Item])
async def new_item(item: Item) -> List[Item]:
    item_data.append(item.dict())
    return item_data

@app.put("/items/{item_id}", response_model=List[Item])
async def update_item(item_id: int, item: Item) -> List[Item]:
    for idx, existing_item in enumerate(item_data):
        if existing_item['id'] == item_id:
            item_data[idx] = item.dict()
            return item_data
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=List[Item])
async def delete_item(item_id: int) -> List[Item]:
    for idx, existing_item in enumerate(item_data):
        if existing_item['id'] == item_id:
            item_data.pop(idx)
            return item_data
    raise HTTPException(status_code=404, detail="Item not found")

