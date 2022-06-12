import cv2 as cv
import numpy as np


img=cv.imread('photos/pa.jpeg')
cv.imshow('park',img)


blank = np.zeros(img.shape[:2],dtype='uint8')#img.shape[:2] used for taking the whole image into account
cv.imshow('blank image',blank)

#masking

mask=cv.circle(blank, (img.shape[1]//2+250,img.shape[0]//2 + 200),100,255,-1)
cv.imshow('mask',mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)







cv.waitKey(0)