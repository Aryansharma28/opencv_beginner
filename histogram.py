import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('photos/ph.jpeg')
cv.imshow('park',img)


blank = np.zeros(img.shape[:2],dtype='uint8')

#creating the shape of the mask
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey',gray)

#creating the mask for the image
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('mask',masked)




# #grayscale histogram  
# gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])


plt.figure()
plt.title('Color histogram')
plt.xlabel('bins')# basically plots the pixel instensity in # pixels
plt.ylabel('# of pixels')



#color histogram
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)    









cv.waitKey(0)