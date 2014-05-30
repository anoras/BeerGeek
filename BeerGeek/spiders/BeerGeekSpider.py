import hashlib
import urlparse
from BeerGeek.items import BeerReviewPage
import re
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from readability import Document


class BeerGeekSpider(CrawlSpider):
    name = "BeerGeekSpider"
    with open('start-urls.txt', 'r') as f:
        start_urls = f.read().splitlines()

    allowed_domains = map(lambda start_url: re.match(r'https?:\/\/([^\/]*)', start_url, re.I).group(1), start_urls)

    def remove_query_string(url):
        result = urlparse.urlparse(url)
        if result.path != '' and result.query != '':
            return url.rsplit('?')[0]
        else:
            return url

    rules = [
        Rule(SgmlLinkExtractor(
            process_value=remove_query_string,
            allow='\d{4}\/\d{2}(\/\d{2})?\/.+$'),
            follow=True,
            callback='parse_item'
        )
    ]

    def parse_item(self, response):
        filename = hashlib.sha1(response.url.encode()).hexdigest()
        readability_document = Document(response.body, url=response.url)
        item = BeerReviewPage()
        item['url'] = response.url
        item['filename'] = filename
        item['depth'] = response.meta['depth']
        item['link_text'] = response.meta['link_text']
        item['title'] = readability_document.short_title()
        with open('data/' + filename + '.html','wb') as html_file:
            html_file.write(readability_document.content())
        print '(' + filename + ') ' + item['title'] + " : " + item['url']
        return item