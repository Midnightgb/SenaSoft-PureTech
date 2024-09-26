from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from crud.user import create_user, get_user_by_email
from schemas.user import UserCreate, User
from core.security import verify_password, create_access_token, oauth2_scheme, logout
from db.session import get_db

router = APIRouter()

@router.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    try:
        return create_user(db=db, user=user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, email=form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email", headers={
                            "WWW-Authenticate": "Bearer"},)
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password", headers={
                            "WWW-Authenticate": "Bearer"},)
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token,
            "token_type": "bearer",
            "user_id": user.id,
            "user_type": user.type}

@router.get("/logout")
async def logout_user(token: str = Depends(oauth2_scheme)):
    logout(token)
    return {"status": True, "message": "Logout successful"}
