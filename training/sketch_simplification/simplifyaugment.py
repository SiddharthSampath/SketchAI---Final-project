import numpy as np
import os
import cv2

path_A = 'data/A/'
path_B = 'data/B/'
save_dir = 'data/B1/'

for filename in os.listdir(path_B):
#    file = filename.split('.')
    im_B = cv2.imread(path_B + filename,1)
    file = filename.rstrip('_gt_result.jpg')
#    print(file)
    cv2.imwrite(save_dir + file + '.jpg', im_B)
    cv2.imwrite(save_dir + file + '_0.jpg', im_B)
    cv2.imwrite(save_dir + file + '_1.jpg', im_B)
    cv2.imwrite(save_dir + file + '_2.jpg', im_B)
    