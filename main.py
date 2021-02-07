import pygame, sys
import random

from pygame.locals import *
import cv2
from gaze_tracking import GazeTracking


def main():
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)
    """ print("1 - single gaze shape consturction")
    print("2 - double gaze shape construction")
    print("3 - constant gaze drawing")
    print("Choose drawmode: ")"""
    #record input then use if else to determine which while loop
    pygame.init()
    infoObject = pygame.display.Info()
    DISPLAY=pygame.display.set_mode((infoObject.current_w, infoObject.current_h),0,0) 

    WHITE=(220,220,220)

    DISPLAY.fill(WHITE)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #optional exit with escape key
                    pygame.image.save(DISPLAY, "test.png") #saves drawing before quiting
                    pygame.quit()
                    raise SystemExit
                elif event.key == pygame.K_RETURN:
                    # We get a new frame from the webcam
                    _, frame = webcam.read()

                    # We send this frame to GazeTracking to analyze it
                    gaze.refresh(frame)
                    hRatio = 1 - gaze.horizontal_ratio()
                    vRatio = gaze.vertical_ratio()
                    x = hRatio * infoObject.current_w
                    y = vratio * infoObject.current_h
                    randomSingleGazeShape(DISPLAY, infoObject, x, y)
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                randomSingleGazeShape(DISPLAY, infoObject, pos[0], pos[1])
            
        pygame.display.update()



