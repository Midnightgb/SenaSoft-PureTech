import sys
import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Añadir el directorio raíz del backend al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from db.session import get_db
from models.base_class import Base
from models.user import User, Rol
from models.material import Material
from models.recycling_point import RecyclingPoint
from models.recycling import Recycling

# Crear una base de datos en memoria para las pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}

def test_health_check():
    response = client.get("/health/health_check")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "Service is up and database is connected"}

def test_register_user():
    response = client.post(
        "/auth/register",
        json={"name": "testuser", "email": "test@example.com", "password": "testpassword", "type": Rol.vulnerable.value}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "testuser"
    assert data["email"] == "test@example.com"
    assert data["type"] == Rol.vulnerable.value
    assert "id" in data

def test_login_user():
    # Primero registramos un usuario
    client.post(
        "/auth/register",
        json={"name": "loginuser", "email": "login@example.com", "password": "loginpassword", "type": Rol.vulnerable.value}
    )
    
    # Ahora intentamos iniciar sesión
    response = client.post(
        "/auth/login",
        data={"username": "login@example.com", "password": "loginpassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_register_duplicate_email():
    # Registramos un usuario
    client.post(
        "/auth/register",
        json={"name": "duplicate", "email": "duplicate@example.com", "password": "password", "type": Rol.vulnerable.value}
    )
    
    # Intentamos registrar otro usuario con el mismo email
    response = client.post(
        "/auth/register",
        json={"name": "another", "email": "duplicate@example.com", "password": "password", "type": Rol.vulnerable.value}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_login_wrong_password():
    # Registramos un usuario
    client.post(
        "/auth/register",
        json={"name": "wrongpass", "email": "wrong@example.com", "password": "correctpass", "type": Rol.vulnerable.value}
    )
    
    # Intentamos iniciar sesión con una contraseña incorrecta
    response = client.post(
        "/auth/login",
        data={"username": "wrong@example.com", "password": "incorrectpass"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect password"

def test_register_material():
    response = client.post(
        "/materials/register",
        json={"name": "Plastic", "points_per_kg": 10}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Plastic"
    assert data["points_per_kg"] == 10
    assert "id" in data

def test_get_material():
    # Primero registramos un material
    material = client.post(
        "/materials/register",
        json={"name": "Glass", "points_per_kg": 15}
    ).json()
    
    # Ahora intentamos obtener el material
    response = client.get(f"/materials/{material['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Glass"
    assert data["points_per_kg"] == 15

def test_get_material_list():
    response = client.get("/materials/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_register_recycling_point():
    response = client.post(
        "/recycling_points/register",
        json={
            "name": "Central Recycling",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "current_capacity": 0,
            "max_capacity": 1000
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Central Recycling"
    assert "id" in data

def test_get_recycling_point():
    # Primero registramos un punto de reciclaje
    point = client.post(
        "/recycling_points/register",
        json={
            "name": "Downtown Recycling",
            "latitude": 34.0522,
            "longitude": -118.2437,
            "current_capacity": 0,
            "max_capacity": 500
        }
    ).json()
    
    # Ahora intentamos obtener el punto de reciclaje
    response = client.get(f"/recycling_points/{point['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Downtown Recycling"

def test_get_recycling_point_list():
    response = client.get("/recycling_points/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_register_recycling():
    # Primero necesitamos un usuario, un material y un punto de reciclaje
    user = client.post(
        "/auth/register",
        json={"name": "recycler", "email": "recycler@example.com", "password": "password", "type": Rol.vulnerable.value}
    ).json()
    
    material = client.post(
        "/materials/register",
        json={"name": "Paper", "points_per_kg": 5}
    ).json()
    
    point = client.post(
        "/recycling_points/register",
        json={
            "name": "Local Recycling",
            "latitude": 51.5074,
            "longitude": -0.1278,
            "current_capacity": 0,
            "max_capacity": 200
        }
    ).json()
    
    response = client.post(
        "/recycling/register",
        json={
            "user_id": user["id"],
            "material_id": material["id"],
            "weight": 10.5,
            "recycling_point_id": point["id"],
            "earned_points": 52
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["weight"] == 10.5
    assert data["earned_points"] == 52
    assert "id" in data

def test_get_recycling():
    # Primero registramos un reciclaje (usando el mismo proceso que en test_register_recycling)
    recycling = client.post(
        "/recycling/register",
        json={
            "user_id": 1,
            "material_id": 1,
            "weight": 10.5,
            "recycling_point_id": 1,
            "earned_points": 52
        }
    ).json()
    
    # Ahora intentamos obtener el reciclaje
    response = client.get(f"/recycling/{recycling['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["weight"] == 10.5
    assert data["earned_points"] == 52

def test_get_recycling_list():
    response = client.get("/recycling/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
