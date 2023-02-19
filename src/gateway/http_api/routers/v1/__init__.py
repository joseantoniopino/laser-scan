from fastapi import APIRouter
from src.gateway.http_api.routers.v1 import scan, targets, shot

version = 'v1'
router = APIRouter(prefix=f'/{version}')

router.include_router(scan.router, tags=[f'{version}.scan'])
router.include_router(targets.router, tags=[f'{version}.targets'])
router.include_router(shot.router, tags=[f'{version}.shot'])
