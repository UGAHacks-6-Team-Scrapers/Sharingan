import cv2
import numpy as np
import dlib
import keyboard as kyb
import math
from gaze_tracking import GazeTracking

#THIS CLASS IS USED FOR TESTING. DO NOT USE FOR FINAL IMPLEMENTATION.

DIST_MOD = 12.0/.0198

#Opens the webcam. (The first if you have several.)
cap = cv2.VideoCapture(0)
gaze = GazeTracking()
ret, img = cap.read()

detector = dlib.get_frontal_face_detector() #Face detection algorithm.
predictor = dlib.shape_predictor("assets/shape_predictor_68_face_landmarks.dat") #Uses model to generate 67 landmark points.

left = [36, 37, 38, 39, 40, 41] #Left eye landmark points.
right = [42, 43, 44, 45, 46, 47] #Right eye landmark points.

#Takes the landmark points associated with eye edges to approx distance
#P36 = left eye left point
#P39 = left eye right point
#P42 = right eye left point
#P45 = right eye right point
def approxDist(p36, p39, p42, p45):
    leftEdgeDist = math.sqrt((p36.x - p39.x)**2 + (p36.y - p39.y)**2)
    rightEdgeDist = math.sqrt((p42.x - p45.x)**2 + (p42.y - p45.y)**2)

    edgeDist = (leftEdgeDist + rightEdgeDist) / 2

    return math.pow(edgeDist, -1) * DIST_MOD

def lookCoords(dist, x, y, h, v):
    h = (2*h) - 1
    v = (2*v) - 1

    lookX = x + (dist / math.cos(h * (math.pi/4)))
    lookY = y + (dist / math.cos(v * (math.pi/4)))

    return lookX, lookY

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gaze.refresh(frame)

    frame = gaze.annotated_frame()

    faces = detector(gray)
    for face in faces:
        #Uses the model and a grayscale background to track the 67 features.
        landmarks = predictor(gray, face)
        
        #Points 36 to 47 are for both eyes.
        for i in range(36, 48):
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            cv2.circle(frame, (x, y), 3, (255, 0, 0), -1)

        dist = approxDist(landmarks.part(36), landmarks.part(39), landmarks.part(42), landmarks.part(45))
        eyeX = (gaze.pupil_left_coords()[0] + gaze.pupil_right_coords()[0]) / 2
        eyeY = (gaze.pupil_left_coords()[1] + gaze.pupil_right_coords()[1]) / 2
        look = lookCoords(dist, eyeX, eyeY, gaze.horizontal_ratio(), gaze.vertical_ratio())
        print(look)
        

    #Webcam + tracking display
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if(kyb.is_pressed("space")):
        break