'''
An image gradient is a directional change in the intensity or color in an image
OpenCV provides three types of gradient methods or High-pass filters:
 1. Sobel
 2. Scharr 
 3. Laplacian
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("./data/messi5.jpg", cv.IMREAD_GRAYSCALE)
# for sobel
img = cv.imread("./data/sudoku.png", cv.IMREAD_GRAYSCALE)
# Laplacian(src, ddepth, dst=None, ksize=None, scale=None, delta=None, borderType=None)
laplacianG = cv.Laplacian(img, cv.CV_64F, ksize=3 )
# to get absolute value of any negative number 
laplacianG = np.uint8(np.abs(laplacianG))

# Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)
SobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
SobelX = np.uint8(np.abs(SobelX))

SobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
SobelY = np.uint8(np.abs(SobelY))

sobelCombined = cv.bitwise_or(SobelX, SobelY)

# Scharr(src, ddepth, dx, dy, dst=None, scale=None, delta=None, borderType=None)
scharrX = cv.Scharr(img, cv.CV_64F, 1, 0 )
scharrX = np.uint8(np.abs(scharrX))

scharrY = cv.Scharr(img, cv.CV_64F, 0, 1 )
scharrY = np.uint8(np.abs(scharrY))

scharrCombined = cv.bitwise_or(scharrX, scharrY)

titles = [ 'Orig_Image', 'Laplacian','SobelX', 'SobelY', 'sobelCombined', 'scharrX', 'scharrY', 'scharrCombined']
images = [ img, laplacianG, SobelX, SobelY, sobelCombined, scharrX, scharrY, scharrCombined]

for i in range(8):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
