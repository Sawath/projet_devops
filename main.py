from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "API FastAPI ! Visitez /docs pour la documentation."
        }


class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


class User(BaseModel):
    id: int
    name: str
    email: str


# J'ai initialiser uneliste pour stocker les items
items = []


# J'ai initialiser une liste pour stocker les utilisateurs
users = []


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


# Nouveau ModelUtilisateur
# GET /users/ - Lister tous les utilisateurs
@app.get("/users/", response_model=List[User])
def read_users():
    return users


# GET /users/{user_id} - Lire un utilisateur par ID
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


# POST /users/ - Créer un nouvel utilisateur
@app.post("/users/", response_model=User)
def create_user(user: User):
    users.append(user)
    return user


# PUT /users/{user_id} - Mettre à jour un utilisateur
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")


# DELETE /users/{user_id} - Supprimer un utilisateur
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
