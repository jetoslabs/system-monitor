import uvicorn
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from loguru import logger

from client.api.api_v1 import api
from client.core.log import setup_logger
from client.core.settings import settings
from client.loop.loop import loop


def create_app():
    fastapi = FastAPI()
    fastapi.include_router(router=api.router, prefix=f"/{settings.API_V1_STR}")
    return fastapi


app = create_app()


@app.on_event("startup")
async def startup_event():
    logger.bind().info("startup event ...")
    # setup logger before everything
    setup_logger()


@app.on_event("shutdown")
async def shutdown_event():
    logger.bind().info("shutdown event ...")


@app.on_event("startup")
@repeat_every(seconds=10, logger=logger)  # 1 min
def infinite_loop():
    loop()


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT,
                reload=settings.APP_RELOAD, workers=settings.APP_WORKERS)
