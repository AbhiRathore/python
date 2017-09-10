import nltk
from nltk import *
import urllib2 
import requests
import re
from bs4 import BeautifulSoup
#http://www.metacritic.com/game/pc/world-of-warcraft/user-reviews


import requests
import json
import csv


categories=['food-and-drink',
'spa-and-massage',
'beauty-and-salon',
'health',
'fitness',
'movies-and-events',
'hobbies-and-learning',
'activities',
'home-and-auto',
'in-store',
'cash-deals']
geo=[['27.1766701','78.0080745'],['31.6339793','74.8722642'],['19.8761653','75.3433139'],['30.7333148','76.7794179'],
     ['11.0168445','76.9558321'],['30.3164945','78.0321918'],['15.2993265','74.123996'],['28.4594965','77.0266383'],
     ['26.1445169','91.7362365'],['22.7195687','75.8577258'],['26.9124336','75.7872709'],['26.2389469','73.0243094'],
     ['26.449923','80.3318736'],['9.9312328','76.2673041'],['26.8466937','80.946166'],['30.900965','75.8572758'],
     ['28.9844618','77.7064137'],['12.2958104','76.6393805'],['21.1458004','79.0881546'],['11.9138598','79.8144722'],
     ['31.1048145','77.1734033'],['21.1702401','72.8310607'],['24.585445','73.712479'],['22.3071588','73.1812187'],
     ['17.6868159','83.2184815'],['19.0759837','72.8776559'],['13.0826802','80.2707184'],['28.7040592','77.1024902'],
     ['12.9715987','77.5945627'],['22.572646','88.363895'],['18.5204303','73.8567437'],['17.385044','78.486671'],
     ['23.022505','72.5713621']]


#f = open( "D:\entity\ids_singapore.txt", "r" )
data1=[]
final_data=[]
master_data={}

for lat,lon in geo:
    for cat in categories:
        #print lat,lon
        #parameters = {"locality_lat":lat,"locality_lng":lon,"radius":100,"category":cat} '13.067439','80.237617'
        parameters = {"locality_lat":lat,"locality_lng":lon,"radius":100,"category":cat}
        url='https://partner-unlimited.nearbuy.com/deals?partner_id=wJvnsJVVO67ILHKoloEUKx4kvHACKAn8E1JMnfdg'
        response=requests.get(url, headers=headers,params=parameters)
        data = response.json()
        data1.append(data)
        #print len(data['deals'])
        try:
            for i in range(0,len(data['deals'])):
                #print 'i:' + str(i)
                #print len(data['deals'])
                #print data['deals'][i].keys()
                uid= data['deals'][i]['merchants'][0]['id']
                #print data['deals']
                category= data['deals'][i]['categories'][0]['name']
                name= data['deals'][i]['merchants'][0]['name']
                address= data['deals'][i]['merchants'][0]['address']
                try:
                    city= data['deals'][i]['merchants'][0]['address']['city']
                except:
                    city='not available'
                #print name,category,uid,address,city
                master_data={"uid":uid,"name":name,"city":city,"category": category,"address":address}
                final_data.append(master_data)
        except:
            q=2
            #print 'fail'
#print json.dumps(final_data)

'''
import csv
def writetocsv(toCSV_dict):
 keys = toCSV_dict[0].keys()
 with open('D:/entity/nearbuy_complete.csv','wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV_dict)
final_data2=[]
for each in final_data:
    try:
        uid=each['uid']
        name=each['name'].encode('utf-8').strip()
        city=each['city'].encode('utf-8').strip()
        address=each['address']['address_line1'].encode('utf-8').strip()
        locality=each['address']['locality'].encode('utf-8').strip()
    except:
        t=9
    data_dict={"uid":uid,"name":name,"city":city,"address":address,"locality":locality}
    final_data2.append(data_dict)
    writetocsv(final_data2)
    
    #print (type(final_data2[0].keys))
'''


        

e=1
for each in final_data:
    print each
    if e > 5:break
    e=e+1
	
final_data2=[]
for each in final_data:
    try:
        uid=each['uid']
        name=each['name'].encode('utf-8').strip()
        city=each['city'].encode('utf-8').strip()
        address=each['address']['address_line1'].encode('utf-8').strip()
        locality=each['address']['locality'].encode('utf-8').strip()
    except:
        t=9
    data_dict={"uid":uid,"name":name,"city":city,"address":address,"locality":locality}
    final_data2.append(data_dict)
    writetocsv(final_data2)
	
y=0
for each in final_data:
    print each
    y=y+1
    if y > 2:break
	
