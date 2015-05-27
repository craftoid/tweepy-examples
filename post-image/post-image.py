from __future__ import absolute_import, print_function

import tweepy
import sys
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

image = "image.png"

print("Tweeting at %s" % api.me().name)
print("Posting image: %s" % image)

if len(sys.argv) == 1:
	api.update_with_media(image, status="I tweet therefor I am!")
else:
	api.update_with_media(image, status=" ".join(sys.argv[1:]))
