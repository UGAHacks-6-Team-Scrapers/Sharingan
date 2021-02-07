import pyautogui, sys

enabled = False
lag = 0

def __init__(enabled, followLag):
    global enabled
    global lag

    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(x=100, y=100)

    enabled = enabled
    lag = followLag


#Toggle mouse left click on and off
def mouseSwitch():
    global enabled

    if enabled:
        enabled = False
        pyautogui.mouseUp(button='left')

    else:
        enabled = True
        pyautogui.mouseDown(button='left')

#Move mouse to new location
def translate(x, y):
    global lag
    pyautogui.moveTo(x, y, lag, pyautogui.easeOutQuad)
    