import win32api
import pyautogui

areaCorners = [[], []]
def rangeSelector():
    startX = -1
    startY = -1
    endX = -1
    endY = -1
    # wait for click unless the escape key is pressed
    # When the escape key is pressed the file terminates without doing anything
    while win32api.GetKeyState(0x1B) >= 0:
        # This if statement is true if the left mouse button is pressed down
        while win32api.GetKeyState(0x01) < 0:
            # Keep checking for escape key
            if win32api.GetKeyState(0x1B) < 0:
                return
            # X and Y Position of the corner
            # Only change if the x and y haven't been set yet.
            # Otherwise, the corner would be updated the whole time the mouse was pressed down
            if startX == -1 & startY == -1:
                startX = pyautogui.position().x
                startY = pyautogui.position().y
            # This if statement is true if the left mouse button is not pressed down
            if win32api.GetKeyState(0x01) >= 0:
                # X and Y Position of the corner
                endX = pyautogui.position().x
                endY = pyautogui.position().y
                return [[startX, startY], [endX, endY]]


def getResult(result):
    areaCorners = result
    print(areaCorners)


print(getResult(rangeSelector()))