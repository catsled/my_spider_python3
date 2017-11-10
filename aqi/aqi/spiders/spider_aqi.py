# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import AqiItem


class SpiderAqiSpider(scrapy.Spider):
    name = 'spider_aqi'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/']

    def parse(self, response):
        city_list = response.xpath('//ul[@class="unstyled"]/div[2]/li/a')
        for city in city_list:
            # 处理每个城市的信息
            item = AqiItem()
            item['city'] = city.xpath('./text()').extract_first()
            item['time_stamp'] = time.time()
            link = response.urljoin(city.xpath('./@href').extract_first())
            print(item, link)
            yield scrapy.Request(link, self.parse_month, meta={'item':item})

    def parse_month(self, response):
        """处理每个月的信息"""
        month_link_url = response.xpath('//ul[@class="unstyled1"]/li/a/@href').extract()
        item = response.meta['item']
        for month_link in month_link_url:
            link = 'https://www.aqistudy.cn/historydata/' + month_link
            item['data_link'] = link
            yield scrapy.Request(link, self.parse_day, meta={'item':item})

    def parse_day(self, response):
        """处理每日的详细信息"""
        day_info_list = response.xpath('//tbody/tr')
        item = response.meta['item']
        for day_info in day_info_list[1:]:
            item['date'] = day_info.xpath('./td[1]/text()').extract_first()
            item['aqi'] = day_info.xpath('./td[2]/text()').extract_first()
            item['level'] = day_info.xpath('./td[3]/span/text()').extract_first()
            item['pm2_5'] = day_info.xpath('./td[4]/text()').extract_first()
            item['pm10'] = day_info.xpath('./td[5]/text()').extract_first()
            item['so2'] = day_info.xpath('./td[6]/text()').extract_first()
            item['co'] = day_info.xpath('./td[7]/text()').extract_first()
            item['no2'] = day_info.xpath('./td[8]/text()').extract_first()
            item['o3_8h'] = day_info.xpath('./td[9]/text()').extract_first()
            yield item