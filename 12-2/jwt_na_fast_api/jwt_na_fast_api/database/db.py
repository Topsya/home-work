from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  jwt_na_fast_api.database.models import Base
import psycopg2
from  jwt_na_fast_api.conf.config import  settings

 
def create_db():
    conn = psycopg2.connect(dbname=f"{settings.postgres_db}", user=f"{settings.POSTGRES_USER}", password=f"{settings.POSTGRES_PASSWORD}", host=f"{settings.POSTGRES_PORT}")
    cursor = conn.cursor()
    conn.autocommit = True
    # команда для создания базы данных rest_app
    sql = "CREATE DATABASE rest_app"
    cursor.execute(sql)
    print("База данных создана")
    
    cursor.close()
    conn.close()

SQLALCHEMY_DATABASE_URL =   settings.sqlalchemy_database_url  
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
   a=  input("Enter 1 for create database")
   if a == '1':
       create_db()
       
        