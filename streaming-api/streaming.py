# -*- coding: utf-8 -*-
# Defining a file encoding for python 2, just in case.
# See: https://docs.python.org/2/howto/unicode.html

import tweepy
import json

from keys import *
from console import colorize, hilight
from sys import argv
from textwrap import wrap

# Authentication details. To  obtain these visit dev.twitter.com

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    """ a listener for twitter streams to print the tweets in a console-friendly format """

    def __init__(self, tag, linewidth=40):

        # call super constuctor
        tweepy.StreamListener.__init__(self)

        # set object attributes
        self.tag = tag
        self.linewidth = linewidth


    def on_data(self, tweet):

        # decode JSON data received from twitter
        data = json.loads(tweet)
        try:
            user = data['user']['screen_name']
            tweet = data['text']

            # make sure to use unicode strings for python 2
            print(u"-" * self.linewidth)
            hilighted = u"{}: {}".format(colorize(user, "blue"), hilight(tweet, self.tag))
            wrapped = u"\n".join(wrap(u"{}: {}".format(colorize(user, "blue"), hilight(tweet, self.tag)), width=self.linewidth))
            print(wrapped)
        except:
            print(colorize('Something went wrong ...'))
        return True

    def on_error(self, status):
        print(colorize(status))

if __name__ == '__main__':

    # get the current mode from the first command line argument
    try:
        mode = argv[1]
    except:
        print ("USAGE: {} [trending|emoji]".format(argv[0]))
        exit()

    # get consumer key and secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # get access token and secret
    auth.set_access_token(access_token, access_token_secret)

    # get a topic from the trending topics
    
    if mode == "trending":

        api = tweepy.API(auth)
        trends = api.trends_place(1)
        topics= trends[0]['trends']
    
        # let's be gentle and pick the very last topic from the list
        top_topic = topics[-1]['name']

    elif mode == "emoji":
        top_topic = u"😃"

    print(u"Filtering for {}.".format(colorize(top_topic)))

    # create a receiver to print the tweets on the console
    receiver = StdOutListener(top_topic)

    # create and configure a twitter stream
    stream = tweepy.Stream(auth, receiver)
    stream.filter(track=[top_topic])
