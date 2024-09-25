from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from models.material import Material
from schemas.material import MaterialCreate

def get_material_by_id(db: Session, id: int):
    return db.query(Material).filter(Material.id == id).first()
  
def create_material(db: Session, material: MaterialCreate):
    db_material = Material(name=material.name, points_per_kg=material.points_per_kg)
    db.add(db_material)
    try:
        db.commit()
        db.refresh(db_material)
    except IntegrityError as e:
        db.rollback()
        raise ValueError("Error creating material")
    return db_material
  
def get_material_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Material).offset(skip).limit(limit).all()
  
