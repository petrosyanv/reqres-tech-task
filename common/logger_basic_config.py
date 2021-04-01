import sys
import time
from logging import StreamHandler, Formatter, INFO, getLogger


def get_configured_logger(logger_name):
    logger = getLogger(logger_name)
    logger.setLevel(INFO)
    stream_handler = StreamHandler(sys.stdout)

    formatter = Formatter(fmt='%(asctime)s : %(message)s', datefmt='%H:%M:%S')
    formatter.converter = time.gmtime
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
