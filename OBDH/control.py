"""
File which runs the control system of Vicinity

- shall call imu()[1] from data_acquisition.py to find the angular velocity of the satellite
- shall input the angular velocity to the PID controller 
- the PID controller shall ouput a new duty cycle %
- shall process the cuty cycle % into the PWM output from the Raspbery pi to the ESC
- shall control the system aginst the agular speed of 0.0279 rad s^-1
"""