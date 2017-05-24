# URL Spider

This custom scrapy spider: `URLSpider` uses [scrapy](https://scrapy.org/) to grab a list of urls specfied in the file: `urls.py` and parse each one using [python newspaper](http://newspaper.readthedocs.io/en/latest/) and convert to json. Newspaper is a library designed to extract important html elements such as title, image, text, etc. from a given url. When the spider is finished crawling through each url, it writes results (both successes and failures) to separate `.txt` files.

## Installations

Please install the `scrapy` and `newspaper` python libraries and run using python 3.

## How to Run

1. Edit the `urls.py` file with a list of the desired urls to scrape.

2. Run `scrapy runspider URLSpider` to execute.

3. See output files `success.txt` and `failed.txt` for the urls successfully grabbed & converted to json, and the urls that failed with their error status code & error reason.
