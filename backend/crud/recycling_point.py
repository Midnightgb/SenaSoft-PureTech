from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from models.recycling_point import RecyclingPoint
from schemas.recycling_point import RecyclingPointCreate
from sqlalchemy.sql import func


def register_recycling_point(db: Session, recycling_point: RecyclingPointCreate):
    db_recycling_point = RecyclingPoint(name=recycling_point.name, address=recycling_point.address, latitude=recycling_point.latitude, longitude=recycling_point.longitude)
    db.add(db_recycling_point)
    try:
        db.commit()
        db.refresh(db_recycling_point)
    except IntegrityError as e:
        db.rollback()
        raise ValueError("Error creating recycling point")
    return db_recycling_point

def get_recycling_point_by_id(db: Session, id: int):
    return db.query(RecyclingPoint).filter(RecyclingPoint.id == id).first()
  
def get_recycling_point_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RecyclingPoint).offset(skip).limit(limit).all()
  
def get_recycling_point_by_name(db: Session, name: str):
  return db.query(RecyclingPoint).filter(func.lower(RecyclingPoint.name).like(f"%{name.lower()}%")).first()
  