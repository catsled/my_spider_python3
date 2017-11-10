# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AqiItem(scrapy.Item):
    # define the fields for your item here like:
    # 数据采集时间
    time_stamp = scrapy.Field()
    # 数据链接
    data_link = scrapy.Field()
    # 城市名称
    city = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # aqi
    aqi = scrapy.Field()
    # 质量等级
    level = scrapy.Field()
    # pm2.5
    pm2_5 = scrapy.Field()
    # pm10
    pm10 = scrapy.Field()
    # so2
    so2 = scrapy.Field()
    # co
    co = scrapy.Field()
    # no2
    no2 = scrapy.Field()
    # o3_8h
    o3_8h = scrapy.Field()
