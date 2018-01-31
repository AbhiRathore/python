# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 01:02:53 2018

@author: OMR
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import argparse
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
import os,cv2
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


os.chdir("E:/baymax/files/train/train")

train=pd.read_csv("E:/baymax/5c5a5632-d-dl2_csvfiles/train.csv")

test=pd.read_csv("E:/baymax/5c5a5632-d-dl2_csvfiles/test.csv")


def age_bin(x):
    bin=''
    if x >=0 and x < 30:
        bin = 'young'
    elif x >= 30 and x < 60:
        bin = 'middle'
    elif x >= 60:
        bin = 'old'
    return bin

train['age_bin']=train['age'].apply(lambda x: age_bin(x) )

train=train[~train['image_name'].isin(wrong_im)]

encode_columns=train[['age_bin','gender','view_position']]
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
X_2 = encode_columns.apply(le.fit_transform)
X_2.head()
enc = preprocessing.OneHotEncoder()

enc.fit(X_2)

onehotlabels = enc.transform(X_2).toarray()






fname = "scan_00010127.png"
image = np.array(ndimage.imread(fname, flatten=False))
image = np.array(ndimage.imread(image_list[2], flatten=False))

num_px=64
my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((1, num_px*num_px)).T




image=cv2.imread("scan_00010127.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])



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


image3=image2vector(image)

image3.shape


image_list=train.image_name

im_total=[]
wrong_im=[]
for each in image_list:
    image = np.array(ndimage.imread(each, flatten=False))
    try:
        my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((1, num_px*num_px)).T
        im_total.append(my_image/255)

    except:
        wrong_im.append(each)
        pass
    #my_image = scipy.misc.imresize(image, size=(32,32))


t=np.append(image3,onehotlabels[0])
t=t.reshape(t.shape[0],1)

tot=[]
for i in range(len(onehotlabels)):
    t=np.append(im_total[i],onehotlabels[i])
    t=t.reshape(t.shape[0],1)
    tot.append(t)
    
tot2=np.array(tot)   
train_X = tot2.reshape(18577, 512,512, 1) 
train_X = train_X.astype('float32')
train_X = train_X / 255.



tot3=tot2.reshape(tot2.shape[0],tot2.shape[1])

tot2=np.array(im_total)
tot3=tot2.reshape(tot2.shape[0],tot2.shape[1])
tot4 = tot2.reshape(18512, 64,64, 1) 




encode_columns_y=train[['detected']]
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
y_2 = encode_columns_y.apply(le.fit_transform)
y_2.head()
enc = preprocessing.OneHotEncoder()

enc.fit(y_2)

onehotlabels_y = enc.transform(y_2).toarray()

X_train, X_test, y_train, y_test = train_test_split(tot3, y_2, random_state = 0)

train_X,valid_X,train_label,valid_label  = train_test_split(tot3, dummy_y, test_size=0.2,random_state = 13)

train_X=train_X.reshape(train_X.shape[0], 512, 512, 1)
valid_X = valid_X.reshape(valid_X.shape[0], 512, 512, 1)


train_X=train_X.reshape(train_X.shape[0], 64, 64, 1)
valid_X = valid_X.reshape(valid_X.shape[0], 64, 64, 1)
train_X = train_X.astype('float32')
valid_X = valid_X.astype('float32')

train_X /= 255
valid_X /= 255






from sklearn.tree import DecisionTreeClassifier
dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train)
dtree_predictions = dtree_model.predict(X_test)

from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.svm import LinearSVC

model = SVC()
model.fit(X_train, y_train)

predicted = model.predict(X_test)

model = LinearSVC(penalty='l2',multi_class='ovr')
model.fit(X_train, y_train)

predicted = model.predict(X_test)
accuracy_score(y_test,predicted)

accuracy_score(y_test,dtree_predictions)

from skmultilearn.problem_transform import LabelPowerset
from sklearn.naive_bayes import GaussianNB

# initialize binary relevance multi-label classifier
# with a gaussian naive bayes base classifier
classifier = LabelPowerset(LinearSVC())

# train
classifier.fit(train_X, train_label)

# predict
predictions = classifier.predict(valid_X)
accuracy_score(valid_label,predictions)




from sklearn.metrics import accuracy_score
accuracy_score(y_test,predictions)


##
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import (RandomTreesEmbedding, RandomForestClassifier,
                              GradientBoostingClassifier)

from sklearn.multiclass import OutputCodeClassifier

classifier=OutputCodeClassifier(GradientBoostingClassifier(max_depth=5,n_estimators=14), code_size=2, random_state=0)

classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)
accuracy_score(y_test,predictions)












# creating a confusion matrix
cm = confusion_matrix(y_test, dtree_predictions)




### test data
test['age_bin']=test['age'].apply(lambda x: age_bin(x) )

test=test[~test['image_name'].isin(wrong_im_test)]


encode_columns_test=test[['age_bin','gender','view_position']]
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
X_test = encode_columns_test.apply(le.fit_transform)
X_test.head()
enc = preprocessing.OneHotEncoder()

enc.fit(X_test)

onehotlabels_test = enc.transform(X_test).toarray()

image_list_test=test.image_name

im_total_test=[]
for each in image_list_test:
    image = ndimage.imread(fname, flatten=False)
    my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((1, num_px*num_px)).T
    im_total_test.append(my_image/255)

