def start_one():
    from scrapy.crawler import CrawlerProcess, CrawlerRunner
    from scrapy.utils.project import get_project_settings
    process = CrawlerProcess(get_project_settings())
    process.crawl('test_spider')
    process.start()


def start_two():
    from twisted.internet import reactor
    from scrapy.crawler import CrawlerRunner
    from scrapy.utils.log import configure_logging
    from scrapy.utils.project import get_project_settings

    # configure_logging()
    settings = get_project_settings()
    settings.set("ITEM_PIPELINES", {'JobSpider.recruit.recruit.pipelines.RecruitPipeline': 300})
    runner = CrawlerRunner(settings)
    from JobSpider.recruit.recruit.spiders.test_spider import TestSpider
    runner.crawl(TestSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


def start_three():
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


if __name__ == "__main__":
    # start_one()
    start_two()
    # start_three()












