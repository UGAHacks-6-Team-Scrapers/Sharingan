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

    pygame.draw.rect(DISPLAY,(170, 170, 170),(0,0,infoObject.current_w, infoObject.current_h), 100)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT: #implemt a way to quit, with eyes maybe
                pygame.quit()
                sys.exit()
        pygame.display.update()


def randomSingleGazeShape(x, y):
    ranShape = random.randint(0,5)
    ranRed = random.randint(0, 255)
    ranGreen = random.randint(0, 255)
    ranBlue = random.randint(0, 255)
    ranThick = random.randint(0, 15)
    ranW = random.ranint(5, 50)
    ranH = random.ranint(5, 50)
    if (ranShape == 0): #line
        print("tex")
    elif (ranShape == 1): #circle
        print("tex")
    elif (ranShape == 2): #rectangle
        pygame.draw.rect(DISPLAY, (ranRed, ranGreen, ranBlue),(x,y, ranW, ranH), ranThick)
    elif (ranShape == 3): #triangle
        print("tex")
    elif (ranShape == 4): #arc
        print("tex")
    elif (ranShape == 5): #polygons
        print("tex")


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