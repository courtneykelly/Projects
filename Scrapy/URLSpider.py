#! /usr/bin/env python3

import scrapy
import logging
from urls import urls
from newspaper import Article
from flask import jsonify

class URLSpider(scrapy.Spider):
    name = "url"
    start_urls = urls

    def __init__(self, *args, **kwargs):
        logger = logging.getLogger('scrapy.middleware')
        logger.setLevel(logging.WARNING)
        super().__init__(*args, **kwargs)

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        article = Article(response.url)
        article.download()
        article.parse()
        response = {'title' : article.title , 'authors' : article.authors,'text' : article.text,'image': article.top_image}
        return response