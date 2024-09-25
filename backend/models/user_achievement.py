from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_class import Base
from models.achievement import Achievement


class UserAchievement(Base):
    __tablename__ = "user_achievements"
    
    user_id = Column(Integer, ForeignKey('users.id'))
    achievement_id = Column(Integer, ForeignKey('achievements.id'))
    id = Column(Integer, primary_key=True, index=True)
    date_obtained = Column(TIMESTAMP, default=datetime.now())
    
    user = relationship("User", back_populates="user_achievements")
    achievement = relationship("Achievement", back_populates="user_achievements")