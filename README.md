Motion Detector
===============

MotionDetector is a python script for Raspberry Pi using OpenCV3 and PiCamera. I use this to "wake" my MagicMirror at home whenever someone comes into view and interacts with the mirror. The mirror remains off/sleeping otherwise to save monitor life and power consumption.

The app waits a specified length of time, takes 2 images, and then measures the difference in pixel values. If the difference in values does not exceed a certain threshold, it assumes no movement and disables the signal to the monitor, causing the monitor to sleep. It then goes into a repeated cycle of taking an image every second. If "motion" is detected (overall difference in pixel values > threshold), it will re-enable the image signal, causing the monitor to wake.

This simplified version has only one camera speed/aperture setting. Very effective where it is currently being used at current settings but different environments will likely yield varying results. 

### ToDo:

1. Implement automated camera settings/configurations based on time of day and/or image quality to improve camera performance anytime day/night/time of year or location.

2. Implement facial/body recognition as a more elegant approach and as a tool for future projects.
