from simple_pid import PID
import time
import board
import adafruit_bno055

pid = PID(0.01 , 20 , 0, setpoint = 0.0279, sample_time = 0.1)     # PID(Kp, Ki, Kd, setpoint(rad/s), sample_time)
i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

pid.output_limits = (0, 5)
 
controlled_system = sensor.gyro                         # sets the gyro output to the value the system is trying to control

w = controlled_system.update(0)




















