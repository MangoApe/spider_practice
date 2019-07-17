# -*- coding: utf-8 -*-
import scrapy


class BossspiderSpider(scrapy.Spider):
    name = 'bossspider'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280600/?query=python&ka=sel-city-101280600']

    def parse(self, response):

        #获取第一页职位列表
        job_list = response.xpath("//div[@class='job-list']/ul/li")
        print(job_list)
        print("职位数：")
        print (len(job_list))
        #遍历职位列表
        for job in job_list:
            item = {}
            #获取职位名称
            item['job_name'] = job.xpath(".//div[@class='job-title']/text()").extract_first()
            #获取职位url
            item['job_url'] = job.xpath(".//div[@class='info-primary']/h3/a/@href").extract_first()
            #获取区域
            item['job_area'] = job.xpath(".//div[@class='info-primary']/p/text()[1]").extract_first()
            #获取薪资待遇
            item['salary'] = job.xpath(".//div[@class='info-primary']/h3/a/span/text()").extract_first()
            #获取学历
            item['education'] = job.xpath(".//div[@class='info-primary']/p/text()[3]").extract_first()
            #获取工作经验
            item['year'] = job.xpath(".//div[@class='info-primary']/p/text()[2]").extract_first()
            print(type(item['job_url']))

    def parse_detail(self, response):
        pass



