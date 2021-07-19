"""
Main file that runs the whole satellite

shall be started by telecommands.py
shall be stopped by telecommands.py
shall contain Initialisation commands
shall consist of a while loop which
    - adds a row to a .csv with the current data readings by  
        - calling the data acquisition functions:
            - index()
            - date()
            - time()
            - light()
            - imu()
        from the data_acquisition.py file
        - calling the thermal() function from thermal.py
        - calling the stereo() function from stereo.py
    - shall send the .csv file to the ground station by calling downlink() from downlink.py
    - shall call control(speed, target_speed, K_p, min_dc, dc) from control.py
    - shall call sun_sensor() from control.py
"""
import time                 # Import time library
import board                # main library for controlling pins 
import pwmio                # PWM library 
import adafruit_bno055      # IMU library 
import adafruit_tca9548a    # multiplexer library
import csv                  # library for writing to .csv
import datetime             
import numpy as np
from control import *
from data_acquisition import *

"""
Initialisation
"""

i2c = board.I2C() # setup I2C
tca = adafruit_tca9548a.TCA9548A(i2c) # begin MLX90640 with I2C comm
sensor = adafruit_bno055.BNO055_I2C(tca[6]) #I2C comm with IMU (channel 6)
pwm= pwmio.PWMOut(board.D18, frequency = 50, duty_cycle = 0) #setting the pwm on GPIO pin 18 physical pin 12
dc = 4.4 # sets duty cycle to the threshold duty cycle for the ESC
target_speed = -5*np.pi/180 # rad s^-1
up_bound = target_speed*1.1 #-0.0279
low_bound = target_speed*0.9 #-0.022
K_p = 0.01
min_dc = 4.5
max_dc = 12
err_speed = 0
pwm.duty_cycle = (dc/100) * (2 ** 16) # starts the PWM running for the ESC to recognise but will have no response until dc = 4.5 
time.sleep(30) # needs some time to pass to initialise the PWM
t =0

"""
Operations
"""

while True:
    ### PAYLOAD SECTION ###

    

    ### CONTROL SECTION ###
    if t == 2:
        dc, err_speed = control_speed(sensor.gyro[1], target_speed, K_p, low_bound, up_bound, min_dc,max_dc, dc, err_speed)  # fetches the new dc from control
        pwm.duty_cycle = (dc/100) * (2 ** 16)   # sets the PWM to the new dc
        t = 0
    t +=1
    fb = open('/home/pi/Documents/MISSION/5dps.csv','a')
    fb.write('%s %s %s %s %s\n' % (date_now(),time_now(),imu(), dc, err_speed))
    fb.close()
    time.sleep(1) #get rid of this sleep for final code and only have 1

    

    



