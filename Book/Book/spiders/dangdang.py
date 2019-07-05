# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from copy import deepcopy

""" 一级分类名称， 二级分类名称，图书名称， 价格 """
class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://book.dangdang.com']
    redis_key = 'dangdang'
    #启动方式发生改变
        #在项目路径下正常启动爬虫， 让他进入等待就绪的状态
        #讓公用的redis中push起始url
            #lpush dangdang 'http://book.dangdang.com'

    def parse(self, response):
        with open('0.html', 'w')as f:
            f.write(response.body.decode('gbk'))
        #获取遍历一级分类列表
        # div_list = response.xpath("//div[@class='level_one']"
        div_list = response.xpath("//div[@class='sidemenu ']/div[3]/div")[:-4]
        for div in div_list:
            #一级分类名称
            one_name = ''
            for i in div.xpath('./dl/dt//text()').extract():
                one_name += i.strip()
            # print(one_name)
        #     print(div.xpath('./@class').extract_first())
        # print(len(div_list))
            #获取遍历二级分类
            dt_list = div.xpath('.//dl[@class="inner_dl"]/dt')
            # print(len(dt_list))
            for dt in dt_list:
            #二级分类的名称
                two_name = dt.xpath('./a/text()').extract_first()
                # print(two_name)
                #获取遍历三级分类
                a_list = dt.xpath("./following-sibling::*[1]/a")
                # print(a_list)
                for a in a_list:
                    # 三级分类的名称
                    three_name = a.xpath('.//text()').extract_first()
                    # 三级分类分类url
                    three_href = a.xpath('./@href').extract_first()
                #构造传递字典
                item = {
                    'one_name': one_name,
                    'two_name': two_name,
                    'three_name': three_name,
                }
                #构造三级分类列表页的请求 --> parse_list
                yield scrapy.Request(url=three_href, callback=self.parse_list, meta={
                   'item': deepcopy(item)
                })



    def parse_list(self,response):
        #先分组在提取
        li_list = response.xpath('//ul[@class="bigimg"]/li')
        print('当前页面共有{}本书'.format(len(li_list)))
        for li in li_list:
            #书名
            name = li.xpath('./p[1]/a/text()').extract_first()
            #价格
            price = li.xpath('./p[@class="price"]/span[1]/text()').extract_first()

        #返回数据

            item = response.meta['item']
            item['name'] = name
            item['price'] = price
            yield item
        #翻页

        next_href = response.xpath('//li[@class="next"]/a/@href').extract_first()

        if next_href != None:
            next_url = 'http://category.dangdang.com' + next_href
            yield scrapy.Request(next_url, callback=self.parse_list, meta={
                'item':response.meta['item']
            })



