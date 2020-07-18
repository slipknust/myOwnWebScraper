from twitterscraper import query_tweets
from twitterscraper.query import query_tweets_from_user
import datetime as dt
import pandas as pd

class TtScraper:
    def __init__(self, title, user):
        self.title = title
        self.user = user
        self.tweets_scp = query_tweets_from_user(user, limit=10)
        self.df = pd.DataFrame(t.__dict__ for t in self.tweets_scp)
        # df = pd.DataFrame(t.__dict__ for t in tweets)

        #self.df = self.df.loc[self.df['screen_name'] == self.user]

        #self.df = self.df['text']

    #tweets = query_tweets_from_user(user)


