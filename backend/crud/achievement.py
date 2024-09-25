from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.achievement import Achievement
from schemas.achievement import AchievementCreate

def get_achievement_by_id(db: Session, id: int):
    return db.query(Achievement).filter(Achievement.id == id).first()
  
def create_achievement(db: Session, achievement: AchievementCreate):
    db_achievement = Achievement(name=achievement.name, description=achievement.description, required_points=achievement.required_points)
    db.add(db_achievement)
    try:
        db.commit()
        db.refresh(db_achievement)
    except IntegrityError as e:
        db.rollback()
        raise ValueError("Error creating achievement")
    return db_achievement
  
def get_achievement_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Achievement).offset(skip).limit(limit).all()
  
