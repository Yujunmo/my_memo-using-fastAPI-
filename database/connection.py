from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DATABASE_URL = "mysql+aiomysql://root:root@localhost:3306/basic"     #set your db 
engine = create_async_engine(DATABASE_URL, echo = True) #echo : Debugging
sessionFactory = sessionmaker(
    autoflush=False
    , autocommit=False
    ,bind=engine
    ,class_=AsyncSession)

async def get_db():
    async with sessionFactory() as session:
        yield session
        await session.commit()
