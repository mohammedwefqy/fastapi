from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from .config import settings
import time

GREEN = "\033[92m"
END = "\033[0m"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
while True:
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        with engine.connect():
            print(GREEN+'connected'+END)
            break  
    except OperationalError as e:
        print(f"OperationalError: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5) 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
