import time               # Import time library
import board
import pwmio
import adafruit_bno055
import adafruit_tca9548a
import csv
import datetime
import numpy as np

#import smbus
#bus = smbus.SMBus(1)
#bus.write_byte_data(0x28, 0x0A, 0b00000100)

i2c = board.I2C() # setup I2C
tca = adafruit_tca9548a.TCA9548A(i2c) # begin MLX90640 with I2C comm
sensor = adafruit_bno055.BNO055_I2C(tca[6]) #I2C comm with IMU (channel 1)
pwm= pwmio.PWMOut(board.D18, frequency = 50, duty_cycle = 0) #setting the pwm on GPIO pin 18 physical pin 12
                                                              #frequency set to 50hz, duty cycle set to 0   

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
#time.sleep(5)
dc=4.4# set dc variable to 0 for 0%
print(dc)
pwm.duty_cycle = (dc/100) * (2 ** 16)
t = 0
time.sleep(40)
dc=4.5# set dc variable to 0 for 0%
print(dc)
pwm.duty_cycle = (dc/100) * (2 ** 16)
target_speed = -0.025
K_p = 0.25
while True:
    if t == 4:
        err = sensor.gyro[1] - target_speed
        dc += K_p*err  #simple control
        t=0
        print(dc)
    if dc <5:
        dc = 5
    pwm.duty_cycle = (dc/100) * (2 ** 16)   # dc between 0.0 and 1.0 where 0.0 = 0.0% and 1.0 = 100.0
                                            #Can be controlled in decimal in full 16 bit. 
    fb = open('/home/pi/Documents/MISSION/data_test_8.csv','a')
    fb.write('%s %s %s %s %s \n' % (date_now(),time_now(),sensor.euler, sensor.gyro, dc))
    fb.close()
    print(sensor.gyro[1])

    t+= 1
    time.sleep(0.25)
    