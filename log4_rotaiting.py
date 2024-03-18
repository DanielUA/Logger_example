import logging
from logging.handlers import RotatingFileHandler

# basic without configuretions
logging.basicConfig(level=logging.INFO)

# 5gb - total value of 1 file, max count of files is 3, after recording
handler = RotatingFileHandler(
    "rotaiting_log.log", maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
)

logger = logging.getLogger()

logger.addHandler(handler)

logger.info("Some text for recording")
logger.error("Eror message for check")
