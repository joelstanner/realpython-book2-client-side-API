# socrata_spider.py


from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from socrata.items import SocrataItem

class MySpider(CrawlSpider):
    name = "socrata2"
    allowed_domains = ["opendata.socrata.com"]
    start_urls = ["http://opendata.socrata.com"]
    
    rules = (Rule (SgmlLinkExtractor(allow=
                                     ("browse\?utf8=%E2%9C%93&amp;page=\d*",)),
             callback="parse_items", follow= True),)
    
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