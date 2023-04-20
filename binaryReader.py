import sys
import numpy as np

f = np.fromfile(open(r"C:\Users\citro\Documents\HackRF\storage\fileSink"), dtype=np.uint8)

np.set_printoptions(threshold=2000000) # I can't get the array to untruncate aniketh!!!!!
# np.set_printoptions(threshold=sys.maxsize)

print("Var type: ")
print(type(f))

print("Truncated array: ")
print(f)