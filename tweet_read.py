# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:01:28 2016

@author: abhishekr
"""


import json
import nltk

f = open('D:/random/python1.json','r')
data1 = f.readlines()

for line1 in data1:
    line = json.loads(line1)
    print(line["user"]["name"])
    print(line["text"])
    print(nltk.word_tokenize(line["text"]))
    


"""

with open('D:/random/python1.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    for lines in line:
        tweet = json.loads(lines) # load it as Python dict
        #tweets=json.dumps(tweet, indent=4) # pretty-print
        print tweet["user"]["name"]
"""
        
        


       
