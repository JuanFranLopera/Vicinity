""" 
File that contains the functions to acquire data from the basic sensors

shall contain the following functions
    - index()
        - shall provide the index of the times the function has been called as an integer
    - date()
        - shall return the date in dd/mm/yyyy as a string
    - time()
        - shall return the time in hh:mm:ss as a string
    - light()
        - shall return a 3x3 matrix of floats in the form of 
        - [[light1Red, light1Blue, light1Green],[light2Red, light2Blue, light2Green],[light3Red, light3Blue, light3Green]]
    - imu()
        - shall return a 3x3 matrix of floats in the form of 
        - [[euler1, euler2, euler3], [gyro1, gyro2, gyro3], [alpha1, alpha2, alpha3]]
"""