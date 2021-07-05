import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def init_in_other():
    logger.info(f'init in other')


def run_in_other():
    logger.info(f'run in other')


def teardown_in_other():
    logger.info(f'teardown in other')
