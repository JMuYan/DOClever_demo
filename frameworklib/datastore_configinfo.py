# -*- coding: utf-8 -*-
from frameworklib.commonlib import IniFile
GLOBAL_VAR_MIN_TIME=0.5
GLOBAL_VAR_MID_TIME=1
GLOBAL_VAR_MAX_TIME=2
GLOBAL_VAR_URL=IniFile.get_ini_value('base', 'url')  # 从配置文件读取数据
GLOBAL_VAR_BROWSER=IniFile.get_ini_value('base', 'browser')  # 从配置文件读取数据







