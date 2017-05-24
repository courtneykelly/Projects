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

Run `scrapy runspider URLSpider` to execute.
See output files `success.txt` and `failed.txt` for the urls successfully grabbed & converted to json, and the urls that failed with their error status code & error reason.