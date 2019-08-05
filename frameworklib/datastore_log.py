# -*- coding: utf-8 -*-
import os
GLOBAL_VAR_CONFIG_FILE=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.ini')
GLOBAL_VAR_LOG_PATH=os.path.join(os.path.dirname(os.path.dirname(__file__)), '')
GLOBAL_VAR_REPORT_PATH=GLOBAL_VAR_LOG_PATH+'runner'
GLOBAL_VAR_REPORT_SCREENSHOTS_PATH=GLOBAL_VAR_REPORT_PATH+'/screenshots'
