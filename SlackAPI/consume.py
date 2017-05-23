#!/usr/bin/env python3

import requests
import json
import yaml
import time
import argparse
from slackclient import SlackClient
from os.path import expanduser

# Load message data
data_file = expanduser("~") + '/.consume_data/data.yml'
data = yaml.safe_load(open(data_file))

# Constants 

TOKEN = data['TOKEN']
CHANNEL = data['CHANNEL']
MESSAGE = data['MESSAGE']
OK = True

# Main Execution

# Parse command line arguments
parser = argparse.ArgumentParser(description='consume a channel on Slack')
parser.add_argument('-t', type=str, help="API token of team to send results to", dest=TOKEN)
parser.add_argument('-c', type=str, help="name or ID of channel to consume", dest=CHANNEL)
parser.add_argument('-m', type=str, help="message to send to consume channel", dest=MESSAGE)
args = parser.parse_args()

# create client
sc = SlackClient(TOKEN)

# start connection
print("[consume.py] starting connection...")
if sc.rtm_connect():  # connect to a Slack RTM websocket
	print("[consume.py] connection successful...")
	time.sleep(1) # wait for response

	# read connection response
	print("[RTM Websocket Response] {}\n".format(sc.rtm_read())) # read initial response
	print("[RTM Websocket Response] {}\n".format(sc.rtm_read())) # read initial response
	
	# get channel
	print("[consume.py] locating channel \'{}\'...".format(CHANNEL))
	response = sc.server.channels.find(CHANNEL)
	CHANNEL_ID = response.id

	# consume until error
	print("[consume.py] consuming...")
	while OK:
		sc.rtm_send_message(CHANNEL_ID, MESSAGE) # send message
		response = sc.rtm_read()
		if 'ok' in response[0]:	# skip other types of responses (i.e. 'reconnect_url')
			OK = response[0]['ok']
		elif 'type' in response[0]:
			if response[0]['type'] == 'error':
				OK = False
		print("[RTM Websocket Response] {}\n".format(response)) # read response
		time.sleep(1)	# wait one second

	# print error 
	print("[RTM Websocket Response] Send Message Error: {}".format(response[0]['error']['msg']))
else:
    print ('[RTM Websocket Connection] FAILED: possible invalid token\n')

# exit on failure
print("[consume.py] exiting...")