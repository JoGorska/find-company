import scrapy


class TrustpReviewSpider(scrapy.Spider):
    name = 'trustp_review'
    allowed_domains = ['trustpilot.com']
    start_urls = ['http://trustpilot.com/']

    def parse(self, response):
        pass