import csv
def writetocsv(toCSV_dict):
 keys = toCSV_dict[0].keys()
 with open('D:/entity/nearbuy_complete_all2.csv','wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV_dict)
	
final_data2=[]
for each in final_data:
    try:
        uid=each['uid']
        name=each['name'].encode('utf-8').strip()
        try:
            city=each['city'].encode('utf-8').strip()
        except:
            city='NA'
        try:
            address=each['address']['address_line1'].encode('utf-8').strip()
        except:
            address='NA'
        category=each['category'].encode('utf-8').strip()
        try:
            locality=each['address']['locality'].encode('utf-8').strip()
        except:
            locality='NA'
    except:
        print "here"
    data_dict={"uid":uid,"name":name,"city":city,"category":category,"address":address,"locality":locality}
    final_data2.append(data_dict)
    writetocsv(final_data2)
	
data1=[]
data_4=[]
data_final_all=[]
data2=[]
final_data=[]
master_data={}
headers={'x-api-key': 'wJvnsJVVO67ILHKoloEUKx4kvHACKAn8E1JMnfdg'}
#categories=['food-and-drink']
categories=['food-and-drink',
'spa-and-massage',
'beauty-and-salon',
'health',
'fitness',
'movies-and-events',
'hobbies-and-learning',
'activities',
'home-and-auto',
'in-store',
'cash-deals']


geo=[['27.1766701','78.0080745'],['31.6339793','74.8722642'],['19.8761653','75.3433139'],['30.7333148','76.7794179'],
     ['11.0168445','76.9558321'],['30.3164945','78.0321918'],['15.2993265','74.123996'],['28.4594965','77.0266383'],
     ['26.1445169','91.7362365'],['22.7195687','75.8577258'],['26.9124336','75.7872709'],['26.2389469','73.0243094'],
     ['26.449923','80.3318736'],['9.9312328','76.2673041'],['26.8466937','80.946166'],['30.900965','75.8572758'],
     ['28.9844618','77.7064137'],['12.2958104','76.6393805'],['21.1458004','79.0881546'],['11.9138598','79.8144722'],
     ['31.1048145','77.1734033'],['21.1702401','72.8310607'],['24.585445','73.712479'],['22.3071588','73.1812187'],
     ['17.6868159','83.2184815'],['19.0759837','72.8776559'],['13.0826802','80.2707184'],['28.7040592','77.1024902'],
     ['12.9715987','77.5945627'],['22.572646','88.363895'],['18.5204303','73.8567437'],['17.385044','78.486671'],
     ['23.022505','72.5713621']]

#for lat,lon in [['13.067439','80.237617']]:
for lat,lon in geo:
    for cat in categories:
        #print lat,lon
        #parameters = {"locality_lat":lat,"locality_lng":lon,"radius":100,"category":cat} '13.067439','80.237617'
        parameters = {"locality_lat":lat,"locality_lng":lon,"radius":100,"category":cat}
        url='https://partner-unlimited.nearbuy.com/deals?partner_id=wJvnsJVVO67ILHKoloEUKx4kvHACKAn8E1JMnfdg'
        response=requests.get(url, headers=headers,params=parameters)
        data = response.json()
        count_all= data['meta_info']['all_count']
                
        N=0
        while N < (data['meta_info']['all_count']):
            #print N
            parameters2 = {"locality_lat":lat,"locality_lng":lon,"radius":100,"category":cat,"offset":N}
            url2='https://partner-unlimited.nearbuy.com/deals?partner_id=wJvnsJVVO67ILHKoloEUKx4kvHACKAn8E1JMnfdg'
            response2=requests.get(url2, headers=headers,params=parameters2)
            data2 = response2.json()
            #data_final_all.append(data2['deals'])
            #print len(data2['deals'])
            try:
                for i in range(0,len(data2['deals'])):
                    #print len(data2['deals'])
                    #print 'i:' + str(i)
                    #print len(data2['deals'])
                    #print data['deals'][i].keys()
                    uid= data2['deals'][i]['merchants'][0]['id']
                    #print data2['deals'][i]
                    try:
                        category= data2['deals'][i]['categories'][0]['name']
                    except:
                        category='na'
                    #print category
                    name= data2['deals'][i]['merchants'][0]['name']
                    address= data2['deals'][i]['merchants'][0]['address']
                    try:
                        city= data2['deals'][i]['merchants'][0]['address']['city']
                    except:
                        city='online'
                    master_data={"uid":uid,"name":name,"city":city,"category": category,"address":address}
                    #print master_data
                    final_data.append(master_data)
            except:
                print 'fail'
            N=N+50
            #print N
#print json.dumps(final_data)

import requests
ids="2887,37047,35887,34412,14324"
headers={'x-api-key': 'wJvnsJVVO67ILHKoloEUKx4kvHACKAn8E1JMnfdg'}
url='https://partner-unlimited.nearbuy.com/deals/37047?partner_id=wJvnsJVVO67ILHKoloEUKx4kvHACKAn8E1JMnfdg'
#parameters = {"locality_lat":lat,"locality_lng":lon,"radius":100,"category":'food-and-drink'}
parameters = {"deal_id":37047}
response=requests.get(url, headers=headers,params=parameters)
#data = response.json()
data=response.json()

data['deal']['offers'][0]

for lat,lon in [['13.067439','80.237617']]:
    parameters = {"locality_lat":lat,"locality_lng":lon,"radius":100,"category":'food-and-drink'}
    url='https://partner-unlimited.nearbuy.com/deals/6032?partner_id=wJvnsJVVO67ILHKoloEUKx4kvHACKAn8E1JMnfdg'
    response=requests.get(url, headers=headers,params=parameters)
    data = response.json()
    #count_all= data['meta_info']['all_count']
    
	
	
data['meta_info']['all_count']

import json
with open('D:\entity\data_total_all.txt', 'w') as outfile:
    for line in data_final_all:
        json.dump(line, outfile)
        outfile.write('\n')
		
		
def writetocsv(toCSV_dict):
 keys = toCSV_dict[0].keys()
 with open('D:/entity/nearbuy_all.csv','wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV_dict)
	
	
import json
p_dict = {'name': 'Varun', 'age': 20,}

p_json = json.dumps(p_dict) # Outputs JSON STRING #################
p_dict = json.loads(p_json) # Outputs Python Dictionary

f = open('a', 'w')

f.write(p_json + "\n") ########################
