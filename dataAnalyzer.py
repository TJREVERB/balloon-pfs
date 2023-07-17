import matplotlib.pyplot as plt
import numpy as np

filename = (input("Name of data file: "))
 
file = open(filename,"r")

#2023-05-25, 16:50:21.222442, 710000000, 715000000, 1000000.00, 20, -48.43, -49.43, -60.15, -48.49, -60.43
num_lines = sum(1 for _ in open('data.txt'))
pts = num_lines*5
xPts = np.zeros(pts)
yPts = np.zeros(pts)
npArrInd = 0
for l in file:
    arr = l.split(", ")
    hzLow=int(arr[2])
    hzHigh=int(arr[3])
    hzIncrement=hzLow
    binWidth = int(float(arr[4]))
    dbInd=6
    while(hzIncrement<hzHigh):
       xPts[npArrInd]=hzIncrement
       yPts[npArrInd]=float(arr[dbInd])
       hzIncrement += binWidth
       dbInd+=1
       npArrInd+=1
    
file.close()

plt.xlabel("Hz Values")
plt.ylabel("db Values")

plt.plot(xPts, yPts)
plt.show()