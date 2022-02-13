#pylint: disable=W0223
#pylint: disable=W0221
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class YellSpider(CrawlSpider):
    '''
    spider to obtain company names of yell
    '''
    name = 'yell'
    allowed_domains = ['yell.com']

    start_urls = ['https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1240993862&keywords=Garages&location=corby']

    rules = [
        # Rule(LinkExtractor(allow=r'.yell.com/biz\/[a-zA-Z\-]+\/[a-zA-Z\-]+[0-9][0-9][0-9][0-9][0-9][0-9][0-9]+\/'), callback='parse_item', follow=True)
    
        Rule(LinkExtractor(allow=r'biz/((?!:).)*$'), callback='parse_item', follow=True)
    
    ]
    def parse(self, response):

        company_name = response.xpath('//h2/text()').extract()
        company_website = response.xpath('//a[@itemprop="url"]/@href').extract_first()
     
        yield {
            'company_name': company_name,
            'company_website': company_website,
            }