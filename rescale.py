import cv2 as cv

img=cv.imread('photos/libg.jpg')
cv.imshow('background image', img)

#this works for images videos and live videos
def rescaleframe(frame,scale=0.5):
    width= int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)
    dimensions=(width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

resized_image=rescaleframe(img)
cv.imshow('Image',resized_image)

#only works for live video
def changeres(width,height):
    capture.set(3,width)
    capture.set(4,height)



capture= cv.VideoCapture('videos/bb.mp4')# used to read video

while True:
    isTrue, frame= capture.read()#it reads what we stored in capture and assigns that to is true and frame
    frame_resized= rescaleframe(frame)
    cv.imshow('video',frame)#shows the video frame by frame as a video is a collection of frames
    cv.imshow('video resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'): # this is the condition that stops the video and its said to make it last for 20 ms & if d is pressed break the video
        break

capture.release()
cv.destroyAllWindows() # its basically like freeing memory so we release 

cv.waitKey(0)