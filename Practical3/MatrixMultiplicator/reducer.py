#!/usr/bin/python

import sys;
import re;

key = None;

conta = 0;
contb = 0;

import numpy as np


A = []
B = []

for line in sys.stdin:
	(k1, k2, v, j, side) = re.split("[ \t]+", line.strip());
	
	if side == "L":
		A.append((k1+k2+j,v))
		conta = conta +1;
			
	elif side == "R":
		B.append((k1+k2+j,v))
		contb = contb +1;	
data = np.array(A)
col = 0
A = data[np.argsort(data[:,col])] 
data = np.array(B)
col = 0
B = data[np.argsort(data[:,col])]

pik = 0;
auxkey = None
currentkey = None

auxkey = A[0][0]
key = auxkey[:2]

for i in range(len(A)):
	auxkey = A[i][0]
	currentkey = auxkey[:2] 
	
	if key == currentkey:
		pik = pik + int(A[i][1])*int(B[i][1])
	else:
		print(key,pik)		
		key = currentkey
		pik = 0 + int(A[i][1])*int(B[i][1])

#print last sum
print(key,pik)

	


