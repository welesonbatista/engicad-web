from typing import Optional
from sqlalchemy.ext.asyncio import (create_async_engine, AsyncSession, async_sessionmaker)

CONNECTION_STRING = "postgresql+asyncpg://admin:admin@localhost:5432/engicad"

engine = create_async_engine(
    CONNECTION_STRING,
    echo=False,
    pool_size=2,
    max_overflow=0,
    pool_timeout=30
)

async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

class DBConnectionHandler:
    def __init__(self) -> None:
        self.session: Optional[AsyncSession] = None

    async def __aenter__(self):
        self.session = async_session()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()