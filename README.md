# Projects
2017 Data Machines Intern Projects

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