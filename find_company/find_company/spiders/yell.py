#pylint: disable=W0223
#pylint: disable=W0221
import scrapy


class YellSpider(scrapy.Spider):
    '''
    spider to obtain company names of yell
    '''
    name = 'cylex-second'
    allowed_domains = ['yell.com']
    start_urls = ['https://www.yell.com/biz/automotive-solutions-corby-ltd-corby-9911336/']

    def parse(self, response):
        company_name = response.css('title').extract()
        yield {'company_name': company_name}