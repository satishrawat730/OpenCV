'''
Canny edge detector is an edge detection operator that uses a multi-stage algorithm to 
    detect a wide range of edges in images. 
The Canny edge detection algorithm is broken down to 5 steps:
    Noise reduction;
    Gradient calculation;
    Non-maximum suppression;
    Double threshold;
    Edge Tracking by Hysteresis.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("./data/messi5.jpg", cv.IMREAD_GRAYSCALE)

# Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
canny = cv.Canny(img, 100, 200)

titles = [ 'Orig_Image', 'canny']
images = [ img, canny ]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
