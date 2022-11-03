import os
from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_session
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("postgresql://admin:admin@host:5432/cessao_fundo")

engine = create_async_engine(DATABASE_URL)

Session: async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)


async def get_session() -> Generator:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()
