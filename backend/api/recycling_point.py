from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from crud.recycling_point import get_recycling_point_by_id, register_recycling_point, get_recycling_point_list, get_recycling_point_by_name
from schemas.recycling_point import RecyclingPointCreate, RecyclingPoint
from db.session import get_db

router = APIRouter()

@router.post("/register", response_model=RecyclingPoint)
def register(recycling_point: RecyclingPointCreate, db: Session = Depends(get_db)):
    try:
        return register_recycling_point(db=db, recycling_point=recycling_point)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id}", response_model=RecyclingPoint)
def get_recycling_point(id: int, db: Session = Depends(get_db)):
    db_recycling_point = get_recycling_point_by_id(db, id)
    if db_recycling_point is None:
        raise HTTPException(status_code=404, detail="Recycling Point not found")
    return db_recycling_point
  
@router.get("/", response_model=list[RecyclingPoint])
def get_recycling_point_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_recycling_point_list(db, skip=skip, limit=limit)
  
@router.get("/search", response_model=RecyclingPoint)
def get_recycling_point_by_name(name: str, db: Session = Depends(get_db)):
    db_recycling_point = get_recycling_point_by_name(db, name)
    if db_recycling_point is None:
        raise HTTPException(status_code=404, detail="Recycling Point not found")
    return db_recycling_point
  
  
