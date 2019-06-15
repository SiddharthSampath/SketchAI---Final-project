from django import template
from PIL import Image
import PIL
import numpy as np
import matplotlib.pyplot as plt
import keras
import cv2
from django.core.files.storage import FileSystemStorage
import scipy.misc
from django.conf import settings

generator=settings.MODEL


# global generator
register = template.Library()

# @register.simple_tag
# def model_load():
#     # global generator
#     # generator = keras.models.load_model('home/pikay2.h5')
#     return 1

@register.simple_tag
def fname(name,url):
    # # x = name[7:]
    # # path = 'media/'+name[7:]
    # # print(path)
    # # return path
    # #return type(name)
    # path = 'media/'
    # path += name
    # #return path
    # if path != "media/":
    #     with Image.open(path) as image:
    #         width, height = image.size
    #         image.save("media/"+name+"converted.jpeg")
    #     return image
    # else:
    #     return ''

    # global generator


    # generator = keras.models.load_model('home/pikay2.h5')

    path = 'media/'
    path += name
    #return path
    if path != "media/":
        img = cv2.imread(path)
        img2 = cv2.resize(img,(256,256))
        x_test = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        x_test = np.array(x_test)/127.5 - 1.
        x_test = x_test.reshape((1, 256, 256, 3)) #1 since keras expects first element of shape to be reserved for batch size
        gen = generator.predict(x_test)

        scipy.misc.imsave("home/static/home/downloaded_images/"+name, gen[0])


        image = img2 #pp is the grayscale gan I/P image
        template = cv2.imread("home/static/home/downloaded_images/"+name) #res is the result after predict

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
        template = cv2.morphologyEx(template, cv2.MORPH_ERODE, kernel,iterations = 1)

        image[template == 0] = 255
    #    cv2.imwrite('resl.jpg', template)


        image = cv2.imread(path)
        image = cv2.resize(image,(256,256))

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
        scipy.misc.imsave('home/static/home/downloaded_images/'+name, cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

        img = PIL.Image.open('home/static/home/downloaded_images/'+name)
        converter = PIL.ImageEnhance.Color(img)
        img2 = converter.enhance(1.5)
        img2.save('home/static/home/downloaded_images/'+name)



        # fs = FileSystemStorage()
        # fs.save("saved_img.png","my.png")
        #plt.imshow(gen[0])
        #print(type(img))
        return ''

    else:

        return ''
