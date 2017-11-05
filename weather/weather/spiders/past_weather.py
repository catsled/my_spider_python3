# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import WeatherItem

class PastWeatherSpider(scrapy.Spider):
    name = 'past_weather'
    allowed_domains = ['tianqi.com']
    start_urls = ['http://lishi.tianqi.com']

    def parse(self, response):
        # 获取所有连接和对应的城市名称
        city_list = response.xpath('//ul[@class="bcity"]/li/a[@target="_blank"]')
        for city in city_list:
            # 获取城市名称与对应的链接
            item = WeatherItem()
            item['area'] = city.xpath('./text()').extract_first()
            item['area_link'] = city.xpath('./@href').extract_first()
            item['collected_date'] = time.time()
            yield scrapy.Request(item['area_link'], self.parse_area, meta={'item':item})

    def parse_area(self, response):
        """处理地区信息"""
        item = response.meta['item']
        date_list = response.xpath('//div[@class="tqtongji1"]/ul/li')
        for date in date_list:
            link = date.xpath('./a/@href').extract_first()
            yield scrapy.Request(link, self.parse_detail, meta={'item':item})

    def parse_detail(self, response):
        """处理详细信息"""
        item = response.meta['item']
        weather_info_list = response.xpath('//div[@class="tqtongji2"]/ul')[1:]
        for weather_info in weather_info_list:
            item['date'] = weather_info.xpath('./li[1]/a/text()|./li[1]/text()').extract_first()
            item['highest_t'] = weather_info.xpath('./li[2]/text()').extract_first()
            item['lowest_t'] = weather_info.xpath('./li[3]/text()').extract_first()
            item['weather'] = weather_info.xpath('./li[4]/text()|./li[4]/a/text()').extract_first()
            item['wind_direction'] = weather_info.xpath('./li[5]/text()|./li[5]/a/text()').extract_first()
            item['wind_force'] = weather_info.xpath('./li[6]/text()|./li[6]/a/text()').extract_first()
            print(item)
            # yield item


