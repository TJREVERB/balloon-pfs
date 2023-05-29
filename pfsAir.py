import sensorloop
import subprocess


# install pkgs

def pkgInstall():
    # sensor pkgs
    subprocess.run("sudo apt-get install i2c-tools", shell = True)
    subprocess.run("sudo pip3 install RPi.bme280", shell = True)
    subprocess.run("sudo pip3 install adafruit-circuitpython-bno055", shell = True)
    subprocess.run("sudo pip3 install adafruit-circuitpython-dps310", shell = True)


try:
    while True:
        try:
            sensorloop.main()

        except ModuleNotFoundError:
            # reinstall pkgs
            pkgInstall()

except:
    print("Program terminated: Flight ended")
