''' 
capture video from camera and display in window
save video in file
'''

import cv2 as cv

# intialize default camera
cap = cv.VideoCapture(0)

# VideoWriter_fourcc ( format) 
# get codec
fourcc = cv.VideoWriter_fourcc(*'XVID')

# VideoWriter ( filename, codec, fps, frame size tuple )
# instance to write video into file )
videoOut = cv.VideoWriter("videoout.avi", fourcc, 20.0, (640,480))

print(" Camera available : ", cap.isOpened())

# properties of captured device can be taken using get()
print(" Frame width  : ", cap.get( cv.CAP_PROP_FRAME_WIDTH ))
print(" Frame height : ", cap.get( cv.CAP_PROP_FRAME_HEIGHT ))

while(True):
    # read return isReadable, frame(image)
    retain, frame = cap.read()

    if retain == True:
        videoOut.write(frame)
        # cvtColor (frame to convert, color convert to)
        # convert color
        grayFrame = cv.cvtColor( frame, cv.COLOR_BGR2GRAY)

        # display captured frame
        cv.imshow("Frame", grayFrame)

        # break loop on press q
        if cv.waitKey( 1 ) & 0xFF == ord('q'):
            break
    else:
        break

# release captured device
cap.release()
cv.destroyAllWindows()
