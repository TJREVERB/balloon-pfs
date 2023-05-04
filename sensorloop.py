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
        writeToFile("Time: "+str(datetime.now()))
        writeToFile("gyro: " + str(sensor.gyro))
        writeToFile("acceleration: " + str(sensor.acceleration))
        writeToFile("gravity: " + str(sensor.gravity))
        writeToFile("magnetic: " + str(sensor.magnetic))
        writeToFile("euler: " + str(sensor.euler))

        data = bme280.sample(bus, address, calib_param)
        writeToFile("TEMP: " + str(data.temperature) + " PRESS: " + str(data.pressure) + " HUMID: " + str(data.humidity))
       	writeToFile("\n")
        time.sleep(1)

