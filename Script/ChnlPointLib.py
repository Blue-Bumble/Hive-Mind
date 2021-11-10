
from playsound import playsound
import time
from threading import Thread
import pydirectinput
import win32gui, win32ui, win32con, win32api
from win32con import *
import os
import sys
import getpass
######################
#     Variables      #
######################

user_name = str(getpass.getuser())
get_sound_location = (f'C:/Users/{user_name}/Desktop/Hive-Mind/Sounds/')

######################
# Conditions/Effects #
######################


class functions():

    def click(): # Spam left clicking
        i = 0 
        time.sleep(2.4)
        while i <= 120:
            time.sleep(.03)
            pydirectinput.leftClick()
            i += 1
            if i == 95:
                print("done")
                break

    def scroll(): # scroll wheel
        h = 0 
        time.sleep(.2)
        while h <= 4:
            time.sleep(3.5)
            #win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, 1, 0)
            h += 1
            if h == 4:
                print("done")
                break
        
    def charge(): # Move forward
        e = 0
        time.sleep(3)
        while e <= 95:
            functions.focus()
            pydirectinput.keyDown('w')
            e += 1
            if e == 95:
                pydirectinput.keyUp('w')
                break

    def left(): # Slide to the left
        e = 0
        time.sleep(3)
        while e <= 95:
            functions.focus()
            pydirectinput.keyDown('a')
            e += 1
            if e == 95:
                pydirectinput.keyUp('a')
                break

    def right(): # Slide to the Right
        e = 0
        time.sleep(3)
        while e <= 95:
            functions.focus()
            pydirectinput.keyDown('d')
            e += 1
            if e == 95:
                pydirectinput.keyUp('d')
                break

    def back(): # Move backwares
        e = 0
        time.sleep(3)
        while e <= 95:
            functions.focus()
            pydirectinput.keyDown('s')
            e += 1
            if e == 95:
                pydirectinput.keyUp('s')
                break

    def focus(): # this detects if vrchat is running to target it or not.
        winname = "VRChat" #name of the window
        get_window = win32gui.FindWindow(None, winname)
        try:
            win32ui.FindWindow(None, winname)
        except win32ui.error:
            print("Vrchat isnt open") #Debugging tool
            return False
        else:
            print("target Vrchat") #Debugging tool
            win32gui.SetForegroundWindow(get_window)
            return True

class sounds():
    def derp(): # this place derpy music
        sound = ( f'{get_sound_location}derp.mp3' )
        playsound(str(sound))

