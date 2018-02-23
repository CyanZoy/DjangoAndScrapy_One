from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from JobSpider.recruit.recruit.spiders.test_spider import TestSpider

configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(TestSpider)
    reactor.stop()

crawl()
reactor.run()