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

def write_to_csv():
    
    with open('/home/pi/Desktop/VICINITY/data-prueba.csv', mode='w') as sensor_readings:
        writer = csv.DictWriter(sensor_readings, fieldnames = ["Number", "Date", "Time", "CPU Temperature", "Green", "Red", "Blue", "Temperature"])
        writer.writeheader()
        i=0
        for i in range(10):
            sensor_write = csv.writer(sensor_readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write_to_log = sensor_write.writerow([(i+1), date_now(),time_now(), cpu_temperature(), light_sensor1(),light_sensor2(),light_sensor3(),avg_temperature_camera()])
            time.sleep(2)
    
    return(write_to_log)

write_to_csv()


















