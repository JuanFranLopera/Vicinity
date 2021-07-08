import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library
import board
import adafruit_bno055
import csv
import datetime
import numpy as np
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus


i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)
#GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use 
                          # Broadcom SOC channel names.
GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(12, 2000)   # Initialize PWM on pwmPin 100Hz frequency

dc = 100                # set dc variable to 0 for 0%
pwm.start(dc)

while True:
    if np.linalg.norm(sensor.gyro) < 0.0279:        #Desired rotation speed
        dc += 1                     #simple control 
        pwm.ChangeDutyCycle(dc)
    fb = open('/home/pi/Documents/MISSION/data.csv','a')
    fb.write('%s %s %s %s %s \n' % (date_now(),time_now(), gyro_speed_now(), gyro_now(), dc))
    fb.close()
    print(dc)
    print(np.linalg.norm(sensor.gyro))
    print(str(sensor.euler))
    time.sleep(2)    