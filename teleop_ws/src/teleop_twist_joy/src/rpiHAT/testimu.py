from datetime import datetime
from time import sleep

from rpiHAT import LSM6DS33

def callimu():
    imu = LSM6DS33()
    imu.enable()

    while True:
        print("Accelerometer (G):", imu.get_gyro_angular_velocity(), imu.getAccelerometer3Angles(), imu.get_accelerometer_angles())
        sleep(1)


if __name__ == '__main__':
    callimu()
