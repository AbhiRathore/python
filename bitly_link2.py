
# coding: utf-8

# In[1]:

import os
import sys
import pandas as pd
import csv
import requests


access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
#longUrl="http%3A%2F%2Fgoogle.com%2F"
longUrl="http://diningoffers.smartbuy.brewfer.com/hdfc/webapp/listing/restaurantlist?searchcity=24&searcharea=&id=&restdetail=&restcat=&searchres=Search"
path='D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/'
urls=pd.read_csv(path + "offer_links.csv")
print urls.head(5)
def converter(url):
    access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
    address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
    url3= address+"longUrl"+"="+str(url)+"&format=json"
    aa = requests.get(url3).json()
    return  aa["data"]["url"]
s=0
bitly=[]

u='19bcb938a27443da99f55d8f7400479b2bc4cf46'

'''
access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
url3= address+"longUrl"+"="+str(link_tr)+"&format=json"
#import pdb;pdb.set_trace()
aa = requests.get(url3).json()
print  aa["data"]["url"]
'''


# In[1]:

import os
import sys
import pandas as pd
import csv
import requests


# In[2]:

urls.shape


# In[2]:

def converter(url):
    access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
    address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
    url3= address+"longUrl"+"="+str(url)+"&format=txt"
    aa = requests.get(url3)
    return  aa.text


# In[3]:

for i in range(0,urls.shape[0]):
    try :
        bitly.append(converter(str(urls['offer_link'].iloc[i])))
        #print urls['Offer_link'].iloc[i]
    except:
        bitly.append('')
    #print "current link" + str(i)
#print bitly

urls['bitly_new']=bitly
urls.to_csv(path + "offer_links_bitly.csv")


# In[3]:

converter('http://diningoffers.smartbuy.brewfer.com/hdfc/?searchcity=1&searcharea=&id=&restdetail=&restcat=&searchres=Search')


# In[7]:

def converter2(url):
    import re
    url1=re.sub('[?]','%3F',re.sub('[&]','%26',re.sub('[=]','%3D',url)))
    access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
    address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
    url3= address+"longUrl"+"="+str(url1)+"&format=json"
    aa = requests.get(url3).json()
    return  aa["data"]["url"]


# In[8]:

converter2('http://diningoffers.smartbuy.brewfer.com/hdfc/?searchcity=1&searcharea=&id=&restdetail=&restcat=&searchres=Search')


# In[12]:

converter2('http://www.nearbuy.com/deal-view/37047?utm_source=PartnerRedirect&utm_campaign=WebandApp&utm_medium=Crayondata')


# In[ ]:



