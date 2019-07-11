# -*- coding: utf-8 -*-
import logging
import scrapy


class WsjSpider(scrapy.Spider):
    name = 'wsj'
    allowed_domains = ['wsj.com']
    start_urls = [
        'https://www.wsj.com/news/archive/20190701',
        'https://www.wsj.com/news/archive/20190702',
    ]

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'wsj-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        articles = response.css('article')
        for article in articles:
            logging.info('flashline: [%s]', article.css('div div div::text').get())
            logging.info('headline: [%s]', article.css('div div h3 a::text').get())
            logging.info('link: [%s]', article.css('div div h3 a::attr(href)').get())
            logging.info('summary: [%s]', article.css('div p span::text').get())

