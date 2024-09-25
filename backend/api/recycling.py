from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from crud.recycling import create_recycling, get_recycling_by_id, get_recycling_list
from schemas.recycling import RecyclingCreate, Recycling
from db.session import get_db

router = APIRouter()

@router.post("/register", response_model=Recycling)
def register(recycling: RecyclingCreate, db: Session = Depends(get_db)):
    try:
        return create_recycling(db=db, recycling=recycling)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id}", response_model=Recycling)
def get_recycling(id: int, db: Session = Depends(get_db)):
    db_recycling = get_recycling_by_id(db, id)
    if db_recycling is None:
        raise HTTPException(status_code=404, detail="Recycling not found")
    return db_recycling
  
@router.get("/", response_model=list[Recycling])
def get_recycling_list_db(skip: int = 0, limit: int = 10, user_id: int = None, material_id: int = None, recycling_point_id: int = None, since_date:datetime = None, until_date:datetime = None, db: Session = Depends(get_db)):
    return get_recycling_list(db, skip=skip, limit=limit, user_id=user_id, material_id=material_id, recycling_point_id=recycling_point_id, since_date=since_date, until_date=until_date)
  
