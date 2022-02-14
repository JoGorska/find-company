# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FindCompanyItem(scrapy.Item):
    '''
    Item containing company details as found on Yell
    '''
    company_name = scrapy.Field()
    company_website = scrapy.Field()
    company_id = scrapy.Field()

class FindReviewItem(scrapy.Item):
    '''
    Item containing data collected 
    from page sumarising company rating
    '''

    company_name = scrapy.Field()
    review_summary = scrapy.Field()

    review_one_header = scrapy.Field()
    review_one_content = scrapy.Field()

    review_two_header = scrapy.Field()
    review_two_content = scrapy.Field()

    review_three_header = scrapy.Field()
    review_three_content = scrapy.Field()
