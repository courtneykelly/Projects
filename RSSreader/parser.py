#! /usr/bin/env python3

# author:		Courtney Kelly
# resources: 	https://github.com/os/slacker
#				https://api.slack.com/methods

import sys
import os
import feedparser
import re
import errno
from strip import MLStripper
from constants import *
from slacker import *

# Constants 

ARGUMENTS   = sys.argv[1:]
HTML_STRIPPER = MLStripper()

# Functions 

def usage(exit_code=0):
   print('''Usage: {} 
   please edit the constant.py file with appropriate variables shown below:

   RSS_URL = <url of the RSS feed to search>
   KEYWORDS = <list of keywords to match>
   SLACK_TOKEN = <API token of team to send results to>
   SLACK_USER = <name of user or channel to send results to>
   STRIP = <boolean: should search results be stripped of HTML tags?>\n'''.format(os.path.basename(sys.argv[0])))
   sys.exit(exit_code)

def search(feed):
	data = ''
	for entry in feed['entries']:
		for keyword in KEYWORDS:
			regex = '.*' + keyword + '.*'
			if re.search(regex, entry['summary'], re.I):
				match = re.search(regex, entry['summary'], re.I)
				data += match.group(0).strip() + '\n\n'
	return data

def push():
	slack = Slacker(SLACK_TOKEN)
	# Get users list
	response = slack.users.list()
	users = response.body['members']
	# find user
	for user in users:
		if user['name'] == SLACK_USER:
			SLACK_ID = user['id']
			print(SLACK_ID)
			slack.chat.post_message(SLACK_ID, DATA, as_user=True)
			return
	# message channel
	try:
		slack.chat.post_message(SLACK_USER, DATA, as_user=True)
	except:
		print("Error: couldn't find /'{}/' slack user/channel".format(SLACK_USER))
		exit(1)


# Main Execution

# Parse command line arguments
while ARGUMENTS and ARGUMENTS[0].startswith('-') and len(ARGUMENTS[0]) > 1:
   arg = ARGUMENTS.pop(0)
   if arg == '-h':
       usage(0)
   else:
       usage(1)

# parse RSS feed & search for keywords
feed = feedparser.parse(RSS_URL)
DATA = search(feed)
print("Search successful")

# Clean up results if specified
if STRIP:
	HTML_STRIPPER.feed(DATA)
	DATA = HTML_STRIPPER.get_data()
	print("Results clean up successful")

# push to slack
push()
print("Push to slack successful")
