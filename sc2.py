# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:21:02 2018

@author: OMR
"""

import numpy as np
import pandas as pd
from keras.callbacks import EarlyStopping
from keras.callbacks import TensorBoard
from keras.layers import Dense, Activation, Flatten, Dropout
from keras.layers import MaxPooling2D
from keras.layers.convolutional import Conv2D
from keras.models import Sequential
from keras.utils import np_utils
from keras.utils.training_utils import multi_gpu_model
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder



def cnn_model(X_train, y_train, kernel_size, nb_filters, channels, nb_epoch, batch_size, nb_classes):
    '''
    Define and run the Convolutional Neural Network
    INPUT
        X_train: Array of NumPy arrays
        X_test: Array of NumPy arrays
        y_train: Array of labels
        y_test: Array of labels
        kernel_size: Initial size of kernel
        nb_filters: Initial number of filters
        channels: Specify if the image is grayscale (1) or RGB (3)
        nb_epoch: Number of epochs
        batch_size: Batch size for the model
        nb_classes: Number of classes for classification
    OUTPUT
        Fitted CNN model
    '''

    model = Sequential()

    '''
    First set of three layers
    Image size: 256 x 256
    nb_filters = 32
    kernel_size = (2,2)
    '''

    model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1]),
                     padding='valid',
                     strides=1,
                     input_shape=(img_rows, img_cols, channels)))
    model.add(Activation('relu'))

    model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
    model.add(Activation('relu'))

    model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(2, 2)))

    '''
    Second set of three layers
    Image Size: 128 x 128
    nb_filters = 64
    kernel_size = 4,4
    '''

    nb_filters = 64
    kernel_size = (4, 4)

    model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
    model.add(Activation('relu'))

    model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
    model.add(Activation('relu'))

    # model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
    # model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(2, 2)))

    '''
    Third set of three layers
    Image Size: 64 x 64
    nb_filters = 128
    kernel_size = 8,8
    '''

    nb_filters = 128
    kernel_size = (8, 8)

    model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
    model.add(Activation('relu'))

    model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
    model.add(Activation('relu'))

    # model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))
    # model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(12, 12)))

    model.add(Flatten())
    print("Model flattened out to: ", model.output_shape)

    model.add(Dense(4096))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(4096))
    model.add(Activation("relu"))
    model.add(Dropout(0.2))

    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))

    #model = multi_gpu_model(model, gpus=nb_gpus)
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    print(model.summary())

    stop = EarlyStopping(monitor='acc',
                         min_delta=0.001,
                         patience=2,
                         verbose=0,
                         mode='auto')

    tensor_board = TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)

    model.fit(X_train, y_train, batch_size=batch_size, epochs=nb_epoch,
              verbose=0,
              validation_split=0.2,
              class_weight='auto',
              callbacks=[stop, tensor_board]
              )
    return model


 batch_size = 100
 nb_classes = 14
 nb_epoch =10
nb_gpus = 1
img_rows, img_cols = 512,512
channels = 1
nb_filters = 32
kernel_size = (2, 2)

model = cnn_model(train_X, train_label, kernel_size, nb_filters, channels, nb_epoch, batch_size, nb_classes)