import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import random
import pickle

path_X = 'data/A1/'
path_y = 'data/B1/'
X = []
y = []
training_data = []

for filename in os.listdir(path_X):
#    print(filename)
    im_X = cv2.imread(path_X + filename, 0)
    im_y = cv2.imread(path_y + filename, 0)
    training_data.append([im_X, im_y])

#print(len(training_data))
random.shuffle(training_data)
for X_img, y_img in training_data:
    X.append(X_img)
    y.append(y_img)

#print(X[0].reshape(-1,X[0].shape[0],X[0].shape[1],1).shape)
X = np.reshape(np.array(X), (-1,X[0].shape[0],X[0].shape[1],1))
y = np.reshape(np.array(y), (-1,y[0].shape[0],y[0].shape[1],1))
print(X.shape, y.shape)

with open('X.p', 'wb') as fout:
    pickle.dump(X, fout)
    
with open('y.p', 'wb') as fout:
    pickle.dump(X, fout)
    
#pickle_in = open("X.p","rb")
#X = pickle.load(pickle_in)
#
#pickle_in = open("y.p","rb")
#y = pickle.load(pickle_in)