def randomSingleGazeShape(DISPLAY, infoObject, x, y):
    ranShape = random.randint(0,6) 
    ranRed = random.randint(0, 255)
    ranGreen = random.randint(0, 255)
    ranBlue = random.randint(0, 255)
    ranThick = random.randint(0, 15)
    ranW = random.randint(30, 50)
    ranH = random.randint(30, 50)
    
    ranRadius = random.randint(15, 40)

    if (ranShape == 0): #shortline single or triple
        ranLength = random.randint(20, 100)
        ranBool = random.randint(0,2)
        if (ranBool == 0):
            ranStartX = x + ranLength
            ranLength = random.randint(0, 100)
            ranStartY = y + ranLength
            ranLength = random.randint(0, 100)
            ranEndX = x - ranLength
            ranLength = random.randint(0, 100)
            ranEndY = y - ranLength
        elif (ranBool == 1):
            ranStartX = x - ranLength
            ranLength = random.randint(0, 100)
            ranStartY = y + ranLength
            ranLength = random.randint(0, 100)
            ranEndX = x + ranLength
            ranLength = random.randint(0, 100)
            ranEndY = y - ranLength
        elif (ranBool == 2):
            ranStartX = x + ranLength
            ranLength = random.randint(0, 100)
            ranStartY = y - ranLength
            ranLength = random.randint(0, 100)
            ranEndX = x - ranLength
            ranLength = random.randint(0, 100)
            ranEndY = y + ranLength
        ranBool = random.randint(0,1)
        if (ranBool == 0):
            pygame.draw.line(DISPLAY, (ranRed, ranGreen, ranBlue), (ranStartX, ranStartY), (ranEndX, ranEndY), ranThick)
        elif (ranBool == 1):
            pygame.draw.line(DISPLAY, (ranRed, ranGreen, ranBlue), (ranStartX, ranStartY), (ranEndX, ranEndY), ranThick)
            pygame.draw.line(DISPLAY, (ranRed, ranGreen, ranBlue), (ranStartX - 20, ranStartY - 20), (ranEndX - 20, ranEndY - 20), ranThick)
            pygame.draw.line(DISPLAY, (ranRed, ranGreen, ranBlue), (ranStartX + 20, ranStartY + 20), (ranEndX + 20, ranEndY + 20), ranThick)
    elif (ranShape == 1): #longline
        ranBool = random.randint(0,3)
        if (ranBool == 0):
            longRanStartX = random.randint(0, x)
            longRanEndX = x
            longRanStartY = random.randint(0, y)
            longRanEndY = y
        elif (ranBool == 1):
            longRanStartX = random.randint(x, infoObject.current_w)
            longRanEndX = x
            longRanStartY = random.randint(y, infoObject.current_h)
            longRanEndY = y 
        elif (ranBool == 2):
            longRanStartX = random.randint(0, x)
            longRanEndX = x
            longRanStartY = random.randint(y, infoObject.current_h)
            longRanEndY = y 
        elif (ranBool == 3):
            longRanStartX = random.randint(x, infoObject.current_w)
            longRanEndX = x
            longRanStartY = random.randint(0, y)
            longRanEndY = y 
        pygame.draw.line(DISPLAY, (ranRed, ranGreen, ranBlue), (longRanStartX, longRanStartY), (longRanEndX, longRanEndY), ranThick)
    elif (ranShape == 2): #rectangle
        ranBool = random.randint(0,1)
        if (ranBool == 0):
            ranRectThick = 0
        else:
            ranRectThick = random.randint(1,5)
        ranBool = random.randint(0, 3)
        if (ranBool == 0): #small rect
            pygame.draw.rect(DISPLAY, (ranRed, ranGreen, ranBlue),(x - ranW/2,y -ranH/2, ranW, ranH), ranRectThick)
        elif (ranBool == 1): #medium square
            ranW = random.randint(100, 150)
            ranH = random.randint(100, 150)
            pygame.draw.rect(DISPLAY, (ranRed, ranGreen, ranBlue),(x - ranW/2, y - ranH/2, ranW, ranH), ranRectThick)
        elif (ranBool == 2): #medium rect
            ranBool = random.randint(0,1)
            if (ranBool == 1):
                ranW = random.randint(100, 150)
            else:
                ranH = random.randint(100, 150)
            pygame.draw.rect(DISPLAY, (ranRed, ranGreen, ranBlue),(x - ranW/2 ,y - ranH/2, ranW, ranH), ranRectThick)
        elif (ranBool == 3): #medium/large rect
            ranBool = random.randint(0,1)
            if (ranBool == 1):
                ranW = random.randint(50, 150)
                ranH = random.randint(100, 450)
            else:
                ranH = random.randint(50, 150)
                ranW = random.randint(100, 450)
            pygame.draw.rect(DISPLAY, (ranRed, ranGreen, ranBlue),(x - ranW /2, y - ranH/2, ranW, ranH), ranRectThick)
    elif (ranShape == 3): #triangle
        ranBool = random.randint(0,1)
        if (ranBool == 0):
            ranTriThick = random.randint(1, 5)
        else:
            ranTriThick = 0
        ranBool = random.randint(0,2)
        if (ranBool == 0):
            ranNum = random.randint(15, 100)
        elif (ranBool == 1):
            ranNum = random.randint(100, 200)
        elif (ranBool == 2):
            ranNum = random.randint(300, 400)
        ranBool = random.randint(0,2)
        if (ranBool ==0):
            ranSecNum = random.randint(15, 100)
        elif (ranBool == 1):
            ranSecNum = random.randint(100, 300)
        elif (ranBool == 2):
            ranSecNum = random.randint(300, 400)

        ranBool = random.randint(0,5)
        if (ranBool == 0): #upside down tri
            pygame.draw.polygon(DISPLAY, (ranRed, ranGreen, ranBlue), ((x - ranNum, y - ranNum), (x, y + ranNum), (x + ranNum, y - ranNum)), ranTriThick)
        elif(ranBool == 1): #upright tri
            pygame.draw.polygon(DISPLAY, (ranRed, ranGreen, ranBlue), ((x + ranNum, y + ranNum), (x, y - ranNum), (x - ranNum, y + ranNum)), ranTriThick)
        elif(ranBool == 2): #long tri
            pygame.draw.polygon(DISPLAY, (ranRed, ranGreen, ranBlue), ((x + ranNum, y + ranSecNum), (x, y - ranNum), (x - ranSecNum, y + ranNum)), ranTriThick)
        elif(ranBool == 3): #strang tri
            pygame.draw.polygon(DISPLAY, (ranRed, ranGreen, ranBlue), ((x + ranSecNum, y + ranSecNum), (x, y - ranNum), (x - ranSecNum, y - ranSecNum)), ranTriThick)
        elif(ranBool == 4): #right angle tri
            pygame.draw.polygon(DISPLAY, (ranRed, ranGreen, ranBlue), ((x + ranNum, y + ranNum), (x, y - ranNum), (x + ranNum, y - ranNum)), ranTriThick)
        elif(ranBool == 5): #strange tri reverse
            pygame.draw.polygon(DISPLAY, (ranRed, ranGreen, ranBlue), ((x - ranSecNum, y - ranSecNum), (x, y + ranNum), (x + ranSecNum, y + ranSecNum)), ranTriThick)
    elif (ranShape == 4): #arc
        ranStartAngle = random.uniform(0, 6.28)
        ranEndAngle = random.uniform(0, 6.28)
        ranBool = random.randint(0, 1)
        if (ranBool == 0):
            ranThick = random.randint(5, 12)
        else:
            ranThick = random.randint(15, 27)
        ranBool = random.randint(3, 3)
        if (ranBool == 0): #small centered
            rect = Rect(x - 50, y - 50, 100, 100)
        elif (ranBool == 1): #small squeezed 
            ranBool = random.randint(0,1)
            if (ranBool == 0):
                rect = Rect(x - 25, y - 62, 50, 125)
            else:
                rect = Rect(x - 62, y - 25, 125, 50)
        elif (ranBool == 2): #medium centered
            rect = Rect(x - 125, y - 125, 250, 250)
        elif (ranBool == 3): #medium squeezed
            ranBool = random.randint(0,1)
            if (ranBool == 0):
                rect = Rect(x - 150, y - 62, 300, 125)
            else:
                rect = Rect(x - 62, y - 150, 125, 300)
        pygame.draw.arc(DISPLAY, (ranRed, ranGreen, ranBlue), rect, ranStartAngle, ranEndAngle, ranThick)
    elif (ranShape == 5): #polygons
        ranBool = random.randint(0,1)
        if (ranBool == 0):
            ranThick = 0
        else:
            ranThick = random.randint(3,6)
        ranBool = random.randint(0,1)
        if (ranBool == 0): #hourglass
            pygame.draw.polygon(DISPLAY, (ranRed, ranGreen, ranBlue), ((x - ranW, y - ranH), (x + ranW, y + ranH), (x - ranW, y + ranH), (x + ranW, y - ranH)), ranThick)
        elif (ranBool == 1): #hexagon
            pygame.draw.polygon(DISPLAY, (ranRed, ranGreen, ranBlue), ((x - ranW + ranW/3, y - ranH), (x + ranW -ranW/3, y - ranH), (x + ranW + ranW/2, y), (x + ranW - ranW/3, y + ranH), (x - ranW + ranW/3, y + ranH), (x - ranW -ranW/2, y)), ranThick)
    elif (ranShape == 6): #circle
        ranBool = random.randint(0,1)
        if (ranBool == 0):
            ranThick = 0
        ranBool = random.randint(0,2)
        if (ranBool == 0): #small circle
            pygame.draw.circle(DISPLAY, (ranRed, ranGreen, ranBlue),(x,y), ranRadius, ranThick)
        elif (ranBool == 1): #medium circle
            ranRadius = random.randint(40, 100)
            pygame.draw.circle(DISPLAY, (ranRed, ranGreen, ranBlue),(x,y), ranRadius, ranThick)
        elif (ranBool == 2): #large circle
            ranRadius = random.randint(100,200)
            pygame.draw.circle(DISPLAY, (ranRed, ranGreen, ranBlue),(x,y), ranRadius, ranThick)

def randomDoubleGazeShape(x1, y1, x2, y2):
    ranShape = random.randint(0,5)
    if (ranShape == 0): #line
        print("tex")
    elif (ranShape == 1): #circle
        print("tex")
    elif (ranShape == 2): #rectangle
        print("tex")
    elif (ranShape == 3): #triangle
        print("tex")
    elif (ranShape == 4): #arc
        print("tex")
main()