import cv2 as cv
import numpy as np


img=cv.imread('photos/p.jpeg')
cv.imshow('park',img)

#averaging

average=cv.blur(img,(3,3))
cv.imshow('avg',average)

#gausian blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('gauss',gauss)

#median blur
median=cv.medianBlur(img,3)
cv.imshow('median',median)


cv.waitKey(0)