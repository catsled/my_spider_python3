# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SplashTestSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()  # 日期
    weekend = scrapy.Field()  # 周几
    start_station = scrapy.Field()  # 出发站
    end_station = scrapy.Field()  # 到达站
    start_time = scrapy.Field()  # 发车时间
    end_time = scrapy.Field()  # 到达时间
    code = scrapy.Field()  # 车编号
    spend_time = scrapy.Field()  # 所需时间
    lowest_price = scrapy.Field()  # 最低票价
    site_type = scrapy.Field()  # 座位类型
    rest = scrapy.Field()  # 剩余票数
