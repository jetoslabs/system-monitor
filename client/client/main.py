from time import sleep

import uvicorn
from fastapi import FastAPI
from loguru import logger

from client.api.v1 import api_v1
from client.core.log import setup_logger
from client.core.settings import settings


def create_app():
    fastapi = FastAPI()
    fastapi.include_router(router=api_v1.router, prefix=f"/{settings.API_V1_STR}")
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


# def main():
#     while True:
#         # stat = get_disk_usage("/")
#         # is_alert, alert_msg = alert_for_disk_usage(stat, free_bytes=20182291968)
#         # print(f"stat:{stat}, is_alert:{is_alert} {alert_msg}")
#         # print(ray.get(obj_ref))
#         # sleep(60 * .5)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT,
                reload=settings.APP_RELOAD, workers=settings.APP_WORKERS)
