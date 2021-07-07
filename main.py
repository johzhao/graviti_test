import logging

from .other import init_in_other, run_in_other, teardown_in_other

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def init():
    logger.info('init')
    init_in_other()


def run(data: dict):
    logger.info(f'run with data {data}')
    run_in_other()


def teardown():
    logger.info('teardown')
    teardown_in_other()
