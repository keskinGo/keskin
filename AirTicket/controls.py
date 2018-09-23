# -*- coding: utf-8 -*-

from urllib.parse import urlencode

import datetime

import AirTicket.constant as constant


class FactoryCallInterface:
    """
    create()：根据url初始化对应的对象
    """

    def __init__(self, fixed_url, find_scope):
        self.fixed_url = fixed_url  # 请求地址中的固定部分
        self.find_scope = find_scope  # 搜索范围（0国内，1国际）

    def create(self):
        """
        根据url初始化对应的对象
        :return:
        """
        # 春秋航空
        if 'https://flights.ch.com/' in self.fixed_url:
            return ChunqiuTicketInfos(self.fixed_url, self.find_scope), '春秋'
        # 去哪儿
        elif 'https://flight.qunar.com' in self.fixed_url:
            return QunaTicketInfos(self.fixed_url, self.find_scope), '去哪儿'
        else:
            raise '没有收纳'


class TicketInfos:
    """
    get_url()：调用get_inland_url或get_abroad_url，返回完整的url（不用重写）
    get_url_head()：获取url中，参数之前的地址
    get_inland_url()：按照国内机票的规则，拼接出url
    get_abroad_url()：按照国际机票的规则，拼接出url
    get_search_args()：获取搜索参数（必须重写）
    """

    def __init__(self, fixed_url, find_scope):
        self.fixed_url = fixed_url
        self.find_scope = find_scope

    def get_url(self, **kwargs):
        """
        返回拼接出的完整url
        :return:
        """
        if self.find_scope == 0:
            return self.get_inland_url(**kwargs)
        elif self.find_scope == 1:
            return self.get_abroad_url(**kwargs)

    def get_url_head(self):
        """
        获取url参数以前的链接
        :return:
        """
        url_head = self.fixed_url
        return url_head

    def get_inland_url(self, **kwargs):
        """
        获取国内航线的url
        :param kwargs:
        :return:
        """
        url_head = self.get_url_head()
        url = url_head + urlencode(kwargs)
        return url

    def get_abroad_url(self, **kwargs):
        """
        获取国际航线的url
        :param kwargs:
        :return:
        """
        url_head = self.get_url_head()
        url = url_head + urlencode(kwargs)
        return url

    def get_search_args(self):
        """
        获取搜索参数
        :return:
        """
        result = []
        search_info = {}
        result.append(search_info)
        return result


class ChunqiuTicketInfos(TicketInfos):
    """
    拼接春秋航空url
    :return:
    """

    def get_inland_url(self, **kwargs):
        """
        获取国内机票的完整url
        :return:
        """
        url = self.fixed_url
        return url

    # def get_url_head(self):
    #     departure_code = constant.AIRPORT_CODE_MAP.get(self.departure)
    #     arrival_code = constant.AIRPORT_CODE_MAP.get(self.arrival)
    #     url_head = self.fixed_url + 'Round-%s-%s.html?' % (departure_code, arrival_code)
    #     url_head = self.fixed_url
    #     return url_head

    def get_search_args(self):
        """
        获取搜索参数：出发地，目的地，出发时间，返程时间， ……
        :return: [{参数字典1}, {参数字典2}, ]
        """
        result = []
        begin_date = constant.NOW_DATE

        for i in range(2):  # 查询今后90天的信息
            search_info = {}
            departure_date = (begin_date + datetime.timedelta(days=i + 1)).strftime("%Y-%m-%d")
            search_info['ActId'] = '0'
            # search_info['Active9s'] = None
            search_info['Arrival'] = '深圳'  # 目的地
            search_info['CabinActId'] = 'null'
            search_info['Currency'] = '0'
            search_info['Departure'] = '上海'  # 始发地
            search_info['DepartureDate'] = departure_date  # 出发时间
            search_info['IfRet'] = 'false'
            search_info['IsBg'] = 'false'
            search_info['IsEmployee'] = 'false'
            search_info['IsIJFlight'] = 'false'
            search_info['IsJC'] = 'false'
            search_info['IsLittleGroupFlight'] = 'false'
            search_info['IsShowTaxprice'] = 'false'
            search_info['ReturnDate'] = 'null'
            search_info['SType'] = '0'
            search_info['SeatsNum'] = '1'  # 座位数量
            search_info['isdisplayold'] = 'false'
            result.append(search_info)
        return result


class QunaTicketInfos(TicketInfos):
    def get_search_args(self):
        """
        获取搜索范围：出发地，目的地，出发时间，返程时间， ……
        :return: [{参数字典1}, {参数字典2}, ]
        """
        result = []
        search_info = {}
        search_info['departureCity'] = '成都'
        search_info['arrivalCity'] = '南京'
        search_info['departureDate'] = '2018-11-04'
        search_info['ex_track'] = None
        search_info['__m__'] = 'f5c3203e925a730f9e41fcea070ba44c'
        search_info['sort'] = None
        result.append(search_info)

        return result
