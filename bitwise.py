import cv2 as cv
from cv2 import bitwise_and
from cv2 import bitwise_or
from cv2 import bitwise_xor
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle= cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

#bitwise AND-> intersecting reigons of both the shapes
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('bit',bitwise_and)


#bitwise or->non intersecting and intersecting reigons of the shapes
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('bitor',bitwise_or)

#bitwise xor->non intersecting reigons are in white now
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise xor',bitwise_xor)

#bitwise not -> inversely colors the image 
bitnot=cv.bitwise_not(circle)
cv.imshow('bitnot',bitnot)

cv.waitKey(0)



