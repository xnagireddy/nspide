# -*- coding: utf-8 -*-
import scrapy


class NytimesSpider(scrapy.Spider):
    name = 'nytimes'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://nytimes.com/']

    def parse(self, response):
        pass
