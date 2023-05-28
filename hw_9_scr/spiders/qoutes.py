import scrapy
from scrapy.crawler import CrawlerProcess

import json


class QoutesSpider(scrapy.Spider):
    name = "qoutes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        
        for quote in response.xpath("/html//div[@class='quote']"):
             yield {
                "tags": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").extract(),
                "quote": quote.xpath("span[@class='text']/text()").get()
            }
        
        #<li class="next"> 
        #   <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>    
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)
            
            
# scrapy crawl qoutes -O quotes.json



# process = CrawlerProcess()
# process.crawl(QoutesSpider)
# process.start()

# print('-------------------------')
# print(type(process))


