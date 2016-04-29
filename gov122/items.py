# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Gov122Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    kcmc = scrapy.Field()
    kkrs = scrapy.Field()
    kscc = scrapy.Field()
    ksrq = scrapy.Field()
    kskm = scrapy.Field()
    kscx = scrapy.Field()

class ResultItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    kcmc = scrapy.Field()
    ksdd = scrapy.Field()
    kscx = scrapy.Field()
    kscc = scrapy.Field()
    kskm = scrapy.Field()
    ksrq = scrapy.Field()
    xh = scrapy.Field()
    ztStr = scrapy.Field()