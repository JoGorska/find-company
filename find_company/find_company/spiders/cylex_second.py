#pylint: disable=W0223
#pylint: disable=W0221
import scrapy


class CylexSecondSpider(scrapy.Spider):
    '''
    spider to obtain company names of cylex
    '''
    name = 'cylex-second'
    allowed_domains = ['cylex-uk.co.uk']
    start_urls = ['https://birmingham.cylex-uk.co.uk/post%20office.html']

    def parse(self, response):
        company_name = response.css('address').extract()
        yield {'company_name': company_name}
