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

def time_now():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    now = str(now)
    return(now)

def date_now():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today = str(today)
    return(today)

def gyro_speed_now():
    gyro_speed = np.linalg.norm(sensor.gyro)
    gyro_speed = str(gyro_speed)
    return(gyro_speed)

def gyro_now():
    gyro_now = sensor.gyro
    gyro_now = str(gyro_now)
    return(gyro_now)

print("active, waiting 30 s ...")
time.sleep(5)
dc=84                              # set dc variable to 0 for 0%
pwm.start(dc)   
while True:
    if np.linalg.norm(sensor.gyro) < 0.0279:        #Desired rotation speed
        dc += 1                     #simple control 
        pwm.ChangeDutyCycle(dc)
    fb = open('/home/pi/Documents/MISSION/data.csv','a')
    fb.write('%s %s %s %s %s \n' % (date_now(),time_now(), gyro_speed_now(), gyro_now(), dc))
    fb.close()

#     with open('/home/pi/Documents/MISSION/data.csv', mode='w') as sensor_readings:
#         writer = csv.DictWriter(sensor_readings, fieldnames = ["Date", "Time", "Angular Speed", "Angular Velocity", "Duty Cycle %" ])
#         writer.writeheader()
#         sensor_write = csv.writer(sensor_readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         write_to_log = sensor_write.writerow([date_now(),time_now(), gyro_speed_now(), gyro_now(), dc])
    print(dc)
    print(np.linalg.norm(sensor.gyro))
    print(str(sensor.euler))
    time.sleep(2)
    