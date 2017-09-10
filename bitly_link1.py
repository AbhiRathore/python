
# coding: utf-8

# In[7]:

import os
import sys
import pandas as pd
import csv
import requests


access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
#longUrl="http%3A%2F%2Fgoogle.com%2F"
#longUrl="http://diningoffers.smartbuy.brewfer.com/hdfc/webapp/listing/restaurantlist?searchcity=24&searcharea=&id=&restdetail=&restcat=&searchres=Search"
path='D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/update_offers_25july/'
urls=pd.read_csv(path + "nb_offused_7aug1.csv")
print urls.head(5)
def converter(url):
    access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
    address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
    url3= address+"longUrl"+"="+str(url)+"&format=json"
    aa = requests.get(url3).json()
    return  aa["data"]["url"]

def converter2(url):
    url1=re.sub('[?]','%3F',re.sub('[&]','%26',re.sub('[=]','%3D',url)))
    access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
    address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
    url3= address+"longUrl"+"="+str(url1)+"&format=json"
    aa = requests.get(url3).json()
    return  aa["data"]["url"]


# In[8]:

urls.keys()


# In[9]:

urls.shape


# In[17]:

def converter2(url):
    import re
    import requests
    url1=re.sub('[?]','%3F',re.sub('[&]','%26',re.sub('[=]','%3D',url)))
    access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
    address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
    url3= address+"longUrl"+"="+str(url1)+"&format=json"
    aa = requests.get(url3).json()
    return  aa["data"]["url"]


# In[11]:

urls['deal_url'].head()


# In[15]:

urls.shape[0]


# In[13]:

path


# In[18]:


converter2(urls['deal_url'].iloc[61])


# In[19]:

s=0
bitly=[]
import re
for i in range(0,urls.shape[0]):
    try :
        bitly.append(converter2(str(urls['deal_url'].iloc[i])))
        #print urls['Offer_link'].iloc[i]
    except:
        bitly.append('')
    #print "current link" + str(i)
#print bitly



# In[20]:

urls['bitly']=bitly
urls.to_csv(path + "nb_offused_7aug2.csv")


# In[ ]:




# In[5]:

turl='http://diningoffers.smartbuy.brewfer.com/hdfc/?searchcity=6&searcharea=&id=&restdetail=&restcat=&searchres=Search'


# In[4]:

converter('http://diningoffers.smartbuy.brewfer.com/hdfc/?searchcity=6&searcharea=&id=&restdetail=&restcat=&searchres=Search')


# In[13]:

import re
turl2=re.sub('[?]','%3F',re.sub('[&]','%26',re.sub('[=]','%3D',turl)))


# In[14]:

converter(turl2)


# In[16]:

converter2(turl)


# In[17]:

turl3='https://offers.smartbuy.hdfcbank.com/offer_details/38596'


# In[18]:

converter2(turl3)


# In[ ]:



