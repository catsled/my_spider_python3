# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QunarCrawlItem(scrapy.Item):
    date = scrapy.Field()  # 日期
    weekend = scrapy.Field()  # 周几
    start_station = scrapy.Field()  # 出发站
    end_station = scrapy.Field()  # 到达站
    start_time = scrapy.Field()  # 发车时间
    end_time = scrapy.Field()  # 到达时间
    code = scrapy.Field()  # 车编号
    duration = scrapy.Field()  # 所需时间

    sit_1 = scrapy.Field()  # 座位类型１
    price_1 = scrapy.Field()  # 价格1
    rest_ticket_1 = scrapy.Field()  # 剩余票数1

    sit_2 = scrapy.Field()  # 座位类型2
    price_2 = scrapy.Field()  # 价格2
    rest_ticket_2 = scrapy.Field()  # 剩余票数2

    sit_3 = scrapy.Field()  # 座位类型3
    price_3 = scrapy.Field()  # 价格3
    rest_ticket_3 = scrapy.Field()  # 剩余票数3

    sit_4 = scrapy.Field()  # 座位类型4
    price_4 = scrapy.Field()  # 价格4
    rest_ticket_4 = scrapy.Field()  # 剩余票数4

    sit_5 = scrapy.Field()  # 座位类型5
    price_5 = scrapy.Field()  # 价格5
    rest_ticket_5 = scrapy.Field()  # 剩余票数5
