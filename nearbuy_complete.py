
# coding: utf-8

# In[22]:

# total code to be used just change directory and file name to write in csv.Also after writing remove duplicates from csv
import json
import csv
import io
import time 
import requests
import re


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
            data_final_all.append(data2['deals'])
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
                h=2
                #print 'fail'
            N=N+50
            #print N
#print json.dumps(final_data)
#from util import inserted_on,list_to_pipe_sep,convert_list_obj_to_str,convert_desc_to_text
def list_to_pipe_sep(obj, sep=' | '):
    return sep.join(x.strip() for x in obj)

def time_convert(etime):
    htime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(etime))
    return htime
def writetocsv(toCSV_dict):
    keys = toCSV_dict[0].keys()
    with open('D:/nb_2/offer_data2.csv', 'wb') as output_file: ### change the folder and file name as per use
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)
j=[]
for line in data_final_all:
    j.append(json.dumps(line))
for line1 in j:
    line = json.loads(line1)
    print '****************************'
    for deal in line:
        print '####'
        for merchant in deal['merchants']:
            dict1={}
            try :
                dict1['merc_name']=merchant['name'].encode('utf-8').strip()
            except :
                dict1['merc_name']=''
            try :
                dict1['merc_desc']=merchant['merc_desc']
            except :
                dict1['merc_desc']=''
            try :
                dict1['merc_facilities']=merchant['facilities']
            except :
                dict1['merc_facilities']=''
            try :
                dict1['merc_add_city']=merchant['address']['city'].encode('utf-8').strip()
            except :
                dict1['merc_add_city']=''
            try :
                dict1['merc_add_line']=merchant['address']['address_line1'].encode('utf-8').strip()
            except :
                dict1['merc_add_line']=''
            try :
                dict1['merc_add_locality']=merchant['address']['locality'].encode('utf-8').strip()
            except :
                dict1['merc_add_locality']=''
            try :
                dict1['merc_add_country']=merchant['address']['country'].encode('utf-8').strip()
            except :
                dict1['merc_add_country']=''
            try :
                dict1['merc_add_pincode']=merchant['address']['pincode'].encode('utf-8').strip()
            except :
                dict1['merc_add_pincode']=''
            try :
                dict1['merc_add_state']=merchant['address']['state'].encode('utf-8').strip()
            except :
                dict1['merc_add_state']=''
            try :
                dict1['merc_add_lat']=merchant['address']['lat']
            except :
                dict1['merc_add_lat']=''
            try :
                dict1['merc_add_lng']=merchant['address']['lng']
            except :
                dict1['merc_add_lng']=''
            try :
                dict1['merc_add_sub_locality']=merchant['address']['sub_locality']
            except :
                dict1['merc_add_sub_locality']=''
            try :
                dict1['merc_id']=merchant['id']
            except :
                dict1['merc_id']=''
            try :
                dict1['merc_website_url']=merchant['website_url']
            except :
                dict1['merc_website_url']=''
            try :
                dict1['deal_url']=deal['deal_url'].encode('utf-8').strip()
            except :
                dict1['deal_url']=''
            try :
                dict1['is_online_deal']=deal['is_online_deal']
            except :
                dict1['is_online_deal']=''
            try :
                dict1['title']=deal['title'].encode('utf-8').strip()
            except :
                dict1['title']=''
            try :
                dict1['nearest_merchant_distance']=deal['nearest_merchant_distance']
            except :
                dict1['nearest_merchant_distance']=''
            try :
                dict1['starts_on']=time_convert(deal['validity']['starts_on'])
            except :
                dict1['starts_on']=''
            try :
                dict1['ends_on']=time_convert(deal['validity']['ends_on'])
            except :
                dict1['ends_on']=''
            try :
                dict1['deal_id']=deal['id']
            except :
                dict1['deal_id']=''
            try :
                dict1['discount_percent']=deal['price_detail']['discount_percent']
            except :
                dict1['discount_percent']=''
            try :
                dict1['is_mrp_visible']=deal['price_detail']['is_mrp_visible']
            except :
                dict1['is_mrp_visible']=''
            try :
                dict1['mrp']=deal['price_detail']['mrp']
            except :
                dict1['mrp']=''
            try :
                dict1['msp']=deal['price_detail']['msp']
            except :
                dict1['msp']=''
            try :
                dict1['categories_id']=[]
                for cat in deal['categories']:
                    dict1['categories_id'].append(cat['id'])
                    dict1['categories_id']= list_to_pipe_sep(dict1['categories_id'])
            except :
                dict1['categories_id']=''
            try :
                dict1['categories_name']=[]
                for cat in deal['categories']:
                    dict1['categories_name'].append(cat['name'])
                    dict1['categories_name']= list_to_pipe_sep(dict1['categories_name'])
            except :
                dict1['categories_name']=''
            try :
                dict1['sub_categories_id']=[]
                for cat in deal['categories']:
                    if cat['sub_categories']:
                        for sub_cat in cat['sub_categories']:
                            #print sub_cat
                            dict1['sub_categories_id'].append(sub_cat['id'])
                    if sub_cat['sub_sub_categories']:
                        for subb_cat in sub_cat['sub_sub_categories']:
                            dict1['sub_categories_id'].append(subb_cat['id'])
                        dict1['sub_categories_id']= list_to_pipe_sep(dict1['sub_categories_id'])
            except  Exception as e:
                print 'except',e
                dict1['sub_categories_id']=''
            try :
                dict1['sub_categories_name']=[]
                for cat in deal['categories']:
                    if cat['sub_categories']:
                        for sub_cat in cat['sub_categories']:
                            #print sub_cat
                            dict1['sub_categories_name'].append(sub_cat['name'])
                            if sub_cat['sub_sub_categories']:
                                for subb_cat in sub_cat['sub_sub_categories']:
                                    dict1['sub_categories_name'].append(subb_cat['name'])
                                dict1['sub_categories_name']= list_to_pipe_sep(dict1['sub_categories_name'])
            except  Exception as e:
                print 'except',e
                dict1['sub_categories_name']=''
            try :
                dict1['sold_count']=deal['sold_count']
            except :
                dict1['sold_count']=''
            try :
                dict1['img_url']=deal['img_url']
            except :
                dict1['img_url']=''
            try :
                dict1['deal_id']=deal['id']
            except :
                dict1['deal_id']=''
            try :
                dict1['fav_count']=deal['fav_count']
            except :
                dict1['fav_count']=''
            try:
                if len(str(dict1['merc_add_city'])) > 0:
                    dict1['url_2']='https://offers.smartbuy.hdfcbank.com/nearbuy_details/'+ str(dict1['deal_id']) + '/' + str(dict1['merc_add_city']) +'/'
                else:
                    dict1['url_2']='https://offers.smartbuy.hdfcbank.com/nearbuy_details/'+ str(dict1['deal_id']) + '/' + 'pune'
            except:
                t=9
            #print dict1
            array1.append(dict1)
    #print array1
    writetocsv(array1)


