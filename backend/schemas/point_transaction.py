from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class TransactionType(Enum):
    redeemed = 0
    earned = 1

class PointTransactionBase(BaseModel):
    points: int
    type: TransactionType

class PointTransactionCreate(PointTransactionBase):
    user_id: int

class PointTransaction(PointTransactionBase):
    id: int
    user_id: int
    date: datetime

    class Config:
        from_attributes = True
