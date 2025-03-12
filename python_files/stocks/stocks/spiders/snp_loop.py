import scrapy
from stocks.items import StocksItem


class SnpLoopSpider(scrapy.Spider):
    name = "snp_loop"
    allowed_domains = ["https://www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        stock = StocksItem()
        table = response.css("table.table.table-hover.table-borderless.table-sm")

        rows = table.xpath("//tr")
        for row in rows:
            stock['company'] = row.xpath("td[2]/a/text()").get()
            stock['symbol'] = row.xpath("td[3]/a/text()").get()
            stock['YTD_return'] = row.xpath("td[4]/text()").get()
            if stock['company']:
                stock['YTD_return'] = stock['YTD_return'].strip()
            yield stock