# In[ ]:

## just to write a file alone- not to be used
def writetocsv(toCSV_dict):
    keys = toCSV_dict[0].keys()
    with open('D:/nb_2/offer_data3.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)
j=[]
for line in data_final_all:
    j.append(json.dumps(line))
for line1 in j:
    line = json.loads(line1)
    print '****************************'
    print i
    i=i+1
    for deal in line:
        print '####'
        for merchant in deal['merchants']:
            dict1={}
            try :
                dict1['merc_name']=merchant['name'].encode('utf-8').strip()
            except :
                dict1['merc_name']=''
            try :
                dict1['merc_desc']=merchant['merc_desc']
            except :
                dict1['merc_desc']=''
            try :
                dict1['merc_facilities']=merchant['facilities']
            except :
                dict1['merc_facilities']=''
            try :
                dict1['merc_add_city']=merchant['address']['city'].encode('utf-8').strip()
            except :
                dict1['merc_add_city']=''
            try :
                dict1['merc_add_line']=merchant['address']['address_line1'].encode('utf-8').strip()
            except :
                dict1['merc_add_line']=''
            try :
                dict1['merc_add_locality']=merchant['address']['locality'].encode('utf-8').strip()
            except :
                dict1['merc_add_locality']=''
            try :
                dict1['merc_add_country']=merchant['address']['country'].encode('utf-8').strip()
            except :
                dict1['merc_add_country']=''
            try :
                dict1['merc_add_pincode']=merchant['address']['pincode'].encode('utf-8').strip()
            except :
                dict1['merc_add_pincode']=''
            try :
                dict1['merc_add_state']=merchant['address']['state'].encode('utf-8').strip()
            except :
                dict1['merc_add_state']=''
            try :
                dict1['merc_add_lat']=merchant['address']['lat']
            except :
                dict1['merc_add_lat']=''
            try :
                dict1['merc_add_lng']=merchant['address']['lng']
            except :
                dict1['merc_add_lng']=''
            try :
                dict1['merc_add_sub_locality']=merchant['address']['sub_locality']
            except :
                dict1['merc_add_sub_locality']=''
            try :
                dict1['merc_id']=merchant['id']
            except :
                dict1['merc_id']=''
            try :
                dict1['merc_website_url']=merchant['website_url']
            except :
                dict1['merc_website_url']=''
            try :
                dict1['deal_url']=deal['deal_url'].encode('utf-8').strip()
            except :
                dict1['deal_url']=''
            try :
                dict1['is_online_deal']=deal['is_online_deal']
            except :
                dict1['is_online_deal']=''
            try :
                dict1['title']=deal['title'].encode('utf-8').strip()
            except :
                dict1['title']=''
            try :
                dict1['nearest_merchant_distance']=deal['nearest_merchant_distance']
            except :
                dict1['nearest_merchant_distance']=''
            try :
                dict1['starts_on']=time_convert(deal['validity']['starts_on'])
            except :
                dict1['starts_on']=''
            try :
                dict1['ends_on']=time_convert(deal['validity']['ends_on'])
            except :
                dict1['ends_on']=''
            try :
                dict1['deal_id']=deal['id']
            except :
                dict1['deal_id']=''
            try :
                dict1['discount_percent']=deal['price_detail']['discount_percent']
            except :
                dict1['discount_percent']=''
            try :
                dict1['is_mrp_visible']=deal['price_detail']['is_mrp_visible']
            except :
                dict1['is_mrp_visible']=''
            try :
                dict1['mrp']=deal['price_detail']['mrp']
            except :
                dict1['mrp']=''
            try :
                dict1['msp']=deal['price_detail']['msp']
            except :
                dict1['msp']=''
            try :
                dict1['categories_id']=[]
                for cat in deal['categories']:
                    dict1['categories_id'].append(cat['id'])
                    dict1['categories_id']= list_to_pipe_sep(dict1['categories_id'])
            except :
                dict1['categories_id']=''
            try :
                dict1['categories_name']=[]
                for cat in deal['categories']:
                    dict1['categories_name'].append(cat['name'])
                    dict1['categories_name']= list_to_pipe_sep(dict1['categories_name'])
            except :
                dict1['categories_name']=''
            try :
                dict1['sub_categories_id']=[]
                for cat in deal['categories']:
                    if cat['sub_categories']:
                        for sub_cat in cat['sub_categories']:
                            #print sub_cat
                            dict1['sub_categories_id'].append(sub_cat['id'])
                    if sub_cat['sub_sub_categories']:
                        for subb_cat in sub_cat['sub_sub_categories']:
                            dict1['sub_categories_id'].append(subb_cat['id'])
                        dict1['sub_categories_id']= list_to_pipe_sep(dict1['sub_categories_id'])
            except  Exception as e:
                print 'except',e
                dict1['sub_categories_id']=''
            try :
                dict1['sub_categories_name']=[]
                for cat in deal['categories']:
                    if cat['sub_categories']:
                        for sub_cat in cat['sub_categories']:
                            #print sub_cat
                            dict1['sub_categories_name'].append(sub_cat['name'])
                            if sub_cat['sub_sub_categories']:
                                for subb_cat in sub_cat['sub_sub_categories']:
                                    dict1['sub_categories_name'].append(subb_cat['name'])
                                dict1['sub_categories_name']= list_to_pipe_sep(dict1['sub_categories_name'])
            except  Exception as e:
                print 'except',e
                dict1['sub_categories_name']=''
            try :
                dict1['sold_count']=deal['sold_count']
            except :
                dict1['sold_count']=''
            try :
                dict1['img_url']=deal['img_url']
            except :
                dict1['img_url']=''
            try :
                dict1['deal_id']=deal['id']
            except :
                dict1['deal_id']=''
            try :
                dict1['fav_count']=deal['fav_count']
            except :
                dict1['fav_count']=''
            #print dict1
            array1.append(dict1)
    #print array1
    writetocsv(array1)


# In[23]:

import json
import csv
import io
import time 
import requests
import re

path='D:/nb_2/offer_data_try.csv'
## just to write a file alone- not to be used
def writetocsv(toCSV_dict):
    keys = toCSV_dict[0].keys()
    with open(path, 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)
i=1
f = open('D:/nb_2/data_total_all2.txt','r')
data1 = f.readlines()
print data1
array1=[]
for line1 in data1:
    line = json.loads(line1)
    #print '****************************'
    #print i
    i=i+1
    for deal in line:
        #print '####'
        for merchant in deal['merchants']:
            dict1={}
            try :
                dict1['merc_name']=merchant['name'].encode('utf-8').strip()
            except :
                dict1['merc_name']=''
            try :
                dict1['merc_desc']=merchant['merc_desc']
            except :
                dict1['merc_desc']=''
            try :
                dict1['merc_facilities']=merchant['facilities']
            except :
                dict1['merc_facilities']=''
            try :
                dict1['merc_add_city']=merchant['address']['city'].encode('utf-8').strip()
            except :
                dict1['merc_add_city']=''
            try :
                dict1['merc_add_line']=merchant['address']['address_line1'].encode('utf-8').strip()
            except :
                dict1['merc_add_line']=''
            try :
                dict1['merc_add_locality']=merchant['address']['locality'].encode('utf-8').strip()
            except :
                dict1['merc_add_locality']=''
            try :
                dict1['merc_add_country']=merchant['address']['country'].encode('utf-8').strip()
            except :
                dict1['merc_add_country']=''
            try :
                dict1['merc_add_pincode']=merchant['address']['pincode'].encode('utf-8').strip()
            except :
                dict1['merc_add_pincode']=''
            try :
                dict1['merc_add_state']=merchant['address']['state'].encode('utf-8').strip()
            except :
                dict1['merc_add_state']=''
            try :
                dict1['merc_add_lat']=merchant['address']['lat']
            except :
                dict1['merc_add_lat']=''
            try :
                dict1['merc_add_lng']=merchant['address']['lng']
            except :
                dict1['merc_add_lng']=''
            try :
                dict1['merc_add_sub_locality']=merchant['address']['sub_locality']
            except :
                dict1['merc_add_sub_locality']=''
            try :
                dict1['merc_id']=merchant['id']
            except :
                dict1['merc_id']=''
            try :
                dict1['merc_website_url']=merchant['website_url']
            except :
                dict1['merc_website_url']=''
            try :
                dict1['deal_url']=deal['deal_url'].encode('utf-8').strip()
            except :
                dict1['deal_url']=''
            try :
                dict1['is_online_deal']=deal['is_online_deal']
            except :
                dict1['is_online_deal']=''
            try :
                dict1['title']=deal['title'].encode('utf-8').strip()
            except :
                dict1['title']=''
            try :
                dict1['nearest_merchant_distance']=deal['nearest_merchant_distance']
            except :
                dict1['nearest_merchant_distance']=''
            try :
                dict1['starts_on']=time_convert(deal['validity']['starts_on'])
            except :
                dict1['starts_on']=''
            try :
             dict1['ends_on']=time_convert(deal['validity']['ends_on'])
            except :
             dict1['ends_on']=''
            try :
             dict1['deal_id']=deal['id']
            except :
             dict1['deal_id']=''
            try :
             dict1['discount_percent']=deal['price_detail']['discount_percent']
            except :
             dict1['discount_percent']=''
            try :
             dict1['is_mrp_visible']=deal['price_detail']['is_mrp_visible']
            except :
             dict1['is_mrp_visible']=''
            try :
             dict1['mrp']=deal['price_detail']['mrp']
            except :
             dict1['mrp']=''
            try :
             dict1['msp']=deal['price_detail']['msp']
            except :
             dict1['msp']=''
            try :
             dict1['categories_id']=[]
             for cat in deal['categories']:
              dict1['categories_id'].append(cat['id'])
             dict1['categories_id']= list_to_pipe_sep(dict1['categories_id'])
            except :
             dict1['categories_id']=''
            try :
             dict1['categories_name']=[]
             for cat in deal['categories']:
                 dict1['categories_name'].append(cat['name'])
                 dict1['categories_name']= list_to_pipe_sep(dict1['categories_name'])
            except :
                dict1['categories_name']=''
            try :
                dict1['sub_categories_id']=[]
                for cat in deal['categories']:
                    if cat['sub_categories']:
                        for sub_cat in cat['sub_categories']:
                            #print sub_cat
                            dict1['sub_categories_id'].append(sub_cat['id'])
                    if sub_cat['sub_sub_categories']:
                        for subb_cat in sub_cat['sub_sub_categories']:
                            dict1['sub_categories_id'].append(subb_cat['id'])
                        dict1['sub_categories_id']= list_to_pipe_sep(dict1['sub_categories_id'])
            except  Exception as e:
                print 'except',e
                dict1['sub_categories_id']=''
            try :
                dict1['sub_categories_name']=[]
                for cat in deal['categories']:
                    if cat['sub_categories']:
                        for sub_cat in cat['sub_categories']:
                            #print sub_cat
                            dict1['sub_categories_name'].append(sub_cat['name'])
                            if sub_cat['sub_sub_categories']:
                                for subb_cat in sub_cat['sub_sub_categories']:
                                    dict1['sub_categories_name'].append(subb_cat['name'])
                                dict1['sub_categories_name']= list_to_pipe_sep(dict1['sub_categories_name'])
            except  Exception as e:
                print 'except',e
                dict1['sub_categories_name']=''
            try :
                dict1['sold_count']=deal['sold_count']
            except :
                dict1['sold_count']=''
            try :
                dict1['img_url']=deal['img_url']
            except :
                dict1['img_url']=''
            try :
                dict1['deal_id']=deal['id']
            except :
                dict1['deal_id']=''
            try :
                dict1['fav_count']=deal['fav_count']
            except :
                dict1['fav_count']=''
            try:
                if len(str(dict1['merc_add_city'])) > 0:
                    dict1['url_2']='https://offers.smartbuy.hdfcbank.com/nearbuy_details/'+ str(dict1['deal_id']) + '/' + str(dict1['merc_add_city']) +'/'
                else:
                    dict1['url_2']='https://offers.smartbuy.hdfcbank.com/nearbuy_details/'+ str(dict1['deal_id']) + '/' + 'pune'
            except:
                t=9

            array1.append(dict1)
            #print array1
    writetocsv(array1)


# In[ ]:




# In[13]:

array1


# In[19]:

import json
import csv
import io
import time 
#from util import inserted_on,list_to_pipe_sep,convert_list_obj_to_str,convert_desc_to_text
def list_to_pipe_sep(obj, sep=' | '):
    return sep.join(x.strip() for x in obj)

def time_convert(etime):
    htime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(etime))
    return htime
def writetocsv(toCSV_dict):
    keys = toCSV_dict[0].keys()
    with open('D:/nb_2/offer_data45.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV_dict)
i=1
f = open('D:/nb_2/data_total_all2.txt','r')
#data1 = f.readlines()
print data1
#data2=json.load(data1)
#print data2
array1=[]
for line1 in data1:
    line = json.loads(line1)
    #print line
    print '****************************'
 


# In[ ]:



