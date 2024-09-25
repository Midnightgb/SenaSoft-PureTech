from pydantic import BaseModel

class RewardBase(BaseModel):
    name: str
    description: str
    cost_points: int

class RewardCreate(RewardBase):
    pass

class Reward(RewardBase):
    id: int

    class Config:
        from_attributes = True
