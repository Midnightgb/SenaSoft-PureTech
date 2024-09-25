from sqlalchemy import Column, Integer, DateTime, TIMESTAMP, Float, String
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_class import Base

class Material(Base):
    __tablename__ = "material"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    points_per_kg = Column(Float)
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    
    recycling = relationship("Recycling", back_populates="material")