import hashlib
from BeerGeek.items import BeerReviewPage
import re
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule


class BeerGeekSpider(CrawlSpider):
    name = "BeerGeekSpider"
    with open('start-urls.txt', 'r') as f:
        start_urls = f.read().splitlines()

    allow_domains = map(lambda start_url: re.match(r'https?:\/\/([^\/]*)', start_url, re.I).group(1), start_urls)

    rules = [
        Rule(SgmlLinkExtractor(allow='\d{4}\/\d{2}(\/\d{2})?\/.+$'), follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        filename = hashlib.sha1(response.url.encode()).hexdigest()

        item = BeerReviewPage()
        item['url'] = response.url
        item['filename'] = filename
        item['depth'] = response.meta['depth']
        item['link_text'] = response.meta['link_text']
        print response.url
        return item