import cv2 as cv #importing the computer vision library

#READING IMAGES


#img = cv.imread('photos/libg.jpg')# we are making the module read the image and save it in img

#cv.imshow('libg', img)#shows the matrix of pixels aka photo in another window

#cv.waitKey(0)# time it should delay to open the image

#READING VIDEOS

capture= cv.VideoCapture('videos/bb.mp4')# used to read video

while True:
    isTrue, frame= capture.read()#it reads what we stored in capture and assigns that to is true and frame
    cv.imshow('video',frame)#shows the video frame by frame as a video is a collection of frames
    if cv.waitKey(20) & 0xFF==ord('d'): # this is the condition that stops the video and its said to make it last for 20 ms & if d is pressed break the video
        break

capture.release()
cv.destroyAllWindows() # its basically like freeing memory so we release 


 