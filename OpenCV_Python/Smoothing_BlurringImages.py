'''
Smoothing or Blurring of Images with OpenCV 
used to remove noise
    morphological operations like 2D Convolution ( Image Filtering ) and  Image Blurring (Image Smoothing) 
    using Averaging, Gaussian Blurring, Median Blurring, Bilateral Filtering etc.
    We will see different functions like :
     cv.filter2D(), 
     cv.blur() : averaging algorithm for blurring
     cv.GaussianBlur() : is matrix with different weight kernel, in both x and y direction
                        pixel at side have lesser weight than pixel at center.
     cv.medianBlur() : this filter replace each pixel's value with the median of its neighbouring pixel.
                     this method is great when dealing with 'salt and pepper noise. 
     cv.bilateralFilter(): bilateralFilter can reduce unwanted noise very well while keeping edges fairly sharp. 
                        However, it is very slow compared to most filters. 

     Low Pass Filters (LPF):- helps in removing noises, blurring the image
     High Pass Filters (HPF):- helps in finding edges in the image
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("./data/opencv-logo.png", cv.IMREAD_ANYCOLOR)
img = cv.imread("./data/Halftone_Gaussian_Blur.jpg", cv.IMREAD_ANYCOLOR)
img = cv.imread("./data/water.png", cv.IMREAD_ANYCOLOR)
img = cv.imread("./data/lena.jpg", cv.IMREAD_ANYCOLOR)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

 # Homogeneous Kernel  = matrix of 5 row X 5 Col of 1's multiply by (1/ {kernel width * kernel height} )
kernel = np.ones((5, 5), np.float32) / 25

# filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None)
dst = cv.filter2D( img, -1, kernel)

# blur(src, ksize, dst=None, anchor=None, borderType=None)
blur = cv.blur( img, (5, 5))

# GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
GaussianBlur = cv.GaussianBlur(img, (5, 5), 0)

# medianBlur(src, ksize, dst=None)
medianBlur = cv.medianBlur(img, 5)

# bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)
bilateralFilter = cv.bilateralFilter( img, 9, 75, 75 )

titles = [ 'Original_Image', '2D convolutional', 'blur', 'GaussianBlur', 'medianBlur', 'bilateralFilter']
images = [ img, dst, blur, GaussianBlur, medianBlur, bilateralFilter ]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
