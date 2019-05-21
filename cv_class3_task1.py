import numpy as np 
import cv2 

def show_video(cap):
    while(True):
        ret, frame = cap.read()

        # we apply the transformations now
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # we define the classifiers
        face_cascade = cv2.CascadeClassifier('haar_classifiers/haar_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haar_classifiers/haarcascade_eye.xml')

        # set the face detection list
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        # iterate the list and draw a rectangle for each face detected
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # in each detected face create the detected eyes list
            eyes = eye_cascade.detectMultiScale(gray)

            # and iterate through it in order to draw the according rectangles
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
        
        # once we've drawn everything for the current frame, display it.
        cv2.imshow('frame', frame)    
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release() 
    cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
show_video(cap)

    