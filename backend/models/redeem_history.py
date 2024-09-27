from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_class import Base
from models.reward import Reward

class RedeemHistory(Base):
    __tablename__ = "redeem_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    reward_id = Column(Integer, ForeignKey('rewards.id'))
    date = Column(TIMESTAMP, default=datetime.now())

    reward = relationship("Reward", back_populates="redeem_history")
    user = relationship("User", back_populates="redeem_history")