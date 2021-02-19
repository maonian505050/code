import scrapy


class Hao123Spider(scrapy.Spider):
    name = 'hao123'
    # allowed_domains = ['hao123.com']
    # start_urls = ['http://www.hao123.com/']
    start_urls = ['http://quotes.toscrape.com/page/1/',
                  # 'http://quotes.toscrape.com/page/2/',
                  ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

