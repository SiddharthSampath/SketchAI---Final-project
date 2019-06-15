import torch
from torchvision import transforms
from torchvision.utils import save_image
from torch.utils.serialization import load_lua

from PIL import Image
import argparse
from django import template
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import keras
import cv2
from django.core.files.storage import FileSystemStorage
import scipy.misc
from django.conf import settings


cache=settings.MODEL5


# global generator
register = template.Library()

# @register.simple_tag
# def model_load():
#     global generator
#     generator = keras.models.load_model('home/anime.h5')

@register.simple_tag
def fname(name,url):
    # global cache

    path = 'media/'
    path += name
    #return path
    if path != "media/":
        use_cuda = torch.cuda.device_count() > 0

        # cache  = load_lua( "home/model_mse.t7", long_size=8 )
        model  = cache.model
        immean = cache.mean
        imstd  = cache.std
        model.evaluate()

        data  = Image.open(path).convert('L')
        data = data.resize((565,565),Image.ANTIALIAS)
        w, h  = data.size[0], data.size[1]
        pw    = 8-(w%8) if w%8!=0 else 0
        ph    = 8-(h%8) if h%8!=0 else 0
        data  = ((transforms.ToTensor()(data)-immean)/imstd).unsqueeze(0)
        if pw!=0 or ph!=0:
            data = torch.nn.ReplicationPad2d( (0,pw,0,ph) )( data ).data

        if use_cuda:
            pred = model.cuda().forward( data.cuda() ).float()
        else:
            pred = model.forward( data )
            save_image( pred[0], "home/static/home/downloaded_images/"+name )
        # img = cv2.imread(path)
        # img2 = cv2.resize(img,(256,256))
        # x_test = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        # x_test = np.array(x_test)/127.5 - 1.
        # x_test = x_test.reshape((1, 256, 256, 3)) #1 since keras expects first element of shape to be reserved for batch size
        # gen = generator.predict(x_test)
        # scipy.misc.imsave("home/static/home/downloaded_images/"+name, gen[0])

        # plt.imsave("main/static/main/img/"+name, gen[0])

        # cv2.imwrite("main/static/main/img/"+name, gen[0])

        # fs = FileSystemStorage()
        # fs.save("saved_img.png","my.png")
        #plt.imshow(gen[0])
        #print(type(img))
        return ''

    else:

        return ''

# parser = argparse.ArgumentParser(description='Sketch simplification demo.')
# parser.add_argument('--model', type=str, default='model_gan.t7', help='Model to use.')
# parser.add_argument('--img',   type=str, default='test.png',     help='Input image file.')
# parser.add_argument('--out',   type=str, default='out.png',      help='File to output.')
# opt = parser.parse_args()

