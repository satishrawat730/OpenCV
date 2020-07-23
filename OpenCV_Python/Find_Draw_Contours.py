'''
Find and Draw Contours in image
  functions : cv2.findContours(), cv2.drawContours().
  The function retrieves contours from the binary image. 
  The contours are a useful tool for shape analysis and object detection and recognition. 
'''

import cv2 as cv
import numpy as np

img    = cv.imread("./data/opencv-logo.png")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 55, 0)

# findContours(image, mode, method, contours=None, hierarchy=None, offset=None)
# each individual contour is a numpy array of (x,y) coordinates of boundary points of the object.
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print( "number of countours = " + str(len(contours )))
print(contours[0])

# drawContours(image, contours, contourIdx, color, thickness=None,
# lineType=None, hierarchy=None, maxLevel=None, offset=None)
# contourIdx = -1 draw all countours
cv.drawContours(img, contours, -1, (0, 255, 0), 3)

cv.imshow("image", img)
cv.imshow("image gray", imgray)

cv.waitKey(0)
cv.destroyAllWindows()
