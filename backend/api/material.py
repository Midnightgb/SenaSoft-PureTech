from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from crud.material import get_material_by_id, create_material, get_material_list
from schemas.material import MaterialCreate, Material
from db.session import get_db

router = APIRouter()

@router.post("/register", response_model=Material)
def register(material: MaterialCreate, db: Session = Depends(get_db)):
    try:
        return create_material(db=db, material=material)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
      
@router.get("/{id}", response_model=Material)
def get_material(id: int, db: Session = Depends(get_db)):
    db_material = get_material_by_id(db, id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material
  
@router.get("/", response_model=list[Material])
def get_material_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_material_list(db, skip, limit)
  