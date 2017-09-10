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
urls=pd.read_csv(path + "store_urls.csv")
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

def converter2(url):
    url1=re.sub('[?]','%3F',re.sub('[&]','%26',re.sub('[=]','%3D',url)))
    access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
    address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
    url3= address+"longUrl"+"="+str(url1)+"&format=json"
    aa = requests.get(url3).json()
    return  aa["data"]["url"]
	
urls['OfferLink'].iloc[61]
s=0
bitly=[]
for i in range(0,urls.shape[0]):
    try :
        bitly.append(converter2(str(urls['url'].iloc[i])))
        #print urls['Offer_link'].iloc[i]
    except:
        bitly.append('')
    #print "current link" + str(i)
#print bitly

urls['bitly']=bitly
urls.to_csv(path + "new_offers_store.csv")

-- --------------
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

def converter(url):
    access_token="19bcb938a27443da99f55d8f7400479b2bc4cf46"
    address="https://api-ssl.bitly.com/v3/shorten?access_token="+access_token+"&"
    url3= address+"longUrl"+"="+str(url)+"&format=txt"
    aa = requests.get(url3)
    return  aa.text

	
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

