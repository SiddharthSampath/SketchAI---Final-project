import requests
import json
import base64
import shutil
import cv2

addr = 'http://localhost:5000'
test_url = addr + '/predict'

# prepare headers for http request
content_type = 'image/jpg'
headers = {'content-type': content_type}

img = cv2.imread('pA.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
#print(response.content)
with open("resAPI.jpg", "wb") as f:
     f.write(response.content)


# expected output: {u'message': u'image received. size=124x124'}