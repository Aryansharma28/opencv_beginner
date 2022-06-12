import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('photos/pa.jpeg')
cv.imshow('park',img)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#simple thresholding
threshold,thresh= cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('thresholded value',thresh)


#inverse thresholding
threshold,thresh_inv= cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('thresholded inverse',thresh_inv)

#adaptive threshold
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
cv.THRESH_BINARY,11,2)
cv.imshow('adaptive thresholding',adaptive_thresh)



cv.waitKey(0) 