#Intruder detection software using GPIO pins in the Raspberry Pi, a motion sensor and a camera
#Software is implemented in Raspberry Pi model 4B
#Once motion is detected, the object causing the motion is previewed through the screen through the camera and takes a picture.

from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4) #pin 4
camera = PiCamera()
camera.rotation = 180 #flip the image by 180 degrees

while True: #continious process
    pir.wait_for_motion()
    print("Intruder detected!")
    camera.start_preview()
    camera.capture('/home/pi/Desktop/thief.jpg') #takes a picture
    pir.wait_for_no_motion()
    camera.stop_preview()
