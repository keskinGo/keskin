# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

"""
定义需要获取的字段
"""

import scrapy


class AirticketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source_code = scrapy.Field()  # 来源，详见SOURCE_NAME_TO_CODE
    search_time = scrapy.Field()  # 查询价格的时间（yyyy-mm-dd hh:mi:ss）
    departure_station = scrapy.Field()  # 始发站
    departure_terminal = scrapy.Field()  # 始发航站楼
    departure_code = scrapy.Field()  # 始发航站楼代码
    departure_time = scrapy.Field()  # 当地出发时间
    arrival_station = scrapy.Field()  # 终点站
    arrival_terminal = scrapy.Field()  # 终点航站楼
    arrival_code = scrapy.Field()  # 终点航站楼
    arrival_time = scrapy.Field()  # 当地到达时间
    flight_time = scrapy.Field()  # 飞行时间
    airplane_type = scrapy.Field()  # 机型
    flight_number = scrapy.Field()  # 航班号
    transfer = scrapy.Field()  # 是否为中转地(1是、0否)
    price = scrapy.Field()  # 票价
    airline = scrapy.Field()  # 航空公司
    is_non_stop = scrapy.Field()  # 是否直飞，１是，０否
    total_time = scrapy.Field()  # 总耗时
    discount_rate = scrapy.Field()  # 折扣率



