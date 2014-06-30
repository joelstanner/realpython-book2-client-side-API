# wikispider.py - spider


from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector

from wikipedia.items import WikipediaItem

from urlparse import urljoin

class MySpider(Spider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Category:2014_films"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//tr[@style="vertical-align: top;"]//li')
        items = []
        for title in titles:
            item = WikipediaItem()
            url = title.select("a/@href").extract()
            item["title"] = title.select("a/text()").extract()
            item["url"] = urljoin("http://en.wikipedia.org", str(url[0]))
            items.append(item)
        return(items)