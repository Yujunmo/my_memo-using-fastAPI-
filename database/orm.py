from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table,Column,Integer,String, ForeignKey
from database.connection import engine
from contextlib import asynccontextmanager
from fastapi import FastAPI

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(100),unique=True,index=True)
    email = Column(String(200))
    hashed_password = Column(String(512))


class Memo(Base):
    __tablename__ = 'memo'
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey('users.id'))
    title = Column(String(100))
    content = Column(String(1000))

@asynccontextmanager
async def app_lifespan(app : FastAPI):
    # when app starts
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    # when app ends
    pass

