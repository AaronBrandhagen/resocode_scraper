# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Field, Item

class ResocodeItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    region = Field()
    url = Field()
    html = Field()
    query = Field()
    crawled = Field()