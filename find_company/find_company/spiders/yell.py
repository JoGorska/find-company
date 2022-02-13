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
        all_containers = response.css('article').xpath('@role="listitem"').extract()
        items_list = []
        i = 0
        for i in range(0, len(all_containers)):
            company_name = response.css('h2.businessCapsule--name::text').extract()[i]
            company_website = response.xpath('//div/a[text()[contains(., "Website")]]/@href').extract()[i]
            item['company_name'] = company_name
            item['company_website'] = company_website
            items_list.append(item)
        for item in items_list:
            yield item

            # company_name = container.css('h2.businessCapsule--name::text').extract()
            # company_website = container.css('div').xpath('//div/a[text()[contains(., "Website")]]/@href').extract()
            # item['company_name'] = company_name
            # item['company_website'] = company_website
