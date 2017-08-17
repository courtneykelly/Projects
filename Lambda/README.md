# AWS Lambda

Getting familiar with AWS Lambda and many other AWS Services, such as API Gateway, S3, IAML, EC2, etc. Here are several lambda functions I created using AWS Services.

* Get IP: returns public IP address

* Names API: two functions, does stuff with names

* Parse HTML: takes url string, and parses HTML content, returns json object

* Lambda Limits: pushes the AWS Lambda limit of 50 MB for a given deployment package, using the [Zappa tool](https://github.com/Miserlou/Zappa) 

* Summarize: takes url string and number of sentences, returns summary of given url with desired # of sentences [default 5]

* Scrapy Splash: attempt to put scrapy splash web scrapers behind a lambda function, so far unsuccessful (so far!)