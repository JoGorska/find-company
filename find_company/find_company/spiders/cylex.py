import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


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
        company = Company()
        company['name'] = response.xpath('//meta[@property="og:title"/@content').get()
        company['url'] = response.url

        return company
