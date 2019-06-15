import numpy as np
import cv2
import scipy.misc
import os
path = '/home/raghav52/pix2pix/mountain/'
print(os.getcwd())
#path_B = 'nB.jpg'
for filename in os.listdir(path):
    img = scipy.misc.imread(path+filename, mode="RGB")
    img2 = scipy.misc.imresize(img,(256,256))
    scipy.misc.imsave('/home/raghav52/pix2pix/mb/'+filename, img2)
    #cv2.imwrite('home/siddharth/pix2pix', img2, interpolation = cv2.INTER_AREA)
    
''''
im_A = cv2.imread(path_A, 1)
im_B = cv2.imread(path_B, 1)
im_AB = np.concatenate([im_A, im_B], 1) # 1 is the axis
cv2.imwrite('1.jpg', im_AB)
'''

