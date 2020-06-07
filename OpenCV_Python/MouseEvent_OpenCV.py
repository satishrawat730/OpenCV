'''
mouse event in opencv
 on LeftBclick show mouse coordinate whereever its clicked on image
 on RightBclick show clor value of image
'''

import numpy as np
import cv2 as cv

# loop into cv dir and get properties named with 'event' 
events = [i for i in dir(cv) if 'EVENT' in i]
print(events)


# callback  function
# param: mouse_event, mouse clicked position x y , 
def click_event(event, x, y, flags, param ):
    if event == cv.EVENT_LBUTTONDOWN :
        print( x , ',' , y)

        fontface = cv.FONT_HERSHEY_SIMPLEX
        # form text
        text = str(x) + ' , ' + str(y)
        # put on display
        cv.putText( img, text, (x,y), fontface, 0.4, (100,220,36), 1, cv.LINE_AA)
        # display captured frame
        cv.imshow("image", img)
    
    if event == cv.EVENT_RBUTTONDOWN :

        blue = img[ y, x, 0]
        green= img[ y, x, 1]
        red  = img[ y, x, 2]
        #print(type(blue))
        print( blue, ' , ' , green, ' , ' , red )

        fontface = cv.FONT_HERSHEY_SIMPLEX
        # form text
        strbgr = str(blue) + ' , ' + str(green)+ ' , ' + str(red)
        # put on display
        cv.putText( img, strbgr, (x,y), fontface, 0.4, (153, 65, 198), 1, cv.LINE_AA)
        # display captured frame
        cv.imshow("image", img)

# create black image
# img = np.zeros([512,512,3], np.uint8 )

img = cv.imread("./data/lena.jpg")

# window name must be same every where
cv.imshow("image", img)

# setMouseCallback(windowName, callback function)
cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
