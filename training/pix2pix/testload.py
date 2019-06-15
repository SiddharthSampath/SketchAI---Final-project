import numpy as np
import matplotlib.pyplot as plt
import keras
import cv2
import scipy.misc

generator = keras.models.load_model('saved_model/pikay2.h5')
x_test = cv2.cvtColor(cv2.imread('pA.jpg'), cv2.COLOR_BGR2RGB)
#x_test = plt.imread('pp.jpg')
x_test = np.array(x_test)/127.5 - 1.
x_test = x_test.reshape((1, 256, 256, 3)) #1 since keras expects first element of shape to be reserved for batch size
gen = generator.predict(x_test)
print(gen[0].shape)
#plt.imshow(gen[0])
#plt.imsave('res.jpg', gen[0])
scipy.misc.imsave('res.jpg', gen[0])