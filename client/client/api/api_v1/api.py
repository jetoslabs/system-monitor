from fastapi import APIRouter

from client.api.api_v1.endpoints import twitter, disk_space

router = APIRouter()
router.include_router(disk_space.router, prefix="/diskspace", tags=["diskspace"])
router.include_router(twitter.router, prefix="/twitter", tags=["twitter"])

