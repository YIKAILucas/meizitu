# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeiziItem(scrapy.Item):
    category = scrapy.Field()
    # sort_1_url = scrapy.Field()
    species = scrapy.Field()
    name = scrapy.Field()
    # page_url = scrapy.Field()
    order = scrapy.Field()
    origin_url = scrapy.Field()
