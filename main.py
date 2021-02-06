import pygame, sys
import random
from pygame.locals import *

def main():
    
    print("1 - single gaze shape consturction")
    print("2 - double gaze shape construction")
    print("3 - constant gaze drawing")
    print("Choose drawmode: ")
    #record input then use if else to determine which while loop
    pygame.init()
    infoObject = pygame.display.Info()
    DISPLAY=pygame.display.set_mode((infoObject.current_w, infoObject.current_h),0,0) 

    WHITE=(220,220,220)

    DISPLAY.fill(WHITE)

    #pygame.draw.rect(DISPLAY,(170, 170, 170),(0,0,infoObject.current_w, infoObject.current_h), 100)
    randomSingleGazeShape(DISPLAY, infoObject, 100, 100)
    pygame.draw.rect(DISPLAY, (0,0,0),(0,0, 100,100), 1)
    """randomSingleGazeShape(DISPLAY, 100, 200)
    randomSingleGazeShape(DISPLAY, 230, 400)
    randomSingleGazeShape(DISPLAY, 600, 60)
    randomSingleGazeShape(DISPLAY, 800, 40)"""
    pygame.draw.rect(DISPLAY, (0,0,0),(0,0 ,1000,600), 1)
    randomSingleGazeShape(DISPLAY, infoObject, 1000, 600)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT: #implemt a way to quit, with eyes maybe
                pygame.quit()
                sys.exit()
        pygame.display.update()



def randomSingleGazeShape(DISPLAY, infoObject, x, y):
    ranShape = random.randint(0,0) #change back
    ranRed = random.randint(0, 255)
    ranGreen = random.randint(0, 255)
    ranBlue = random.randint(0, 255)
    ranThick = random.randint(0, 15)
    ranW = random.randint(5, 50)
    ranH = random.randint(5, 50)
    ranStartX = random.randint(x - 100, x + 100)
    ranStartY = random.randint(y - 100, y + 100)
    ranEndX = random.randint(x - 100, x + 100)
    ranEndY = random.randint(y - 100, y + 100)
    ranRadius = random.randint(1, 40)

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


    if (ranShape == 0): #shortline single or triple
        ranBool = random.randint(0,1)
        if (ranBool == 0):
            pygame.draw.line(DISPLAY, (ranRed, ranGreen, ranBlue), (ranStartX, ranStartY), (ranEndX, ranEndY), ranThick)
        elif (ranBool == 1):
            pygame.draw.line(DISPLAY, (ranRed, ranGreen, ranBlue), (ranStartX, ranStartY), (ranEndX, ranEndY), ranThick)
            pygame.draw.line(DISPLAY, (ranRed, ranGreen, ranBlue), (ranStartX - 20, ranStartY - 20), (ranEndX - 20, ranEndY - 20), ranThick)
            pygame.draw.line(DISPLAY, (ranRed, ranGreen, ranBlue), (ranStartX + 20, ranStartY + 20), (ranEndX + 20, ranEndY + 20), ranThick)
    elif (ranShape == 1): #longline
        pygame.draw.line(DISPLAY, (ranRed, ranGreen, ranBlue), (longRanStartX, longRanStartY), (longRanEndX, longRanEndY), ranThick)
    elif (ranShape == 2): #rectangle
        pygame.draw.rect(DISPLAY, (ranRed, ranGreen, ranBlue),(x,y, ranW, ranH), ranThick)
    elif (ranShape == 3): #triangle
        pygame.draw.polygon(DISPLAY, (ranRed, ranGreen, ranBlue), ((x - 15, x - 15), (y + 25, y - 15), (y - 15, y - 15)), ranThick)
    elif (ranShape == 4): #arc
        print("tex")
    elif (ranShape == 5): #polygons
        print("tex")
    elif (ranShape == 6): #circle
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