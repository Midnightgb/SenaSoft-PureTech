from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime
from models.base_class import Base

class Report(Base):
  __tablename__ = "reports"
  
  id = Column(Integer, primary_key=True, index=True)
  start_date = Column(DateTime, default=datetime.now())
  end_date = Column(DateTime, default=datetime.now())
  data = Column(String)
