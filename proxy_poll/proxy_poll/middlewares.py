# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ProxyPollSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxiesMillde(object):
    """代理下载中间件"""
    def process_request(self, request, spider):
        # request.meta['proxy'] = 'http://210.59.249.33:8080'
        request.meta['referer'] = 'http://www.kuaidaili.com/'
        # cookies = {
        #     'yd_cookie':'bb96b1fc-de86-439bce804bc7b2e86cc2c3dd3da5ab0ee2e8;',
        #     'channelid':'0;',
        #     '_ga':'GA1.2.1363947957.1510278366;',
        #     '_gid':'GA1.2.1993491041.1510278366;',
        #     'Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31':'1510278365,1510279226,1510279450;',
        # }
        # request.meta['cookie'] = cookies






