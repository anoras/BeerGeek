# Scrapy settings for BeerGeek project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'BeerGeek'

SPIDER_MODULES = ['BeerGeek.spiders']
NEWSPIDER_MODULE = 'BeerGeek.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BeerGeek (+http://www.yourdomain.com)'

SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': 200,
    'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': 150
}

DEPTH_STATS_VERBOSE = True
CONCURRENT_REQUESTS = 100
DOWNLOAD_TIMEOUT = 15
LOG_LEVEL = 'INFO'
RETRY_ENABLED = False
DEPTH_LIMIT = 20