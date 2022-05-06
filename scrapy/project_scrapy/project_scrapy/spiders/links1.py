# Libraries
import scrapy

# Creating scrappy object - Link
class Link(scrapy.Item):
    link = scrapy.Field()

# 
class LinkListsSpider(scrapy.Spider):
    name = 'link_lists'
    allowed_domains = ['https://www.goodreads.com/']
    start_urls = ['https://www.goodreads.com/list/show/1']

    def parse(self, response):
        xpath = '//a[@class="bookTitle"]/@href'
               
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://www.goodreads.com' + s.get()
            yield l
    
