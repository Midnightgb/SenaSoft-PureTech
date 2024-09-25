from pydantic import BaseModel
from datetime import datetime

class UserAchievementBase(BaseModel):
    user_id: int
    achievement_id: int

class UserAchievementCreate(UserAchievementBase):
    pass

class UserAchievement(UserAchievementBase):
    id: int
    date_obtained: datetime

    class Config:
        orm_mode = True