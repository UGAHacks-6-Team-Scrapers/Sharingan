import cv2
import numpy as np
import dlib
import keyboard as kyb

#Opens the webcam. (The first if you have several.)
cap = cv2.VideoCapture(0)
ret, img = cap.read()

detector = dlib.get_frontal_face_detector() #Face detection algorithm.
predictor = dlib.shape_predictor("assets/shape_predictor_68_face_landmarks.dat") #Uses model to generate 67 landmark points.

left = [36, 37, 38, 39, 40, 41] #Left eye landmark points.
right = [42, 43, 44, 45, 46, 47] #Right eye landmark points.


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        #Uses the model and a grayscale background to track the 67 features.
        landmarks = predictor(gray, face)
        
        #Points 36 to 47 are for both eyes.
        for i in range(36, 48):
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            cv2.circle(frame, (x, y), 3, (255, 0, 0), -1)

    #Webcam + tracking display
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if(kyb.is_pressed("space")):
        break
