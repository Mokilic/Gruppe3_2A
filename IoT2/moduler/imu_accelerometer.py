from mpu6050 import mpu6050
import time

def imu():
    # Create an instance of the MPU6050 sensor class, using the default address of 0x68
    sensor = mpu6050(0x68)
    
    # Get the current acceleration data from the sensor
    accel_data = sensor.get_accel_data()
    
    # Extract the x, y, and z acceleration values from the data
    x = int(accel_data['x'])
    y = int(accel_data['y'])
    z = int(accel_data['z'])

    # Return the x, y, and z values as a tuple
    return x, y, z
