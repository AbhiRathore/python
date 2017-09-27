# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 09:02:21 2016

@author: abhishekr
"""
import tweepy
import json
import sys
import pika
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
import nltk
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from time import sleep

sid = SentimentIntensityAnalyzer()
consumer_key='CY3nwLF7mbcJL8f7eZPmvSgXT'
consumer_secret='xpwFSidZbx1KtilXsrQ9ISyjkmDaapn1cPNKFab5OCijMxOrpk'
access_token='3138454441-rxJh3uZ7nzJhNcm4rFJiCkNZD8NxYYmZy5Fbl8x'
access_secret='MAqyxlZNshrKW8e6B9xWdpU0pJSqlnUvp9PaKbuKq1mCC'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            ar=[]
            dict1={}
            adj=['JJ']
            line = json.loads(data)
            #tweets=' '.join(re.sub("([^A-ZIa-z0-9])|([^0-9IA-Za-z \t]|(\w+:\/\/\S+))"," ",line["text"]).split())
            #print tweets
            dict1['name']=line["user"]["name"].encode('utf-8').strip()
            dict1['tweet']=line["text"].encode('utf-8').strip()
            #dict1['tweet']=line["retweet_count"]
            dict1['tweet']=line['place']
            #dict1['tweet']=line['created_at']
            time.sleep(5)
            print dict1['name']
            print line["text"].encode('utf-8').strip()
            print line['place']
            print line["retweet_count"]
            time.sleep(5)
            #print dict1['tweet']
            #dict1['geo']=line.geo
            #print dict1
            time.sleep(5)
            #with open('python.json', 'a') as f:
                #f.write(data)
                #return True
        except BaseException as e:
            print('&quot;Error on_data:')
        return True
    time.sleep(20)

    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
happy=["happy","glee","bliss","smiles","wonder"]
tw=["Chennai","chennai"]
twitter_stream.filter(track=tw,stall_warnings=True)
