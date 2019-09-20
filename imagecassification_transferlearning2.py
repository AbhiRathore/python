# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:00:19 2019

@author: RathoreA
"""

############ using different models
import keras
import numpy as np
from keras.applications import vgg16, inception_v3, resnet50, mobilenet
import pandas as pd
import os,re,sys,cv2
#Load the VGG model
from keras import optimizers
from sklearn.model_selection import train_test_split

from os.path import basename

from keras.models import Model
from keras import models
from keras.layers import Dense,Conv2D,MaxPooling2D,BatchNormalization,GlobalAveragePooling2D
from keras.layers import Flatten
vgg_model = vgg16.VGG16(weights='imagenet')
import glob
#Load the Inception_V3 model
inception_model = inception_v3.InceptionV3(weights='imagenet')
 
#Load the ResNet50 model
resnet_model = resnet50.ResNet50(weights='imagenet')
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
 
os.chdir('C:/Users/RathoreA/Downloads/HE_Challenge_data/data/')
sys.path.insert(0,'./train')
sys.path.insert(0,'./test')
trainf=pd.read_csv('train.csv')
testf=pd.read_csv('test.csv')

labels=len(trainf.category.unique())

num_classes=labels


l=glob.glob('./train/*')



for i in l[:4]:
    filename = i
    # load an image in PIL format
    original = load_img(i, target_size=(224, 224,3))
    print('PIL image size',original.size)
    #plt.imshow(original)
    #plt.show()
    numpy_image = img_to_array(original)
    #plt.imshow(np.uint8(numpy_image))
    #plt.show()
    print('numpy array size',numpy_image.shape)

    # Convert the image / images into batch format
    # expand_dims will add an extra dimension to the data at a particular axis
    # We want the input matrix to the network to be of the form (batchsize, height, width, channels)
    # Thus we add the extra dimension to the axis 0.
    image_batch = np.expand_dims(numpy_image, axis=0)
    print('image batch size', image_batch.shape)
    #plt.imshow(np.uint8(image_batch[0]))
    
    
    ## label prediction
    # prepare the image for the VGG model
    processed_image = vgg16.preprocess_input(image_batch.copy())

    # get the predicted probabilities for each class
    predictions = vgg_model.predict(processed_image)
    # print predictions

    # convert the probabilities to class labels
    # We will get top 5 predictions which is the default
    label = decode_predictions(predictions)
    print('predicted label is {}'.format(label))
    
    
    
    


## model architecture
    
imgsize=224  
## customizing the model using vgg architecture
vgg_model_wtl = vgg16.VGG16(weights='imagenet',input_shape=(imgsize,imgsize,3),
                    include_top=False)
vgg_model_wtl.summary()


## stacking vgg with custom layers

layername='block3_conv3'

mymodel=Model(inputs=vgg_model_wtl.input,outputs=vgg_model_wtl.get_layer(layername).output)
mymodel.summary()


newmodel1=models.Sequential()
newmodel1.add(mymodel)

newmodel1.add(Conv2D(128,(3,3),activation='relu',padding='same'))
newmodel1.add(MaxPooling2D((2,2),padding='same'))

newmodel1.add(Conv2D(128,(3,3),activation='relu',padding='same'))
newmodel1.add(MaxPooling2D((2,2),padding='same'))


newmodel1.add(Conv2D(256,(3,3),activation='relu',padding='same'))
newmodel1.add(MaxPooling2D((2,2),padding='same'))

newmodel1.add(GlobalAveragePooling2D())
newmodel1.add(Dense(64,activation='relu'))
newmodel1.add(BatchNormalization())

newmodel1.add(Dense(num_classes,activation='softmax'))

newmodel1.layers[0].trainable=False
newmodel1.summary()

newmodel1.compile(loss='binary_crossentropy', optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])






## data generator


#train_y=np.asarray(trainf['category'])
# performing one-hot encoding for the target variable
 
#train_y=pd.get_dummies(train_y)
#train_y=np.array(train_y)

l=glob.glob('./train/*')
trainf2=pd.get_dummies(trainf['category'])

trainf2=trainf[['image_id']].join(trainf2)

import random
import math
all_image_paths = [str(path) for path in l]
random.shuffle(all_image_paths)



batch=400
totalrounds=math.ceil(len(all_image_paths)/batch)


for j in range(totalrounds):

    train_img=[]
    k=0
    imgname=[]
    
    
    for i in all_image_paths[k:k+batch]:
        filename = i
        imgname.append(basename(filename).split('.')[0])
    
        temp_img=load_img(filename,target_size=(224,224))
    
        temp_img=img_to_array(temp_img)
    
        train_img.append(temp_img)
    
    #converting train images to array and applying mean subtraction processing
    
    train_img=np.array(train_img)
    train_img=vgg16.preprocess_input(train_img)
    
    k += batch
    
    tr_name=pd.DataFrame(data=imgname,columns=['image_id'])
    tr_name['image_id']=tr_name['image_id'].astype(np.int64)
    #train_y2=train_y[:400]
    
    tr_name2=tr_name.merge(trainf2,on='image_id',how='left')
    
    train_y2=tr_name2.iloc[:,1:]
    X_train, X_valid, Y_train, Y_valid=train_test_split(train_img,train_y2,test_size=0.2, random_state=42)
    newmodel1.fit(X_train, Y_train, epochs=20, batch_size=128,validation_data=(X_valid,Y_valid))






testl=glob.glob('./test/*')



test_img=[]
for i in testl[:400]:
    filename = i

    temp_img=load_img(filename,target_size=(224,224))

    temp_img=img_to_array(temp_img)

    test_img.append(temp_img)

test_img=np.array(test_img)
test_img=vgg16.preprocess_input(test_img)

    

 



predclasses=newmodel1.predict_classes()


