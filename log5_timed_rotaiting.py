import logging
from logging.handlers import TimedRotatingFileHandler

#basic without configuretions
logging.basicConfig(level=logging.INFO)

#evry midnight creat log 
handler = TimedRotatingFileHandler("timed_daily_log.log", when="midnight", interval=1, backupCount=7, encoding="utf-8") 

logger = logging.getLogger()

logger.addHandler(handler)

logger.info("Some text for recording")
logger.error("Eror message for check")