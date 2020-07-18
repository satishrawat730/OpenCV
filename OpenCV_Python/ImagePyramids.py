'''
Image Pyramids with Python and OpenCV.
multiple resolution images are created by half the previous level
There are two kinds of Image Pyramids.
 1) Gaussian Pyramid  created by cv.pyrDown() and cv.pyrUp() functions
 2) Laplacian Pyramids a level in laplacian pyramid is formed by the  difference between that level
    in Gaussian Pyramid and expanded version of its upper level in Gaussian pyramid
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("./data/lena.jpg")

'''
# layer 
lvlDwn1 = cv.pyrDown(img)
lvlDwn2 = cv.pyrDown(lvlDwn1)
lvlUp1  = cv.pyrUp(lvlDwn2)

cv.imshow("orig", img)
cv.imshow("pyrdown 1 image", lvlDwn1)
cv.imshow("pyrdown 2 image", lvlDwn2)
cv.imshow("pyrup 1 image", lvlUp1)
'''

layer = img.copy()
gp = [layer]
cv.imshow("orig", img)

for i in range(5):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow('G'+ str(i), layer)

# LAPLACIAN PYRAMID
layer = gp[5]
cv.imshow('upper level Gaussian pyramid', layer)
lp = [layer]

for i in range(5 , 0 , -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)

cv.waitKey(0)
cv.destroyAllWindows()
