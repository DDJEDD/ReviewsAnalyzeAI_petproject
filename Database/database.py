from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import ASYNC_DATABASE_URL
engine = create_async_engine(
    ASYNC_DATABASE_URL,
    pool_pre_ping=True,
)
SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
        async with SessionLocal() as session:
            yield session
class Base(DeclarativeBase):
    pass