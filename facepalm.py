#!/usr/env/python3
# facepalm.py
#
# detects faces in images.
#
from PIL import Image
import face_recognition

# Read image
image = face_recognition.load_image_file("obama_and_biden.jpg")


face_locs = face_recognition.face_locations(
        image,
        number_of_times_to_upsample=0, model="cnn")

print("Found %s faces" % len(face_locs))
for (top, right, bottom, left) in face_locs:
    print(top, right, bottom, left)

