# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
from pymongo import MongoClient

class ProxyPollPipeline(object):
    def __init__(self):
        self.client = MongoClient(settings['MONGO_HOST'],settings['MONGO_PORT'])
        self.db = self.client['proxies']
        self.col = self.db['proxy']

    def process_item(self, item, spider):
        dict_item = dict(item)
        self.col.insert(dict_item)
        return item

    def __del__(self):
        self.client.close()