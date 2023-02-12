from fastapi import FastAPI
from src.gateway.http_api.api import api_router


def create_app() -> FastAPI:
    api = FastAPI()
    api.include_router(api_router)
    return api


app = create_app()
