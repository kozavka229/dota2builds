from loguru import logger

logger.add("log.log", rotation="1 MB")
