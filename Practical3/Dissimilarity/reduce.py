#!/usr/bin/python

import sys;
import re;
import math;

key = None;
dik = 0.0;
auxkey = None
currentkey = None
cont = 0;
aux = 0;
#values are organized in order

#take first key value
for line in sys.stdin:
	(k1, k2, v) = re.split("[ \t]+", line.strip());
	key = k1+k2
	aux = int(v)
	cont = 1;	
	break

for line in sys.stdin:
	(k1, k2, v) = re.split("[ \t]+", line.strip());	
	
	currentkey = k1+k2	
	
	if key == currentkey:
		if cont == 0:
			aux = int(v)
			cont = 1;
		else:
			dik = dik + ( aux - int(v))*( aux - int(v))
			cont = 0;
	else:
		print(key,  math.sqrt(dik))		
		key = currentkey
		aux = int(v)
		cont = 1
		dik = 0
		
		
#print last calc
print(key,math.sqrt(dik))

	


