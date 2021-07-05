import logging
import sys

import other

logger = logging.getLogger(__name__)


def main():
    logger.info(f'execute task with args {sys.argv}')
    other.some_func()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s (%(name)s) [%(levelname)s]: %(message)s')
    try:
        main()
    except Exception as e:
        logger.exception(f'exception:\n{e}')
    finally:
        logger.info('all finished.')
