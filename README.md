# Projects
2017 Data Machines Intern Projects

## RSS Reader
python code to parse an RSS feed (i.e. the US-Cert security advisory feed) and run a regex (i.e. search for 'cisco') and push to Slack (i.e. #security). Run `./parser.py -h` for usage.

## Slack API
two examples of externally interacting with Slack. `message.py` uses the Slack API and slack team generated API token to send messages to a specific user. `consume.py` uses a [Webhook](https://api.slack.com/incoming-webhooks) to consume a specified channel #trolling. run `./message.py -h` or `./consume.py -h` for usage.


