# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class BossFilePipeline(object):
    def open_spider(self, spider):  # 在爬虫开启的时候仅执行一次
        if spider.name == 'bossspider':
            self.f = open('Boss直聘.json', 'a', encoding='utf-8')

    def close_spider(self, spider):  # 在爬虫关闭的时候仅执行一次
        if spider.name == 'bossspider':
            self.f.close()

    def process_item(self, item, spider):
        if spider.name == 'bossspider':
            self.f.write(json.dumps(dict(item), ensure_ascii=False, indent=2) + ',\n')
        return item  #
