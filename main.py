import logging
import other

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def init():
    logger.info('init')
    other.init_in_other()


def run():
    logger.info('run')
    other.run_in_other()


def teardown():
    logger.info('teardown')
    other.teardown_in_other()
