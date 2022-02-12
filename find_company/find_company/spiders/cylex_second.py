#pylint: disable=W0223
import scrapy


class CylexSecondSpider(scrapy.Spider):
    '''
    spider to obtain company names of cylex
    '''
    name = 'cylex-second'
    allowed_domains = ['cylex-uk.co.uk']
    start_urls = ['https://bristol.cylex-uk.co.uk/company/thornhill-lock---safe-ltd-14678135.html']

    def parse(self, response):
        company_name = response.css('address').extract()
        yield {'company_name': company_name}
