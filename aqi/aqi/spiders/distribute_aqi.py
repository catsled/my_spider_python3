# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class DistributeAqiSpider(CrawlSpider):
    name = 'distribute_aqi'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/']

    'month=201401'
    rules = (
        # 获取所有的城市
        Rule(LinkExtractor(allow=r'monthdata.php\?city=\w+'), follow=True),
        #　获取所有城市的月份
        Rule(LinkExtractor(allow=r'daydata.php\?city=\w+&month=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
