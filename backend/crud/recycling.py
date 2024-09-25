from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from models.recycling import Recycling
from schemas.recycling import RecyclingCreate

def get_recycling_by_id(db: Session, id: int):
    return db.query(Recycling).filter(Recycling.id == id).first()
  
def create_recycling(db: Session, recycling: RecyclingCreate):
    db_recycling = Recycling(user_id=recycling.user_id, material_id=recycling.material_id, weight=recycling.weight, earned_points=recycling.earned_points, recycling_point_id=recycling.recycling_point_id)
    db.add(db_recycling)
    try:
        db.commit()
        db.refresh(db_recycling)
    except IntegrityError as e:
        db.rollback()
        raise ValueError("Error creating recycling")
    return db_recycling
  
def get_recycling_list(db: Session, skip: int = 0, limit: int = 10, user_id: int = None, material_id: int = None, recycling_point_id: int = None, since_date:datetime = None, until_date:datetime = None):
    query = db.query(Recycling)
    if user_id:
        query = query.filter(Recycling.user_id == user_id)
    if material_id:
        query = query.filter(Recycling.material_id == material_id)
    if recycling_point_id:
        query = query.filter(Recycling.recycling_point_id == recycling_point_id)
    if since_date:
        query = query.filter(Recycling.date >= since_date)
    if until_date:
        query = query.filter(Recycling.date <= until_date)
    return query.offset(skip).limit(limit).all()