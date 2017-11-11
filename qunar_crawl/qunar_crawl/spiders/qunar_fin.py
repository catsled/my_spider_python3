# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from ..items import QunarCrawlItem
import re


class QunarFinSpider(scrapy.Spider):
    name = 'qunar_fin'
    allowed_domains = ['qunar.com']
    start_urls = ['https://train.qunar.com/stationToStation.htm?fromStation=%E4%B8%8A%E6%B5%B7&toStation=%E5%8C%97%E4%BA%AC&date=2017-11-11&drainage=']

    script = """
        function main(splash)
            assert(splash:go(splash.args.url))
            splash:wait(3)
            return splash:html()
        end
    """

    tackle_method = {
        1: 'self.get_train_code',
        2: 'self.get_start_end_station',
        3: 'self.get_start_end_time',
        4: 'self.get_duration',
        5: 'self.get_site_info',
        6: 'self.get_rest_tickets',
    }

    site_info = {
        1: ['sit_1', 'price_1', 'rest_ticket_1'],
        2: ['sit_2', 'price_2', 'rest_ticket_2'],
        3: ['sit_3', 'price_3', 'rest_ticket_3'],
        4: ['sit_4', 'price_4', 'rest_ticket_4'],
        5: ['sit_5', 'price_5', 'rest_ticket_5'],
    }

    link_pattern = re.compile(r'https://.*?drainage=')

    def start_requests(self):
        """处理处理url"""
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_link, endpoint='execute',
                                args={'lua_source':self.script})


    def parse_link(self, response):
        link_list = self.link_pattern.finditer(response.body.decode())
        for link in link_list:
            link = re.sub(r'amp;', '', link.group())
            yield SplashRequest(link, self.parse_content, args={'lua_source': self.script},
                                endpoint='execute')


    def parse_content(self, response):
        """获取内容"""
        info_list = response.xpath('//ul[@class="tbody"]/li')
        date = re.search(r'(?<=date=)((.*)?)&', response.url).group(2)
        for info in info_list:
            item = QunarCrawlItem()
            item['date'] = date
            self.assignment(info, item)
            yield item

    def assignment(self, info, item):
        """任务分派"""
        task_list = info.xpath('./div/div')
        for index, task in enumerate(task_list[:6], 1):
            # self.get_train_code()
            eval(self.tackle_method[index])(task, item)

    def get_train_code(self, task, item):
        """获取火车号"""
        item['code'] = task.xpath('./h3/text()').extract_first().strip()

    def get_start_end_station(self, task, item):
        """获取起始站"""
        item['start_station'] = task.xpath('./p[@class="start"]/span/text()').extract_first().strip()
        item['end_station'] = task.xpath('./p[@class="end"]/span/text()').extract_first().strip()

    def get_start_end_time(self, task, item):
        """获取出发时间和到达时间"""
        item['start_time'] = task.xpath('./time[@class="startime"]/text()').extract_first().strip()
        item['end_time'] = task.xpath('./time[@class="endtime daytime"]/text()').extract_first().strip()

    def get_duration(self, task, item):
        """获取所需时间"""
        item['duration'] = task.xpath(r'./time/text()').extract_first()

    def get_site_info(self, task, item):
        """获取座位信息"""
        sit_info_list = task.xpath('./p')
        for index, sit_info in enumerate(sit_info_list, 1):
            which_site = self.site_info[index]
            item[which_site[0]] = sit_info.xpath('./text()').extract_first().strip()
            item[which_site[1]] = '¥' + sit_info.xpath('./span/text()').extract_first()

    def get_rest_tickets(self, task, item):
        """获取剩余票数"""
        ticket_info_list = task.xpath('./p')
        for index, ticket_info in enumerate(ticket_info_list, 1):
            which_site = self.site_info[index]
            try:
                item[which_site[2]] = ticket_info.xpath('./text()').extract()[0]
            except:
                item[which_site[2]] = None