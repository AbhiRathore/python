import nltk
from nltk import *
import urllib2 
import requests
import re
from bs4 import BeautifulSoup
#http://www.metacritic.com/game/pc/world-of-warcraft/user-reviews

req = urllib2.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
response = urllib2.urlopen(req)
the_page = response.read()


url='http://www.metacritic.com/game/pc/world-of-warcraft'
url2='http://www.metacritic.com/game/pc/guild-wars-2'
url3='http://www.metacritic.com/game/pc/tera'
url4='http://www.metacritic.com/game/pc/eve-online-special-edition'
url5='http://www.metacritic.com/game/pc/star-wars-the-old-republic'
url6='http://www.metacritic.com/game/pc/blade-soul'
url7='http://www.metacritic.com/game/pc/black-desert-online'
url8='http://www.metacritic.com/game/pc/star-trek-online'
url9='http://www.metacritic.com/game/pc/archeage'
url10='http://www.metacritic.com/game/pc/rift'


num=[0,1,2,3,4,5,6,7]

num=[0,1,2]
res=[]
for i in num:
    print i
	
	
num=[0,1,2,3,4,5,6,7]
res=[]
res1=[]
j1=[]
k1=[]
import re
for i in num:
    print i
    print '#########################################################################################'
    j=[]
    url='http://www.metacritic.com/game/pc/world-of-warcraft/user-reviews?sort-by=date&num_items=100&page='+str(i)
    print url
    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
    req = urllib2.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib2.urlopen(req)
    the_page = response.read()
    soup = BeautifulSoup(the_page)
    try:
        j=soup.find_all(class_='blurb blurb_expanded')
        o=soup.find_all(class_='review_grade')
        for g in j:
            print g
            e = re.sub("[^a-zA_Z\,.! 0-9: ]","",g)
            j1.append(e)
            
        k=soup.find_all(class_='review_body')
        for d in k:
            t= re.sub("[^a-zA_Z\,.! 0-9: ]","",d)
            ki.append(t)
        print('222222222222222222222')
        #print j
    except:
        #j=soup.find_all(class_='review_body')
        print('444444444444444444444444')
        #print j
    res.append(j)
    res1.append(k)
    #print res
    
    
### FINAL CODE TO BE USED 
########################################################################################
num=[0,1,2,3,4,5,6,7]
res=[]
res1=[]
resp=[]
resp1=[]
j1=[]
k1=[]
#game_name0='http://www.metacritic.com/game/pc/guild-wars-2/user-reviews'

game_name0=url10
game_name=game_name0 + '/user-reviews'
import re
for i in num:
    print i
    print '#########################################################################################'
    j=[]
    url=game_name + '?sort-by=date&num_items=100&page='+str(i)
    print url
    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
    req = urllib2.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib2.urlopen(req)
    the_page = response.read()
    soup = BeautifulSoup(the_page)
    try:
        j=soup.find_all(class_='blurb blurb_expanded')
        o=soup.find_all(class_='review_grade')
        #print j
        for g in j:
            e=re.sub("^[a-zA_Z\,.! 0-9:' ]","",g.text).encode('utf-8').strip()
            print ('in expanded')
            j1.append(e)
    except:
        e=''
    
    try:
        k=soup.find_all(class_='review_body')
        o=soup.find_all(class_='review_grade')
        for d in k:
            t= re.sub("^[a-zA_Z\,.! 0-9:' ]","",d.text).encode('utf-8').strip()
            k1.append(t)
            print('in review body')
    except:
        #j=soup.find_all(class_='review_body')
        t=''
        
    res.append(j1)
    res1.append(k1)
#resp.append(res)
#resp1.append(resp)
    #print res
    
