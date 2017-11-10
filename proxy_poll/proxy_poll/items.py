# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyPollItem(scrapy.Item):
    typed = scrapy.Field()  # 代理类型(http, https)
    ip = scrapy.Field()
    port = scrapy.Field()
