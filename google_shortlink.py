
# coding: utf-8

# In[13]:

import requests
import json
from time import sleep
API_KEY='AIzaSyA47WYUjfwugTdJLifhFMR8ktTHG5pYBUg'
def shorten_url(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={}'.format(API_KEY)
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    p=r.json()
    sleep(1)
    return p['id']


# In[18]:

url1='https://medium.com/the-mission/why-successful-people-spend-10-hours-a-week-on-compound-time-79d64d8132a8'


# In[19]:

shorten_url(url1)


# In[16]:

3500000/3600


# In[17]:

972/24


# In[ ]:



