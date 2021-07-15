"""
File which runs the control system of Vicinity

- shall take the current speed, target speed, proportional coefficient and threshold dc% and current dc from main
- shall return a new duty cycle %
- shall control the system aginst the agular speed of target speed rad s^-1
"""
import time
from simple_pid import PID
import numpy as np
dc = 0


def control(speed, target_speed, K_p, min_dc, dc):   
    """
    speed = the measured speed from the IMU
    target_speed = the desired speed
    K_p = proportional coefficient 
    min_dc = threshold dc (normally 4.4)
    dc = current dc
    """
    err = speed - target_speed      # the error in the speed of the satellite.  
    dc += K_p*err  #simple control
    if dc < min_dc:
        dc = min_dc
    return dc