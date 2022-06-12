import cv2 as cv
img=cv.imread('photos/ph.jpeg')
# cv.imshow('cat',img)

# #converting to greyscale
# gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('greyscale',gray)

# #blur an image

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascade

canny=cv.Canny(blur,150,150)
cv.imshow('canny',canny)

#dilating the image

dilated=cv.dilate(canny,(7,7),iterations=4)
cv.imshow('dilated',dilated)

#eroding an image
erode=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',erode)

#resizing an image

resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)

cv.imshow('resized',resized)

#cropping
cropping=img[50:200,200:700]
cv.imshow('cropped',cropping)






cv.waitKey(0)