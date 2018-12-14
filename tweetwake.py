#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-user-timeline
#  - displays a user's current timeline.
#-----------------------------------------------------------------------

from twitter import *
import datetime
import time
from wakeonlan import send_magic_packet
import time

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import config

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

#-----------------------------------------------------------------------
# this is the user we're going to query.
#-----------------------------------------------------------------------
user = config.user
#-----------------------------------------------------------------------
# query the user timeline.
# twitter API docs:
# https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
print("=========  Fetching timeline for {}  =========".format(user))
results = twitter.statuses.user_timeline(screen_name = user)

#-----------------------------------------------------------------------
# loop through each status item, and print its content.
#-----------------------------------------------------------------------
for status in results:
    print("(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore")))

    tweet_time_str = status["created_at"]
    # Convert to format Thu Dec 13 03:36:41 +0000 2018
    tweet_time = datetime.datetime.strptime(tweet_time_str, '%a %b %d %H:%M:%S %z %Y')

    # Convert to Unix timestamps in UTC
    tweet_ts = time.mktime(tweet_time.timetuple())
    current_ts = time.mktime(datetime.datetime.utcnow().timetuple())

    # They are now in seconds, subtract and then divide by 60 to get minutes.
    diff_mins = int(current_ts-tweet_ts) / 60
 
    if(diff_mins < 3):
        print("Wake up! Sending packet")
        send_magic_packet(config.mac_address)

 



