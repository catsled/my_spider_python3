# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings


class AqiPipeline(object):
    def __init__(self):
        self.client = MongoClient(settings['MONGO_HOST'], settings['MONGO_PORT'])
        self.db = self.client[settings['MONGO_DB']]
        self.col = self.db[settings['MONGO_COLLECTION']]

    def process_item(self, item, spider):
        dict_item = dict(item)
        self.col.insert(dict_item)
        return item

    def __del__(self):
        self.client.close()