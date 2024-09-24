from sqlalchemy import Column, Integer, TIMESTAMP, DateTime, String
from datetime import datetime
from models.base_class import Base

class Achievement(Base):
    __tablename__ = "achievements"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    required_points = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)