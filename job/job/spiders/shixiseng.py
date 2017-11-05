# -*- coding: utf-8 -*-
"""
    获取实习僧上的python招聘信息
    该网站上的数字会被转意,　所以需要转回来(&#x3180)
"""


import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ShiXiSeng
import html
import re


class ShixisengSpider(CrawlSpider):
    name = 'shixiseng'
    allowed_domains = ['www.shixiseng.com']
    start_urls = ['http://www.shixiseng.com/interns?k=Python']

    rules = (
        # 获取详情页面的url
        Rule(LinkExtractor(allow=r'/intern/\w+'), callback='parse_item', follow=True),
        # 下一页的url
        # Rule(LinkExtractor(allow=r'/interns\?k=Python&p=\d+'), follow=True),
    )


    position_pattern = re.compile(r'(?<=<p>岗位职责：</p>)(.*)(?=<p><br></p>)', re.S)
    requirement_pattern = re.compile(r'(?<=<p>任职要求：</p>)(.*?)(?=</div>)', re.S)
    # html.unescape

    def parse_item(self, response):
        with open('sxs.html', 'wb') as fout:
            fout.write(response.body)
        # try:
        #     item = ShiXiSeng()
        #     item['position'] = response.xpath('//div[@class="new_job_name"]/text()').extract_first()
        #     item['company_name'] = response.xpath('//div[@class="com-name"]/text()').extract_first()
        #     item['salary'] = (re.sub('／','/',response.xpath('//span[@class="job_money cutom_font"]/text()').extract_first()))
        #     item['base_info'] = re.sub('／', '/', ' '.join([i.strip() for i in (response.xpath('//div[@class="job_msg"]/span/text()').extract()[1:])]))
        #     item['job_detail'] = ''.join([i.strip() for i in (response.xpath('//div[@class="job_detail"]/p/text()').extract())])
        #     # item['duty'] = re.sub(r'<p>|</p>', '', self.position_pattern.search(response.text).group(1))
        #     # item['requirement'] = re.sub(r'<p>|</p>', '', self.requirement_pattern.search(response.text).group(1))
        #     yield item
        # except:
        #     pass
        # # return item
