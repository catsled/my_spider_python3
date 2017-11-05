# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # 地区名称
    area = scrapy.Field()
    # 页面链接
    area_link = scrapy.Field()
    # 数据采集时间
    collected_date = scrapy.Field()
    # 时间
    date = scrapy.Field()
    # 最高气温
    highest_t = scrapy.Field()
    # 最低气温
    lowest_t = scrapy.Field()
    # 天气
    weather = scrapy.Field()
    # 风向
    wind_direction = scrapy.Field()
    # 风力
    wind_force = scrapy.Field()
