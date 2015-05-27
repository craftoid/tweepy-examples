import tweepy
import time
from sys import argv
from keys import *

# authentication stuff ...
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# sleep a small number of seconds after every tweet
sleep_time = 3

# limit the number of tweets so we don't hit the rate limit
max_tweets = 10

# limit size of a tweet
tweet_size = 140

# debugging, without annoying twitter
debug = False


# let's get a text file to use for our bot
try:
    textfile = argv[1]
except IndexError:
    print("Please provide a filename")
    exit()

# let's get a linenumber, where we start tweeting
try:
    first_line = int(argv[2])
except ValueError:
    print("Please insert Linenumber as second argument")
    exit()
except IndexError:
    print("Please provide a Linenumber")
    exit()

# trying to open it
try:
    with open(textfile) as lines:
        print("Tweeting {} line by line".format(textfile))

        # name = api.me().name
        # print("Tweeting at http://twitter.com/" + api.me().name )
  
        # create a list for the sake of slicing it apart
        lines = list(lines)[first_line - 1:first_line - 1 + max_tweets]

        # possivly adjust the number of maximum tweets
        if max_tweets > len(lines):
            max_tweets = len(lines)

        # iterate over the lines, tweeting them one by one
        for linenumber, line in enumerate(lines, first_line):

            # create a series of tweets in the format "1/10: ..."
            line = line.strip()
            line = "{}/{}: {}".format(linenumber - first_line + 1, max_tweets, line) 
  
            # make sure our line is not longer than the maximum tweet size
            if len(line) > tweet_size:
                line = line[:tweet_size]
 
            # if the line is empty just continue with the next one
            if line == "":
                print("{} is an empty line".format(linenumber))
                continue
            else:
                print("Number of chars: {}".format(len(line)))
           

            try:
                if debug:
                    # feedback on the command line
                    print("DEBUG {} >>> {}".format(linenumber, line))

                else:
                    # feedback on the command line
                    print("TWEET {} >>> {}".format(linenumber, line))

                    # use the twitter API to send a tweet
                    api.update_status(status=line)

                    # sleep a while so we don't hit the rate limit
                    time.sleep(sleep_time)

            except tweepy.TweepError as e:
                print("Uh, oh! Something went wrong:")
                print(e)


except IOError:
    print("Wait. Are you sure the file '{}' exists?".format(textfile))


