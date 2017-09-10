
In [2]:

# dining tags
import pandas as pd
import requests
from StringIO import StringIO  
dining='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=1948946144&single=true&output=csv'
d = requests.get(dining)
data = d.content
dining_data = pd.read_csv(StringIO(data))
In [158]:

# city
import pandas as pd
import requests
from StringIO import StringIO 
city='https://docs.google.com/spreadsheets/d/1GofFotFrQ2ThkMoUvhkSmlCBzAp2EphJqyXeFqEYy3A/pub?gid=70096510&single=true&output=csv'
c = requests.get(city)
dataa = c.content
city_data = pd.read_csv(StringIO(dataa))
In [152]:

city_data.shape
Out[152]:
(500, 7)
In [96]:

dining_data2=dining_data.head(50)
In [163]:

city_data.head(3)
Out[163]:
merchant	behav_category	counter	,	name	tags2	tags	corrected
0	mcdonaldsf	dining	1	MCDONALD'S F36227 CYPRESS TX	Mcdonald`s	take away,accept cards,breakfast,brunch,lunch,...	take away,accept cards,breakfast,brunch,lunch,...	
1	subway	dining	2	SUBWAY 00016154 SANTA MONICA CA	Subway	take away,kid friendly,affordable,accepts card...	take away,kid friendly,affordable,accepts card...	
2	burgerking	dining	3	BURGER KING #3784 Q07 WAYNESVILLE NC	Burger King	take away,accept cards,breakfast,brunch,lunch,...	take away,accept cards,breakfast,brunch,lunch,...	
In [162]:

city_data['corrected']=''
​
In [160]:

del city_data[' '] # removing extra null column
In [164]:

# final code
for i in range(0,city_data.shape[0]):
    tags=[]
    tags2=[]
    for j in range(0,dining_data.shape[0]):
        try:
            for tag in city_data['tags2'][i].split(','):
                #print tag
                if tag in str(dining_data['original'][j]):
                    tags.append(dining_data['total_tags'][j].encode('utf-8').strip())
                    tags2=set(tags)
        except:
            t=9
    city_data['corrected'][i]= tags2
In [165]:

city_data.to_csv('D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/city_dining_final.csv')
In [156]:

import pandas as pd
city_dining=pd.read_csv('D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/city_dining.csv')
city_dining['corrected'] = ''
# final code
for i in range(0,city_dining.shape[0]):
    tags=[]
    tags2=[]
    for j in range(0,dining_data.shape[0]):
        try:
            for tag in city_dining['tags2'][i].split(','):
                #print tag
                if tag in str(dining_data['original'][j]):
                    tags.append(dining_data['total_tags'][j].encode('utf-8').strip())
                    tags2=set(tags)
        except:
            t=9
    city_dining['corrected'][i]= tags2
In [157]:

city_dining.to_csv('D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/city_dining2.csv')
In [166]:

apparel_tags='https://docs.google.com/spreadsheets/d/16rgpD6Petx9AvO-_kbVMg7gCWK9vEnbX4umqAae5ZKI/pub?gid=383697026&single=true&output=csv'
In [243]:

import pandas as pd
import requests
from StringIO import StringIO  
a = requests.get(apparel_tags)
data = a.content
apparel_data = pd.read_csv(StringIO(data))
In [244]:

## apparels city data
import pandas as pd
import requests
from StringIO import StringIO 
apparel='https://docs.google.com/spreadsheets/d/1GofFotFrQ2ThkMoUvhkSmlCBzAp2EphJqyXeFqEYy3A/pub?gid=1718609643&single=true&output=csv'
r = requests.get(apparel)
data_r = r.content
city_apparel = pd.read_csv(StringIO(data_r))
In [215]:

city_apparel2=city_apparel[1:3]
In [208]:

for i in str(city_apparel2['tags2']).split(","):
    print i
2    clothing store
 women
 girls
 trendy clothing
...
Name: tags2
 dtype: object
In [222]:

city_apparel2['tags2'][1]
Out[222]:
'clothing store, women, men, kids, home decor, affordable price, trendy clothing, chain outlet,  school uniforms, casual wear, party wear, swimwear'
In [242]:

