# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ResocodePipeline(object):
    def __init__(self):
        pass
    def process_item(self, item, spider):
        # item is a dict or item object
        # spider is a spider obj


        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(

        )

    def open_spider(self, spider):
        pass
    def close_spider(self, spider):
        pass
