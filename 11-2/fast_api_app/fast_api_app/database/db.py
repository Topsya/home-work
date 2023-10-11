from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fast_api_app.database.models import Base
import psycopg2
 
def create_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="567234", host="localhost")
    cursor = conn.cursor()
    conn.autocommit = True
    # команда для создания базы данных rest_app
    sql = "CREATE DATABASE rest_app"
    cursor.execute(sql)
    print("База данных создана")
    
    cursor.close()
    conn.close()

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:567234@localhost:5432/rest_app"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Base.metadata.create_all(engine) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


        