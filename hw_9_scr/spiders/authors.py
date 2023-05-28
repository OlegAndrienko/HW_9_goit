import scrapy
from scrapy.crawler import CrawlerProcess

import json


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    
    # def start_requests(self):
        
    #     next_author_page = response.xpath("/html//span/a/@href")
    #     authors_pathes = []
        
    #     for next_page in next_author_page:
    #         patern = 'author'
    #         current_page = next_page.get()
    #         autor_page = current_page.find(patern)
    #         if autor_page >=0:
    #             authors_pathes.append(current_page)
        
    #     res_url_authors = []
    #     for el in authors_pathes:
    #         if el not in  res_url_authors:
    #              res_url_authors.append(el)
    #     print('---------------')
    #     print(res_url_authors)
    #     print('---------------')
        
    #     start_urls_new = []
        
    #     for el in res_url_authors:
    #         full_page_path = self.start_urls[0] + el
    #         start_urls_new.append(full_page_path)
    #     print(start_urls_new)   
        
        
    #     return super().start_requests()

    def parse(self, response):
          
        # for author in response.xpath("/html//div[@class='quote']"):
            
        #     yield {
        #         #/html/body/div/div[2]/div[1]/div[1]/span[2]/small
        #         # "fullname": author.xpath("div[@class='tags']/a/text()").extract(),
        #         # "born_date": author.xpath("span/small/text()").extract(),
        #         # "born_location": author.xpath("span[@class='text']/text()").get(),
        #         # "description":  author.xpath("span[@class='text']/text()").get()
                
        #         #/html/body/div/div[2]/div[1]/div[1]/span[2]/a
        #         'href': author.xpath("span/a").get(),  
        #         "author": author.xpath("span/small/text()").get()
        #     }
        
        
        #/html/body/div/div[2]/div[1]/div[2]/span[2]/a
        # authors = response.xpath("/html//span/a/@href")
        
        #Colect all author urls
        
        next_author_page = response.xpath("/html//span/a/@href")
        authors_pathes = []
        
        for next_page in next_author_page:
            patern = 'author'
            current_page = next_page.get()
            autor_page = current_page.find(patern)
            if autor_page >=0:
                authors_pathes.append(current_page)
        
        res_url_authors = []
        for el in authors_pathes:
            if el not in  res_url_authors:
                 res_url_authors.append(el)
    
        
        # for el in res_url_authors:
        #     yield scrapy.Request(url=self.start_urls[0] + el)
            
        authors_info = response.xpath("/html//div[@class='author-details']")
        for el in authors_info:
            yield {
                "fullname": el.xpath("h3[@class='author-title']/text()").get(),
                "born_date": el.xpath("p/span[@class='author-born-date']/text()").get(),
                "born_location": el.xpath("p/span[@class='author-born-locatio']/text()").get(),
                "description":  el.xpath("div[@class='author-description']/text()").get()
            }
        
        print('+++++++++++++++++++++')
        print(authors_info)
        for el in res_url_authors:
            yield scrapy.Request(url=self.start_urls[0] + el)
        
   # scrapy crawl authors -O authors.json 


