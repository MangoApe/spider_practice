# -*- coding: utf-8 -*-
import scrapy
import json

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    start_urls = []
    for page in range(1, 194):
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1560423549414&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex=%s&pageSize=10&language=zh-cn&area=cn' % page
        start_urls.append(url)
    # start_urls = ['https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006&index=1']

    def parse(self, response):
        #提取数据，并返回
        # print(response.url)

        content = response.body.decode(encoding='utf-8')
        data = json.loads(content)
        job_list = data["Data"]["Posts"]
        print(job_list)
        # print(len(job_list))
        for job in job_list:
            item = {}
            item['title'] = job['RecruitPostName']
            item['location'] = job['LocationName']
            item['duty'] = job['Responsibility']
            item['detailURL'] = job['PostURL']
            # print(type(item))
            yield scrapy.Request(item['detailURL'],callback=self.parse_detail,meta={"item":item})
    def parse_detail(self, response):


