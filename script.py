import pyautogui
from pyautogui import *
import time
import keyboard
import win32api
import win32con

def click(x, y):
    try:
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    except:
        pass
    
c1,c2,c3,c4 = False, False, False, False

while True:
    try:
        while not keyboard.is_pressed("q"):
            if pyautogui.pixel(700, 700)[0] == 0 and not c1:
                click(700, 700)
                c1 = True
                c2,c3,c4 = False, False, False
            if pyautogui.pixel(851, 700)[0] == 0 and not c2:
                click(851, 700)        
                c2 = True
                c1,c3,c4 = False, False, False
            if pyautogui.pixel(1000, 700)[0] == 0 and not c3:
                click(1000, 700)
                c3 = True
                c1,c2,c4 = False, False, False
            if pyautogui.pixel(1150, 700)[0] == 0 and not c4:
                click(1150, 700)
                c4 = True
                c1,c2,c3 = False, False, False
    except:
        pass