# MotionDetector
# Author: Michael Symonds
# Updated: 8/2/17

from picamera import PiCamera
import time
from time import sleep
import os
import cv2
import numpy as np
import datetime

# You will need to un-note the following commands, 
# They disable the monitor's screen saver so
# it won't interfere with the script. This is 
# necessary as PiCamera cannot function while the monitor
# is sleeping due to code limitations, which is why
# this scrpt disables the mointor rather than just 
# putting it in sleep mode.

#os.system('xset -d :0 s reset && xset -d :0 dpms force on')
#os.system('xset -d :0 s off')
#os.system('xset -d :0 s noblank')
#os.system('xset -d :0 -dpms')

def getTime():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%y-%m-%d %H:%M:%S')
    return st

def preSleepCheck():
    camera = PiCamera()
    camera.iso=800
    camera.brightness=70
    sleep(1)
    camera.capture('primary.jpg')
    os.system('cp -f ./primary.jpg ./previous.jpg')
    sleep(1)
    camera.capture('primary.jpg')
    
    previous = cv2.imread("previous.jpg")
    current = cv2.imread("primary.jpg")
    previous = cv2.cvtColor(previous, cv2.COLOR_BGR2GRAY)
    current = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)
    err = np.sum((previous.astype("float") - current.astype("float")) ** 2)
    err /= float(previous.shape[0] * current.shape[1])
    camera.close()
    if err > 75.0 :
        return True
    else:
        return False

def sleepCycle():
    camera = PiCamera()
    camera.iso = 800
    camera.brightness=70
    noMovement = True
    while(noMovement):
        os.system('cp -f ./primary.jpg ./previous.jpg')
        sleep(1)
        camera.capture('primary.jpg')
        previous = cv2.imread("previous.jpg")
        current = cv2.imread("primary.jpg")
        previous = cv2.cvtColor(previous, cv2.COLOR_BGR2GRAY)
        current = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)
        err = np.sum((previous.astype("float") - current.astype("float")) ** 2)
        err /= float(previous.shape[0] * current.shape[1])
        if err > 75.0:
            noMovement = False
    camera.close()
    os.system("vcgencmd display_power 1")
    
if __name__ == '__main__':
    while(True):
        sleep(10)
        if not preSleepCheck():
            os.system("vcgencmd display_power 0")
            sleepCycle()
