from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.user import User
from schemas.user import UserCreate
from core.security import get_password_hash

def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password, name=user.name, type=user.type.name, eco_points=user.eco_points)
    db.add(db_user) 
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError as e:
        db.rollback()
        if "users_email_key" in str(e):
            raise ValueError("Email already registered")
        else:
            raise
    return db_user