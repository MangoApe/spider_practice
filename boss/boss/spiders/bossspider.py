# -*- coding: utf-8 -*-
import scrapy


class BossspiderSpider(scrapy.Spider):
    name = 'bossspider'
    allowed_domains = ['xxx.cn']
    start_urls = ['http://xxx.cn/']

    def parse(self, response):
        pass
