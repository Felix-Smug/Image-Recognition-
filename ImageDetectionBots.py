from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os

screen_x = 960
screen_y = 540

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while 1:

    #if the image on screen is 35% accurate it will click
    try:
        if pyautogui.locateOnScreen('ow2Bot.png', grayscale=True, confidence=0.4) != None:
            print("Image found")
            click(screen_x, screen_y)
            time.sleep(1)

    except pyautogui.ImageNotFoundException:
        print("Image not found")
        time.sleep(1)