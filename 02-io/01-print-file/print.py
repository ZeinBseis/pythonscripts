import sys
import os

fileToRead = sys.argv[1]

f = open(fileToRead, "r")

for x in f:
	print(x)


f.close
