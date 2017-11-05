# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    position = scrapy.Field()  # 职位
    area = scrapy.Field()  # 区
    company = scrapy.Field()  # 公司名称
    payment = scrapy.Field()  # 薪资
    requirement = scrapy.Field()  # 要求
    species = scrapy.Field()  # 种类
    detail_link = scrapy.Field()  # 详情链接

class TjobItem(scrapy.Item):
    """腾讯招聘信息"""
    position = scrapy.Field()  # 职位
    species = scrapy.Field()  # 类型
    people_n = scrapy.Field()  # 招聘人数
    place = scrapy.Field()  # 工作地点
    pub_date = scrapy.Field()  # 发布时间
    duty = scrapy.Field()  # 工作职责
    requirement = scrapy.Field()  # 岗位要求


class ShiXiSeng(scrapy.Item):
    """实习僧招聘信息"""
    position = scrapy.Field()  # 工作职位
    company_name = scrapy.Field()  # 公司名称
    salary = scrapy.Field()  # 工资
    base_info = scrapy.Field()  # 基础信息
    job_detail = scrapy.Field()  # 工作描述
    # duty = scrapy.Field()  #　责任
    # requirement = scrapy.Field()  # 要求