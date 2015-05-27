import tweepy
import time
from sys import argv
from keys import *

# authentication stuff ...
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# sleep for 6 seconds after every tweet
sleep_time = 6

# let's get a text file to use for our bot
try:
    textfile = argv[1]
except IndexError:
    textfile = "bible.txt"

# trying to open it
try:
    with open(textfile) as lines:
        print("Tweeting {} line by line".format(textfile))

        # print("Tweeting at http://twitter.com/" + api.me().name )

        # iterate over the lines, tweeting them one by one
        for line in lines:
            try:
                print("Trying to tweet the next line:")
                print(line)
                print
                api.update_status(status=line)
            except tweepy.TweepError as e:
                print("Uh, oh! Something went wrong:")
                print(e)
                # print("Twitter Error {}: '{}'".format(e["code"], e["message"]))

            # sleep a while so we don't hit the rate limit
            time.sleep(sleep_time)

except IOError:
    print("Wait. Are you sure the file '{}' exists?".format(textfile))