def writetocsv1(toCSV_dict):
    import csv
    keys = toCSV_dict[0].keys()
    name='D:/games/'+url[re.search('game/pc/',url).end():re.search('/user-reviews',url).start()]+'1'+'.csv'
    with open(name,'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)

def writetocsv2(toCSV_dict):
    import csv
    keys = toCSV_dict[0].keys()
    name='D:/games/'+url[re.search('game/pc/',url).end():re.search('/user-reviews',url).start()]+'2'+'.csv'
    with open(name,'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)
    
	

### FINAL CODE TO BE USED --- trial
########################################################################################
num=[0]
res=[]
res1=[]
resp=[]
resp1=[]
j1=[]
j2=[]
k1=[]
k2=[]
#game_name0='http://www.metacritic.com/game/pc/guild-wars-2/user-reviews'

game_name0=url10
game_name=game_name0 + '/user-reviews'
import re
for i in num:
    print i
    print '#########################################################################################'
    j=[]
    url=game_name + '?sort-by=date&num_items=100&page='+str(i)
    print url
    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
    req = urllib2.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib2.urlopen(req)
    the_page = response.read()
    soup = BeautifulSoup(the_page)
    try:
        j=soup.find_all(class_='blurb blurb_expanded')
        o=soup.find_all(class_='review_grade')
        #print j
        for g in j:
            e=re.sub("^[a-zA_Z\,.! 0-9:' ]","",g.text).encode('utf-8').strip()
            print ('in expanded')
            j1.append(e)
        for g in o:
            r=re.sub("^[0-9]","",o.text).encode('utf-8').strip()
            #r=re.sub("^[a-zA_Z\,.! 0-9:' ]","",g.text[re.search('indiv\">',g.text).end():re.search('</div>\n</div>',g.text).start()]).encode('utf-8').strip()
            #url[re.search('game/pc/',url).end():re.search('/user-reviews',url).start()]
            rf=e + '|' + str(r)
            j2.append(rf)
        print j2
    except:
        e=''
    
    try:
        k=soup.find_all(class_='review_body')
        o=soup.find_all(class_='review_grade')
        
        #print o
        for d in k:
            t= re.sub("^[a-zA_Z\,.! 0-9:' ]","",d.text).encode('utf-8').strip()
            k1.append(t)
        for g in o:
            r=re.sub("^[0-9]","",o.text).encode('utf-8').strip()
            #r=re.sub("^[a-zA_Z\,.! 0-9:' ]","",g.text[re.search('indiv\">',g.text).end():re.search('</div>\n</div>',g.text).start()]).encode('utf-8').strip()
            #url[re.search('game/pc/',url).end():re.search('/user-reviews',url).start()]
            rf=e + '|' + str(r)
            print('in review body')
    except:
        #j=soup.find_all(class_='review_body')
        t=''
        
    res.append(j1)
    res1.append(k1)
#resp.append(res)
#resp1.append(resp)
    #print res

j1=[]
j=[]
a=[]
b=[]
c=[]
aa=[]
bb=[]
cc=[]
url_2='http://www.metacritic.com/game/pc/world-of-warcraft/user-reviews?sort-by=date&num_items=100'
req = urllib2.Request(url_2,headers={'User-Agent': 'Mozilla/5.0'})
response = urllib2.urlopen(req)
the_page = response.read()
soup = BeautifulSoup(the_page)
try:
    j=soup.find_all(class_='reviews user_reviews')
    #o=soup.find_all(class_='review_grade')
    #print j
    for each in j:
        a= each.find_all(class_='review_grade')
        b= each.find_all(class_='review_body')
        c= each.find_all(class_='helpful_summary thumb_count')
        for w in a:
            aa.append(re.sub('[^0-9]','',str(w)))
        for w in b:
            bb.append(re.sub("[^a-z A-Z 0-9 \\!?,.\\@\\']","",w.text.encode('utf-8').strip().lower()))
        for w in c:
            cc.append(re.sub("users found this helpful","",re.sub("[^a-z A-Z 0-9 \\!?,.\\@\\']","",w.text.encode('utf-8').strip().lower())))
            
        #e=re.sub("^[a-zA_Z\,.! 0-9:' ]","",g.text).encode('utf-8').strip()
        print ('in expanded')
        #j1.append(e)
except:
    print 'not happening'
        
        
#print j1

len(a),len(b),len(c)

aa=[]
for w in a:
    aa.append(re.sub('[^0-9]','',str(w)))
	
	
re.sub("[^a-z A-Z 0-9 \\!?,.\\@\\']","",b[2].text.encode('utf-8').strip().lower())


aa=[]
for g in c:
    aa.append(re.sub("users found this helpful","",re.sub("[^a-z A-Z 0-9 \\!?,.\\@\\']","",g.text.encode('utf-8').strip().lower())))
	
	
import re
k=[]
for i in range(0,99):
    k.append(re.sub('[^0-9]','',str(a[i])))
	
from gensim.corpora import  WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


resp_1=[]
s=1
reviews={}
for i in range(0,8):
    for each in res[i]:
        review=each
        rid=s
        reviews={'rid':rid,'review':review}
        s=s+1
        resp_1.append(reviews)
    
t='<div class="review_grade">\n<div class="metascore_w user medium game negative indiv">2</div>\n</div>'


re.sub("[^0-9]","",t)

resp_2=[]
s=1
reviewss={}
for i in range(0,8):
    for each in res1[i]:
        revieww=each
        ridd=s
        reviewss={'rid':ridd,'review':revieww}
        s=s+1
        resp_2.append(reviewss)
    
	
	
writetocsv2(resp_2)

writetocsv1(resp_1)


def writetocsv1(toCSV_dict):
    import csv
    keys = toCSV_dict[0].keys()
    name='D:/games/'+url[re.search('game/pc/',url).end():re.search('/user-reviews',url).start()]+'1'+'.csv'
    with open(name,'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)

def writetocsv2(toCSV_dict):
    import csv
    keys = toCSV_dict[0].keys()
    name='D:/games/'+url[re.search('game/pc/',url).end():re.search('/user-reviews',url).start()]+'2'+'.csv'
    with open(name,'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)
		
url[re.search('game/pc/',url).end():re.search('/user-reviews',url).start()]


import re

string = 'This is laughing laugh'

a = re.search(r'\b(laugh)\b', string)
print(a.end())

def writetocsv1(toCSV_dict):
    import csv
    keys = toCSV_dict[0].keys()
    name='D:/games/'+url[re.search('game/pc/',url).end():re.search('/user-reviews',url).start()]+'1'+'.csv'
    with open(name,'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)
		
		
def writetocsv2(toCSV_dict):
    import csv
    keys = toCSV_dict[0].keys()
    name='D:/games/'+url[re.search('game/pc/',url).end():re.search('/user-reviews',url).start()]+'2'+'.csv'
    with open(name,'wb') as output_file:def writetocsv1(toCSV_dict):
    import csv
    keys = toCSV_dict[0].keys()
    name='D:/games/'+url[re.search('game/pc/',url).end():re.search('/user-reviews',url).start()]+'1'+'.csv'
    with open(name,'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)
		
		
rev="If you are looking for a long lasting MMO this is not your game.The pve side is complete banal and braindead that due to the complete and absurd unbalance between the classes create a nasty toxicity.If you are looking for a moba/PvP/ realm vs realm game either this one should be your choice. The game is in a pretty bad aspect in competitive side, to such point is not even fun at all.If you are looking for a long lasting MMO this is not your game.The pve side is complete banal and braindead that due to the complete and absurd unbalance between the classes create a nasty toxicity. If you are looking for a moba/PvP/ realm vs realm game either this one should be your choice. The game is in a pretty bad aspect in competitive side, to such point is not even fun at all. The seasonal class gets so bumped in buffs is a joke to most of the players go for that.There is no freedom of choice as you have your roles assigned and you can't get ur from them. Other than that is just an spamfest from 1 to 0. No strategy no skill. A mobile game that takes thousands of hours (months actually) of brain dead and puking PvE grinding  to get any worth having perfect for RTM bots. If you are thinking in this game: Avoid it. It is not 2012, This is a game that works in Dx9 in 2017 and runs like crap. Not stunning graphics, not fun mechanics. Right now is a no no .â€¦ Expand"

import re
rev=re.sub("^[a-zA_Z\,.! 0-9:' ]","",rev)


from __future__ import print_function
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups



n_samples = 2000
n_features = 1000
n_topics = 10
n_top_words = 20


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()
	
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                   max_features=n_features,
                                   stop_words='english')
								   
								   
								   
								   
tfidf = tfidf_vectorizer.fit(raw_documents=res[0])
tfidf


document_0 = "China has a strong economy that is growing at a rapid pace. However politically it differs greatly from the US Economy."
document_1 = "At last, China seems serious about confronting an endemic problem: domestic violence and corruption."
document_2 = "Japan's prime minister, Shinzo Abe, is working towards healing the economic turmoil in his own country for his view on the future of his people."
document_3 = "Vladimir Putin is working hard to fix the economy in Russia as the Ruble has tumbled."
document_4 = "What's the future of Abenomics? We asked Shinzo Abe for his views"
document_5 = "Obama has eased sanctions on Cuba while accelerating those against the Russian Economy, even as the Ruble's value falls almost daily."
document_6 = "Vladimir Putin is riding a horse while hunting deer. Vladimir Putin always seems so serious about things - even riding horses. Is he crazy?"

all_documents = [document_0, document_1, document_2, document_3, document_4, document_5, document_6]



from __future__ import division
import string
import math

tokenize = lambda doc: doc.lower().split(" ")
def jaccard_similarity(query, document):
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)

def term_frequency(term, tokenized_document):
    return tokenized_document.count(term)

def sublinear_term_frequency(term, tokenized_document):
    count = tokenized_document.count(term)
    if count == 0:
        return 0
    return 1 + math.log(count)

def augmented_term_frequency(term, tokenized_document):
    max_count = max([term_frequency(t, tokenized_document) for t in tokenized_document])
    return (0.5 + ((0.5 * term_frequency(term, tokenized_document))/max_count))

def inverse_document_frequencies(tokenized_documents):
    idf_values = {}
    all_tokens_set = set([item for sublist in tokenized_documents for item in sublist])
    for tkn in all_tokens_set:
        contains_token = map(lambda doc: tkn in doc, tokenized_documents)
        idf_values[tkn] = 1 + math.log(len(tokenized_documents)/(sum(contains_token)))
    return idf_values

def tfidf(documents):
    tokenized_documents = [tokenize(d) for d in documents]
    idf = inverse_document_frequencies(tokenized_documents)
    tfidf_documents = []
    for document in tokenized_documents:
        doc_tfidf = []
        for term in idf.keys():
            tf = sublinear_term_frequency(term, document)
            doc_tfidf.append(tf * idf[term])
        tfidf_documents.append(doc_tfidf)
    return tfidf_documents
def cosine_similarity(vector1, vector2):
    dot_product = sum(p*q for p,q in zip(vector1, vector2))
    magnitude = math.sqrt(sum([val**2 for val in vector1])) * math.sqrt(sum([val**2 for val in vector2]))
    if not magnitude:
        return 0
    return dot_product/magnitude
	
	
tfidf_representation = tfidf(all_documents)
our_tfidf_comparisons = []
for count_0, doc_0 in enumerate(tfidf_representation):
    for count_1, doc_1 in enumerate(tfidf_representation):
        our_tfidf_comparisons.append((cosine_similarity(doc_0, doc_1), count_0, count_1))
		
 from nltk.sentiment.vader import SentimentIntensityAnalyzer
 
 from nltk import tokenize
 
 sid = SentimentIntensityAnalyzer()
 
 
 for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
        print()
		
g=sid.polarity_scores(rev)

g.keys()