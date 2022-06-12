import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')#uint8 basically means image
cv.imshow('blank',blank)

# #1.printing the image in a certain color

# blank[:]= 0,255,0 #making the entire img green
# cv.imshow('green',blank)

#2.drawing a rectangle

# cv.rectangle(blank, (0,0),(blank.shape[1]//2,blank.shape[0]//2), (255,0,0), thickness=-1)
# cv.imshow('rectangle',blank)

# #3. Draw a circle 

# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 40,(255,255,0), thickness=-1)
# cv.imshow('circle',blank)

# #4. Draw a line
# cv.line(blank,(100,250),(300,400),(0,0,255), thickness=3)
# cv.imshow('line', blank)

#5 write text
cv.putText(blank,'hello world',(000,255),cv.FONT_HERSHEY_TRIPLEX,3.0,(120,120,120),thickness=2)
cv.imshow('text',blank)
cv.waitKey(0)