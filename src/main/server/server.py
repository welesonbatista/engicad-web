from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core.database_connection_handler import engine
from src.core.metadata import Base
from src.main.routes.generate_part import generate_part
from src.main.routes.generate_bolt import generate_bolt

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(generate_part)
app.include_router(generate_bolt)
