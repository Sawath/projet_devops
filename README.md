# projet_devops

# API REST FastAPI pour la gestion d'items, et d'users

Ce projet est une API REST développée en Python avec FastAPI. Elle permet de gérer des items et inclut des fonctionnalités CRUD (Create, Read, Update, Delete), des tests unitaires, une analyse de la qualité du code, une pipeline CI/CD et un déploiement automatique.

## Fonctionnalités

L'API implémente les fonctionnalités suivantes :

* **Gestion des Items :**
    * Création, lecture, mise à jour et suppression d'items.
    * Chaque item possède les attributs : `id` (entier), `name` (chaîne), `price` (float), `in_stock` (booléen).
* **Endpoints :**
    * `GET /items` : Liste tous les items.
    * `GET /items/{id}` : Affiche un item spécifique.
    * `POST /items` : Crée un nouvel item.
    * `PUT /items/{id}` : Met à jour un item existant.
    * `DELETE /items/{id}` : Supprime un item.

* **Gestion des Users :**
    * Création, lecture, mise à jour et suppression d'utilisateurs.
    * Chaque users possède les attributs : `id` (entier), `name` (chaîne), `email` (str).
* **Endpoints :**
    * `GET /users` : Liste tous les utilisateurs.
    * `GET /users/{id}` : Affiche un utilisateur spécifique.
    * `POST /users` : Crée un nouvel item.
    * `PUT /users/{id}` : Met à jour un utilisateur existant.
    * `DELETE /users/{id}` : Supprime un utisateur.


* **Tests Unitaires :**
    * Tests écrits avec `pytest` pour assurer le bon fonctionnement de chaque endpoint.
* **Qualité du Code :**
    * Analyse de la qualité du code avec `flake8` pour respecter les conventions de style Python.
    * Je l'ai appliquer juste sur le fichier main.py et les dossiers /tests et /.github
* **CI/CD :**
    * Pipeline CI/CD mise en place avec GitHub Actions pour automatiser le linting, les tests et le déploiement.
* **Déploiement :**
    * Déploiement automatique de l'API sur Render.
* **Bonus (si implémentés) :**
    * Gestion des utilisateurs (modèle supplémentaire).
    * Vérification de sécurité avec Bandit.
      * Je l'ai ajouter au fichier requiments, ensuite dans la pipeline mais je n'arrivais pas à renforcer la sécurité
    * Documentation interactive avec Swagger.

## Structure du projet

Le projet est organisé de la manière suivante :
├── main.py           # Code source principal de l'API FastAPI
├── tests/            # Dossier contenant les tests unitaires
│   └── test_main.py  # Fichier des tests pytest
├── requirements.txt  # Liste des dépendances Python
└── .github/          # Configuration de GitHub Actions
    └── workflows/
        └── ci.yml    # Fichier de la pipeline CI/CD
└── README.md

1. Crée un environnement virtuel (recommandé) :

    ```bash
    python -m venv .venv
    venv\Scripts\activate   # Sur Windows
    ```

2. Installe les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

3.  Lance l'API :

    ```bash
    uvicorn main:app --reload
    ```

4.  Accède à la documentation Swagger :

    * Ouvre ton navigateur et va à l'URL `http://localhost:8000/docs`.

## Tests

Pour exécuter les tests unitaires :

```bash
pytest


## Linting
Pour analyser la qualité du code :

Bash

flake8 main.py tests/ .github/

CIC/D
La pipeline CI/CD est configurée avec GitHub Actions. Elle s'exécute automatiquement à chaque push sur la branche main et à chaque pull request. 

Déploiement
L'API est déployée automatiquement sur Render à partir de la branche main.

API en ligne : https://projet-devops-1.onrender.com/docs
