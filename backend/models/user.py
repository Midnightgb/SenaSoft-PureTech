from sqlalchemy import Column, Integer, String, TIMESTAMP, DateTime, Enum
from datetime import datetime
from models.base_class import Base
from enum import Enum as PyEnum

class Rol(PyEnum):
    Admin = "Administrador"
    Employee = "Employee"
    vulnerable = "vulnerable"
    non_vulnerable = "no_vulnerable"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    rol = Column(Enum(Rol), nullable=False, default=Rol.no_vulnerable)
    eco_points = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    


