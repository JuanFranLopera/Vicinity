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
    - shall call control() from control.py
    - shall call sun_sensor() from control.py
"""
from data_acquisition import imu
import time
