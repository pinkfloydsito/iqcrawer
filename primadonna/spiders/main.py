import scrapy


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['sigat.procesos-iq.com']
    start_urls = ['http://sigat.procesos-iq.com/']

    def parse(self, response):
        pass
