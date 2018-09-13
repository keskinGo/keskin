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
    source = scrapy.Field()  # 来源（１去哪，２携程，３飞猪......）
    date = scrapy.Field()  # 日期
    starting_station = scrapy.Field()  # 始发站
    starting_terminal = scrapy.Field()  # 始发航站楼
    starting_time = scrapy.Field()  # 当地出发时间
    destination_station = scrapy.Field()  # 终点站
    destination_terminal = scrapy.Field()  # 终点航站楼
    destination_time = scrapy.Field()  # 当地到达时间
    transfer = scrapy.Field()  # 中转站：[{'中转地':['到达时间']}]???
    price = scrapy.Field()  # 票价
    airline = scrapy.Field()  # 航空公司
    is_non_stop = scrapy.Field()  # 是否直飞，１是，０否
    total_time = scrapy.Field()  # 总耗时
    discount_rate = scrapy.Field()  # 折扣率



