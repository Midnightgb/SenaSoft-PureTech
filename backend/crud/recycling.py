from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from models.recycling import Recycling
from schemas.recycling import RecyclingCreate
from crud.user import get_user_by_id
from crud.material import get_material_by_id
from crud.recycling_point import get_recycling_point_by_id

def get_recycling_by_id(db: Session, id: int):
    return db.query(Recycling).filter(Recycling.id == id).first()

def create_recycling(db: Session, recycling: RecyclingCreate):
    user = get_user_by_id(db, recycling.user_id)
    if user is None:
        raise ValueError("User not found")
    material = get_material_by_id(db, recycling.material_id)
    if material is None:
        raise ValueError("Material not found")
    recycling_point = get_recycling_point_by_id(db, recycling.recycling_point_id)
    if recycling_point is None:
        raise ValueError("Recycling point not found")
    
    db_recycling = Recycling(user_id=recycling.user_id, material_id=recycling.material_id, weight=recycling.weight, earned_points=recycling.earned_points, recycling_point_id=recycling.recycling_point_id)
    print("adding points to user")
    print(f"User points: {user.eco_points}")
    user.eco_points += recycling.earned_points
    print(f"User points after adding: {user.eco_points}")
    #update user points
    db.add(user)
    db.add(db_recycling)
    try:
        db.commit()
        db.refresh(user)
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