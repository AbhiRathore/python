import requests
import re 
import urllib2
import csv
import json
from requests import *
import xml.etree.ElementTree as ET

def writetocsv(toCSV_dict):
    keys = toCSV_dict[0].keys()
    with open('D:\enitity\crayon_newpartner.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)


auth_token="4a984c8696a8bacccc06c12e856c0618"
url="https://api.ocbc.com:8243/Card_Rewards/1.0?limit=100"
req=urllib2.Request(url, None, {"Authorization": "Bearer %s" %auth_token})
response=urllib2.urlopen(req)
html=response.read()
json_obj=json.loads(html)
json_reward=json_obj['rewards']
masterdict=[]
import pdb;pdb.set_trace()
for obj in json_reward:
    #print(obj)
    dict1={}
    dict1['category']=obj['category'].encode('utf-8').strip()
    dict1['redemptionItem']=obj['redemptionItem'].encode('utf-8').strip()
    dict1['merchantName']=obj['merchantName'].encode('utf-8').strip()
    dict1['price']=obj['price']
    dict1['instruction']=obj['instruction']
    dict1['outlets']=obj['outlets']
    dict1['merchantDesc']=obj['merchantDesc'].encode('utf-8').strip()
    dict1['terms']=obj['terms']
    dict1['image']=obj['image'].encode('utf-8').strip()
    dict1['validityDate']=obj['validityDate'].encode('utf-8').strip()
    masterdict.append(dict1)
cont=json.dumps(masterdict)
print(cont)
writetocsv(masterdict)




