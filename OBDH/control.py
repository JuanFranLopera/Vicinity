"""
File which runs the control system of Vicinity

- shall call imu()[1] from data_acquisition.py to find the angular velocity of the satellite
- shall input the angular speed to the PID controller 
- shall return a new duty cycle %
- shall control the system aginst the agular speed of 0.0279 rad s^-1
"""
from data_acquisition import imu
import time
from simple_pid import PID
import numpy as np



def control():
    pid = PID(0.01 , 20 , 0, setpoint = 0.0279, sample_time = 0.1) 

    return