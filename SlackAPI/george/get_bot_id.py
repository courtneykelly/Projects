#!/usr/bin/env python3

import yaml
from slackclient import SlackClient
from os.path import expanduser

# Load message data
data_file = expanduser("~") + '/.bot_data/data.yml'
data = yaml.safe_load(open(data_file))

# Constants 
TOKEN = data['TOKEN']
BOT_NAME = 'george'

# Main Execution

slack_client = SlackClient(TOKEN)

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)