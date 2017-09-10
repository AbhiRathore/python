import tweepy
import json
import nltk
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

f = open('D:/random/python_jaya2.json','r')
data1 = f.readlines()
ar=[]
dict1={}

for line1 in data1:
    line = json.loads(line1)
    #print line["user"]["name"]
    tweets=' '.join(re.sub("([^@A-Za-z0-9$])|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",line["text"]).split())
    tweets=re.sub("(Cares|HDFCBank|ICICBank|Care|IDBI|Bank|KotakBankLtd|[IC?])","",tweets)
    #print tweets
    #print line["text"]
    print line['place']
    dict1['name']=line["user"]["name"].encode('utf-8').strip()
    dict1['tweet']=line["text"].encode('utf-8').strip()
    ss = sid.polarity_scores(tweets)
    #print dict1
    #print("sentiment_score"+":"+str(ss['compound']))
    if ss['compound']<=0:
        print line["user"]["name"]
        print tweets
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
    print("###########")

    

"""
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]))
    print "-----------------------------------"
"""
    #for sentence in line["text"]:
        #print(sentence)
        
    


"""
with open('D:/random/python1.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    for lines in line:
        tweet = json.loads(lines) # load it as Python dict
        #tweets=json.dumps(tweet, indent=4) # pretty-print
        print tweet["user"]["name"]
"""
        
        


       
