# -*- coding: utf-8 -*-
import scrapy
import base64
from scrapy_splash import SplashRequest



class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['train.qunar.com']
    start_urls = ['http://touch.train.qunar.com/trainList.html?startStation=%E5%8C%97%E4%BA%AC&endStation=%E4%B8%8A%E6%B5%B7&date=2017-11-10&searchType=stasta&bd_source=qunar&filterTrainType=&filterTrainType=&filterTrainType=']

    def start_requests(self):
        for url in self.start_urls:
            script = """
            function main(splash)
 	            splash:set_user_agent('Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1Query String Parametersview sourceview URL encoded')
	            assert(splash:go('http://touch.train.qunar.com/trainList.html?startStation=%E5%8C%97%E4%BA%AC&endStation=%E4%B8%8A%E6%B5%B7&date=2017-11-10&searchType=stasta&bd_source=qunar&filterTrainType=&filterTrainType=&filterTrainType='))
	            splash:wait(3)
	            return splash:html()
            end
            """
            splash_args = {
                'lua_source': script,
            }
            yield SplashRequest(url, args={'lua_source': script}, endpoint='execute', callback=self.parse)

    def parse(self, response):
        print(response.body_as_unicode())
        # print(response.request.headers)




