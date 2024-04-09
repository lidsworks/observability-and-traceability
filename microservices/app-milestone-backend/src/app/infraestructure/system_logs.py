import logging
import os
import sys


class Logs:
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    log_level = logging.getLevelName(log_level)
    logging.basicConfig(level=log_level, stream=sys.stdout)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stderr))
    logging.getLogger('sqlalchemy.engine').setLevel(log_level)
