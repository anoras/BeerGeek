import re
from scrapy.contrib.spiders import CrawlSpider

class BeerGeekSpider(CrawlSpider):
    name = "BeerGeekSpider"
    with open('start-urls.txt','r') as f:
        start_urls = f.read().splitlines()

    allow_domains = map(lambda start_url: re.match(r'https?:\/\/([^\/]*)', start_url, re.I).group(1), start_urls)

    def parse(self, response):
        print response.url
        pass