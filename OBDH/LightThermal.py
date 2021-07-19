import time
import board
import adafruit_mlx90640
import numpy as np
import adafruit_tca9548a
import matplotlib.pyplot as plt
import adafruit_bno055
import smbus

def thermal():
    global frame_values
    frame_values = []

    for h in range(24):
        for w in range(32):
            frame_values = np.append(frame_values,round(frame[h * 32 + w],2))

    global tt
    tt = np.resize(frame_values, (24,32))
    print(frame_values)
    return frame_values
    return tt

def LightSensor(multiplexer,i2c_channel_setup):
    global green, red, blue
#     bus = smbus.SMBus(1) #define the bus
    bus.write_byte(multiplexer,channel_array[i2c_channel_setup]) #tell the mux which channel to connect
#
#     # Select configuration-1 register, 0x01(01)
#     # and 0x0D(13) Operation: RGB, Range: 10000 lux, Res: 16 Bits
#     # or 0x05(5) Operation: RGB, Range: 375 lux (better accuracy), Res: 16 Bits
#     bus.write_byte_data(isl29125_address, 0x01, 0x05)
#     time.sleep(0.5)
    data = bus.read_i2c_block_data(isl29125_address, 0x09, 6) #read data

    # Convert data
    green = data[1] * 256 + data[0] #[lux]
    red = data[3] * 256 + data[2] #[lux]
    blue = data[5] * 256 + data[4] #[lux]


    return green, red, blue

def imu():
    global imu_out
    imu_out = [imu_i2c.euler, imu_i2c.gyro, imu_i2c.acceleration]
    return imu_out

####################

mux_address = 0x70
isl29125_address = 0x44
isl29125_top_channel = 7
isl29125_mid_channel = 3
isl29125_bottom_channel = 2

i2c = board.I2C() # setup I2C
tca = adafruit_tca9548a.TCA9548A(i2c) # begin MLX90640 with I2C comm

tsl6 = adafruit_mlx90640.MLX90640(tca[4]) #I2C comm with thermal camera (channel 4)
tsl6.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ # set refresh rate
frame = [0] * 768 # setup array for storing all 768 temperatures

imu_i2c = adafruit_bno055.BNO055_I2C(tca[6]) #I2C comm with IMU (channel 6)

bus = smbus.SMBus(1) #define the bus
# Select configuration-1 register, 0x01(01)
# and 0x0D(13) Operation: RGB, Range: 10000 lux, Res: 16 Bits
# or 0x05(5) Operation: RGB, Range: 375 lux (better accuracy), Res: 16 Bits
bus.write_byte(mux_address,channel_array[isl29125_top_channel]) #tell the mux to connect with channel 0
bus.write_byte_data(isl29125_address, 0x01, 0x05) #selecting op mode, range, and res
bus.write_byte(mux_address,channel_array[isl29125_mid_channel]) #tell the mux to connect with channel 4
bus.write_byte_data(isl29125_address, 0x01, 0x05) #selecting op mode, range, and res
bus.write_byte(mux_address,channel_array[isl29125_bottom_channel]) #tell the mux to connect with channel 5
bus.write_byte_data(isl29125_address, 0x01, 0x05) #selecting op mode, range, and res

#If you want a colored thermal image, uncomment this line and the ones in the while loop:
# create_plot()

while True:
####################
# Read thermal camera
    stamp = time.monotonic()
    tsl6.getFrame(frame)
    frame = print_temp_values()

####################
# Write data
#     fb = open('/home/pi/Documents/Sensors/MLX90640/Frame_data','a')
#     fb.write('%s \n' % (frame))
#     fb.close()

####################
# Read light sensor
    data1 = I2C_setup(mux_address,isl29125_top_channel)
    data2 = I2C_setup(mux_address,isl29125_mid_channel)
    data3 = I2C_setup(mux_address,isl29125_bottom_channel)
    light = [data1,data2,data3]
    print(data1, data2, data3)

####################
# Read IMU
    print(imu()[0])
    f = open("Thermal.csv", "a")
    np.savetxt(f,tt, fmt="%1.1f",delimiter=",")
    f.write("\n")
    f.close()

    f = open("IMU.csv", "a")
    np.savetxt(f,imu_out, fmt="%1.1f",delimiter=",")
    f.write("\n")
    f.close()

    f = open("Light.csv", "a")
    np.savetxt(f,light, fmt="%1.1f",delimiter=",")
    f.write("\n")
    f.close()

####################
#If you want a colored thermal image, uncomment these lines:
#     t1 = time.monotonic()
#     try:
#         print_plot()
#     except ValueError:
#         print('error')
#         continue # if error, just read again

####################
# Mandatory pause
    plt.pause(0.5)
