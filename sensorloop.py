import time
import adafruit_bno055 as adb
import board
import time
import bme280
import smbus2
from datetime import datetime

def writeToFile(str):
    try:
        f = open("sensor.txt","x")
    except FileExistsError:
        f = open("sensor.txt","a")
    f.write(str + "\n")


def main():
    i2c = board.I2C()

    port = 1
    address = 0x77
    bus = smbus2.SMBus(port)
    calib_param = bme280.load_calibration_params(bus, address)

    sensor = adb.BNO055_I2C(i2c)

    while True:
        writeToFile(datetime.now() + "")
        writeToFile("gyro: " + str(sensor.gyro), end = " ")
        writeToFile("acceleration: " + str(sensor.acceleration), end = " ")
        writeToFile("gravity: " + str(sensor.gravity), end = " ")
        writeToFile("magnetic: " + str(sensor.magnetic), end = " ")
        writeToFile("euler: " + str(sensor.euler))
        time.sleep(1)

        data = bme280.sample(bus, address, calib_param)
        writeToFile("TEMP: " + str(data.temperature) + " PRESS: " + str(data.pressure) + " HUMID: " + str(data.humidity))
        time.sleep(1)