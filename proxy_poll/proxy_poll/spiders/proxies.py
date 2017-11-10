# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ProxyPollItem


class ProxiesSpider(CrawlSpider):
    name = 'proxies'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free']

    rules = (
        Rule(LinkExtractor(allow=r'free/inha/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        info_list = response.xpath('//tbody/tr')
        for info in info_list:
            try:
                ip = info.xpath('./td[@data-title="IP"]/text()').extract_first()
                port = info.xpath('./td[@data-title="PORT"]/text()').extract_first()
                typed = info.xpath('./td[@data-title="类型"]/text()').extract_first()
            except:
                pass
            else:
                item = ProxyPollItem()
                item['ip'] = ip
                item['port'] = port
                item['typed'] = typed
                yield item