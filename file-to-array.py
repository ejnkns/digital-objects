import sys
import numpy as np
from math import sqrt
import os

def getBits(f):
    while True:
            b = f.read(1)
            if not b: break
            b = ord(b)
            for i in range(8):
                    yield b & 1
                    b >>= 1

filePath = sys.argv[1]
f = open(filePath, "rb")

fileSize = os.path.getsize(filePath)

with open(filePath, 'rb') as file:
	i = 1 
	integers = []
	tempBits = ""
	for bit in getBits(file):
		tempBits += str(bit)
		if i%8==0:
			integers.append(int(tempBits, 2))
			tempBits = ""
		i += 1
numpy_integers = np.asarray(integers)
numpy_integers.tofile(filePath + "-array.csv", sep="\n")
