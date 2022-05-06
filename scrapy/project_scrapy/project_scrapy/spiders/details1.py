# -*- coding: utf-8 -*-
import scrapy

class Book(scrapy.Item):
    title          = scrapy.Field()
    author         = scrapy.Field()
    year           = scrapy.Field()
    publisher      = scrapy.Field()
    genre          = scrapy.Field()
    votes          = scrapy.Field()
    rating         = scrapy.Field()
    pages          = scrapy.Field()


class LinksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['www.goodreads.com']
    try:
        with open("link_lists.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []
    
    print(start_urls)
    
    def parse(self, response):
        p = Book()

        title_xpath          = '//h1[@id="bookTitle"]/text()'
        author_xpath         = '//span[@itemprop="name"]/text()'
        year_xpath           = '(//div[@id="details"]/div[@class="row"])[2]/text()'
        publisher_xpath      = '(//div[@id="details"]/div[@class="row"])[2]/text()'
        genre_xpath          = '//a[@class="actionLinkLite bookPageGenreLink"]/text()'
        votes_xpath          = '//meta[@itemprop="ratingCount"]/@content'
        rating_xpath         = '//span[@itemprop="ratingValue"]/text()'
        pages_xpath          = '//span[@itemprop="numberOfPages"]/text()'
        
        p['title']           = [x.strip() for x in response.xpath(title_xpath).getall()]
        p['author']          = response.xpath(author_xpath).getall()[0]
        p['year']            = response.xpath(year_xpath).re('[0-9]{4}')
        p['publisher']       = response.xpath(publisher_xpath).re('by.+')[0].strip()[3:]
        p['genre']           = response.xpath(genre_xpath).getall()[0]
        p['votes']           = response.xpath(votes_xpath).getall()
        p['rating']          = [x.strip() for x in response.xpath(rating_xpath).getall()]
        p['pages']           = response.xpath(pages_xpath).re('[0-9]+')
        

        yield p
