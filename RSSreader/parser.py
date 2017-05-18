#! /usr/bin/env python3

import feedparser
import re
from strip import MLStripper
from slacker import Slacker

# Variables
RSS_URL = "https://www.us-cert.gov/ncas/alerts.xml"
KEYWORDS = ["cisco"]
STRIP = True
HTML_STRIPPER = MLStripper()
SLACK_TOKEN = 'xoxp-17641790740-18528869586-186143857559-8c7bf68fbf54f0b641348a4cec11d6b6'
#SLACK_ID = 

# parse RSS feed
feed = feedparser.parse(RSS_URL)

# search for KEYWORDS
DATA = ""
for entry in feed['entries']:
	for keyword in KEYWORDS:
		regex = '.*' + keyword + '.*'
		if re.search(regex, entry['summary'], re.I):
			match = re.search(regex, entry['summary'], re.I)
			DATA += match.group(0).strip() + '\n\n'

# Clean up results if specified
if STRIP:
	HTML_STRIPPER.feed(DATA)
	DATA = HTML_STRIPPER.get_data()

# Push to slack
slack = Slacker(SLACK_TOKEN)
user_list = slack.users.list(SLACK_TOKEN)
for member in user_list['members']:
	print(member)
# 	if member['name'] == 'courtneykelly':
# 		SLACK_ID = member['id']
# print(SLACK_ID)
#slack.chat.post_message("@courtneykelly", DATA)