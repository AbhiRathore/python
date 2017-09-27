# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:59:27 2017

@author: abhishekr
"""
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import seaborn as sns
from sklearn.svm import SVC
import numpy as np
import nltk
import pandas as pd
import os
import pprint
import re
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

## data

# 
train=pd.read_csv("D:/av_tweets_sent/train.csv")
test=pd.read_csv("D:/av_tweets_sent/test.csv")
train['source']='train'
test['source']='test'

    
# TF-IDF
vectorizer = TfidfVectorizer(analyzer="word",tokenizer=None,preprocessor=None,stop_words=None,max_features=5000)
train_data_features = vectorizer.fit_transform(clean_train_reviews)
train_data_features2 = train_data_features.toarray()

### cleaning codes
def tok(tweets):
    b=nltk.word_tokenize(tweets)
    x=Counter(b)
    #z=x.most_common(15)
    y=nltk.pos_tag(x)
    #print y
    stops = ['@','the','an','#',"b'"]
    unwanted = ["RB", "VB", "NNP"]
    meaningful_word = [w[0] for w in y if w[0] not in stops and w[1] not in unwanted and len(w[0]) >2 and len(w[0]) < 6]
    return meaningful_word
#
def review_to_words(raw_review):
    review_text = BeautifulSoup(raw_review).get_text()
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    words = letters_only.lower().split()
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if w not in stops and len(w) >2 and len(w) < 6]
    return " ".join(meaningful_words)

############

# train
num_reviews = train["tweet"].size
sentiment_train = train["label"].values
clean_train_reviews = []
print("cleaning training data...")
for i in range(0, num_reviews):
    clean_train_reviews.append(review_to_words(train['tweet'][i]))
    
clf = MultinomialNB().fit(train_data_features2, sentiment_train)
clf2=SVC().fit(train_data_features2, sentiment_train)




# test data
clean_test_reviews = []
num_reviews = test["tweet"].size
print("cleaning test data...")
for i in range(0, num_reviews):
    clean_test_reviews.append(review_to_words(test['tweet'][i]))
   
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray() 
predict=clf.predict(test_data_features)
predict2=clf2.predict(test_data_features)
test['predict']=predict
test.to_csv("submission1.csv")

