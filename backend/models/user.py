from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from models.base_class import Base
from enum import Enum as PyEnum
from models.redeem_history import RedeemHistory
from models.point_transaction import PointTransaction
from models.recycling import Recycling
from backend.models.user_achievement import UserAchievement

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
    type = Column(Enum(Rol), nullable=False, default=Rol.non_vulnerable)
    eco_points = Column(Integer, default=0)
    
    redeem_history = relationship("RedeemHistory", back_populates="user")
    point_transactions = relationship("PointTransaction", back_populates="user")
    recycling = relationship("Recycling", back_populates="user")
    user_achievements = relationship("UserAchievement", back_populates="user")
