from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings 

# This is for the database engine and session management. 
engine = create_async_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False , autoflush=False, bind=engine , class_=AsyncSession)

# Dependency 
async def get_db(): 
    async with SessionLocal() as session: 
        yield session 