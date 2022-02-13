#pylint: disable=W0223
#pylint: disable=W0221
import scrapy
from scrapy.spiders import CrawlSpider, Rule, SitemapSpider
from scrapy.linkextractors import LinkExtractor


class YellSpider(SitemapSpider):
    '''
    spider to obtain company names of yell
    '''
    name = 'yell'
    allowed_domains = ['yell.com']
    sitemap_urls = ['https://www.yell.com/sitemaps.xml']
    # start_urls = ['https://www.yell.com/biz/automotive-solutions-corby-ltd-corby-9911336/']

    # rules = [
    #     Rule(LinkExtractor(allow=r'cylex-uk.co.uk/company\/[a-zA-Z\-]+\/[a-zA-Z\-]+[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]+.html'), callback='parse_item', follow=True)
    # ]
    def parse(self, response):

        company_name = response.xpath('//title/text()').extract_first()
        company_website = response.xpath('//a[@itemprop="url"]/@href').extract_first()
     
        yield {
            'company_name': company_name,
            'company_website': company_website,
            }