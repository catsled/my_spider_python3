# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import SplashTestSpiderItem
from scrapy_splash import SplashRequest



class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['train.qunar.com']
    start_urls = ['http://touch.train.qunar.com/trainList.html?startStation=%E5%8C%97%E4%BA%AC%E5%8D%97&endStation=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&date=2017-11-11']

    next_script = """
            function main(splash)
                splash:set_user_agent('Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1Query String Parametersview sourceview URL encoded')
                assert(splash:go(splash.args.url))
                splash:wait(3)
                --local element = splash:select("#btn-calendar-next")
                --element:mouse_click()
                --splash:wait(5)
                return { html = splash:html(), url = splash:url() }
            end
    """

    tackle_method = {
        1: 'self.get_time',
        2: 'self.get_stations',
        3: 'self.code_spend',
        4: 'self.site_money_numbers',
    }

    # data_pattern = re.compile(r'(?<=data-href=")(.*?)"', re.S)

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, args={'lua_source': self.next_script}, endpoint='execute', callback=self.parse)

    def parse(self, response):
        ticket_info_list = response.xpath('//ul[@id="m-lists"]/li')
        print(response.url)
        for ticket_info in ticket_info_list:
            item = SplashTestSpiderItem()
            ceil_info_list = ticket_info.xpath('./a/span')
            for index, span in enumerate(ceil_info_list, 1):
                eval(self.tackle_method.get(index))(span, item)
            print(item)
            yield item


    def get_time(self, span1, items):
        """处理并获取时间"""
        time_list = span1.xpath('./em/text()').extract()
        items['start_time'] = time_list[0]
        items['end_time'] = time_list[1]

    def get_stations(self, span2, items):
        """处理并获取车站信息"""
        stations_list = span2.xpath('./em/text()').extract()
        items['start_station'] = stations_list[0]
        items['end_station'] = stations_list[1]

    def code_spend(self, span3, items):
        """处理并获取车号和花费时间"""
        code_spend_list = span3.xpath('./em/text()').extract()
        items['code'] = code_spend_list[0]
        items['spend_time'] = code_spend_list[1]

    def site_money_numbers(self, span4, items):
        """处理并获取剩余票数以及价格"""
        # 处理已发车的情况
        try:
            assert(len(span4.xpath('./em')) > 0)
        except:
            items['lowest_price'] = None
            items['site_type'] = None
            items['rest'] = None
        else:
            site_money_numbers_list = span4.xpath('./em')
            items['lowest_price'] = site_money_numbers_list[0].xpath('./text()').extract_first()
            verbose = site_money_numbers_list[1]
            items['site_type'] = verbose.xpath('./text()').extract_first()
            items['rest'] = verbose.xpath('./i/text()').extract_first()
