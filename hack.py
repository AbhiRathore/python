# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 09:02:21 2016

@author: abhishekr
"""
import tweepy
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
consumer_key='CY3nwLF7mbcJL8f7eZPmvSgXT'
consumer_secret='xpwFSidZbx1KtilXsrQ9ISyjkmDaapn1cPNKFab5OCijMxOrpk'
access_token='3138454441-rxJh3uZ7nzJhNcm4rFJiCkNZD8NxYYmZy5Fbl8x'
access_secret='MAqyxlZNshrKW8e6B9xWdpU0pJSqlnUvp9PaKbuKq1mCC'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

"""
for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status.text)

#def process_or_store(tweet):
    #print(json.dumps(tweet))
    
 
#for status in tweepy.Cursor(api.home_timeline).items(10):
 
       #process_or_store(status._json) 

f=[]
for tweet in tweepy.Cursor(api.user_timeline).items():
       data1=json.dumps(tweet._json,ensure_ascii=True)
       h=json.loads(data1)
       
       #print(h)
       #f.append(h)
#f_total=",".join(f)
#print("last one "+" "+h)
"""
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('D:/random/python_hdfcfeb.json', 'a') as f:
                f.write(data)
                return True
                print(data)
        except BaseException as e:
            print("fail")
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['@HDFCBANK_Cares'])



       
       