tags=[]
tags2=[]
for j in range(0,apparel_data.shape[0]):
    try:
        for tag in city_apparel2['tags2'][2].split(','):
            #print tag
            if tag.strip() == '':
                y=2 
            else:
                if tag.strip() == apparel_data['original'][j]:
                    print tag
                    tags.append(apparel_data['total_tags'][j].encode('utf-8').strip())
                    tags2=set(tags)
                    print tag + ':' + apparel_data['original'][j] + ':' + apparel_data['total_tags'][j].encode('utf-8').strip()
                    #print tag,(tags2)
                    
    except:
        t=9
print tags2
 
In [247]:

for i in range(0,city_apparel.shape[0]):
    tags=[]
    tags2=[]
    for j in range(0,apparel_data.shape[0]):
        try:
            for tag in city_apparel['tags2'][i].split(','):
                #print tag
                if tag.strip() == '':
                    y=2 
                else:
                    if tag == str(apparel_data['original'][j]):
                                  tags.append(apparel_data['total_tags'][j].encode('utf-8').strip())
                                  tags2=set(tags)
        except:
            t=9
    city_apparel['corrected']=tags2
        

In [246]:

city_apparel['corrected']=''
In [248]:

city_apparel.to_csv('D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/123.csv')
In [250]:

path='D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/Crayon/Crayon/'
fl=pd.read_csv(path+'send_merchant_desc.csv')
In [260]:

f2=fl.head(3)
f2.keys()
Out[260]:
Index([u'MERCHANT_NAME'], dtype='object')
In [378]:

f2['merchant']=''
f2['city']=''
f2['country']=''
C:\Users\abhishekr\AppData\Local\Continuum\Anaconda2\envs\quill\lib\site-packages\ipykernel_launcher.py:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  """Entry point for launching an IPython kernel.
C:\Users\abhishekr\AppData\Local\Continuum\Anaconda2\envs\quill\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  
C:\Users\abhishekr\AppData\Local\Continuum\Anaconda2\envs\quill\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  This is separate from the ipykernel package so we can avoid doing imports until
In [ ]:

​
In [379]:

for index,row in f2.iterrows():
    for s in row['MERCHANT_NAME'].split("\t"):
        f2['merchant']=s[:re.search("\  ",s).end()].strip()
        f2['country']=s[-3:].strip()
        f2['city']=s[re.search("\  ",s[:-2]).end():][:re.search("\  ",s[re.search("\  ",s[:-2]).end():]).end()].strip()
C:\Users\abhishekr\AppData\Local\Continuum\Anaconda2\envs\quill\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  This is separate from the ipykernel package so we can avoid doing imports until
C:\Users\abhishekr\AppData\Local\Continuum\Anaconda2\envs\quill\lib\site-packages\ipykernel_launcher.py:4: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  after removing the cwd from sys.path.
C:\Users\abhishekr\AppData\Local\Continuum\Anaconda2\envs\quill\lib\site-packages\ipykernel_launcher.py:5: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  """
In [268]:

import re
s="BEER & WINE SHOP A2Z  DELHI         IN"
​
In [385]:

f2['merchant'][0]
Out[385]:
'"GANESH"-PLATINUM TOWE Warszawa'
In [275]:

s[:re.search("\  ",s).end()].strip()
Out[275]:
'BEER & WINE SHOP A2Z'
In [ ]:

s[re.search("\  ",s).end():].strip()
In [310]:

re.search("\  ",s).start()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-310-56af567f4ec1> in <module>()
----> 1 re.search("\  ",s[-1]).start()

AttributeError: 'NoneType' object has no attribute 'start'

In [351]:

s[re.search("\  ",s[::-1]).end():].strip()
Out[351]:
'& WINE SHOP A2Z  DELHI         IN'
In [352]:

re.search("\  ",s[::-1]).end()
Out[352]:
4
In [356]:

s[-3:].strip()
Out[356]:
'IN'
In [369]:

r=s[re.search("\  ",s[:-2]).end():]
In [388]:

​
Out[388]:
'"GANESH"-PLATINUM TOWE Warszawa'
In [374]:

r[:re.search("\  ",r).end()].strip()
Out[374]:
'DELHI'
In [387]:

s[re.search("\  ",s[:-2]).end():][:re.search("\  ",s[re.search("\  ",s[:-2]).end():]).end()].strip()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-387-cb0454bceed8> in <module>()
----> 1 s[re.search("\  ",s[:-2]).end():][:re.search("\  ",s[re.search("\  ",s[:-2]).end():]).end()].strip()

AttributeError: 'NoneType' object has no attribute 'end'

In [386]:

s=f2['merchant'][0]
In [390]:

fl.shape[0]
Out[390]:
2195326
In [ ]:

​
