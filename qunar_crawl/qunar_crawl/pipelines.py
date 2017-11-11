# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class QunarCrawlPipeline(object):
    def __init__(self):
        self.files = open('qunar.json', 'w')

    def process_item(self, item, spider):
        dict_item = dict(item)
        if '99' not in dict_item['duration']:
            str_item = json.dumps(dict_item, ensure_ascii=False) + ',\n'
            self.files.write(str_item)
        return item

    def __del__(self):
        self.files.close()