# -*- coding: utf-8 -*-

"""
常量定义
"""
import datetime

AIRPORT_CODE_MAP = {
    "上海": "SHA",
    "深圳": "SZX",
}

# 当前时间（'yyyy-mm-dd hh:mi:ss'）
NOW_TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 信息来源映射关系
SOURCE_NAME_TO_CODE = {
    '春秋': 1,
}

# 是否为中转站（1是 0否）
IS_TRANSFER = 1
IS_NOT_TRANSFER = 0

# 是否为直飞（1是 0否）
IS_NON_STOP = 1
IS_NOT_NON_STOP = 0