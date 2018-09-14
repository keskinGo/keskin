# -*- coding: utf-8 -*-

from urllib.parse import urlencode


class FactoryCallInterface:
    def __init__(self, fixed_url, find_scope):
        self.fixed_url = fixed_url  # 请求地址中的固定部分
        self.find_scope = find_scope  # 搜索范围（0国内，1国际）

    def create(self):
        """
        根据url初始化对应的对象
        :return:
        """
        # 春秋航空
        if self.fixed_url == 'https://flights.ch.com/':
            return ChunqiuTicketInfos(self.fixed_url, self.find_scope)


class TicketInfos:
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
        pass

    def get_abroad_url(self, **kwargs):
        """
        获取国际航线的url
        :param kwargs:
        :return:
        """
        pass

    def get_search_scope(self):
        """
        获取搜索参数
        :return:
        """
        return [{}]


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
        data = {}
        data['Departure'] = kwargs.get('Departure')  # 出发地
        data['Arrival'] = kwargs.get('Arrival')  # 目的地
        data['FDate'] = kwargs.get('FDate')  # 去程时间
        data['RetDate'] = kwargs.get('RetDate')  # 返程时间
        data['ANum'] = kwargs.get('ANum', 1)  # 成人数（12岁以上）
        data['CNum'] = kwargs.get('CNum', 0)  # 小孩数（2--12岁）
        data['INum'] = kwargs.get('INum', 0)  # 婴儿数（2岁以下）
        data['MType'] = kwargs.get('MType', 0)  #
        data['IfRet'] = kwargs.get('IfRet', 'true')  #
        data['SType'] = kwargs.get('SType', '01')  #
        data['isBg'] = kwargs.get('isBg', 'false')  #
        data['IsJC'] = kwargs.get('IsJC', 'false')  #
        data['IsNew'] = kwargs.get('IsNew', 1)  #

        url_head = self.get_url_head()
        url = url_head + urlencode(data)
        return url

    def get_url_head(self):
        departure_code = 'SHA'
        arrival_code = 'SZX'
        url_head = self.fixed_url + 'Round-%s-%s.html?' % (departure_code, arrival_code)
        return url_head

    def get_search_scope(self):
        """
        获取搜索范围：出发地，目的地，出发时间，返程时间
        :return:
        """
        result = []
        search_info = {}
        search_info['Departure'] = '上海'
        search_info['Arrival'] = '沈阳'
        search_info['FDate'] = '2018-10-01'
        search_info['RetDate'] = '2018-10-10'
        result.append(search_info)
        return result


class QunaTicketInfos(TicketInfos):
    def get_url(self):
        """
        去哪儿类
        :return:
        """
        data = {}
        data['fromCity'] = '成都'
        data['toCity'] = '南京'
        data['fromDate'] = '2018-11-04'
        data['toDate'] = '2018-11-10'
        data['fromCode'] = 'CTU'
        data['toCode'] = 'NYC'
        data['from'] = 'flight_dom_search'  # 猜测：flight_dom_search国内，flight_int_search国际
        data['lowestPrice'] = 'null'
        # data['isInter'] = 'true'
        # data['favoriteKey'] = ''
        # data['showTotalPr'] = 'null'
        # data['adultNum'] = '1'
        # data['childNum'] = '0'
        # data['cabinClass'] = ''
        url_head = "https://flight.qunar.com/site/roundtrip_list_new.htm?"  # interroundtrip_compare是什么鬼？
        url = url_head + urlencode(data)
        return url
