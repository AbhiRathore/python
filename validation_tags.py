
# coding: utf-8

# In[1]:

#retail tags
from StringIO import StringIO  
retail='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=0&single=true&output=csv'
import requests
import pandas as pd
r = requests.get(retail)
data = r.content
retail_data = pd.read_csv(StringIO(data))
ret_tags=[]
for tag in retail_data['total_tags2']:
    tag1=tag.split(',')
    for each in tag1:
        ret_tags.append(each.strip())
    
retail_tags=set(ret_tags)



# In[2]:

# dining tags
from StringIO import StringIO  
dining='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=1948946144&single=true&output=csv'
import requests
d = requests.get(dining)
data = d.content
dining_data = pd.read_csv(StringIO(data))
din_tags=[]
for tag in dining_data['total_tags2']:
    #print tag
    tag1=tag.split(',')
    for each in tag1:
        din_tags.append(each.strip())
    
dining_tags=set(din_tags)



# In[3]:

#personal service provider tags
from StringIO import StringIO  
psp='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=2075785202&single=true&output=csv'
import requests
p = requests.get(psp)
data = p.content
psp_data = pd.read_csv(StringIO(data))

psp_tags=[]
for tag in psp_data['total_tags2']:
    try:
        tag1=tag.split(',')
        for each in tag1:
            psp_tags.append(each.strip())
    except:
        t=4
    
psp_tags=set(psp_tags)


# In[ ]:

# travel tags
from StringIO import StringIO  
travel='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=0&single=true&output=csv'
import requests
r = requests.get(travel)
data = r.content
retail_data = pd.read_csv(StringIO(data))


# In[50]:

# all tags tab from all tags tab in nearbuy
all_tags='https://docs.google.com/spreadsheets/d/15OuhrMxE4t8IloFN8eLL6q4nQy_akVVyp0hs_cvsfdM/pub?gid=523656085&single=true&output=csv'
from StringIO import StringIO  
import requests
r = requests.get(all_tags)
data = r.content
alltags_data = pd.read_csv(StringIO(data),header=0)


all_tagss=[]
for tag in alltags_data['all_tags']:
    try:
        tag1=tag.split(',')
        for each in tag1:
            all_tagss.append(each.strip())
    except:
        t=4
    
all_tagss=set(all_tagss)



# In[37]:

alltags_data.keys()


# In[ ]:

# mstore tags
from StringIO import StringIO  
mstore='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=0&single=true&output=csv'
import requests
r = requests.get(retail)
data = r.content
retail_data = pd.read_csv(StringIO(data))


# In[ ]:

# entertainment
from StringIO import StringIO  
enter='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=0&single=true&output=csv'
import requests
r = requests.get(retail)
data = r.content
retail_data = pd.read_csv(StringIO(data))


# In[4]:

# apparel
from StringIO import StringIO  
apparel='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=383697026&single=true&output=csv'
import requests
a = requests.get(apparel)
data = a.content
apparel_data = pd.read_csv(StringIO(data))

app_tags=[]
for tag in apparel_data['total_tags2']:
    tag1=tag.split(',')
    for each in tag1:
        app_tags.append(each.strip())
    
apparal_tags=set(app_tags)


# In[5]:

total_tag=apparal_tags.union(retail_tags)


# In[6]:

total_tags=total_tag.union(dining_tags)


# In[7]:

total_tags2=total_tags.union(psp_tags)


# In[13]:

from autocorrect import spell
for word in total_tags2:
    for each in word.split(' '):
        w=spell(each)
        if w != each:
            print w + " :correct ",each + " :incorrect"
        else:
            t=5


# In[310]:

ret_tags=[]
for tag in retail_data['total_tags']:
    tag1=tag.split(',')
    for each in tag1:
        ret_tags.append(each)
    
retail_tags=set(ret_tags)



# In[8]:

import nltk
from nltk import *


# In[306]:

ret_tags=[]
for tag in retail_data['total_tags']:
    tag1=tag.split(',')
    for each in tag1:
        ret_tags.append(each)import nltk
from nltk import *
    
retail_tags=set(ret_tags)



# In[ ]:

urls='https://docs.google.com/spreadsheets/d/1Sk39eQtBL-yIvkgzZvtKE-NeixK2-dh47RjqY6StgoQ/edit?ts=5952a211#gid=0'


# In[56]:

d = {'id' : [1, 2, 3,4 ],
      'tags' : [" airlines,bakery,accepts applepay, random,random2", " airlines,bakery,accepts applepay, random,random2", 
                " airlines,bakery,accept applepay, random,random2", " airlines,bakery,accepts applepy, random,random2"]}


# In[49]:

import pandas as pd


# In[496]:

#nearbuy
from StringIO import StringIO  # got moved to io in python3.
import requests
n = requests.get('https://docs.google.com/spreadsheets/d/15OuhrMxE4t8IloFN8eLL6q4nQy_akVVyp0hs_cvsfdM/pub?gid=1130467823&single=true&output=csv')
dat = n.content
nb = pd.read_csv(StringIO(dat))


# In[60]:

#instore
#nearbuy
from StringIO import StringIO  # got moved to io in python3.
import requests
instore='https://docs.google.com/spreadsheets/d/15OuhrMxE4t8IloFN8eLL6q4nQy_akVVyp0hs_cvsfdM/pub?gid=498541021&single=true&output=csv'
instr = requests.get(instore)
daat = instr.content
nb_instore = pd.read_csv(StringIO(daat))


# In[11]:

beauty='https://docs.google.com/spreadsheets/d/15OuhrMxE4t8IloFN8eLL6q4nQy_akVVyp0hs_cvsfdM/pub?gid=1541825466&single=true&output=csv'
#nearbuy
from StringIO import StringIO  # got moved to io in python3.
import requests
n_beauty = requests.get(beauty)
dat3 = n_beauty.content
nb_beauty = pd.read_csv(StringIO(dat3))


