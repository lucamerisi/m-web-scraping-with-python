import scrapy

class GoodReadsSpider(scrapy.Spider):
    #identity
    name = 'quotestoscrape'

    #requests
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            'http://quotes.toscrape.com/page/3/',
            'http://quotes.toscrape.com/page/4/',
            'http://quotes.toscrape.com/page/5/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #response
    def parse(self, response):
        page_number = response.url.split("/")[-2]
        _file = "{0}.html".format(page_number)
        with open(_file, 'wb') as f:
            f.write(response.body)