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

        # print(f'ARTICLE ID {article_id_list}')
        items_list = []
        i = 0
        for id in article_id_list:
            article_xpath = '//article[@id="'+ id +'"]'
            company_id =  id
            company_name = response.xpath(article_xpath).css('h2.businessCapsule--name::text').extract_first()
            company_website = response.xpath(article_xpath +'/div/div/div/div/a[text()[contains(., "Website")]]/@href').extract_first()
            item['company_id'] = company_id
            item['company_name'] = company_name
            item['company_website'] = company_website
            # print(f'WHAT DO WE HAVE INSIDE ITEM {item}')
            yield item
        # print(f'ITEM LIST HERE {items_list}')
        # for item in items_list:
        #     yield item


    # def parse(self, response):
    #     item = FindCompanyItem()
    #     all_containers = response.css('article').xpath('@role="listitem"').extract()
    #     items_list = []
    #     i = 0
    #     for i in range(0, 2):
    #         company_name = response.css('h2.businessCapsule--name::text').extract()[i]
    #         company_website = (
    #             if (response.xpath('//div/a[text()[contains(., "Website")]]/@href').extract()[i]):
    #                 return response.xpath('//div/a[text()[contains(., "Website")]]/@href').extract()[i]
    #             else:
    #                 return response.css('h2.businessCapsule--name::text').extract()[i]
    #             )
    #         item['company_name'] = company_name
    #         item['company_website'] = company_website
    #         items_list.append(item)
    #     for item in items_list:
    #         yield item

            # company_name = container.css('h2.businessCapsule--name::text').extract()
            # company_website = container.css('div').xpath('//div/a[text()[contains(., "Website")]]/@href').extract()
            # item['company_name'] = company_name
            # item['company_website'] = company_website
