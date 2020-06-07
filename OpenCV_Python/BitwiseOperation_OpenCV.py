'''
Bitwise Operation in OpenCV 
Bitwise AND, OR, NOT, XOR.
'''

import numpy as np
import cv2 as cv

img1 = np.zeros((250,500,3), np.uint8)
# rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
# Draws a simple rectangle.
img1 = cv.rectangle(img1, (200, 0), (300,100), (255,255,255), -1 )
img2 =  cv.imread("./data/messi5.jpg")

img2 = cv.resize( img2, (500,250))
print(img2.shape)

# bitwise operation
bitAnd = cv.bitwise_and(img2, img1)
bitOr  = cv.bitwise_or(img2, img1)
bitNot = cv.bitwise_not(img2)
bitXor = cv.bitwise_xor(img2, img1)

cv.imshow('image1', img1)
cv.imshow('image2', img2)

cv.imshow('Bit_and', bitAnd)
cv.imshow('Bit_or', bitOr)
cv.imshow('Bit_not', bitNot)
cv.imshow('Bit_xor', bitXor)

cv.waitKey(0)
cv.destroyAllWindows()
