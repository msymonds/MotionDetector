
# Author: Michael Symonds
# Date: March 20, 2017

# SimpleMotionDetector is used in conjuction with a raspberry pi using the pyCamera
# and requires PiCamera and OpenCV (which must be installed) as a dependency

from picamera import PiCamera
import time
from time import sleep
import os
import cv2
import numpy as np
import datetime


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
    os.system('cp -f /home/pi//MagicMirror/primary.jpg /home/pi/MagicMirror/previous.jpg')
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
        os.system('cp -f /home/pi//MagicMirror/primary.jpg /home/pi/MagicMirror/previous.jpg')
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
        sleep(120)
        if not preSleepCheck():
            os.system("vcgencmd display_power 0")
            sleepCycle()
