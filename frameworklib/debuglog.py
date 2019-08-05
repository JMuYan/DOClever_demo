# -*- coding: utf-8 -*-
import logging
from frameworklib import datastore_log

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
DATE_FORMAT = '%Y/%m/%d/ %H:%M:%S %p'
logger_name = 'frmework_log'
logging.basicConfig(
    filename=datastore_log.GLOBAL_VAR_LOG_PATH + 'debuglog.log', level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
logger = logging.getLogger(logger_name)
