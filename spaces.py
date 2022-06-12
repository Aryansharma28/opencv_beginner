import cv2 as cv
import matplotlib.pyplot as plt


img=cv.imread('photos/ph.jpeg')
cv.imshow('phto',img)

plt.imshow(img)
plt.show()


#BGR TO GREY
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey',gray)


#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)



cv.waitKey(0)
