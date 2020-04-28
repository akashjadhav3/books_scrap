# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
# from os import path

class BooksToScrapePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x,meta={'bookname': item.get('book_name')}) for x in item.get(self.images_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        filename = request.meta['bookname'].replace(':', '')
        return 'full/%s.jpg' % (filename)

