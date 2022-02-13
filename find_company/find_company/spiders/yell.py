#pylint: disable=W0223
#pylint: disable=W0221
import scrapy


class YellSpider(scrapy.Spider):
    '''
    spider to obtain company names of yell
    '''
    name = 'yell'
    allowed_domains = ['yell.com']
    start_urls = ['https://www.yell.com/biz/automotive-solutions-corby-ltd-corby-9911336/']

    def parse(self, response):
        # using css selector
        # company_name = response.css('title::text').extract_first()
        # company_website = response.css('a.businessCard--callToAction').extract()

        # xpath selector
        company_name = response.xpath('//title/text()').extract_first()

        # xpath, but I don't like result 
        # https://www.automotivesolutionscorby.com/?utm_source=yell&utm_medium=referral&utm_campaign=yell'
        company_website = response.xpath('//a[@itemprop="url"]/@href').extract_first()
     
        # mix
        # company_website = response.css('nav a').xpath('@href').extract()
        # .xpath('//a[@class="businessCard--callToAction"]').extract()
      
        yield {
            'company_name': company_name,
            'company_website': company_website,
            }