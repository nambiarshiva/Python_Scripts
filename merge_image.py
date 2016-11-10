import sys
from PIL import Image
import glob

# list to hold image file names
left_images = []
right_images = []

left_file_count = len(glob.glob("left/*.png"))
right_file_count = len(glob.glob("right/*.png"))
file_count = max(left_file_count, right_file_count)

# sliced the images into 36 pieces horizontally
for i in range(1, file_count + 1):
    right_file = './right/slice_right_' + str(i) + '.png'
    left_file = './left/slice_left_' + str(i) + '.png'
    right_images.append(right_file)
    left_images.append(left_file)

images_left = list(map(Image.open, left_images))
images_right = list(map(Image.open, right_images))

# calculating the max image height
max_height = 0
for im in images_left:
    max_height += im.size[1]
for im in images_right:
    max_height += im.size[1]

new_im = Image.new('RGB', (500, max_height))

y_offset = 0
x_offset = 0
for i in range(1, file_count):
    # correcting the shift in every 4 slices
    if i % 6 == 0: x_offset -= 1
    new_im.paste(images_left[i], (x_offset, y_offset))
    y_offset += images_left[i].size[1]
    new_im.paste(images_right[i], (x_offset, y_offset))
    y_offset += images_right[i].size[1]

# rotating the image to make it readable
rot_img = new_im.rotate(90)
rot_img.save('flag.jpg')
