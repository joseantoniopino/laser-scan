from fastapi import APIRouter
from src.presentation.http_api.routers.v1 import lasers, targets

version = 'v1'
router = APIRouter(prefix=f'/{version}')

router.include_router(lasers.router, tags=[f'{version}.lasers'])
router.include_router(targets.router, tags=[f'{version}.targets'])
