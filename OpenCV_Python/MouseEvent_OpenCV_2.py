'''
more mouse event in opencv
 draw line using mouse
 color pick and show in different window
'''

import numpy as np
import cv2 as cv

# callback  function
# param: mouse_event, mouse clicked position x y , 
def click_event(event, x, y, flags, param ):
    if event == cv.EVENT_LBUTTONDOWN :
        cv.circle(img, (x,y), 3, (10,10,150), -1)
        points.append((x,y))

        # draw line between last and 2nd last point 
        if len(points) >=2 :
            cv.line(img, points[-1], points[-2], (255,255,255), 3)
        # display captured frame
        cv.imshow("image", img)

    if event == cv.EVENT_RBUTTONDOWN :    
        blue = img[ y, x, 0]
        green= img[ y, x, 1]
        red  = img[ y, x, 2]
        #print( blue, ' , ' , green, ' , ' , red )
        cv.circle(img, (x,y), 3, (0,0,255), -1)
        
        colorImage = np.zeros([512,512,3], np.uint8 )
        colorImage[:] = [blue, green, red]

        # display colored image
        cv.imshow("color", colorImage)

# create black image
#img = np.zeros([512,512,3], np.uint8 )
img = cv.imread("./data/lena.jpg")

# window name must be same every where
cv.imshow("image", img)
points = []
# setMouseCallback(windowName, callback function)
cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
