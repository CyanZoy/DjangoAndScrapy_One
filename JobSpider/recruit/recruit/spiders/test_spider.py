import scrapy
from JobSpider.recruit.recruit.items import RecruitItem, TestbotItem
from scrapy.utils.project import get_project_settings

class TestSpider(scrapy.Spider):
    name = "test_spider"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = RecruitItem()
            item['text'] = quote.css('span.text::text').extract_first()
            item['author'] = quote.xpath('span/small/text()').extract_first()
            print('TestSpider:%s' % item['author'])
            yield item
        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

    custom_settings = {'BOT_NAME': 'recruit', 'CONCURRENT_REQUESTS_PER_IP': 16,
                       'DOWNLOAD_DELAY': 0.5, 'DOWNLOAD_TIMEOUT': 100,
                       'NEWSPIDER_MODULE': 'recruit.spiders', 'SPIDER_MODULES': ['recruit.spiders']}