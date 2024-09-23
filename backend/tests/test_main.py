# backend/tests/test_main.py

import sys
import os

# Añadir el directorio raíz del backend al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from db.session import get_db
from models.user import Base
from config import settings

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
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login_user():
    # Primero registramos un usuario
    client.post(
        "/auth/register",
        json={"username": "loginuser", "email": "login@example.com", "password": "loginpassword"}
    )
    
    # Ahora intentamos iniciar sesión
    response = client.post(
        "/auth/login",
        data={"username": "loginuser", "password": "loginpassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_register_duplicate_username():
    # Registramos un usuario
    client.post(
        "/auth/register",
        json={"username": "duplicate", "email": "duplicate@example.com", "password": "password"}
    )
    
    # Intentamos registrar otro usuario con el mismo nombre de usuario
    response = client.post(
        "/auth/register",
        json={"username": "duplicate", "email": "another@example.com", "password": "password"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already registered"

def test_login_wrong_password():
    # Registramos un usuario
    client.post(
        "/auth/register",
        json={"username": "wrongpass", "email": "wrong@example.com", "password": "correctpass"}
    )
    
    # Intentamos iniciar sesión con una contraseña incorrecta
    response = client.post(
        "/auth/login",
        data={"username": "wrongpass", "password": "incorrectpass"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"

