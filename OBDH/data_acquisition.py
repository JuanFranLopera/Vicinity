"""
File that contains the functions to acquire data from the basic sensors

shall contain the following functions
    - index()
        - shall provide the index of the times the function has been called as an integer
    /- date_now()
        - shall return the date in dd/mm/yyyy as a string
    /- time_now()
        - shall return the time in hh:mm:ss as a string
    - light()
        - shall return a 3x3 matrix of floats in the form of
        - [[light1Red, light1Blue, light1Green],[light2Red, light2Blue, light2Green],[light3Red, light3Blue, light3Green]]
    /- imu()
        - shall return a 3x3 matrix of floats in the form of
        - [[euler1, euler2, euler3], [gyro1, gyro2, gyro3], [alpha1, alpha2, alpha3]]
"""
import time
import board
import adafruit_bno055
import adafruit_tca9548a    # multiplexer library
import csv
import datetime
import numpy as np

i2c = board.I2C() # setup I2C
tca = adafruit_tca9548a.TCA9548A(i2c) # begin MLX90640 with I2C comm
sensor = adafruit_bno055.BNO055_I2C(tca[6]) #I2C comm with IMU (channel 6)

def date_now():
    today = datetime.datetime.now().strftime("%Y-%m-%d")                    #produce date in dd/mm/yyyy
    today = str(today)                                                      #convert to string
    return today

def time_now():
    now = datetime.datetime.now().strftime("%H:%M:%S")                      #produce time in hh:mm:ss
    now = str(now)                                                          #convert to string
    return now

def imu():
    imu_out = [[sensor.euler], [sensor.gyro], [sensor.acceleration]]        #sets up the IMU sensor output matrix
    return imu_out

def thermal():
    global frame_values
    frame_values = []
    for h in range(24):
        for w in range(32):
            frame_values = np.append(frame_values,round(frame[h * 32 + w],2))

    global tt
    tt = np.resize(frame_values, (24,32))
    print(frame_values)
    return tt
