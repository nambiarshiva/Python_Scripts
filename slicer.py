from __future__ import division
from PIL import Image
import math
import os

def long_slice(image_path, out_name, outdir, slice_size):
    """slice an image into parts slice_size tall"""
    img = Image.open(image_path)
    width, height = img.size
    upper = 0
    left = 0
    slices = int(math.ceil(height/slice_size))

    count = 1
    for slice in range(slices):
        #if we are at the end, set the lower bound to be the bottom of the image
        if count == slices:
            lower = height
        else:
            lower = int(count * slice_size)  
        #set the bounding box! The important bit     
        bbox = (left, upper, width, lower)
        working_slice = img.crop(bbox)
        upper += slice_size
        #save the slice
        slice_name = './' + out_name + "/slice_"
        working_slice.save(os.path.join(outdir, slice_name + out_name + "_" + \
            str(count) + ".png"))
        count +=1

def check_if_directory_exists(directory):
    """creats a directory if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)

if __name__ == '__main__':
    check_if_directory_exists("left")
    check_if_directory_exists("right")

    img = Image.open('warp_speed.5978d1405660e365872cf72dddc7515603f657f12526bd61e56feacf332cccad.jpg')
    w, h = img.size
    half_width = w/2
    img_left = img.crop((0, 0, half_width, h)).save('warp-left.png')
    img_right = img.crop((half_width, 0, w, h)).save('warp-right.png')

    #slice_size is the max height of the slices in pixels
    long_slice("warp-right.png", "right", os.getcwd(), 7)
    long_slice("warp-left.png", "left", os.getcwd(), 7)
