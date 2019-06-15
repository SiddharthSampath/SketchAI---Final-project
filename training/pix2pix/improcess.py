import numpy as np
import cv2
from matplotlib import pyplot as plt 
import scipy.misc
import PIL
from PIL import Image
import PIL.ImageEnhance

if __name__ == '__main__':

    image = cv2.imread('pp.jpg') #pp is the grayscale gan I/P image
    template = cv2.imread('res.jpg') #res is the result after predict

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    template = cv2.morphologyEx(template, cv2.MORPH_ERODE, kernel,iterations = 1)

    image[template == 0] = 255
#    cv2.imwrite('resl.jpg', template)


    image = cv2.imread('pp.jpg') 
    
    mask = np.zeros(image.shape[:2], np.uint8) 
       
    backgroundModel = np.zeros((1, 65), np.float64) 
    foregroundModel = np.zeros((1, 65), np.float64) 
    
    rectangle = (0, 0, 255, 255) 
       
    cv2.grabCut(image, mask, rectangle,   
                backgroundModel, foregroundModel, 
                3, cv2.GC_INIT_WITH_RECT) 
       
    mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')  
    image = image * mask2[:, :, np.newaxis] 
#    cv2.imwrite('temp2.jpg', image)
    result = template
    gray = image
    
    result[gray<=2] = 255
#    cv2.imshow('res', result)
#    cv2.imshow('gray', gray)
#    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    scipy.misc.imsave('final.jpg', cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    
    img = PIL.Image.open('final.jpg')
    converter = PIL.ImageEnhance.Color(img)
    img2 = converter.enhance(1.5)
    img2.save('finalEnhanced.jpg')
    