''' 
open image and write image on key press
'''

# import opencv
import cv2 as cv

'''
Flag 
1  : IMREAD_COLOR loads the image in the BGR 8-bit format. This is the default that is used here.
-1 : IMREAD_UNCHANGED loads the image as is (including the alpha channel if present)
0  : IMREAD_GRAYSCALE loads the image as an intensity one
'''

# imread( image path, flag ) : read image file
# if image NA result is none
img = cv.imread("./data/lena.jpg", 1)

# image array having pixel color info
print( img )
print( img.shape)

# imshow( title, image) : show image in window
cv.imshow("Image viewer", img)

# waitkey(milliseconds) : wait 
# 0 for unlimited time
# 
keypress = cv.waitKey(0) & 0xFF
print(keypress)
if keypress == 27: # escape key
    # closes all windows opened
    cv.destroyAllWindows()
elif keypress == ord('s'):
    # imwrite ( filename to save, file to be saved) 
    # write image to file and close window
    cv.imwrite("Lenacopy.png", img)
    cv.destroyAllWindows()

