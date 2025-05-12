import numpy as np
import cv2
import os
import time
import serial

from variables import filepath #alter filepath as see fit

#Serial comm., turn LED n on/off (see Arduino sketch):
def cmd(ledIndex, ledState):
    command = f"{ledIndex},{ledState}\n"
    arduino.write(command.encode())

#Image capture process: 
def capture(ledIndex):
    print(f"turn on LED_{ledIndex}")
    cmd(ledIndex,1)
    verify, image = aerialPhoto.read()
    time.sleep(2) #some opencv confusion, latency fixes this
    cmd(ledIndex,0)
    print(f"turn off LED_{ledIndex}")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    os.makedirs(filepath, exist_ok=True)
    cv2.imwrite(f"{filepath}/led_{ledIndex}.png", image) #save locally for further use
    return image


#Closes the camera. May otherwise remain open and uncallable:
cv2.destroyAllWindows()

#Serial connection:
arduino = serial.Serial("COM4", baudrate=115200)  #need to get port based on connection
time.sleep(2) #some opencv confusion, latency fixes this

#Set up camera:
aerialPhoto = cv2.VideoCapture(1) 
aerialPhoto.set(cv2.CAP_PROP_FRAME_WIDTH, 3840) #USB Cam.: 3840*2160px. Seems to be necessary w/ opencv
aerialPhoto.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)  

#Execute multi-illumination and capture:
time.sleep(0.5)
if __name__ == "__main__":   
    for i in range(0,20):
        capture(i)
        time.sleep(0.1) #some opencv confusion, latency fixes this

#Closes the camera:
cv2.destroyAllWindows()
aerialPhoto.release()

