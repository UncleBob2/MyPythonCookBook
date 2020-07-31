import numpy as np
import imageio
import scipy.ndimage
import cv2

img_data = "brinkley.jpg"


def to_gray_scale(rgb):
    """ this is the two 2D array to convert image to gray scale"""
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


def bake(front, back):
    final_sketch = front * 255 / (255 - back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype("uint8")


sample = imageio.imread(img_data)  # read the given image
gray_image = to_gray_scale(sample)  # convert color image to gray scale (BW)

enhance = 255 - gray_image  # RGB 0,0,0 is black and 255,255,255 is white

# blur the image
blur = scipy.ndimage.filters.gaussian_filter(
    enhance, sigma=15
)  # sigma is the level of the filter

create_sketch = bake(
    blur, gray_image
)  # create image to sketch using inputs: blur and gray_image

cv2.imwrite("blinkley_sketch.png", create_sketch)
print("Sketch Completed")
