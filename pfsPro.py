#importing sensors code, here its printing smth for testing
from sensorloop import main
import subprocess
import threading

#install pkgs
def pkgInstall():
    # radio pkgs
    subprocess.run("conda install -c conda-forge gnuradio", shell = True)
    subprocess.run("conda install -c conda-forge gnuradio-osmosdr", shell = True)
    subprocess.run("conda install -c conda-forge sip", shell = True)
    subprocess.run("conda install -c conda-forge pyqt5-sip", shell = True)
    subprocess.run("conda install -c conda-forge gnuradio-qtgui", shell = True)
    subprocess.run("conda install -c conda-forge argparse", shell = True)
    subprocess.run("conda install -c conda-forge hackrf", shell=True)

     # sensor pkgs
    subprocess.run("sudo apt-get install i2c-tools", shell = True)
    subprocess.run("sudo pip3 install RPi.bme280", shell = True)
    subprocess.run("sudo pip3 install adafruit-circuitpython-bno055", shell = True)
    subprocess.run("sudo pip3 install adafruit-circuitpython-dps310", shell = True)
    print("Pkgs installed")
   
i=0

def HackRF():
    #try:
    #    f = open("sweep.txt","x")
    #except FileExistsError:
    #    f = open("sweep.txt","a")
    #f.close()
    subprocess.Popen("hackrf_sweep -r 'sweep{}.txt' ".format(i), shell=True)


try:
    print("entered try main")
    while True:
        try:
            i+=1
            # HackRF init
            #threadHackRF = threading.Thread(target = HackRF)
            # sensor init
            #sensorThread = threading.Thread(target = main)
          
            # starting HackRF init
            #threadHackRF.start()
            # starting sensor init
            #sensorThread.start()
            HackRF()
            main()
           
           
        except ModuleNotFoundError:
            # reinstall pkgs
            print("installing pkgs")
            pkgInstall()


except:
    print("Program terminated: Flight ended")
    #threadHackRF.join()
    #sensorThread.join()
