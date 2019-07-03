# -*- coding: utf-8 -*-
import scrapy
import json
from copy import deepcopy
"""把deep copy补上， 要求不能修改meta参数字典中的key"""

class JdbookSpider(scrapy.Spider):
    name = 'jdbook'
    allowed_domains = ['list.jd.com', 'p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):

        #获取大分类
        for dt in response.xpath("//div[@class='mc']//dt"):
            #获取大分类名称：
            dt_name = dt.xpath('./a/text()').extract_first()
            #获取小分类名称：
            em_list = dt.xpath('./following-sibling::*[1]/em')
            for em in em_list:
                em_name = em.xpath("./a/text()").extract_first()
                #url/文本内容
                em_url = 'https:' + em.xpath("./a/@href").extract_first()
                #构造发送小分类列表页的请求--》 parse——list
                yield scrapy.Request(em_url, callback=self.parse_list, meta={
                    'dt_name': dt_name,
                    'em_name': em_name,
                    'em_url': em_url
                })


    def parse_list(self, response):
        li_list = response.xpath('//div[@id="plist"]//li')
        for li in li_list:
            name = li.xpath('.//div[@class="p-name"]/a/em/text()').extract_first().strip()
            skuid = li.xpath('./div[1]/@data-sku').extract_first()
            if skuid != None:
                price_url = 'https://p.3.cn/prices/mgets?&skuIds=J_' + skuid
                yield scrapy.Request(price_url, callback=self.parse_price, meta={
                    'name': name,
                    'dt_name': response.meta['dt_name'],
                    'em_name': response.meta['em_name'],
                    'em_url': response.meta['em_url']

                })
        #翻页: 获取下一页的url
        next_href = response.xpath("//a[@class='pn-next']/@href")
        if next_href != None:
            next_url = 'https://list.jd.com' + next_href
            yield scrapy.Request(next_url, callback=self.parse_list, meta={
                'dt_name': response.meta['dt_name'],
                'em_name': response.meta['em_name'],
                'em_url': response.meta['em_url']
            })


    def parse_price(self,response):
        print(response.body.decode())
        try:
            price = json.loads(response.body.decode())[0]['op']
        except:
            price = '获取失败，稍后单补'
        item = {}
        item['price'] = price
        item['name'] = response.meta['name']
        item['dt_name'] = response.meta['dt_name']
        item['em_name'] = response.meta['em_name']
        item['em_url'] = response.meta['em_url']

        yield item

