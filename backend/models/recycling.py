from sqlalchemy import Column, Integer, DateTime, TIMESTAMP, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_class import Base
from models.material import Material
from models.recycling_point import RecyclingPoint

class Recycling(Base):
    __tablename__ = "recycling"
  
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    material_id = Column(Integer, ForeignKey('material.id'))
    weight = Column(Float)
    earned_points = Column(Integer)
    recycling_point_id = Column(Integer, ForeignKey('recycling_point.id'))    
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="recycling")
    material = relationship("Material", back_populates="recycling")
    recycling_point = relationship("RecyclingPoint", back_populates="recycling")