# In[13]:

spa='https://docs.google.com/spreadsheets/d/15OuhrMxE4t8IloFN8eLL6q4nQy_akVVyp0hs_cvsfdM/pub?gid=1130467823&single=true&output=csv'

#nearbuy
from StringIO import StringIO  # got moved to io in python3.
import requests
n_spa = requests.get(spa)
dat_spa = n_spa.content
nb_spa = pd.read_csv(StringIO(dat_spa))


# In[57]:

#wrong_id=[]
cat1=[]
for index, row in nb_instore.iterrows():
    wrong=[]
    #print row['id'],row['tags']
    try:
        for u  in  row['tags'].split(','):
            if u.strip()   in all_tagss:
                r=2
            else:
                wrong.append(u)
                #r=2
        if len(wrong) > 0:
            print "cat:" + row['category'] + " " + "id:"+ str(row['cid']),";"+ "wrongtags:" + str(wrong)
            cat1.append(row['category'])

    except:
        y=2
    
        #print "tag is not here"
print set(cat1)


# In[15]:

#wrong_id=[]
cat1=[]
for index, row in nb_beauty.iterrows():
    wrong=[]
    #print row['id'],row['tags']
    try:
        for u  in  row['tags'].split(','):
            if u.strip()   in total_tags2:
                r=2
            else:
                wrong.append(u)
                #r=2
        if len(wrong) > 0:
            print "cat:" + row['category'] + " " + "id:"+ str(row['cid']),";"+ "wrongtags:" + str(wrong)
            cat1.append(row['category'])

    except:
        y=2
    
        #print "tag is not here"
print set(cat1)


# In[ ]:




# In[14]:

#wrong_id=[]
cat1=[]
for index, row in nb_spa.iterrows():
    wrong=[]
    #print row['id'],row['tags']
    try:
        for u  in  row['tags'].split(','):
            if u.strip()   in total_tags2:
                r=2
            else:
                wrong.append(u)
                #r=2
        if len(wrong) > 0:
            print "cat:" + row['category'] + " " + "id:"+ str(row['cid']),";"+ "wrongtags:" + str(wrong)
            cat1.append(row['category'])

    except:
        y=2
    
        #print "tag is not here"
print set(cat1)


# In[54]:

#smart buy
from StringIO import StringIO  # got moved to io in python3.
import requests
ur1='https://docs.google.com/spreadsheets/d/1Sk39eQtBL-yIvkgzZvtKE-NeixK2-dh47RjqY6StgoQ/pub?gid=0&single=true&output=csv'
ur='https://docs.google.com/spreadsheets/d/1Sk39eQtBL-yIvkgzZvtKE-NeixK2-dh47RjqY6StgoQ/pub?gid=0&single=true&output=csv'
ur2='https://docs.google.com/spreadsheets/d/1Sk39eQtBL-yIvkgzZvtKE-NeixK2-dh47RjqY6StgoQ/pub?gid=1916985649&single=true&output=csv'
#r = requests.get('https://docs.google.com/spreadsheets/d/15OuhrMxE4t8IloFN8eLL6q4nQy_akVVyp0hs_cvsfdM/pub?output=csv')
sb_data=requests.get(ur2)
data_sb = sb_data.content
sb = pd.read_csv(StringIO(data_sb))


# In[547]:

sb_online='https://docs.google.com/spreadsheets/d/1Sk39eQtBL-yIvkgzZvtKE-NeixK2-dh47RjqY6StgoQ/pub?gid=915083041&single=true&output=csv'

#smart buy
from StringIO import StringIO  # got moved to io in python3.
import requests
#r = requests.get('https://docs.google.com/spreadsheets/d/15OuhrMxE4t8IloFN8eLL6q4nQy_akVVyp0hs_cvsfdM/pub?output=csv')
sb_online=requests.get(sb_online)
data_sb_online = sb_online.content
sb_online = pd.read_csv(StringIO(data_sb_online))



# In[548]:

sb_online.head()


# In[513]:

sb = pd.read_csv(StringIO(data_sb))


# In[541]:

total_tags2


# In[504]:

for i in sb[sb['S.no']==577 ]['Tags']:
    print i


# In[351]:

set(df['category'])


# In[237]:

df = pd.read_csv(StringIO(data), index_col=1)


# In[239]:

set(df['category'])


# In[175]:

val_file=pd.read_csv("D:/entity/hdfc_dining28june1.csv")


# In[55]:

#wrong_id=[]
cat1=[]
for index, row in sb.iterrows():
    wrong=[]
    #print row['id'],row['tags']
    try:
        for u  in  row['Tags'].split(','):
            if u.strip()   in total_tags2:
                r=2
            else:
                wrong.append(u)
                #r=2
        if len(wrong) > 0:
            print "cat:" + row['category'] + " " + "id:"+ str(row['S.no']),";"+ "wrongtags:" + str(wrong)
            cat1.append(row['category'])

    except:
        t=8
    
        #print "tag is not here"
print set(cat1)


# In[10]:

#wrong_id=[]
cat1=[]
for index, row in sb_online.iterrows():
    wrong=[]
    #print row['id'],row['tags']
    try:
        for u  in  row['Tags'].split(','):
            if u.strip()   in total_tags2:
                r=2
            else:
                wrong.append(u)
                #r=2
        if len(wrong) > 0:
            print "cat:" + row['Category'] + " " + "id:"+ str(row['OfferID']),";"+ "wrongtags:" + str(wrong)
            cat1.append(row['Category'])

    except:
        t=8
    
        #print "tag is not here"
print set(cat1)


# In[ ]:



