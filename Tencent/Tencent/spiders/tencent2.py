# -*- coding: utf-8 -*-
import scrapy
import json

class Tencent2Spider(scrapy.Spider):
    name = 'tencent2'
    allowed_domains = ['careers.tencent.com']
    start_urls = []
    for page in range(1, 193):
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1560423549414&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex=%s&pageSize=10&language=zh-cn&area=cn' % page
        start_urls.append(url)

    def parse(self, response):
        #提取数据，并返回
        # print(response.url)

        content = response.body.decode(encoding='utf-8')
        data = json.loads(content)
        job_list = data["Data"]["Posts"]
        # print(job_list)
        # print(len(job_list))
        for job in job_list:
            item = {}
            item['title'] = job['RecruitPostName']
            item['location'] = job['LocationName']
            item['duty'] = job['Responsibility']
            # print(type(item))
            yield item
        # #提取下一页的url，构造程request对象并返回
        # next_href = response.
        # print(div_list)
