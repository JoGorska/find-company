#pylint: disable=W0223
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from find_company.items import Company


class CylexSpider(CrawlSpider):
    '''
    spider that finds companies' names on cylex pages
    '''
    name = 'cylex'
    allowed_domains = ['cylex-uk.co.uk']
    start_urls = ['https://www.cylex-uk.co.uk/']

    rules = [
        Rule(LinkExtractor(allow=r'cylex-uk.co.uk/company/((?!:).)*$'), callback='parse_item', follow=True)
    ]

    def parse_info(self, response):
        '''
        gets company name from the meta tag with property og:title
        '''
        company = Company()
        company['name'] = response.xpath('//meta[@property="og:title"/@content').get()

        return company
