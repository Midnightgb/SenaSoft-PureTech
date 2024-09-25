from sqlalchemy import Column, Integer, DateTime, TIMESTAMP, Float, String
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_class import Base

class RecyclingPoint(Base):
  __tablename__ = "recycling_points"
  
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  latitude = Column(Float)
  longitude = Column(Float)
  current_capacity = Column(Integer)
  max_capacity = Column(Integer)
  created_at = Column(TIMESTAMP, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now)
  
  recycling = relationship("Recycling", back_populates="recycling_point") 
  