from fastapi import APIRouter
from src.gateway.http_api.routers.v1 import router as v1_router

api_router = APIRouter(prefix='/api')
api_router.include_router(v1_router)
