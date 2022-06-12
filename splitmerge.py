import cv2 as cv
import numpy as np


img=cv.imread('photos/p.jpeg')
cv.imshow('phto',img)


b,g,r=cv.split(img)

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)



cv.waitKey(0)