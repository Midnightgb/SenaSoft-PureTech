from sqlalchemy import Column, Integer, TIMESTAMP, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_class import Base
from enum import Enum as PyEnum

class TransactionType(PyEnum):
    redeemed = 0
    earned = 1

class PointTransaction(Base):
    __tablename__ = "point_transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    points = Column(Integer)
    typeTransaction = Column(Enum(TransactionType), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship("User", back_populates="point_transactions")