#!/usr/bin/python

import sys;
import re;

#dimensions of mats
l = int(sys.argv[1]);
m = int(sys.argv[2]);
n = int(sys.argv[3]);

mat = [[0 for row in range(m)] for col in range(l)]
#B = [[0 for row in range(n)] for col in range(m)]


#import mat
for line in sys.stdin:
	(namem,i, j, v) = re.split("[ \t]+", line.strip());
	i = int(i)
	j = int(j)
	v = int(v)

	mat[i][j] = v	
	
#produce output map - key value

for i in range(0,l):
	for j in range(0,m):
		for k in range(0,n):
			print("%d %d \t%d" % (i, k, mat[i][j]))
			#print("%d %s %s\t%s R" % (c, i, j, v));
