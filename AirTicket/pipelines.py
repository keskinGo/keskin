# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi

import pymysql
import codecs
import json

import AirTicket.settings as settings

"""
定义存储方式
"""


class AirticketPipeline(object):
    # def __init__(self):
    #     self.connect = pymysql.connect(
    #         host=settings.MYSQL_HOST,
    #         db=settings.MYSQL_DBNAME,
    #         user=settings.MYSQL_USER,
    #         passwd=settings.MYSQL_PASSWD,
    #         charset='utf8',
    #         use_unicode=True
    #     )
    #     self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        """
        每个item pipeline组件都需要调用该方法
        这个方法必须返回一个Item对象，或是抛出DropItem异常
        :param item: 被爬去的item
        :param spider: 爬取该item的spider
        :return:
        """
        return item

    # def open_spider(self):
    #     """
    #     在spider开启的时候自动被调用，在此可做一些初始化的操作
    #     :return:
    #     """
    #     pass
    #
    # def close_spider(self):
    #     """
    #     当spider被关闭时，这个方法被调用
    #     :return:
    #     """
    #     pass

    # @classmethod
    # def from_settings(cls, settings):
    #     dbparams = {
    #         'host': settings['MYSQL_HOST'],
    #         'db': settings['MYSQL_DBNAME'],
    #         'user': settings['MYSQL_USER'],
    #         'passwd': settings['MYSQL_PASSWD'],
    #         'charset': 'utf8',
    #         'cursorclass': Mysql
    #     }
