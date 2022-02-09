from fastapi import APIRouter

from client.api.v1 import hello

router = APIRouter()
router.include_router(hello.router, prefix="/hello", tags=["hello"])
