from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text
from core.utils.logger import Logger

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def server_status(db):
    try:
        db.execute(text('SELECT 1'))
        Logger.success("Database server status: OK")
        return True
    except OperationalError:
        Logger.error("Database server status: ERROR")
        return False