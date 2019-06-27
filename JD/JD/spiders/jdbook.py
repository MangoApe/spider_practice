# -*- coding: utf-8 -*-
import scrapy


class JdbookSpider(scrapy.Spider):
    name = 'jdbook'
    allowed_domains = ['xxx.cn']
    start_urls = ['http://xxx.cn/']

    def parse(self, response):
        pass
