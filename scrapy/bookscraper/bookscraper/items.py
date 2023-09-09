# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(scrapy.Item):
    url = scrapy.Field()
    category = scrapy.Field()
    category_link = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    stars = scrapy.Field()
    img = scrapy.Field()
    description = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    excl_tax = scrapy.Field()
    incl_tax = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    reviews = scrapy.Field()
