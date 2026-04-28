from fastapi import FastAPI
from src.main.routes.generate_part import router


app = FastAPI()

app.include_router(router)