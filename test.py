# Process

# Make API call
import cognitive_face as CF
import requests
import pandas as pd

KEY = '9f4243734f6e4d89a7e24b3aa39c0a2f'  # My subscription key
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # My regional Base URL
CF.BaseUrl.set(BASE_URL)

# Create two face IDs for the two photos using Face - Detect
image1 = './img/known/rachel-cropped-dl.jpg'
image2 = './img/rachel-selfie-small.jpg'

face1 = CF.face.detect(image1)
face2 = CF.face.detect(image2)

face1_id = face1[0]['faceId']
face2_id = face2[0]['faceId']

print(face1_id, face2_id)

# print(face1, face2)
# Then use Face-Verify




# You can use this example JPG or replace the URL below with your own URL to a JPEG image.