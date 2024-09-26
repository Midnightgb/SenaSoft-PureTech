from sqlalchemy.orm import Session
from models.user import User

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
