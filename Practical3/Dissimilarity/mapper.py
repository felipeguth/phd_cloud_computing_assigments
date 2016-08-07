#!/usr/bin/python

import sys;
import re;

#dimensions of mats
n = int(sys.argv[1]);
p = int(sys.argv[2]);

A = [[0 for col in range(p)] for row in range(n)]


#import mat
for line in sys.stdin:
	(i, j, v) = re.split("[ \t]+", line.strip());
	i = int(i)
	j = int(j)
	v = int(v)
	A[i][j] = v	
	
#produce output map - key value

for no in range(1,n):
	aux =0
	#while(aux != no):
	for aux in range(0,p):
		if aux != no:
			for ne in range(0,p):
				print("%d %d \t%d" % (no,aux,A[no][ne]))		
				#print(no,aux,A[no][ne])
				print("%d %d \t%d" % (no,aux, A[aux][ne]))
		aux = aux + 1;
