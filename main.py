import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def init():
    logger.info('init')


def run():
    logger.info('run')


def teardown():
    logger.info('teardown')
