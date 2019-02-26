# -*- coding: utf-8 -*-

import telnetlib

import random
import requests
import re

import AirTicket.constant as constant


def get_all_valid_proxy():
    """
    在配置文件中读取所有的可用代理
    :return: 代理列表
    """
    with open(constant.PROXY_PATH, 'r') as f:
        proxy = f.read()
        now_proxy = re.findall('(ALL_VALID_PROXY[\s\S]*?\])', proxy)[0]
        exec(now_proxy, globals())
        return ALL_VALID_PROXY


def update_invalid_proxy(old_proxy):
    """
    替换无效的代理
    :param old_proxy:
    :return:
    """
    old_proxy = re.sub('http://', '', old_proxy)
    new_proxy = get_a_new_valid_proxy()
    msg = ''
    with open(constant.PROXY_PATH, 'r+') as f:
        for line in f.readlines():
            line_new = line.replace(old_proxy, new_proxy)
            msg += line_new
    with open(constant.PROXY_PATH, 'w') as f:
        f.writelines(msg)


def create_valid_proxy():
    """
    全量更新代理ip信息，保证有10个以上可用代理
    :return:
    """
    now_proxy = get_all_valid_proxy()
    all_valid_proxy = []
    # 检验当前已存在的代理
    for proxy in now_proxy:
        if check_proxy_isvalid(proxy):
            all_valid_proxy.append(proxy)
    # 新增代理
    while len(all_valid_proxy) < 10:
        new_proxy_text = requests.get(constant.GET_PROXY_URL).text
        new_proxy_list = re.findall('(\d.*?)\s', new_proxy_text)
        for proxy in new_proxy_list:
            if check_proxy_isvalid(proxy):
                all_valid_proxy.append(proxy)
    with open(constant.PROXY_PATH, 'w') as f:
        msg = 'ALL_VALID_PROXY = ' + str(all_valid_proxy)
        msg = re.sub('\[', '[\n    ', msg)
        msg = re.sub(',', ',\n   ', msg)
        msg = re.sub('\]', ',\n]', msg)
        f.writelines(msg)


def check_proxy_isvalid(proxy):
    """
    判断代理是否可用
    :param proxy: 格式实例--127.0.0.1:8000
    :return:
    """
    host, port = re.findall('([\d\.]*?):(\d*)', proxy)[0]
    try:
        telnet = telnetlib.Telnet(host, port, constant.TELNET_TIMEOUT)
    except:
        return False
    else:
        telnet.close()
        return True


def get_a_new_valid_proxy():
    """
    获取一个全新可用的代理
    :return:
    """
    while 1:
        new_proxy_text = requests.get(constant.GET_PROXY_URL).text
        new_proxy_list = re.findall('(\d.*?)\s', new_proxy_text)
        for proxy in new_proxy_list:
            if check_proxy_isvalid(proxy):
                return proxy


def get_a_valid_proxy():
    """
    从现有列表中获取一个代理
    :return:
    """
    all_proxy = get_all_valid_proxy()
    proxy = 'http://' + random.choice(all_proxy)
    return proxy
