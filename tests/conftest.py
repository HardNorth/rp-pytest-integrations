

import logging
import pytest
from reportportal_client import RPLogger

# Uncomment the following lines to get full HTTP logging in console
# from http.client import HTTPConnection
# HTTPConnection.debuglevel = 1


@pytest.fixture(scope='session')
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger
