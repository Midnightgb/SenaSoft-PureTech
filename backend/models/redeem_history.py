from sqlalchemy import Column, Integer, TIMESTAMP, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_class import Base
from models.reward import Reward

class RedeemHistory(Base):
    __tablename__ = "redeem_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    reward_id = Column(Integer, ForeignKey('rewards.id'))
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    reward = relationship("Reward", back_populates="redeem_history")
    user = relationship("User", back_populates="redeem_history")