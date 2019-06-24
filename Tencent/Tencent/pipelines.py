# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    def process_item(self, item, spider):

        with open('tencent_job.txt','a', encoding='utf-8')as f:
            f.write(json.dumps(item, ensure_ascii=False) + "\r\n")
            # f.write(item)
        # fp = open('tencent_job.txt', 'a', encoding='utf-8')
        # json.dump(dict(item), fp, ensure_ascii=False)
        return item
