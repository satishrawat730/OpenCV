'''
Image Thresholding is used for image segmentation. Thresholding is the simplest method of image segmentation. From a grayscale image, thresholding can be used to create binary images.
In Thresholding we Pick a threshold T.
1.Pixels above threshold get new intensity A.
2.Pixels above threshold get new intensity B.  
In Thresholding, pixels that are alike in gray scale(or in some other feature) are grouped together.
'''

import cv2 as cv
import numpy as np

img = cv.imread("./data/gradient.png", 0)

# threshold(src, thresh, maxval, type, dst=None)
# THRESH_BINARY split into black white
_, thres1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY )
_, thres2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV )
# THRESH_TRUNC  truncate color value after threshold and remain original till threshold
_, thres3 = cv.threshold(img, 120, 255, cv.THRESH_TRUNC)
# THRESH_TOZERO till threshold img value is 0 after thres img remain same
_, thres4 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO)
_, thres5 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO_INV)

cv.imshow("image", img)
cv.imshow("thres1", thres1)
cv.imshow("thres2", thres2)
cv.imshow("thres3", thres3)
cv.imshow("thres4", thres4)
cv.imshow("thres5", thres5)

cv.waitKey(0)
cv.destroyAllWindows()