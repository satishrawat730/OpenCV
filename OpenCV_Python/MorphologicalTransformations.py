'''
Morphological Transformations with OpenCV. 
    morphological operations like Erosion, Dilation, Opening, Closing etc.
    functions like : cv.erode(), cv.dilate(), cv.morphologyEx() etc.

    for morphological to happen we need 2 thing binary image and kernel.
    Kernel tells how to change value of any given pixel by combining it with different amount of 
    the neighbouring pixels.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("./data/smarties.png", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV )

# color patch to be pasted over 
kernel = np.ones((5,5), np.uint8)

# we will use dilation to remove black dot from white ball in mask
dilation = cv.dilate(mask, kernel, iterations=2)
erosion  = cv.erode(mask, kernel, iterations=1)

# opening is erosion followed by dilation
opening  = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
# closing is dilation followed by erosion
closing  = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
mgradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
topHat    = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)

titles = [ 'Original_Image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mgradient', 'topHat' ]
images = [ img, mask, dilation, erosion, opening, closing, mgradient, topHat ]

for i in range(8):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])

plt.show()
