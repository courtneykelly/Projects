# Projects
2017 Data Machines Intern Projects

## AWS Lambda Projects
Getting familiar with AWS Lambda and many other AWS Services, such as API Gateway, S3, IAML, EC2, etc. Created several functions, to see what services could be be put behind Lambda in order to scale. 

## RSS Reader
python code to parse an RSS feed (i.e. the US-Cert security advisory feed) and run a regex (i.e. search for 'cisco') and push to Slack (i.e. #security). 

Run `./parser.py -h` for usage.

## Slack API
two examples of externally interacting with Slack. `message.py` uses the Slack API and slack team generated API token to send messages to a specific user. `consume.py` uses a [Webhook](https://api.slack.com/incoming-webhooks) to consume a specified channel #trolling. 

Run `./message.py -h` or `./consume.py -h` for usage.

## Scrapy
scrapy code that reliabily grabs a list of urls, runs them through python newspaper, and outputs the data to json. Fully supports utf-8 and also outputs a list of urls it failed to fetch and why it failed.

## Crypto-currency transaction database

Set up Abe (https://github.com/bitcoin-abe/bitcoin-abe) or similar to start logging transactions into a database for BitCoin. Do this for as many currencies as possible. Fine if also logs to disk via json. Make the process repeatable. Provide a REST API via Python Flask that allows querying of the database with a cryptocurency address and returns transactions involving that address.

## Data Locality

Explored basics of data locality of Map Reduce based on research and formula from the School of Informatics and Computing from Indiana University Bloomingtom.