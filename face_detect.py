import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('photos/group.jpeg')
cv.imshow('person',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray P',gray)


haar_cascade=cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)

print(f'number of faces found={len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('detected faces',img)
cv.waitKey(0)
