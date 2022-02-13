#pylint: disable=W0223
#pylint: disable=W0221
import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse


class YellSpider(scrapy.Spider):
    '''
    spider to obtain company names of yell
    '''
    name = 'yell'
    allowed_domains = ['yell.com']
    start_urls = ['https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1240993862&keywords=Garages&location=corby&pageNum=2']

    def parse(self, response):
        company_name = response.css('h2.businessCapsule--name::text').extract()
        company_website = response.xpath('//div/a[text()[contains(., "Website")]]/@href').extract()
        
        yield {
            'company_name': company_name,
            'company_website': company_website,
            } 