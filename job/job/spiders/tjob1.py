# -*- coding: utf-8 -*-
"""
    获取腾讯招聘网页上的所有有关python的招聘信息, 同时获取每个招聘信息的详细信息
    1. 获取每个招聘信息的信息
    2. 进入对应连接获取相应的信息
    3. 进入下一页

    对应正则表达式
    1. 查找每一条招聘信息  r'<tr class="odd|even">.*?</tr>'
    2. 获取每条招聘信息的详细页面连接,职位, 职位类别, 招聘人数, 地点, 发布时间
      (1): r'<td class="l square"><a .*?href="(.*?)">(.*?)</a>'
      (2): r'<td>([\w-]+)</td>   产生一个列表(职位类别, 招聘人数, 地点, 发布时间)
    3. 详情页面
        (1) 获取工作职责和工作要求对应的html
        正则: r'.*?工作职责.*?<ul class="squareli">(.*?)</ul>'
             r'.*?工作要求.*?<ul class="squareli">(.*?)</ul>'
             职责, 要求: r'<li class>(.*?)</li>'
"""


from ..items import TjobItem
import scrapy
import re

class Tjob1Spider(scrapy.Spider):
    name = 'tjob1'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?keywords=python&lid=0&tid=0&start=0#a']

    w_info_pattern = re.compile(r'(<tr class="(odd|even)">.*?</tr>)', re.S)
    base_info_pattern = re.compile(r'<td class="l square"><a .*?href="(.*?)">(.*?)</a>', re.S)
    other_info_pattern = re.compile(r'<td>([\w-]+)</td>', re.S)

    duty_info_pattern = re.compile(r'工作职责.*?<ul class="squareli">(.*?)</ul>', re.S)
    requirement_info_pattern = re.compile(r'工作要求.*?<ul class="squareli">(.*?)</ul>', re.S)

    detail_pattern = re.compile(r'<li>(.*?)</li>', re.S)

    next_page_pattern = re.compile(r'41</a><a href="(.*?)" id="next">下一页</a>', re.S)

    def parse(self, response):
        page_source = response.text
        w_info_list = self.w_info_pattern.findall(page_source)
        for source in w_info_list:
            item = TjobItem()
            base_info = self.base_info_pattern.search(source[0])
            other_info_list = self.other_info_pattern.findall(source[0])
            link = 'http://hr.tencent.com/' + base_info.group(1)
            try:
                item['position'] = base_info.group(2)
                item['species'] = other_info_list[0]
                item['people_n'] = other_info_list[1]
                item['place'] = other_info_list[2]
                item['pub_date'] = other_info_list[3]
            except:
                pass
            yield scrapy.Request(url=link, callback=self.parse_detail, meta={"item":item})

        try:
            next_page = 'http://hr.tencent.com/' + response.xpath('//a[@id="next"]/@href').extract_first()
            print("#"*39, next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
        except:
            pass

    def parse_detail(self, response):
        """处理详细页面"""
        page_source = response.text
        item = response.meta['item']
        # 添加工作职责
        duty_info = self.duty_info_pattern.search(page_source).group(1)
        item['duty'] = ''.join(self.detail_pattern.findall(duty_info))
        # 添加工作要求
        requirement_info = self.requirement_info_pattern.search(page_source).group()
        item['requirement'] = ''.join(self.detail_pattern.findall(requirement_info))
        yield item
