'''
Basic and Arithmetic Operations on Images. 
use cv2.resize, cv2.add, cv2.addWeighted. 
'''

import numpy as np
import cv2 as cv

img = cv.imread("./data/messi5.jpg")
img2 =  cv.imread("./data/opencv-logo.png")

# shape : return tuple of number of row, column, channel
print(img.shape)

print(img2.shape)

# shape are different therefore will resize both image to equal size
# resize(src img, size) resizes the image src down to or up to the specified size.
img = cv.resize( img , (512,512))
img2 = cv.resize( img2 , (512,512))

# add(src1, src2, dst=None, mask=None, dtype=None)
# add calculates: . - Sum of two arrays when both input arrays have 
# the same size and the same number of channels: 
dest = cv.add(img, img2)
cv.imshow('image', dest)

# addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)
# The function addWeighted calculates the weighted sum of two arrays as follows: 
# texttt{dst} (I)= \texttt{saturate} ( \texttt{src1} (I)* \texttt{alpha} + \texttt{src2} (I)* \texttt{beta} + \texttt{gamma} )\f]
dest = cv.addWeighted(img, 0.9, img2, 0.1, 0)
cv.imshow('image weighted', dest)

cv.waitKey(0)
cv.destroyAllWindows()
