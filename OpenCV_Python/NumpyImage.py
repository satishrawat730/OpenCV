''' 
Draw primitive over numpy array image
'''

# import opencv
import cv2 as cv
import numpy as np

# black background
# 512 X 512 image size , # 3 channel BGR
img = np.zeros([512,512,3], np.uint8 )

# straight Line( image file, begin point1, end point2, color(BGR), line tickness)
img = cv.line( img, (0,0), (200,200), (255,0,0), 2 )

img = cv.rectangle( img, (100,100), (300,300), (100,30,200), 3 )

# draw circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
img = cv.circle( img, (300,300), 30, (175,65,96), -1)

fontface = cv.FONT_HERSHEY_SIMPLEX
# draw text : putText(img, text, org, fontFace, fontScale, color, thickness=None,
#  lineType=None, bottomLeftOrigin=None)
img = cv.putText( img, "Open CV", (10,500), fontface, 1, (100,220,36), 2, cv.LINE_AA)

# imshow( title, image) : show image in window
cv.imshow(" Image viewer", img)

cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
