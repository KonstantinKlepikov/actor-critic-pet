from loguru import logger

from config import settings
from core.logging import setup_logging


def main() -> None:
    """Start service."""
    setup_logging(settings.log_level)
    while True:
        logger.info('Im start!')


if __name__ == '__main__':
    main()
