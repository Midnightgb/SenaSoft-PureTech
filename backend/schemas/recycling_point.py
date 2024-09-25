from pydantic import BaseModel

class RecyclingPointBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    current_capacity: int
    max_capacity: int

class RecyclingPointCreate(RecyclingPointBase):
    pass

class RecyclingPoint(RecyclingPointBase):
    id: int

    class Config:
        orm_mode = True
