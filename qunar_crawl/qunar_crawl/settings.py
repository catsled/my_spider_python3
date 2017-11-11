# -*- coding: utf-8 -*-

# Scrapy settings for qunar_crawl project

BOT_NAME = 'qunar_crawl'

SPIDER_MODULES = ['qunar_crawl.spiders']
NEWSPIDER_MODULE = 'qunar_crawl.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36Query String Parametersview sourceview URL encoded'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 2

DOWNLOADER_MIDDLEWARES = {
    # Engine side
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    # Downloader side
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

ITEM_PIPELINES = {
   'qunar_crawl.pipelines.QunarCrawlPipeline': 300,
}


SPLASH_URL = 'http://127.0.0.1:8050/'
# SPLASH_URL = 'http://192.168.59.103:8050/'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'