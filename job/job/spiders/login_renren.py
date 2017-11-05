# -*- coding: utf-8 -*-
"""模拟登录人人网"""


import scrapy


class LoginRenrenSpider(scrapy.Spider):
    name = 'login_renren'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']


    # def start_requests(self):
    #     """重写父类的方法"""
    #     post_data = {
    #         "email": "17173805860",
    #         "password": "1qaz@WSX3edc"
    #     }
    #     for url in self.start_urls:
    #         yield scrapy.FormRequest(url=url, formdata=post_data)

    def parse(self, response):
        post_data = {
            "email": "17173805860",
            "password": "1qaz@WSX3edc"
        }
        yield scrapy.FormRequest.from_response(response, formid='loginForm', formdata=post_data, callback=self.parse_login)

    def parse_login(self, response):
        with open('renren.html', 'w') as fout:
            fout.write(response.text)
