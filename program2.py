import tweepy
import sys
from textblob import TextBlob

with open('/Users/josephbrock/twitter_keys', 'r') as mykeys:
	Keys = mykeys.read()
Keys = Keys.split('\n')
consumer_key = Keys[0].split()[0]
consumer_secret = Keys[1].split()[0]
access_token = Keys[2].split()[0]
access_token_secret = Keys[3].split()[0]

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#tesla')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
