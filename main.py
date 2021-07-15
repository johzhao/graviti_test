import logging
from typing import Callable

from .other import init_in_other, run_in_other, teardown_in_other

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def user_filter():
    pass


def init(params: dict) -> Callable:
    logger.info('init')
    init_in_other()
    return user_filter


def run(data: dict, filter_fun: Callable = None) -> bool:
    logger.info(f'run with data {data}')
    run_in_other()
    return True


def teardown():
    logger.info('teardown')
    teardown_in_other()
