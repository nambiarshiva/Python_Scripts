from PIL import Image
import sys

flag_img = Image.open(sys.argv[-1])

w, h  = flag_img.size

msg = ""
for x in range(w):
    r, g, b = flag_img.getpixel((x, 0))
    if r == 255 or g == 255 or b == 255: msg += str(1)
    else : msg += str(0)

print (msg)
