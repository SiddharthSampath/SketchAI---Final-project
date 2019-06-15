#from PIL import Image
#
#im_old = Image.open('nB.jpg')
#old_size = im_old.size
#print(old_size)
#new_size = (512, 256)
#new_im = Image.new("RGB", new_size)
#new_im.paste(im_old, (256, 0))
#new_im.show()
#new_im.save('2.jpg')

'''To make the combined test image with blank dummy. Not needed anymore'''

import cv2

img = cv2.imread('nB.jpg')

color = [255, 255, 255] # white

# border widths; I set them all to 150
top, bottom, left, right = 0, 0, 256, 0

img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
#cv2.imshow('ImageWindow', img_with_border)
#cv2.waitKey()
print(img_with_border.shape)
cv2.imwrite('3.jpg', img_with_border)
