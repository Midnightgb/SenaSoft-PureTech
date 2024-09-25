from pydantic import BaseModel
from datetime import datetime

class ReportBase(BaseModel):
    start_date: datetime
    end_date: datetime
    data: str

class ReportCreate(ReportBase):
    pass

class Report(ReportBase):
    id: int

    class Config:
        orm_mode = True
