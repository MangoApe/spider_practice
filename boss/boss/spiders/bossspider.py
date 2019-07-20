# -*- coding: utf-8 -*-
import scrapy
from time import sleep


class BossspiderSpider(scrapy.Spider):
    name = 'bossspider'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280600/?query=python&ka=sel-city-101280600']

    def parse(self, response):

        #获取第一页职位列表
        job_list = response.xpath("//div[@class='job-list']/ul/li")
        print("职位数：")
        print (len(job_list))
        #遍历职位列表
        for job in job_list:
            sleep(1)
            item = {}
            #获取职位名称
            item['job_name'] = job.xpath(".//div[@class='job-title']/text()").extract_first()
            #获取职位url
            item['job_url'] = "https://www.zhipin.com" + job.xpath(".//div[@class='info-primary']/h3/a/@href").extract_first()
            #获取区域
            item['job_area'] = job.xpath(".//div[@class='info-primary']/p/text()[1]").extract_first()
            #获取薪资待遇
            item['salary'] = job.xpath(".//div[@class='info-primary']/h3/a/span/text()").extract_first()
            #获取学历
            item['education'] = job.xpath(".//div[@class='info-primary']/p/text()[3]").extract_first()
            #获取工作经验
            item['year'] = job.xpath(".//div[@class='info-primary']/p/text()[2]").extract_first()
            #获取公司名字
            item['company'] = job.xpath(".//div[@class='company-text']/h3/a/text()").extract_first()
            # print(item)
            yield scrapy.Request(item['job_url'], callback=self.parse_detail, meta={
                'job_name': item['job_name'],
                'job_url': item['job_url'],
                'job_area': item['job_area'],
                'salary': item['salary'],
                'education': item['education'],
                'year': item['year'],
                'company': item['company']
            })


        #实现翻页

        next_href = response.xpath("//div[@class='page']/a[@class='next']/@href").extract_first()
        next_url = "https://www.zhipin.com" + next_href
        item['next_url'] = next_url
        print(item)
        if next_url is not None:

            yield scrapy.Request(next_url, callback=self.parse,meta={
                "item": item
            })

    def parse_detail(self, response):
        item = response.meta
        sleep(1)
        #css样式提取
        # detail = response.css('div.job-sec div.text ::text').extract()
        #xpath提取
        detail = response.xpath('//div[@class="job-sec"]/div[@class="text"]/text()').extract()
        details = ''.join(detail).replace(' ', '')
        item['description'] = details
        item['location'] = response.xpath("//div[@class='location-address']/text()").extract_first()
        yield item