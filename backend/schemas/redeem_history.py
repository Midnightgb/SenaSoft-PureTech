from pydantic import BaseModel
from datetime import datetime

class RedeemHistoryBase(BaseModel):
    user_id: int
    reward_id: int

class RedeemHistoryCreate(RedeemHistoryBase):
    pass

class RedeemHistory(RedeemHistoryBase):
    id: int
    date: datetime

    class Config:
        from_attributes = True
