from sqlalchemy import Column, Integer, String, TIMESTAMP, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_class import Base
from enum import Enum as PyEnum
from models.redeem_history import RedeemHistory
from models.point_transaction import PointTransaction
from models.recycling import Recycling
from models.user_achievements import UserAchievement

class Rol(PyEnum):
    Admin = 1
    Employee = 2
    vulnerable = 3
    non_vulnerable = 4

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    rol = Column(Enum(Rol), nullable=False, default=Rol.non_vulnerable)
    eco_points = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    redeem_history = relationship("RedeemHistory", back_populates="user")
    point_transactions = relationship("PointTransaction", back_populates="user")
    recycling = relationship("Recycling", back_populates="user")
    user_achievements = relationship("UserAchievement", back_populates="user")
