from sqlalchemy import Column, Integer, String, TIMESTAMP, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_class import Base
from models.achievement import Achievement


class UserAchievement(Base):
    __tablename__ = "user_achievements"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    achievement_id = Column(Integer, ForeignKey('achievements.id'))
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    user = relationship("User", back_populates="user_achievements")
    achievement = relationship("Achievement", back_populates="user_achievements")