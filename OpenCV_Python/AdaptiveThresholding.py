'''
Adaptive Thresholding algorithm provide the image in which Threshold values vary over the image as a 
 function of local image characteristics. So Adaptive Thresholding involves two following steps
(i) Divide image into strips 
(ii) Apply global threshold method to each strip.

So in Adaptive Thresholding, Threshold depends on both f(x,y) and p(x,y). 
Adaptive thresholding changes the threshold dynamically over the image. 
Adaptive thresholding typically takes a gray scale or color image as input and, 
in the simplest implementation, outputs a binary image representing the segmentation.
'''

import cv2 as cv
import numpy as np

img = cv.imread("./data/sudoku.png", 0)

# threshold(src, thresh, maxval, type, dst=None)
# THRESH_BINARY split into black white
_, thres1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY )

# adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, Constant or weight, dst=None)
thres2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,  2)

thres3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11,  2)

cv.imshow("image", img)
# result due to different lighting image have different
cv.imshow("thres1", thres1)

cv.imshow("thres2", thres2)
cv.imshow("thres3", thres3)

cv.waitKey(0)
cv.destroyAllWindows()
