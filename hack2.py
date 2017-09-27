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
            with open('D:/random/python_hdfc6feb.json', 'a') as g:
                g.write(data)
                return True
                ar=[]
                dict1={}
                #for line1 in data:
                #print line1
                line = json.loads(data)
                #print line["user"]["name"]
                #print line["text"]
                tweets=' '.join(re.sub("([^A-ZIa-z0-9])|([^0-9IA-Za-z \t]|(\w+:\/\/\S+))"," ",line["text"]).split())
                tweets=re.sub("(Cares|HDFCBank|ICICBank|Care|IDBI|Bank|KotakBankLtd|[IC?])","",tweets)
                #print tweets
                #print line["text"]
                dict1['name']=line["user"]["name"].encode('utf-8').strip()
                dict1['tweet']=line["text"].encode('utf-8').strip()
                ss = sid.polarity_scores(tweets)
                #print dict1
                #print("sentiment_score"+":"+str(ss['compound']))
                #if ss['compound']<=0:
                print line["user"]["name"]
                print tweets
                print line["retweet_count"]
                print line['place']
                print line['created_at']
                print ("sentiment_score"+":"+str(ss['compound']))
                #ar.append(dict1)
                #print ar
                try:
                    y= nltk.pos_tag(nltk.word_tokenize((tweets)))
                    wanted = ["JJ","VB"]
                    unwanted=["@","the"]
                    new_list = []
                    for val in y:
                        if val[1] in wanted and val[0] not in unwanted:
                            new_list.append(val)
                            print(new_list)
                except:
                    print dict1['tweet']
                print("----------------------------------------------------------------------------------------")
                sleep(4)
                    
                    #print(f.write(data))
        except BaseException as e:
            print("fail")
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['@HDFCBANK_Cares'])

"""

f = open('D:/random/python_jaya2.json','r')
data1 = f.readlines()
print data1
ar=[]
dict1={}
#for line1 in data:
#print line1
line = json.loads(data1)
#print line["user"]["name"]
#print line["text"]
tweets=' '.join(re.sub("([^A-ZIa-z0-9])|([^0-9IA-Za-z \t]|(\w+:\/\/\S+))"," ",line["text"]).split())
tweets=re.sub("(Cares|HDFCBank|ICICBank|Care|IDBI|Bank|KotakBankLtd|[IC?])","",tweets)
#print tweets
#print line["text"]
dict1['name']=line["user"]["name"].encode('utf-8').strip()
dict1['tweet']=line["text"].encode('utf-8').strip()
ss = sid.polarity_scores(tweets)
#print dict1
#print("sentiment_score"+":"+str(ss['compound']))
#if ss['compound']<=0:
print line["user"]["name"]
print tweets
print line["retweet_count"]
print line['place']
print line['created_at']
print ("sentiment_score"+":"+str(ss['compound']))
#ar.append(dict1)
#print ar
try:
    y= nltk.pos_tag(nltk.word_tokenize((tweets)))
    wanted = ["JJ","VB"]
    unwanted=["@","the"]
    new_list = []
    for val in y:
        if val[1] in wanted and val[0] not in unwanted:
            new_list.append(val)
            print(new_list)
except:
    print dict1['tweet']
print("----------------------------------------------------------------------------------------")
sleep(4)

"""

       
       
