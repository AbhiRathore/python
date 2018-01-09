
# coding: utf-8

# In[2]:


# Importing the Keras libraries and packages
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import argparse
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import os,cv2
os.chdir("E:/baymax/files/train/train")



# In[4]:


train=pd.read_csv("E:/baymax/5c5a5632-d-dl2_csvfiles/train.csv")


# In[17]:


train.head(10)


# In[16]:


train['age_bin']=''
for i in range(len(train)):
    if train['age'][i] >=0 and train['age'][i] < 30:
        train['age_bin'][i] = 'young'
    elif train['age'][i] >= 30 and train['age'][i] < 60:
        train['age_bin'][i] = 'middle'
    elif train['age'][i] >= 60:
        train['age_bin'][i] = 'old'


# In[18]:


encode_columns=train[['age_bin','gender','view_position']]


# In[21]:


from sklearn import preprocessing
le = preprocessing.LabelEncoder()
X_2 = encode_columns.apply(le.fit_transform)
X_2.head()


# In[25]:


enc = preprocessing.OneHotEncoder()
# 2. FIT
enc.fit(X_2)
# 3. Transform
onehotlabels = enc.transform(X_2).toarray()
onehotlabels.shape


# In[28]:


onehotlabels[0]


# In[29]:


image=cv2.imread("scan_0000.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()


# In[30]:


chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
features = []
 
# loop over the image channels
for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    features.extend(hist)
    # plot the histogram
    plt.plot(hist, color = color)
    plt.xlim([0, 256])


# In[42]:


image2=cv2.resize(image,(32,32))


# In[43]:


def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    v = image.reshape(image.shape[0]*image.shape[1]*image.shape[2],1)
    ### END CODE HERE ###
    
    return v


# In[44]:


image3=image2vector(image2)


# In[51]:


image3.shape


# In[52]:


t=np.append(image3,onehotlabels[0])
t=t.reshape(t.shape[0],1)


# In[54]:


t.shape

