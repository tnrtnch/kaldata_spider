# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class KaldataItem(scrapy.Item):
    title = scrapy.Field()
    pubdate = scrapy.Field()
    author = scrapy.Field()
    body = scrapy.Field()
