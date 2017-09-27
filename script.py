# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 10:48:20 2017

@author: abhishekr
"""
from collections import Counter
import nltk
#from nltk.corpus import stopwords

def tok(tweets):
    b=nltk.word_tokenize(tweets)
    x=Counter(b)
    #z=x.most_common(15)
    y=nltk.pos_tag(x)
    #print y
    stops = ['@','the','an']
    unwanted = ["RB", "VB", "NNP"]
    meaningful_word = [w[0] for w in y if w[0] not in stops and w[1] not in unwanted]
    print meaningful_word
tok('I will go there but not meet @harish becahse he is not a good guy and he is a cheat')
            
def tok(tweets):
    b=nltk.word_tokenize(tweets)
    x=Counter(b)
    #z=x.most_common(15)
    y=nltk.pos_tag(x)
    #print y
    stops = ['@','the','an','#',"b'"]
    unwanted = ["RB", "VB", "NNP"]
    meaningful_word = [w[0] for w in y if w[0] not in stops and w[1] not in unwanted]
    return meaningful_word

tweets=[]
for i in range(0,91298):
    tweets.append(tok(str(train['tweet'].iloc[i])))
    