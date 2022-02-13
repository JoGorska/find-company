# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FindCompanyItem(scrapy.Item):

    company_name = scrapy.Field()
    company_website = scrapy.Field()
    company_id = scrapy.Field()

