from cProfile import label
import os
import cv2 as cv
import numpy as np
from requests import head

people=['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']


DIR= r'/home/aryan/Desktop/opencv/faces/'


features=[]
labels=[]

haar_cascade=cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')


def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        
        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()

print('training done')
features=np.array(features,dtype='object')
labels=np.array(labels)

face_recognizer= cv.face.LBPHFaceRecognizer_create()

#Train the recognizer
face_recognizer.train(features,labels)
face_recognizer.save('/home/aryan/Desktop/opencv/face_trained.yml')

np.save('features.npy',features)
np.save('labels.npy',labels)


















