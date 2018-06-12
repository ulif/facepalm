#!/usr/env/python3
# facepalm.py
#
# detects faces in images.
#
from PIL import Image, ImageDraw, ImageFilter
import face_recognition

# Read image
image = face_recognition.load_image_file("obama_and_biden.jpg")
pil_image = Image.fromarray(image)


face_locs = face_recognition.face_locations(
        image,
        number_of_times_to_upsample=0, model="cnn")

print("Found %s faces" % len(face_locs))
drawing = ImageDraw.Draw(pil_image)
for (top, right, bottom, left) in face_locs:
    print(top, right, bottom, left)
    drawing.rectangle(
        ((left, top), (right, bottom)),
        outline=(0x00, 0x00, 0xff))

del drawing

def pixelate(im, box):
    im_w, im_h = im.size
    y0, x1, y1, x0 = box
    w, h = x1 - x0, y1 - y0
    snippet = im.crop((x0, y0, x1, y1), )
    snippet = snippet.resize((int(w/15.0), int(h/15.0)), )
    snippet = snippet.resize((w, h), )
    im.paste(snippet, box=(x0, y0))
    return im

pil_image = pixelate(pil_image, face_locs[0])

w, h = pil_image.size
pil_image = pil_image.resize((int(w/25.0), int(h/25.0)), )
pil_image = pil_image.resize((w, h), )
print("Size: %s", pil_image.size)

pil_image.show()

