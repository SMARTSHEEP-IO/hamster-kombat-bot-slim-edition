import sys
from loguru import logger

logger.remove()

logger.add(
    sink=sys.stdout,
    format=(
        "<white>{time:YYYY-MM-DD HH:mm:ss}</white> | "
        "<level>{level: <8}</level> | "
        "<cyan><b>{module}:{line}</b></cyan> - "
        "<white><b>{message}</b></white>"
    ),
    colorize=True,
)

logger.add(
    sink="app.log",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level: <8} | "
        "{module}:{line} - {message}"
    ),
    rotation="1 week",
    retention="1 month",
    compression="zip",
)

logger = logger.opt(colors=True)


# if __name__ == "__main__":
#     logger.debug("Debug message")
#     logger.info("Info message")
#     logger.success("Success message")
#     logger.warning("Warning message")
#     logger.error("Error message")
#     logger.critical("Critical message")
