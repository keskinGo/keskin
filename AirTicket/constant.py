# -*- coding: utf-8 -*-

"""
常量定义
"""
import datetime

AIRPORT_CODE_MAP = {
    "上海": "SHA",
    "深圳": "SZX",
}

# 与格林威治时差
UTC_DIFF = 8

# 当前时间（字符串）
NOW_STR_TIME_SS = (datetime.datetime.utcnow() + datetime.timedelta(hours=UTC_DIFF)).strftime("%Y-%m-%d %H:%M:%S")
NOW_STR_TIME_MM = (datetime.datetime.utcnow() + datetime.timedelta(hours=UTC_DIFF)).strftime("%Y-%m-%d %H:%M:00")
NOW_STR_TIME_HH = (datetime.datetime.utcnow() + datetime.timedelta(hours=UTC_DIFF)).strftime("%Y-%m-%d %H:00:00")
NOW_STR_TIME_DD = (datetime.datetime.utcnow() + datetime.timedelta(hours=UTC_DIFF)).strftime("%Y-%m-%d")

NOW_DATE = datetime.datetime.utcnow() + datetime.timedelta(hours=UTC_DIFF)

# 信息来源映射关系（只能新增，不能更新）
SOURCE_NAME_TO_CODE = {
    '春秋': 1,
}

# 是否为中转站（1是 0否）
IS_TRANSFER = 1
IS_NOT_TRANSFER = 0

# 是否为直飞（1是 0否）
IS_NON_STOP = 1
IS_NOT_NON_STOP = 0

# 代理ip超时时间(秒)
TELNET_TIMEOUT = 3

# 可用代理ip
ALL_VALID_PROXY = [
    '183.164.238.128:40557',
    '127.0.0.1:33556',
]

# 代理ip文件地址
PROXY_PATH = './AirTicket/validProxy.py'

# 获取代理ip地址
GET_PROXY_URL = 'http://httpapi.datatocrm.com/index.php?token=suzhouqizx'
