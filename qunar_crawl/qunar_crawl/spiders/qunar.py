# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest
from scrapy.http import HtmlResponse
from w3lib.url import canonicalize_url
import re


class QunarSpider(CrawlSpider):
    name = 'qunar'
    allowed_domains = ['train.qunar.com']
    start_urls = ['https://train.qunar.com/stationToStation.htm?fromStation=上海&toStation=北京&date=2017-11-11&drainage=']

    rules = (
        Rule(LinkExtractor(allow=r'https://.*?drainage='),
             callback='parse_item',
             follow=True,
             process_request='splash_request',
             process_links='process_link'),
    )

    script = """
        function main(splash)
            assert(splash:go(splash.args.url))
            splash:wait(5)
            return splash:html()
        end
    """

    def start_requests(self):
        """处理起始url请求"""
        for url in self.start_urls:
            yield SplashRequest(url, args={'lua_source': self.script}, endpoint='execute',
                                callback=self.parse_item,
                                meta={'real_url': url}, dont_filter=True,
                                dont_process_response=True)

    def splash_request(self, request):
        """将请求方法改为splash的请求方式"""
        print('2'*10, request.meta.get('real_url'))
        return SplashRequest(url=request.url, args={'lua_source': self.script},
                             meta={'real_url': request.meta['real_url']},
                             dont_process_response=True)

    def process_link(self, links):
        """处理链接"""
        links = [x for x in links if self._link_allowed(x)]
        if self.canonicalize:
            for link in links:
                link.url = canonicalize_url(link.url)
                link.url = re.sub(r'amp;', '', link.url)
        links = self.link_extractor._process_links(links)
        return links

    def parse_item(self, response):
        # print('*'*10, response.meta.get('real_url'))
        # print(response.body_as_unicode())
        link_pattern = re.compile(r"https://.*?drainage=")
        print(link_pattern.findall(response.body.decode()))
        print(type(response))
