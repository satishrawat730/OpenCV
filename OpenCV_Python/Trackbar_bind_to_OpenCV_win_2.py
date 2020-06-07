'''
examples of TrackBar :
 changing colored image to grayscale image using Trackbar switch. 
 show tracbar position on image
'''

import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

# namedWindow(winname, flags=None)
cv.namedWindow('image')

# createTrackbar(trackbarName, windowName, value, count, callback func)
cv.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(True):
    # open image
    img = cv.imread("./data/lena.jpg")
    # The function returns the current position of the specified trackbar 
    pos = cv.getTrackbarPos('CP', 'image')

    fontface = cv.FONT_HERSHEY_SIMPLEX
    # put position on display
    cv.putText( img, str(pos), (50,50), fontface, 2, (0, 0, 255), 2)

    k = cv.waitKey(1) & 0xFF
    if k==27:
        break

    # getTrackbarPos(trackbarname, winname)    
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else: # convert image to gray
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('image', img)

cv.destroyAllWindows()
