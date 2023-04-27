import smbus
import time

# Define I2C bus number and device address
bus_number = 1
device_address = 0x68

# Define register addresses for BN055
reg_acc = 0x3B
reg_gyro = 0x43
reg_mag = 0x03

# Initialize I2C bus
bus = smbus.SMBus(bus_number)

# Enable accelerometer and gyroscope
bus.write_byte_data(device_address, 0x6B, 0b00000000)

while True:

    # Read gyroscope data
    gyro_x = bus.read_word_data(device_address, reg_gyro)
    gyro_y = bus.read_word_data(device_address, reg_gyro + 2)
    gyro_z = bus.read_word_data(device_address, reg_gyro + 4)


    gyro_x = -(gyro_x & 0xFFFF ^ 0xFFFF) if gyro_x & 0x8000 else gyro_x
    gyro_y = -(gyro_y & 0xFFFF ^ 0xFFFF) if gyro_y & 0x8000 else gyro_y
    gyro_z = -(gyro_z & 0xFFFF ^ 0xFFFF) if gyro_z & 0x8000 else gyro_z

    # Print data
    print("Gyroscope (deg/s): x = %.2f, y = %.2f, z = %.2f" % (gyro_x / 131.0, gyro_y / 131.0, gyro_z / 131.0))
