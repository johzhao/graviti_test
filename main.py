import logging

logger = logging.getLogger(__name__)


def init():
    logger.info('init')


def run():
    logger.info('run')


def teardown():
    logger.info('teardown')
