from loguru import logger

from client.controllers import disk_space


async def loop():
    logger.bind().debug("looping...")
    await disk_space.run()
