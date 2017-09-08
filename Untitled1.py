
# coding: utf-8

# In[2]:

path='F:/timeseries/indian_prison/'


# In[3]:

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:

import os
os.chdir(path)


# In[5]:


age=pd.read_csv('Age_group.csv')
caste=pd.read_csv('Caste.csv')
death=pd.read_csv('Death_sentence.csv')
edu=pd.read_csv('Education.csv')
ed_fac=pd.read_csv('Education_facilities.csv')


# In[9]:

age.keys()


# In[15]:

states=age[['state_name','age_16_18']].groupby('state_name').sum()


# In[17]:

states.to_csv('states_ab.csv')


# In[18]:

state_ab=pd.read_csv('states_ab.csv')


# In[19]:

state_ab.keys()


# In[21]:

age2=pd.merge(age,state_ab,how='left',left_on=['state_name'], right_on=['state_name'])


# In[23]:

age2.head()


# In[38]:

headd=lambda x:x.head(5)


# In[39]:

names=[age2,caste,edu,death,ed_fac]
for each in names:
    print ('###########')
    print headd(each)


# In[ ]:



