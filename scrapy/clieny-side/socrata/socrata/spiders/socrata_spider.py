# socrata_spider.py


from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector

from socrata.items import SocrataItem

class MySpider(Spider):
    name = "socrata"
    allowed_domains = ["opendata.socrata.com"]
    start_urls = ["http://opendata.socrata.com"]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        names = hxs.select('//tr[@itemscope = "itemscope"]')
        items = []
        for name in names:
            item = SocrataItem()
            item["name"] =  name.select('td[2]/div/span/text()').extract()

            item["url"] = name.select('td[2]/div/a/@href').extract()
            item["views"] = name.select('td[3]/span/text()').extract()
            items.append(item)
        return(items)