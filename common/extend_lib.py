# -*- coding: utf-8 -*-
import os
import random
import re

import time


class VariableLib(object):
    def __init__(self):
       pass

    def dyelot_num(self):  # 根据日期和时间生成缸号
        t1 = time.strftime("%H", time.localtime(time.time()))
        if 0 <= int(t1) <= 8:
            letter = "C"
        if 9 <= int(t1) <= 13:
            letter = "A"
        if 14 <= int(t1) <= 23:
            letter = "B"
        t2 = time.strftime("%d%H%M", time.localtime(time.time()))
        # dyelot_nums 入库输入的缸号
        dyelot_nums = letter + t2
        self.dyelot_nums = dyelot_nums
        return self.dyelot_nums




