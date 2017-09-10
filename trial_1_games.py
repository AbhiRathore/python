
# coding: utf-8

# In[1]:

import pandas as pd
import nltk
from nltk import *
import csv


# In[2]:

path="D:/games/final_data/reviews/"


# In[3]:

game1=pd.read_csv(path+'tera_final.csv')


# In[54]:

t=0
for review in game1['review']:
    t=4


# In[55]:

r="Many complain about the quests, but most can be completely ignored if you don't like them, just go bash mobs, and collect the rewards from the repeatable quests for doing so from the UI, rather than a NPC. As you level up mobs will drop shards that will give you some very nice weapons appropriate for your level. The repeatable quests you can get rewards for from the UI also give you tokens you can exchange for armour, and accessories, as well as provide you with crystals for your equipment. Result of this is that gearing up a levelling character is very easy, the equipment grind is just at end-game, and by the time you get there, which doesn't take too long, you'll know if that's a class you want to invest in. That's some examples of the kind of changes they've made to the game for the better."


# In[56]:

for each in nltk.pos_tag(nltk.word_tokenize(r)):
    if each[1] in ("JJ","JJR","JJS"):
        print each[0],sid.polarity_scores(each[1])


# In[22]:

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


# In[50]:

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
wordnet_lemmatizer.lemmatize('dogs')
from nltk.stem.rslp import RSLPStemmer


# In[47]:

from nltk.stem.lancaster import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer("english")


# In[118]:



for each in r.split(" "):
    print lancaster_stemmer.stem(each),each,snowball_stemmer.stem(each),wordnet_lemmatizer.lemmatize(each),porter_stemmer.stem(each)


# In[104]:

sent=" the boy knew what to do then"


# In[109]:

for w in sent.split(" "):
    if w not in [stop,'then']:
        print w


# In[ ]:




# In[ ]:




# In[ ]:




# In[106]:

stop


# In[101]:

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))


# In[114]:

porter_stemmer.stem('eaten'),nltk.pos_tag(nltk.word_tokenize("walked"))


# In[100]:

lancaster_stemmer.stem('eat')


# In[ ]:




# In[92]:

snowball_stemmer.stem('ate'),nltk.pos_tag(nltk.word_tokenize("repeatable"))


# In[115]:

lancaster_stemmer.stem('eaten'),nltk.pos_tag(nltk.word_tokenize("repeatable"))


# In[66]:

lancaster_stemmer.stem('repeatable'),porter_stemmer.stem('repeatable')


# In[67]:

from nltk.stem.api import StemmerI
from nltk.stem.regexp import RegexpStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.isri import ISRIStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.rslp import RSLPStemmer


# In[42]:

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
porter_stemmer.stem('eaten')


# In[ ]:




# In[35]:

wordnet_lemmatizer.lemmatize('walk')


# In[16]:

nltk.pos_tag(nltk.word_tokenize(r))


# In[29]:

nltk.download()


# In[1]:

import re


# In[37]:




# In[38]:

pin=[]
pincode=[]
for each in addd.split():
    try:
        pin = each[re.search("\\d{6}",each).start():re.search("\\d{6}",each).end()]
        if len(pin) ==6:
            pincode.append(pin)
    except:
        pin=''
print pincode


# In[ ]:



