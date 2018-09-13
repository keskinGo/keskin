"""
spiders文件夹是编写爬虫的区域
此文件为爬虫方法模块
"""

# 引入文件
import scrapy
import re
from scrapy.http import Request  # 一个单独的request模块，需要跟进url的时候，需要使用
from AirTicket.items import AirticketItem  # 需要保存的字段类


# 自己编写的spider方法
class Ticket(scrapy.Spider):
    # 用于区别Spider，在整个项目中是唯一，不可重复的
    name = "AirTicket"
    # 允许访问的域，不在该范围的会被忽略（不是必须的参数）
    allowed_domains = ['qunar.com']
    # 爬取的地址
    start_urls = [
        "https://flight.qunar.com/site/interroundtrip_compare.htm?fromCity=%E6%88%90%E9%83%BD&toCity=%E7%BA%BD%E7%BA%A6&fromDate=2018-11-04&toDate=2018-11-10&fromCode=CTU&toCode=NYC&from=flight_int_search&lowestPrice=null&isInter=true&favoriteKey=&showTotalPr=null&adultNum=1&childNum=0&cabinClass=",
    ]
    # other
    # bash_url = 'http://www.23wx.com/class/'
    # bashurl = '.html'

    # # 拼接需要爬取的url
    # def start_requests(self):
    #     for i in range(1, 11):
    #         url = self.bash_url + str(i) + '_1' + self.bashurl
    #         yield Request(url, callback=self.parse)  # 回调函数，需要哪个方法来处理，则调用对应的方法

    # 爬取方法
    def parse(self, response):
        filename = 'test.txt'
        with open(filename, 'w') as f:
            f.write(response.text)