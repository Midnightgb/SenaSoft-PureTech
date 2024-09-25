from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_class import Base

class Achievement(Base):
    __tablename__ = "achievements"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    required_points = Column(Integer, default=0)

    user_achievements = relationship("UserAchievement", back_populates="achievement")