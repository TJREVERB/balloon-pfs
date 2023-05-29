def writeToFile(data):
    with open("sensor.txt", "a") as f:
        f.write(data + "\n")

def main():
    import time
    import adafruit_bno055 as adb
    import board
    import time
    import bme280
    import smbus2
    from datetime import datetime
    import adafruit_dps310

    i2c = board.I2C()

    port = 1
    address_bme = 0x77
    address_dps = 0x77
    bus = smbus2.SMBus(port)
    calib_param = bme280.load_calibration_params(bus, address_bme)

    bno_sensor = adb.BNO055_I2C(i2c)
    dps_sensor = adafruit_dps310.DPS310(bus, address=address_dps)

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writeToFile("Time: " + timestamp)

        writeToFile("Gyro: " + str(bno_sensor.gyro))
        writeToFile("Acceleration: " + str(bno_sensor.acceleration))
        writeToFile("Gravity: " + str(bno_sensor.gravity))
        writeToFile("Magnetic: " + str(bno_sensor.magnetic))
        writeToFile("Euler: " + str(bno_sensor.euler))

        bme_data = bme280.sample(bus, address_bme, calib_param)
        writeToFile("Temperature: " + str(bme_data.temperature) + " C")
        writeToFile("Pressure: " + str(bme_data.pressure) + " Pa")
        writeToFile("Humidity: " + str(bme_data.humidity) + " %")

        dps_temp = dps_sensor.temperature
        dps_pressure = dps_sensor.pressure
        writeToFile("DPS310 Temperature: " + str(dps_temp) + " C")
        writeToFile("DPS310 Pressure: " + str(dps_pressure) + " Pa")

        writeToFile("")  # Empty line for separation

        time.sleep(1)

if __name__ == "__main__":
    main()
