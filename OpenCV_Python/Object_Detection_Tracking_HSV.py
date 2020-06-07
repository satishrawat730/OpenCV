''' 
show How to do Object Detection and Object Tracking Using HSV Color Space. 
Implementing color and shape-based object detection and tracking using 
hue-saturation-value (HSV) color model
'''

import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

# camera
cap = cv.VideoCapture(0)
# namedWindow(winname, flags=None)
cv.namedWindow('Tracking')

cv.createTrackbar('LH','Tracking', 0,255, nothing)
cv.createTrackbar('LS','Tracking', 0,255, nothing)
cv.createTrackbar('LV','Tracking', 0,255, nothing)
cv.createTrackbar('UH','Tracking', 255,255, nothing)
cv.createTrackbar('US','Tracking', 255,255, nothing)
cv.createTrackbar('UV','Tracking', 255,255, nothing)

while(True):
    # open image
    # img = cv.imread("./data/smarties.png")

    # change over video 
    _, img = cap.read()

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lh = cv.getTrackbarPos('LH','Tracking')
    ls = cv.getTrackbarPos('LS','Tracking')
    lv = cv.getTrackbarPos('LV','Tracking')
    uh = cv.getTrackbarPos('UH','Tracking')
    us = cv.getTrackbarPos('US','Tracking')
    uv = cv.getTrackbarPos('UV','Tracking')
    
    l_b = np.array([lh, ls, lv]) # [110, 50, 50]
    u_b = np.array([uh, us, uv]) # [130, 255, 255]

    mask = cv.inRange(hsv, l_b, u_b)

    res = cv.bitwise_and(img, img, mask=mask)
    cv.imshow('image', img)
    cv.imshow('mask', mask)
    cv.imshow('result', res)

    k = cv.waitKey(1) & 0xFF
    if k==27:
       break

cap.release()
cv.destroyAllWindows()
