from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_class import Base




class Reward(Base):
    __tablename__ = "rewards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    cost_points = Column(Integer, default=0)
    
    redeem_history = relationship("RedeemHistory", back_populates="reward")