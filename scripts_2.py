# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import absolute_import, division, print_function
import sklearn
import sklearn.manifold
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import seaborn as sns
import numpy as np
import nltk
import scipy
import pandas as pd
import codecs
import glob
import logging
import multiprocessing
import os
import pprint
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords


# 
train=pd.read_csv("D:/av_tweets_sent/train.csv")
test=pd.read_csv("D:/av_tweets_sent/test.csv")
train['source']='train'
test['source']='test'
#train['tweets']=nltk.word_tokenize(train['tweet'])
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

tweets1=[]
for i in range(0,39392):
    tweets1.append(tok(str(test['tweet'].iloc[i])))


train['tweets']=tweets
test['tweets']=tweets1

#####
'''
docs_new = ['OpenGL on the GPU is fast']
X_new_counts = count_vect.fit_transform(docs_new)
X_new_tfidf = tf_transformer.transform(X_new_counts)
predicted = clf.predict(X_new_tfidf)
for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc,train['label']))
'''