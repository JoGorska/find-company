#pylint: disable=W0223
#pylint: disable=W0221
import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse
from ..items import FindCompanyItem


class YellSpider(scrapy.Spider):
    '''
    spider to obtain company names of yell
    '''
    name = 'yell'
    allowed_domains = ['yell.com']
    start_urls = ['https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1240993862&keywords=Garages&location=corby&pageNum=2']

    def parse(self, response):
        item = FindCompanyItem()
        article_id_list = response.xpath('//article[@role="listitem"]/@id').extract()

        for id in article_id_list:
            article_xpath = '//article[@id="'+ id +'"]'
            company_id =  id
            company_name = response.xpath(article_xpath).css('h2.businessCapsule--name::text').extract_first()
            company_website = response.xpath(article_xpath +'/div/div/div/div/a[text()[contains(., "Website")]]/@href').extract_first()

            item['company_name'] = company_name
            item['company_website'] = company_website
            item['company_id'] = company_id
            yield item

