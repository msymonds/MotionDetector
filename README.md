# SimpleMotionDetector
motion detector written in python for raspberry pi using a pycamera
App sleeps for 2 minutes then takes 2 images, measures the difference in pixel values.
If the difference in values does not exceed a certain threshold, it assumes no movement and disables the signal 
to the monitor, causing the monitor to sleep. It then goes into a repeated cycle taking an image every second,
if "motion" is detected (overall difference in pixel values > threshold), it will re-enable the image signal, 
causing the monitor to wake.

Image location info is hardcoded at this time and so not usable to others until that is fixed.
This version requires PyCamera and Installing OpenCV as a dependency.

Simplified version has only one camera speed/aperture setting.
ToDo: 
1. Implement varied setting camera settings/configurations based on time of day and/or image quality to improve 
camera performance anytime day/night/time of year.
2. make image file location relative.
