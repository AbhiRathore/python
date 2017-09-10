import urllib2
import requests
import pandas as pd
import csv
import xml.etree.ElementTree as ET
import re
import json

#reading files
c=0
path="D:/enitity/singapore_data.csv"
with open(path,'rb') as csvfile:
    crayon=csv.DictReader(csvfile)
    for row in crayon:
        print(row['address'],row['name'],row['geo'])
        c += 1
        if c == 3:break

f = open( "D:\enitity\ids_singp_smp.txt", "r" )
a = []
for line in f:
    a.append(line)
master_name=[]
master_address=[]
for i in a:
    url1= "http://multicodes.giatamedia.com/webservice/rest/1.0/properties/" + re.sub('[^0-9]',"",i)
    url2="http://ghgml.giatamedia.com/webservice/rest/1.0/items/"+re.sub('[^0-9]',"",i)
    url3="http://ghgml.giatamedia.com/webservice/rest/1.0/factsheets/"+re.sub('[^0-9]',"",i)
    url4="http://ghgml.giatamedia.com/webservice/rest/1.0/texts/en/"+re.sub('[^0-9]',"",i)
    id=str(i)
    


    #url = 'http://multicodes.giatamedia.com/webservice/rest/1.0/properties/p'
    username = 'bhaskar|crayondata.com'
    password = 'hkUrJ2oo'
    l_1=requests.get(url1, auth=(username, password))
    l_2=requests.get(url2, auth=(username, password))
    l_3=requests.get(url3, auth=(username, password))
    l_4=requests.get(url4, auth=(username, password))
    #print l_1
    #print l_2
    #print l_3
    #print l_4
    #import pdb;pdb.set_trace()
    
    root1 = ET.fromstring((l_1.text.encode("utf-8")))
    root1_a=root1[0]
    first= root1.tag
    root2 = ET.fromstring((l_2.text.encode("utf-8")))
    second= root2.tag
    root2_a=root2[0]
    #print root2_a
    #print root2_a.tag
    root3 = ET.fromstring((l_3.text.encode("utf-8")))
    root3_a=root3[0]
    third= root3.tag
    if third != "error":
        #import pdb;pdb.set_trace()
        root4 = ET.fromstring(l_4.text.encode("utf-8"))
        root4_a=root4[0]
        fourth= root4_a
        if fourth == "error":
            #print root3_a[4][0]
            try:
                for section in root3_a[4][0]:
                    fact_master_dict[section.attrib["name"]] = {}
                    for fact in section[0]:
                        fact_attrib = fact.attrib
                        fact_master_dict[section.attrib["name"]][fact_attrib["name"]] = fact[0].text
            except:
                fact_master_dict = {}
                
                    #import pdb;pdb.set_trace()
            #print fact_master_dict
            
            fact_master_dict2 = {}
            try:
                ad = [add.text for add in root1_a.find("addresses").find("address").iter("addressLine")]
                address = ", ".join(ad)
            except:
                address={}
            try:
                latitude=root1_a.find("geoCodes").find("geoCode").find("latitude").text
            except:
                latitude={}
            try:
                email=root1_a.find("emails").find("email").text
            except:
                email={}
            try:
                website=root1_a.find("urls").find("url").text
            except:
                website={}
            try:
                longitude=root1_a.find("geoCodes").find("geoCode").find("longitude").text
            except:
                longitude={}
            try:
                name=root1_a.find("name").text
            except:
                name={}
                
            phone_dict={}
            try:
                for phone in root1_a.find("phones"):
                    phone_attrib=phone.attrib
                    phone_dict[phone_attrib["tech"]]=phone.text
            except:
                phone_dict={}
            
            image=[]
            try:
                images=root2_a.find("images")
                for im in images.findall("image"):
                    typ=im.get("type")
                    image.append(typ)
                imag=",".join(image)
            except:
                imag={}
            master_dict = {"id": id,"name": name,"address": address,"email":email,"website":website,"latitude": latitude,"longitude": longitude,"image": imag,"contact": phone_dict,"factsheet": fact_master_dict,"details": fact_master_dict2}
            #master_dict2.append("name:"+master_dict['name']+" "+"address:"+master_dict['address'])
            master_name.append(master_dict['name'])
            master_address.append(master_dict['address'])

                        
        else:
            #print root4_a[0][0][0]
            #print root4_a[0]
            #print root4_a[0][0][0]



            fact_master_dict = {}
            #print root3_a[4][0]
            try:
                for section in root3_a[4][0]:
                    fact_master_dict[section.attrib["name"]] = {}
                    for fact in section[0]:
                        fact_attrib = fact.attrib
                        fact_master_dict[section.attrib["name"]][fact_attrib["name"]] = fact[0].text
            except:
                fact_master_dict = {}
                
                    #import pdb;pdb.set_trace()
            #print fact_master_dict
            
            fact_master_dict2 = {}
            try:
                for section in root4_a[0][0][0]:
                    fact_master_dict2[section[0].text]= section[1].text
                    #print fact_master_dict2
                    #for title in section:
                        #print title
                        #fact_master_dict2[section[0].text] = {}
                        #tit=section.text
            except:
                fact_master_dict2 = {}
            try:
                ad = [add.text for add in root1_a.find("addresses").find("address").iter("addressLine")]
                address = ", ".join(ad)
            except:
                address={}
            try:
                email=root1_a.find("emails").find("email").text
            except:
                email={}
            try:
                website=root1_a.find("urls").find("url").text
            except:
                website={}
            try:
                latitude=root1_a.find("geoCodes").find("geoCode").find("latitude").text
            except:
                latitude={}
            try:
                longitude=root1_a.find("geoCodes").find("geoCode").find("longitude").text
            except:
                longitude={}
            try:
                name=root1_a.find("name").text
            except:
                name={}
                
            phone_dict={}
            try:
                for phone in root1_a.find("phones"):
                    phone_attrib=phone.attrib
                    phone_dict[phone_attrib["tech"]]=phone.text
            except:
                phone_dict={}
            
            image=[]
            try:
                images=root2_a.find("images")
                for im in images.findall("image"):
                    typ=im.get("type")
                    image.append(typ)
                imag=",".join(image)
            except:
                imag={}
            master_dict = {"id": id,"name": name,"address": address,"email":email,"website":website,"latitude": latitude,"longitude": longitude,"image": imag,"contact": phone_dict,"factsheet": fact_master_dict,"details": fact_master_dict2}
            cont=json.dumps(master_dict)
            #master_dict2.append("name:"+master_dict['name']+" "+"address:"+master_dict['address'])
            master_name.append(master_dict['name'])
            master_address.append(master_dict['address'])

            
    else:
        #import pdb;pdb.set_trace()
        root4 = ET.fromstring(l_4.text.encode("utf-8"))
        root4_a=root4[0]
        fourth= root4_a
        if fourth == "error":
            fact_master_dict2 = {}
            
        else:
            #print root4_a[0][0][0]
            #print root4_a[0]
            #print root4_a[0][0][0]



            fact_master_dict = {}
            #print root3_a[4][0] 
            #import pdb;pdb.set_trace()
            #print fact_master_dict
            
            fact_master_dict2 = {}
            try:
                for section in root4_a[0][0][0]:
                    fact_master_dict2[section[0].text]= section[1].text
                    #print fact_master_dict2
                    #for title in section:
                        #print title
                        #fact_master_dict2[section[0].text] = {}
                        #tit=section.text
            except:
                fact_master_dict2 = {}
            try:
                ad = [add.text for add in root1_a.find("addresses").find("address").iter("addressLine")]
                address = ", ".join(ad)
            except:
                address={}
            try:
                email=root1_a.find("emails").find("email").text
            except:
                email={}
            try:
                website=root1_a.find("urls").find("url").text
            except:
                website={}
            try:
                latitude=root1_a.find("geoCodes").find("geoCode").find("latitude").text
            except:
                latitude={}
            try:
                longitude=root1_a.find("geoCodes").find("geoCode").find("longitude").text
            except:
                longitude={}
            try:
                name=root1_a.find("name").text
            except:
                name={}
                
            phone_dict={}
            try:
                for phone in root1_a.find("phones"):
                    phone_attrib=phone.attrib
                    phone_dict[phone_attrib["tech"]]=phone.text
            except:
                phone_dict={}
            
            image=[]
            try:
                images=root2_a.find("images")
                for im in images.findall("image"):
                    typ=im.get("type")
                    image.append(typ)
                imag=",".join(image)
            except:
                imag={}
            master_dict = {"id": id,"name": name,"address": address,"email":email,"website":website,"latitude": latitude,"longitude": longitude,"image": imag,"contact": phone_dict,"factsheet": fact_master_dict,"details": fact_master_dict2}
            cont=json.dumps(master_dict)
            #master_dict2.append("name:"+master_dict['name']+" "+"address:"+master_dict['address'])
            master_name.append(master_dict['name'])
            master_address.append(master_dict['address'])

for name in master_name:
    print master_name

