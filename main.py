import logging
import sys

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def main():
    logger.info(f'execute task with args {sys.argv}')


if __name__ == '__main__':
    main()
