''' 
Use matplotlib with opencv 
'''

# import opencv
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("./data/lena.jpg", 1)

# imshow( title, image) : show image in window
cv.imshow("Image", img)

# convert BGR to RGB
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)
# hide ticks in plot
# plt.xticks([]) , plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
