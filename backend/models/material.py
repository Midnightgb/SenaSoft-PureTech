from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship
from models.base_class import Base

class Material(Base):
    __tablename__ = "material"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    points_per_kg = Column(Float)

    recycling = relationship("Recycling", back_populates="material")