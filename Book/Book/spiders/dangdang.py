# -*- coding: utf-8 -*-
import scrapy


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['xxx.cn']
    start_urls = ['http://xxx.cn/']

    def parse(self, response):
        pass