tp='E:/baymax/files/dl2_teimages/test/'
im_total_test=[]
wrong_im_test=[]
for each in image_list_test:
    image = np.array(ndimage.imread(tp+each, flatten=False))
    try:
        my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((1, num_px*num_px)).T
        im_total_test.append(my_image/255)

    except:
        wrong_im_test.append(each)
        pass
    
    
imt=np.array(ndimage.imread(tp+'scan_00013264.png',flatten=False))
#t=np.append(image3,onehotlabels[0])
#t=t.reshape(t.shape[0],1)

tot_test=[]
for i in range(len(onehotlabels_test)):
    t=np.append(im_total_test[i],onehotlabels_test[i])
    t=t.reshape(t.shape[0],1)
    tot_test.append(t)
    
tot2_test=np.array(im_total_test)   
 
tot3_test=tot2_test.reshape(tot2_test.shape[0],tot2_test.shape[1])

ts_X = tot3_test.reshape(tot3_test.shape[0], 64, 64, 1)

ts_X = ts_X.astype('float32')
ts_X /= 255

dtree_predictions2 = dtree_model.predict(tot3_test)
dtree_predictions2 = classifier.predict(tot3_test)

i=le.inverse_transform(dtree_predictions2)

sub1=pd.DataFrame(test['row_id'])
sub1['detected']=list(i)

sub1=sub1.reset_index()

sub1.to_csv('sub1.csv')




## trying keras
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline



# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(encode_columns_y)
encoded_Y = encoder.transform(encode_columns_y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)


# define baseline model
def baseline_model():
	# create model
    model = Sequential()
    model.add(Dense(8, input_dim=4096, activation='relu'))
    model.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
    model.add(Dense(14, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

model.fit(tot3, dummy_y, batch_size = 10, epochs = 50)

estimator = KerasClassifier(build_fn=baseline_model, epochs=10, batch_size=10)

kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

results = cross_val_score(estimator, tot3, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
    



from keras.models import Sequential
from keras.layers import *
model = Sequential()
model.add(Embedding(4103,64))
model.add(LSTM(64,activation='tanh', inner_activation='hard_sigmoid'))#Create Input Layer
model.add(Dense(14, init='uniform'))#Create output layer
model.add(Activation('softmax')) 
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

model.fit(tot3, dummy_y, batch_size = 10, epochs = 50,shuffle=True)

##

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

model = Sequential()
model.add(Dense(5000, activation='relu', input_dim=tot3.shape[1]))
model.add(Dropout(0.1))
model.add(Dense(600, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(dummy_y.shape[1], activation='sigmoid'))

sgd = SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy',
              optimizer=sgd)

model.fit(tot3, dummy_y, epochs=10, batch_size=200)

preds = model.predict(tot3)
preds[preds>=0.3] = 1
preds[preds<0.3] = 0















from keras.models import Model
from keras.layers import Input, LSTM, Dense

# Define an input sequence and process it.
encoder_inputs = Input(shape=(None, 4096))
encoder = LSTM(latent_dim, return_state=True)
encoder_outputs, state_h, state_c = encoder(encoder_inputs)
# We discard `encoder_outputs` and only keep the states.
encoder_states = [state_h, state_c]

# Set up the decoder, using `encoder_states` as initial state.
decoder_inputs = Input(shape=(None, num_decoder_tokens))
# We set up our decoder to return full output sequences,
# and to return internal states as well. We don't use the 
# return states in the training model, but we will use them in inference.
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs,
                                     initial_state=encoder_states)
decoder_dense = Dense(num_decoder_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

# Define the model that will turn
# `encoder_input_data` & `decoder_input_data` into `decoder_target_data`
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

















##############
import keras
from keras.models import Sequential,Input,Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU

batch_size = 64
epochs = 50
num_classes = 14

fashion_model = Sequential()
fashion_model.add(Conv2D(32, kernel_size=(3, 3),activation='linear',input_shape=(64,64,1),padding='same'))
fashion_model.add(LeakyReLU(alpha=0.1))
fashion_model.add(MaxPooling2D((2, 2),padding='same'))
fashion_model.add(Conv2D(64, (3, 3), activation='linear',padding='same'))
fashion_model.add(LeakyReLU(alpha=0.1))
fashion_model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
fashion_model.add(Conv2D(128, (3, 3), activation='linear',padding='same'))
fashion_model.add(LeakyReLU(alpha=0.1))                  
fashion_model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
fashion_model.add(Flatten())
fashion_model.add(Dense(128, activation='linear'))
fashion_model.add(LeakyReLU(alpha=0.1))                  
fashion_model.add(Dense(num_classes, activation='softmax'))

fashion_model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])
fashion_model.summary()


fashion_train = fashion_model.fit(train_X, train_label, batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(valid_X, valid_label))
test_eval = fashion_model.evaluate(valid_X, valid_label, verbose=0)

pred=fashion_model.predict(valid_X)
print('Test loss:', test_eval[0])
print('Test accuracy:', test_eval[1])

y_pred = np.argmax(pred, axis=1)
y_test = np.argmax(valid_label, axis=1)


from sklearn.metrics import precision_score, recall_score, f1_score

f1 = f1_score(y_test, y_pred, average="weighted")


pred_t=fashion_model.predict(ts_X)


pred_t2 = np.argmax(pred_t, axis=1)


sub1=pd.DataFrame(test['row_id'])
sub1['detected']=list(pred_t2)

sub1=sub1.reset_index()

sub1.to_csv('sub3.csv')

