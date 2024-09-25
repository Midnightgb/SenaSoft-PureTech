from pydantic import BaseModel
from datetime import datetime

class RecyclingBase(BaseModel):
    weight: float
    earned_points: int

class RecyclingCreate(RecyclingBase):
    user_id: int
    material_id: int
    recycling_point_id: int

class Recycling(RecyclingBase):
    id: int
    user_id: int
    material_id: int
    date: datetime
    recycling_point_id: int

    class Config:
        from_attributes = True
