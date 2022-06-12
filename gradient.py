from lib2to3.pgen2.token import LPAR
import cv2 as cv
from cv2 import bitwise_and
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('photos/pa.jpeg')
cv.imshow('park',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#edge detection- LAPLACIAN
lap=cv.Laplacian (gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)


#edge detection-SOBEL
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)

combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow('combined sobel',combined_sobel)

cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)

canny=cv.Canny(gray,150,175)
cv.imshow('canny',canny)




cv.waitKey(0)