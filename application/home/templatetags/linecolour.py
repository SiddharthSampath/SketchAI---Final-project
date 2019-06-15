from django import template
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import keras
import cv2
from django.core.files.storage import FileSystemStorage
import scipy.misc
from django.conf import settings

generator=settings.MODEL3


# global generator
register = template.Library()

# @register.simple_tag
# def model_load():
#     global generator
#     generator = keras.models.load_model('home/anime.h5')

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


    # generator = keras.models.load_model('home/anime.h5')

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

        # plt.imsave("main/static/main/img/"+name, gen[0])

        # cv2.imwrite("main/static/main/img/"+name, gen[0])

        # fs = FileSystemStorage()
        # fs.save("saved_img.png","my.png")
        #plt.imshow(gen[0])
        #print(type(img))
        return ''

    else:

        return ''
