import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.preprocessing.image import img_to_array
import cv2
import scipy.misc
import io
from flask import Flask, request, send_file
from PIL import Image

app = Flask(__name__, static_url_path='')
model = None

def load_model():
    global model
    model = keras.models.load_model('saved_model/pikax.h5')
    model._make_predict_function()

def prepare_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image,(256,256))
    scipy.misc.imsave('testl.jpg', image)
#    image = img_to_array(image)
    image = np.array(image)/127.5 - 1.
    image = image.reshape((1, 256, 256, 3))

    return image

@app.route("/predict", methods=["POST"])
def predict():

    # ensure an image was properly uploaded to our endpoint
    if request.method == "POST":
        r = request
        nparr = np.fromstring(r.data, np.uint8)
        # decode image
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image = prepare_image(image)
            # classify the input image and then initialize the list
            # of predictions to return to the client
        pred = model.predict(image)
        scipy.misc.imsave('reslpika.jpg', pred[0])

    return send_file('reslpika.jpg', mimetype='image/jpg')

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    load_model()
    app.run(debug=True)