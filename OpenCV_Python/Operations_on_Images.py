'''
Basic and Arithmetic Operations on Images. 
use img.shape, img.size, img.dtype,  cv2.split, cv2.merge.
we will also see region of interest (ROI) in an image in OpenCv
'''

import numpy as np
import cv2 as cv

img = cv.imread("./data/messi5.jpg")
# shape : return tuple of number of row, column, channel
print(img.shape)
# size : return number of pixel  = row * col * channel
print(img.size)
# dtype : return image datatype e.g uint8
print(img.dtype)

# split : split image in 3 channel
b, g, r = cv.split(img)
print(b)

# highlight blue change
# b[:] = 255
# g[:] = 0
# r[:] = 0

# merge : merge 3 channel into single image
img = cv.merge( (b, g, r) )

ball = img[ 280:340, 330:390 ]
img[ 273:333, 100:160 ] = ball

cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()
