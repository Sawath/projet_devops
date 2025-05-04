import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app



client = TestClient(app)


# Test pour recuperer la liste des items
def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test pour recuperer un item spécifique
def test_get_item():
    client.post(
        "/items/",
        json={"id": 1, "name": "Item1", "price": 10.0, "in_stock": True}
    )
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Item1",
        "price": 10.0,
        "in_stock": True,
    }


# Test pour creer un item
def test_create_item():
    response = client.post(
        "/items/",
        json={"id": 2, "name": "Item2", "price": 20.0, "in_stock": False}
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "name": "Item2",
        "price": 20.0,
        "in_stock": False,
    }


# Test pour modifier les items
def test_update_item():
    response = client.put(
        "/items/1",
        json={"id": 1, "name": "Item_update", "price": 15.0, "in_stock": True},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Item_update",
        "price": 15.0,
        "in_stock": True,
    }


# Test pour supprimer un item
def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}
    # Verifie que l'Item a été bien supprimer
    response = client.get("/items/1")
    assert response.status_code == 404
