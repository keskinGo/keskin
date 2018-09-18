# -*- coding: utf-8 -*-

"""
spiders文件夹是编写爬虫的区域
此文件为爬虫方法模块
"""

# 引入文件
import scrapy
import re
import json

from urllib.parse import urlencode
from scrapy.http import Request  # 一个单独的request模块，需要跟进url的时候，需要使用

import AirTicket.controls as controls
import AirTicket.constant as constant

from AirTicket.items import AirticketItem  # 需要保存的字段类


# 自己编写的spider类
class Ticket(scrapy.Spider):
    # 用于区别Spider，在整个项目中是唯一，不可重复的
    name = "AirTicket"
    # 允许访问的域，不在该范围的会被忽略（不是必须的参数）
    # allowed_domains = ['qunar.com']

    # 爬取的地址
    # start_urls = [
    #     # "https://flight.qunar.com/site/interroundtrip_compare.htm?fromCity=%E6%88%90%E9%83%BD&toCity=%E7%BA%BD%E7%BA%A6&fromDate=2018-11-04&toDate=2018-11-10&fromCode=CTU&toCode=NYC&from=flight_int_search&lowestPrice=null&isInter=true&favoriteKey=&showTotalPr=null&adultNum=1&childNum=0&cabinClass=",
    #     "https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/settings.html"
    # ]

    # 拼接需要爬取的url
    def start_requests(self):
        # 请求地址的固定部分
        fixed_url = 'https://flights.ch.com/Flights/SearchByTime'
        # 搜索范围（0国内，1国际）
        find_scope = 0
        # 初始化对应厂商实例
        ticket_instance, source_name = controls.FactoryCallInterface(fixed_url, find_scope).create()
        source_code = constant.SOURCE_NAME_TO_CODE[source_name]
        # 获取筛选参数们
        search_infos = ticket_instance.get_search_args()
        # 根据筛选参数拼接url
        for search_info in search_infos:
            url = ticket_instance.get_url(**search_info)
            print('url:', url)
            yield scrapy.FormRequest(url=url,
                                     formdata=search_info,
                                     callback=self.parse,
                                     meta={'source_code': source_code})
            # yield Request(url, callback=self.parse)  # 回调函数，需要哪个方法来处理，则调用对应的方法

    # 爬取方法
    def parse(self, response):
        filename = 'test.html'
        with open(filename, 'w') as f:
            f.write(response.text)

        all_infos = json.loads(response.text)
        ticket_infos = all_infos['Route']
        item = AirticketItem()

        for ticket_info in ticket_infos:
            ticket_info = ticket_info[0]
            item['source_code'] = response.meta['source_code']  # 来源，详见SOURCE_NAME_TO_CODE
            item['search_time'] = constant.NOW_TIME  # 查询价格的时间（yyyy-mm-dd hh:mi:ss）
            item['departure_station'] = ticket_info['Departure']  # 始发站
            item['departure_terminal'] = ticket_info['DepartureStation']  # 始发航站楼
            item['departure_code'] = ticket_info['DepartureCode']  # 始发航站楼代码
            item['departure_time'] = ticket_info['DepartureTime']  # 当地出发时间
            item['arrival_station'] = ticket_info['Arrival']  # 终点站
            item['arrival_terminal'] = ticket_info['ArrivalStation']  # 终点航站楼
            item['arrival_code'] = ticket_info['ArrivalCode']  # 终点航站楼代码
            item['arrival_time'] = ticket_info['ArrivalTime']  # 当地到达时间
            item['flight_time'] = ticket_info['FlightTime']  # 飞行时间
            item['airplane_type'] = ticket_info['Type']  # 机型
            item['flight_number'] = ticket_info['No']  # 航班号
            item['transfer'] = constant.IS_NOT_TRANSFER  # 是否为中转地(1是、0否)
            item['price'] = ticket_info['MinCabinPrice']  # 票价
            item['airline'] = '春秋航空'  # 航空公司
            item['is_non_stop'] = constant.IS_NON_STOP  # 是否直飞，１是，０否
            item['total_time'] = ticket_info['FlightTime']  # 总耗时
            item['discount_rate'] = None  # 折扣率
            print('*********************************', item)
            yield item
