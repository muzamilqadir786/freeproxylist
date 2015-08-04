# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FreeproxylistItem(scrapy.Item):
    IPAddress = scrapy.Field()
    Port = scrapy.Field()
    Protocol = scrapy.Field()
    City = scrapy.Field()
    Uptime = scrapy.Field()
   
