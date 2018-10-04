#!/usr/bin/env python3

# test commit

import os
import time
import datetime
import json

print("Checking host statuses...")

# Url variable initialization
url_down = 0 #Count of how many times the url has been pinged as down until a successful ping resets the count
url_timestamp = 0 #Timestamp of the ping

# Load config.json
with open('config.json', 'r') as f:
    config = json.load(f)

url = config['URL']
url_grace = config['URL_GRACE']
interval = config['INTERVAL']

#url = url of host to check; url_grace = how many minutes of being down before you want to be notified
def check(url, url_grace):
    response = os.system("ping -c 1 " + url)
    global url_down
    global url_timestamp
    if response == 0:
        print(url + " is up.")
        url_down = 0
    else:
        print (url + " is down!")
        url_down += 1
        url_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(url_timestamp)
        if url_down >= url_grace - 1:
            print("and has been down for", url_down - 1, "minutes")

while True:
    check(url, url_grace)
    time.sleep(interval)
