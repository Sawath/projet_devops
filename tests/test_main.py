
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

    # Vérifie que l'item a été bien supprimé
    response = client.get("/items/1")
    assert response.status_code == 404


# Test pour récupérer la liste des utilisateurs
def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test pour créer un utilisateur
def test_create_user():
    response = client.post(
        "/users/",
        json={"id": 1, "name": "Alice", "email": "alice@example.com"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }


# Test pour récupérer un utilisateur spécifique
def test_get_user():
    # On s'assure que l'utilisateur existe
    client.post(
        "/users/",
        json={"id": 2, "name": "Bob", "email": "bob@example.com"}
    )
    response = client.get("/users/2")
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "name": "Bob",
        "email": "bob@example.com"
    }


# Test pour mettre à jour un utilisateur
def test_update_user():
    response = client.put(
        "/users/2",
        json={"id": 2, "name": "Bob Updated", "email": "bob@example.com"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "name": "Bob Updated",
        "email": "bob@example.com"
    }


# Test pour supprimer un utilisateur
def test_delete_user():
    response = client.delete("/users/2")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted"}

    # Vérifie que l'utilisateur a bien été supprimé
    response = client.get("/users/2")
    assert response.status_code == 404
