# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' #爬虫名
    allowed_domains = ['www.itcast.cn'] #允许爬虫爬去范围的域名，可以是多个
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] #起始域名

    def parse(self, response):
        li_list = response.xpath('//div[@class="tea_con"]//li')#返回类list类型， 由selector对象构成，每一个对象可以继续xpath，必须是html标签
        for li in li_list:
            item = {}
            item['name']= li.xpath(".//h3/text()").extract_first()
            # print(li)
            # print(name)
            item['level'] = li.xpath(".//h4/text()").extract()
            # print(level)


            yield item #让整个函数变成一个生成器， 只能yield： BaseItem， Requestrian，dict， None