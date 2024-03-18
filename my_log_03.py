from my_logger import logger

def buz(num: int):
    logger.info(f"Start function buz")
    foo_ = 100
    result = foo_ + num
    logger.debug(f"result: {result}")
    return result

def foo():
    logger.error("AAAAA!!")


if __name__== "__main__":
    buz(10)
    foo()