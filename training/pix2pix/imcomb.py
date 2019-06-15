import numpy as np
import cv2
import scipy.misc
import os
path_A = 'msnow/A/'
path_B = 'msnow/B/'

for filename in os.listdir(path_A):
    file = filename.split('.')
    
    im_A = cv2.imread(path_A + file[0] +'.jpg',1)
    im_B = cv2.imread(path_B + file[0] +'_gt.jpg',1)
    im_AB = np.concatenate([im_A, im_B], 1) # 1 is the axis
    cv2.imwrite('datasets/mt/train/'+filename, im_AB)
    
''''
im_A = cv2.imread(path_A, 1)
im_B = cv2.imread(path_B, 1)
im_AB = np.concatenate([im_A, im_B], 1) # 1 is the axis
cv2.imwrite('1.jpg', im_AB)
'''

