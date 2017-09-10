from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
from nltk.twitter import Twitter
import tweepy
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

Twitt ="D:/randomt/twitter.txt"

tw = Twitter()
tw.tweets(keywords='jayalalitha', stream=False, limit=10)
