#! /usr/bin/env python3

import scrapy
import logging
from urls import urls
from errorcodes import codes
from newspaper import Article

class URLSpider(scrapy.Spider):
    name = "url"
    start_urls = urls
    handle_httpstatus_list = codes.keys()
    success_urls = {}
    failed_urls = {}

    def __init__(self, *args, **kwargs):
        logger = logging.getLogger('scrapy.middleware')
        logger.setLevel(logging.WARNING)
        super().__init__(*args, **kwargs)

    def parse(self, response):
        self.logger.info('Processing: \'%s\'', response.url)
        if response.status in self.handle_httpstatus_list:
            self.failed_urls[response.url] = '{}: {}'.format(response.status, codes[response.status])
        else:
            article = Article(response.url)
            article.download()
            article.parse()
            json = {'title' : article.title , 'authors' : article.authors,'text' : article.text,'image': article.top_image}
            self.success_urls[response.url] = json

    def closed(self, reason):
        # output files
        s = open('success.txt', 'w')
        f = open('failed.txt', 'w')

        # output results
        print('\n\n\n\n')
        self.logger.info('Successful urls: \n')
        for k in self.success_urls:
            s.write("{}:\n{}\n\n".format(k, self.success_urls[k]))
            print("{}:\n{}\n\n".format(k, self.success_urls[k]))
        self.logger.info('\nFailed urls: \n')
        for k in self.failed_urls:
            f.write('{}:  {}\n'.format(k, self.failed_urls[k]))
            print('{}:  {}'.format(k, self.failed_urls[k]))
        print('\n\n')

        # close files
        s.close()
        f.close()

