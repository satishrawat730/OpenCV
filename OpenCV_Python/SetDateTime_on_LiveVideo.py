''' 
display date time on Live video
also display frame size
'''

import cv2 as cv
import datetime as dt

# intialize default camera
cap = cv.VideoCapture(0)

print(" Camera available : ", cap.isOpened())

# properties of captured device can be taken using get()
framewidth  = cap.get( cv.CAP_PROP_FRAME_WIDTH )
frameheight = cap.get( cv.CAP_PROP_FRAME_HEIGHT )

print(" Frame width  : ", framewidth)
print(" Frame height : ", frameheight)

while(True):
    # read return isReadable, frame(image)
    retain, frame = cap.read()

    if retain == True:
        
        fontface = cv.FONT_HERSHEY_SIMPLEX
        # form text
        text = ' W: ' + str(framewidth) + '  ' + 'H: ' + str(frameheight) + ' Date: ' + str(dt.datetime.now())
        # put on display
        frame = cv.putText( frame, text, (0,20), fontface, 0.4, (100,220,36), 1, cv.LINE_AA)
        # display captured frame
        cv.imshow("Frame", frame)

        # break loop on press q
        if cv.waitKey( 1 ) & 0xFF == ord('q'):
            break
    else:
        break
# release captured device
cap.release()
cv.destroyAllWindows()
