'''
examples of TrackBar :
 including using Trackbar as the Color Palette
 get user input with OpenCV trackbars.
'''

import cv2 as cv
import numpy as np

def nothing(x):
    print(x)
    
# create black image
img = np.zeros((300,512,3), np.uint8)

# namedWindow(winname, flags=None)
cv.namedWindow('image')

# createTrackbar(trackbarName, windowName, value, count, callback func)
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(True):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k==27:
        break

    # getTrackbarPos(trackbarname, winname)
    # The function returns the current position of the specified trackbar 
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv.destroyAllWindows()
