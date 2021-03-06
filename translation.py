import cv2 as cv
import numpy as np
img=cv.imread('photos/ph.jpeg')
cv.imshow('boston',img)

#translation
def translate(img,x,y):
    transMAt=np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMAt,dimensions)


translate=translate(img,100,100)
cv.imshow('translate',translate)

cv.waitKey(0)

#rotation

def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat =cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated=rotate(img, 45)
cv.imshow('rotated',rotated)

#resizing
resized = cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('resized',resized)
cv.waitKey(0)



