import tensorflow as tf
import keras.backend as K
from keras.optimizers import Adadelta
#print(keras.__version__)
from keras.models import Sequential, Model
#from keras.layers.convolutional import Conv2d
from keras.layers import BatchNormalization, Activation, Input, Dense
from keras.layers.convolutional import Conv2D, Conv2DTranspose
import cv2
import numpy as np
import pickle

pickle_in = open("X.p","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.p","rb")
y = pickle.load(pickle_in)

X = X/255.0
y = y/255.0

#x = cv2.imread('mangashade.jpg', 0)
#y = cv2.imread('mangasketch.jpg', 0)
#x = x/255.0
#y = y/255.0
#x = np.reshape(x, (-1, 424, 424, 1))
#y = np.reshape(y, (-1, 424, 424, 1))

model = Sequential()
model.add(Conv2D(48, (5,5), strides=(2,2), padding='valid', input_shape=(424,424,1)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(128, (3,3), strides=(1,1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(128, (3,3), strides=(1,1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
#print(downconv1.output_shape)

model.add(Conv2D(256, (3,3), strides=(2, 2), padding='same'))#input shape=(-1,-1,-1,128)
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(256, (3,3), strides=(1, 1), padding='same'))#input shape=(-1,-1,-1,128)
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(256, (3,3), strides=(1, 1), padding='same'))#input shape=(-1,-1,-1,128)
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2D(256, (3,3), strides=(2, 2), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(512, (3,3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(1024, (3,3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2D(1024, (3, 3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(1024, (3, 3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(1024, (3, 3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(512, (3, 3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(256, (3, 3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2DTranspose(256, (4, 4), strides=(2, 2), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(256, (3, 3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(128, (3, 3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2DTranspose(128, (4, 4), strides=(2, 2), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(128, (3, 3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(48, (3, 3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2DTranspose(48, (4, 4), strides=(2, 2), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(24, (3, 3), strides=(1, 1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(1, (3, 3), strides=(1, 1), padding='same'))
model.add(Activation('sigmoid'))

model.summary()
model.compile(optimizer=Adadelta(), loss='mean_squared_error', metrics=['accuracy'])
model.fit(X, y, epochs=1)





