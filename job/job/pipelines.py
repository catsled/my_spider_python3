# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient
from scrapy.conf import settings


class JobPipeline(object):
    def open_spider(self, spider):
        self.fout = open('job1.json', 'w')

    def process_item(self, item, spider):
        dict_data = dict(item)
        data = json.dumps(dict_data, ensure_ascii=False) + ',\n'
        self.fout.write(data)
        return item

    def close_spider(self, spider):
        self.fout.close()

class ShixiShengPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = self.client[settings['MONGO_DB']]
        self.collection = self.db[settings['MONGO_COLLECTION']]

    def process_item(self, item, spider):
        dict_data = dict(item)
        self.collection.insert(dict_data)
        return item

    def close_spider(self, spider):
        self.client.close()