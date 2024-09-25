from pydantic import BaseModel

class MaterialBase(BaseModel):
    name: str
    points_per_kg: float

class MaterialCreate(MaterialBase):
    pass

class Material(MaterialBase):
    id: int

    class Config:
        orm_mode = True
