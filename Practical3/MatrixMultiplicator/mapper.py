#!/usr/bin/python

import sys;
import re;

#dimensions of mats
l = int(sys.argv[1]);
m = int(sys.argv[2]);
n = int(sys.argv[3]);

A = [[0 for row in range(m)] for col in range(l)]
B = [[0 for row in range(n)] for col in range(m)]


#import mat
for line in sys.stdin:
	(mat, i, j, v) = re.split("[ \t]+", line.strip());
	i = int(i)
	j = int(j)
	v = int(v)
	if mat == "a":
		A[i][j] = v	
	elif mat == "b":
		B[i][j] = v
	
#produce output map - key value

#A
for i in range(0,l):
	for j in range(0,m):
		for k in range(0,n):
			print("%d %d \t%d %d %s" % (i, k, A[i][j],j,"L"))
			#print("%d %s %s\t%s R" % (c, i, j, v));

#B
for j in range(0,m):
	for k in range(0,n):
		for i in range(0,l):
			print("%d %d \t%d %d %s" % (i, k, B[j][k], j, "R"))
