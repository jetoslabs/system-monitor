from loguru import logger

from client.controllers import disk_space


def loop():
    logger.bind().debug("looping...")
    disk_space.run()
