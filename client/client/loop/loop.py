from fastapi_utils.tasks import repeat_every
from loguru import logger

from client.controllers import disk_usage


def loop():
    logger.bind().debug("looping...")
    disk_usage.run()
