#引入文件
import scrapy
import re
from scrapy.http import Request
from AirTicket.items import AirticketItem

class Ticket(scrapy.Spider):
    #用于区别Spider
    name = "AirTicket"
    #允许访问的域，不在该范围的会被忽略
    allowed_domains = ['qunar.com']
    #爬取的地址
    start_urls = [
        "https://flight.qunar.com/site/interroundtrip_compare.htm?fromCity=%E6%88%90%E9%83%BD&toCity=%E7%BA%BD%E7%BA%A6&fromDate=2018-08-04&toDate=2018-08-10&fromCode=CTU&toCode=NYC&from=flight_int_search&lowestPrice=null&isInter=true&favoriteKey=&showTotalPr=null&adultNum=1&childNum=0&cabinClass=",
    ]
    #爬取方法
    def parse(self, response):
        filename = 'test'
        with open(filename, 'wb') as f:
            f.write(response.body)