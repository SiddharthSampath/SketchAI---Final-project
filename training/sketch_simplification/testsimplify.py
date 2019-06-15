import tensorflow as tf
import keras.backend as K
import numpy as np
import matplotlib.pyplot as plt
import keras
import cv2
import scipy.misc
from PIL import Image

generator = keras.models.load_model('saved_model/simplify2.h5')
#generator = keras.models.load_model('saved_model/simplify.h5', custom_objects={'loss_func': loss_func})
#x_test = cv2.cvtColor(cv2.imread('pp.jpg'), cv2.COLOR_BGR2RGB)
x_test = cv2.imread('data/A/anime17.jpg', 0)
#x_test = plt.imread('pp.jpg')
x_test = np.array(x_test)/255.0
x_test = x_test.reshape((1, 256, 256, 1)) #1 since keras expects first element of shape to be reserved for batch size
gen = generator.predict(x_test)
print(gen[0])
im = gen[0].squeeze()
#scipy.misc.imshow(im)
#plt.imshow(im, cmap='gray')

#plt.imsave('res.jpg', gen[0])
scipy.misc.imsave('resl.jpg', im)

