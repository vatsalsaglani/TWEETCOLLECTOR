import twitter, re, datetime
import pandas as pd


#create a miner class to mine the tweets you want for a particular user

class miner():

    # there are some rate-limits which restricts the developer to get only 75 tweets per day 
    # read this at https://developer.twitter.com/en/docs/basics/rate-limits
    request_limit = 70
    api = False
    data = []

    # your the below given keys to the space, you can get this keys and secrets from 
    # developer.twitter.com and by creating a App With Twitter
    twitter_keys = {
        'consumer_key': "<YOUR SECRETS/KEY OVER HERE>",
        'consumer_secret': "<YOUR SECRETS/KEY OVER HERE>",
        'access_token_key': "<YOUR SECRETS/KEY OVER HERE>",
        'access_token_secret': "<YOUR SECRETS/KEY OVER HERE>" 

    }

    def __init__(self, request_limit = 70):

        self.request_limit = request_limit
       # call the api 
        self.set_api()

    def set_api(self):

        self.api = twitter.Api(
            consumer_key = self.twitter_keys['consumer_key'],
            consumer_secret = self.twitter_keys['consumer_secret'],
            access_token_key = self.twitter_keys['access_token_key'],
            access_token_secret = self.twitter_keys['access_token_secret']
        )


    def mineUserTweets(self, user = "thevatsal_s", mine_reweets = False):


        # can read the docs about the library(python-twitter) which we are using to access the api
        # from https://python-twitter.readthedocs.io/en/latest/index.html
        statuses = self.api.GetUserTimeline(screen_name = user, count = self.request_limit)

        data = []
        # adding the data we want to mine for a particular user to the data list we created(data) using the mined dicts//
        for item in statuses:
            mined = {
                'tweet_id': item.id,
                'handle': item.user.name,
                'retweet_count': item.retweet_count,
                'text': item.text,
                'mined_at': datetime.datetime.now(),
                'created_at': item.created_at,
            }

            data.append(mined)

        return data

# here we call miner as mine 
mine = miner()


# let's mine some tweets so we give a twitter handle name in here.
someTweets = mine.mineUserTweets("OnePlus_IN")
randomDF = pd.DataFrame(someTweets, columns=['tweet_id', 'handle', 'retweet_count', 'text', 'mined_at', 'created_at'])
randomDF.to_csv('randomDF.csv', header=True, index=False)
