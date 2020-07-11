'''
Picture in Picture using matplotlib and opencv
'''

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("./data/gradient.png", 0)

# threshold(src, thresh, maxval, type, dst=None)
# THRESH_BINARY split into black white
_, thres1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY )
_, thres2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV )
_, thres3 = cv.threshold(img, 120, 255, cv.THRESH_TRUNC)
_, thres4 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO)
_, thres5 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO_INV)

titles = [ 'Original_Image', 'BINARY', 'BINARY_INV', 'THRESH_TRUNC' , 'THRESH_TOZERO', 'THRESH_TOZERO_INV']
images = [ img, thres1, thres2, thres3, thres4, thres5]

for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])

plt.show()
