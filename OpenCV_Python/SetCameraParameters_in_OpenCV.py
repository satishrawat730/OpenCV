''' 
Change camera properties

note: properties will change if hardware support it. 
Like property change to HD resolution if camera support it
'''

import cv2 as cv

# intialize default camera
cap = cv.VideoCapture(0)

print(" Camera available : ", cap.isOpened())

# properties of captured device can be taken using get()
print(" Frame width : ",  cap.get( cv.CAP_PROP_FRAME_WIDTH ))
print(" Frame height : ", cap.get( cv.CAP_PROP_FRAME_HEIGHT ))

# properties of captured device  can be changed using set()
# set( property , value)
# you can also gave property as numeric value
cap.set( cv.CAP_PROP_FRAME_WIDTH, 240)
cap.set( 4, 320) #cv.CAP_PROP_FRAME_HEIGHT is 4


print("after properties change")
print(" Frame width : ",  cap.get( cv.CAP_PROP_FRAME_WIDTH ))
print(" Frame height : ", cap.get( cv.CAP_PROP_FRAME_HEIGHT ))

while(True):
    # read return isReadable, frame(image)
    retain, frame = cap.read()

    if retain == True:
        
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
