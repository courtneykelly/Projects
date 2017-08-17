# Scrapy Splash

Attempted to put the library splash and scrapy-splash behind a lambda, due to limited time I was able to deploy to Lambda, but I was never able to successfully run a Spider.

I was close, but I was never able to figure out how to launch a scrapy crawl via lambda -- Scrapy is built on top of the Twisted asynchronous networking library, so you need to run it inside the Twisted reactor
