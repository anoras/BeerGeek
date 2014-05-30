# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BeerReviewPage(Item):
    url = Field()
    body = Field()
    depth = Field()
    filename = Field()
    link_text = Field()
    title = Field()