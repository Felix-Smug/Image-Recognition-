from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


while 1:
    
    try:

        if pyautogui.locateOnScreen('bot1.png') != None:
            print("I can see it")
            time.sleep(0.5)
        else:
            print("I am unable to see it")
            time.sleep(0.5)
            
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(0.5)