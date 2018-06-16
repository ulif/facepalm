#!/usr/env/python3
# facepalm.py
#
# detects faces in images.
#
from PIL import Image, ImageDraw, ImageFilter
import face_recognition

def pixelate(im, box):
    im_w, im_h = im.size
    y0, x1, y1, x0 = box
    w, h = x1 - x0, y1 - y0
    snippet = im.crop((x0, y0, x1, y1), )
    snippet = snippet.resize((int(w/15.0), int(h/15.0)), )
    snippet = snippet.resize((w, h), )
    im.paste(snippet, box=(x0, y0))

# Read image
image = face_recognition.load_image_file("obama_and_biden.jpg")
pil_image = Image.fromarray(image)


face_locs = face_recognition.face_locations(
        image,
        number_of_times_to_upsample=0, model="cnn")

print("Found %s faces" % len(face_locs))
drawing = ImageDraw.Draw(pil_image)
for face_loc in face_locs:
    pixelate(pil_image, face_loc)

del drawing

pixelate(pil_image, face_locs[0])
pil_image.show()

