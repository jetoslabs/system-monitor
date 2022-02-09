from fastapi import APIRouter

from client.api.api_v1.endpoints import hello, disk_space

router = APIRouter()
router.include_router(hello.router, prefix="/hello", tags=["hello"])
router.include_router(disk_space.router, prefix="/monitor", tags=["monitor"])
