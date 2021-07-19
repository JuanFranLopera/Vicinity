"""
File which runs the control system of Vicinity

- shall take the current speed, target speed, proportional coefficient and threshold dc% and current dc from main
- shall return a new duty cycle %
- shall control the system aginst the agular speed of target speed rad s^-1
"""
import time
import numpy as np
dc = 0


def control_speed(speed, target_speed, K_p, low_bound, up_bound, min_dc, max_dc, dc):   
    """
    speed = the measured speed from the IMU
    target_speed = the desired speed
    K_p = proportional coefficient 
    low_bound = lower deadband value
    up_bound = upper deadband value
    min_dc = lower threshold dc (normally 4.4)
    max_dc = higher threshold dc (normally 12.5) 
    dc = current dc
    """
    err = speed - target_speed      # the error in the speed of the satellite.
    if speed <= up_bound and speed >= low_bound:
        pass
    else:
        dc += K_p*err #simple control
    if dc < min_dc:
        dc = min_dc
    if dc > max_dc:
        dc = max_dc
    return dc, err






"""
def control_pos(target, current, speed, min_dc, max_dc, dc, K_p1, K_p2):
    speed_deg = speed * 180/np.pi
    err_pos = current - target
    dc += err*K_p1 + K_p2*
    if dc < min_dc:
        dc = min_dc
    if dc > max_dc:
        dc = max_dc
    return dc
    """