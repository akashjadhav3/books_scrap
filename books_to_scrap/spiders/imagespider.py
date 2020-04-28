# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from books_to_scrap.items import BooksToScrapItem


class ImagesToScrapSpider(scrapy.Spider):
    # name = 'imagespider'
    name = 'downloader'
    # allowed_domains = ['http://books.toscrape.com/']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for article in response.xpath("//article[@class='product_pod']"):
            loader = ItemLoader(item=BooksToScrapItem(), selector=article)
            relative_url = article.xpath(".//div[@class='image_container']/a/img/@src").extract_first()
            absoulte_url = response.urljoin(relative_url)
            loader.add_value('image_urls', absoulte_url)
            loader.add_xpath('book_name', './/h3/a/@title')
            yield loader.load_item()
            

