# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()  # 作者姓名
    title = scrapy.Field()  # 文章题目
    article_species = scrapy.Field()  # 文章分类
    visited_nums = scrapy.Field()  # 浏览数量
    like_nums = scrapy.Field()  # 点赞数量
