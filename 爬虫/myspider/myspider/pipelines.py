# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient

class MyspiderWriteFilePipeline(object):
    # 写入文件
    def open_spider(self, spider):
        self.f = open('数据.json','w+', encoding='utf-8')#开启文件


    def close_spider(self,spider):
        self.f.close()#关闭文件

    def process_item(self, item, spider):
        self.f.write(json.dumps(item, ensure_ascii=False, indent=2) + ',\n')
        #一定要写return item
        return item


class MyspiderWriteMongoPipeline(object):
    #写入mongo数据库

    def open_spider(self,spider):
        self.col = MongoClient().itcast.teachers


    def process_item(self, item, spider):
        self.col.insert(item) #写入mongo后， item自动发生改变，多了_id字段
        del item['_id']
        return item
