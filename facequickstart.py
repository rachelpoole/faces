import requests
from io import BytesIO
from PIL import Image, ImageDraw
import cognitive_face as CF

KEY = '9f4243734f6e4d89a7e24b3aa39c0a2f'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
faces = CF.face.detect(img_url)
print(faces)

# #Convert width height to a point in a rectangle
# def getRectangle(faceDictionary):
#     rect = faceDictionary['faceRectangle']
#     left = rect['left']
#     top = rect['top']
#     bottom = left + rect['height']
#     right = top + rect['width']
#     return ((left, top), (bottom, right))

# #Download the image from the url
# response = requests.get(img_url)
# img = Image.open(BytesIO(response.content))

# #For each face returned use the face rectangle and draw a red box.
# draw = ImageDraw.Draw(img)
# for face in faces:
#     draw.rectangle(getRectangle(face), outline='red')

# #Display the image in the users default image browser.
# img.show()