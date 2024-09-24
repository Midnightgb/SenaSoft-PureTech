from sqlalchemy import Column, Integer, String, TIMESTAMP, DateTime
from datetime import datetime
from models.base_class import Base



class Reward(Base):
    __tablename__ = "rewards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    cost_points = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    