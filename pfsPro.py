#importing sensors code, here its printing smth for testing
import sensorloop
import subprocess
import threading

#install pkgs
def pkgInstall():
    # radio pkgs
    #subprocess.run("conda install -c conda-forge gnuradio", shell = True)
    #subprocess.run("conda install -c conda-forge gnuradio-osmosdr", shell = True)
    #subprocess.run("conda install -c conda-forge sip", shell = True)
    #subprocess.run("conda install -c conda-forge pyqt5-sip", shell = True)
    #subprocess.run("conda install -c conda-forge gnuradio-qtgui", shell = True)
    #subprocess.run("conda install -c conda-forge argparse", shell = True)
    subprocess.run("conda install -c conda-forge hackrf", shell=True)
    # sensor pkgs
    subprocess.run("sudo apt-get install i2c-tools python3-pip", shell = True)
    subprocess.run("sudo pip3 install RPi.bme280", shell = True)
    subprocess.run("sudo pip3 install adafruit-circuitpython-bno055", shell = True)

def HackRF():
    try:
        f = open("sweep.txt","x")
    except FileExistsError:
        f = open("sweep.txt","a")
    f.close()
    subprocess.run("hackrf_sweep -r 'sweep.txt' ", shell=True)

try:
    while True:
        try:
            # HackRF init
            threadHackRF = threading.Thread(target = HackRF())
            # sensor init
            sensorThread = threading.Thread(target = sensorloop.main())

            # starting HackRF init
            threadHackRF.start()
            # starting sensor init
            sensorThread.start()

        except ModuleNotFoundError:
            # reinstall pkgs
            pkgInstall()

except:
    print("Program terminated: Flight ended")
