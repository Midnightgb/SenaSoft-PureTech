from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship
from models.base_class import Base

class RecyclingPoint(Base):
  __tablename__ = "recycling_points"
  
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  latitude = Column(Float)
  longitude = Column(Float)
  current_capacity = Column(Integer)
  max_capacity = Column(Integer)

  recycling = relationship("Recycling", back_populates="recycling_point") 
  