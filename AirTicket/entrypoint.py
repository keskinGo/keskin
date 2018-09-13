"""
由于scrapy默认不能在IDE中调试，需要添加该文件
前两个参数不变，最后一个参数为自己spider文件的名字
"""

from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'ticket'])