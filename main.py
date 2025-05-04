from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


# J'ai initialiser uneliste pour stocker les items
items = []


# GET /items – liste tous les items
@app.get("/items", response_model=List[Item])
def get_items():
    return items


# GET /items/{id} – affiche un item
@app.get("/items/{id}", response_model=Item)
def get_item(id: int):
    for item in items:
        if item.id == id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# POST /items – crée un item
@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item


# PUT /items/{id} – modifie un item
@app.put("/items/{id}", response_model=Item)
def update_item(id: int, new_item: Item):
    for index, item in enumerate(items):
        if item.id == id:
            items[index] = new_item
            return new_item
    raise HTTPException(status_code=404, detail="Item not found")


# DELETE /items/{id} – supprime un item
@app.delete("/items/{id}")
def delete_item(id: int):
    for index, item in enumerate(items):
        if item.id == id:
            items.pop(index)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
