#from typing import Annotated
#from fastapi import Depends, FastAPI, HTTPException, Query
#from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg
from psycopg.rows import dict_row, namedtuple_row
import time
from .config import settings

#+psycopg
SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#connection to db without sql alchemy
# while True:
#     try:
#         conn = psycopg.connect(host='localhost', dbname='mydb', user='myuser', password='mypassword', row_factory=dict_row)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Database connection failed")
#         print("Error: ", error)
#         time.sleep(5)