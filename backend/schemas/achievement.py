from pydantic import BaseModel

class AchievementBase(BaseModel):
    name: str
    description: str
    required_points: int

class AchievementCreate(AchievementBase):
    pass

class Achievement(AchievementBase):
    id: int

    class Config:
        from_attributes = True
