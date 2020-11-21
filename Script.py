import pyautogui
from python_imagesearch.imagesearch import *
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
import pydirectinput
import threading
import time 
import keyboard 
import random
import win32api, win32con

while 1:
    mouse = Controller()
    keyboard = Controller()
    pos = imagesearch("press_f.png")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        press('f')
        press('f')
        press('f')

    pos = imagesearcharea("nv.png", 0, 0, 1400, 900)
    if pos[0] != -1:
        pydirectinput.moveTo(pos[0], pos[1])
        pyautogui.scroll(-10)
        pyautogui.tripleClick()
        press('e')
    #pydirectinput.moveTo(None, 30)
    #else:
        #press('w')
    #temos que separar isso daqui em outra execucao
    #keyboard.press('w')
    #time.sleep(10)
    #keyboard.release('w')

            


    
    


    
