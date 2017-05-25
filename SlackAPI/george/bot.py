#!/usr/bin/env python3

import yaml
import time
import random
import praw
from slackclient import SlackClient
from os.path import expanduser

# Load message data
data_file = expanduser("~") + '/.bot_data/data.yml'
data = yaml.safe_load(open(data_file))

# Constants 
TOKEN = data['TOKEN']
BOT_ID = data['BOT_ID']
AT_BOT = "<@" + BOT_ID + ">"
COMMAND = "tell me a joke"
READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose

# Functions
def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response1 = "Not sure what you mean. try the *" + COMMAND + \
               "* command"
    response2 = ""
    if command.startswith(COMMAND):
        try:
        	reddit = connect_to_reddit()
        	joke_list = list(reddit.subreddit('dadjokes').top(limit=50))
        	joke_id = random.choice(joke_list)
        	joke = reddit.submission(id=str(joke_id))
        	response1 = joke.title
        	response2 = joke.selftext
        except Exception as e:
        	response1 = "Whoops, something went wrong. Try again real soon! "
        	response2 = "exception: {}".format(e)
    
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response1, as_user=True)
    time.sleep(3)
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response2, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

def connect_to_reddit():
	reddit = praw.Reddit(client_id=data['CLIENT_ID'],
	                     client_secret=data['CLIENT_SECRET'],
	                     password=data['PASSWORD'],
	                     user_agent=data['USER_AGENT'],
	                     username=data['USERNAME'])
	return reddit

# Main Execution
if __name__ == "__main__":

	slack_client = SlackClient(TOKEN)
	
	if slack_client.rtm_connect():
		while True:
			command, channel = parse_slack_output(slack_client.rtm_read())
			if command and channel:
				handle_command(command, channel)
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print("Connection failed. Invalid Slack token or bot ID?")