#! /usr/bin/env python3

import scrapy
from scrapy_splash import SplashRequest
from flask import Flask, jsonify, request
from scrapy.crawler import CrawlerProcess


app = Flask(__name__)

class TestSpider(scrapy.Spider):
        name = "test"
        start_urls = ["http://example.com", 
        "http://example.com/foo"]
        results = {}

        def start_requests(self):
            for url in self.start_urls:
                yield SplashRequest(url, self.parse, args={'wait': 0.5})

        def parse(self, response):
            # response.body is a result of render.html call; it contains HTML processed by a browser.
            # html = response.body
            title = response.css('title').extract_first()
            self.results[response.url] = title

        def closed(self, reason):

            # output results
            print('\n\n\n\n')
            print('RESULTS:')
            print(self.results)
            print('\n\n\n\n')

            # return results
            return "hi"

@app.route('/', methods=['GET'])
def index():
    
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(TestSpider)
    process.start() # the script will block here until the crawling is finished

    return TestSpider()

if __name__ == '__main__':
    app.run()