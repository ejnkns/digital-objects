import json
import sys
import numpy as np
from PIL import Image
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
with open("integers.txt", "w") as outfile:
	json.dump(integers, outfile)
	numpy_integers = np.asarray(integers)
	numpy_integers.tofile("integers.csv", sep="\n")
with open("integers.txt", "r") as infile:
	integers = json.load(infile)

print(len(integers))
pixels = int(sqrt(len(integers)/3))
# 1 byte = 8 bits, 
w, h, d = pixels, pixels, 3
#integers = integers[::w*h*d]
data = np.zeros((h, w, d), dtype=np.uint8)

count = 0
for i in range(w):
	for j in range(h):
		data[i, j] = [integers[count], integers[count+1], integers[count+2]] 
		count += 3 

img = Image.fromarray(data, 'RGB')
img.save(filePath + '.png')
