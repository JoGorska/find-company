#pylint: disable=W0223
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from find_company.items import Company
import requests
from urllib.request import Request, urlopen


class CylexSpider(scrapy.Spider):
    '''
    spider that finds companies' names on cylex pages
    '''
    name = 'cylex'
    allowed_domains = ['cylex-uk.co.uk']
    start_urls = ['https://corby.cylex-uk.co.uk/company/alexs-15659626.html']
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36',
    #     'cookie': 'your cookie',
    # }

    # response = requests.get('https://corby.cylex-uk.co.uk/company/alexs-15659626.html', headers=headers)
    
    req = Request('https://corby.cylex-uk.co.uk/company/alexs-15659626.html', headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read()

    def parse_info(self, response):
        '''
        gets company name from the meta tag with property og:title
        '''
        company = Company()
        company['name'] = response.xpath('//meta[@property="og:title"/@content').get()
        company['url'] = response.url
        return company


# class CylexSpider(CrawlSpider):
#     '''
#     spider that finds companies' names on cylex pages
#     '''
#     name = 'cylex'
#     allowed_domains = ['cylex-uk.co.uk']
#     start_urls = ['https://belfast.cylex-uk.co.uk/company/sloan%27s-gym-26980970.html']

#     rules = [
#         Rule(LinkExtractor(allow=r'cylex-uk.co.uk/company/[a-zA-Z\-]+[0-9]+.html'), callback='parse_item', follow=True)
#     ]

#     def parse_info(self, response):
#         '''
#         gets company name from the meta tag with property og:title
#         '''
#         company = Company()
#         company['name'] = response.xpath('//meta[@property="og:title"/@content').get()

#         return company
