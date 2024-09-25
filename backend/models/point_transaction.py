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
    type = Column(Enum(TransactionType), nullable=False)
    date = Column(TIMESTAMP, default=datetime.now())

    user = relationship("User", back_populates="point_transactions")