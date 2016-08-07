#!/usr/bin/python

#read and generate file 
import sys;
import re;
import random

n = int(raw_input("Enter the number of Objects n:"))
m = int(raw_input("Enter the number dimensions p:"))

a = [[0 for col in range(m)] for row in range(n)]

for i in range(n):
	for j in range(m):
		a[i][j] = raw_input("A enter element %d %d " %(i,j))
		
	#save to file
	orig_stdout = sys.stdout
	f = file('A.txt', 'w')
	sys.stdout = f
	
	for i in range(n):
			for j in range(m):
				print("%d %d\t%s" %(i, j, a[i][j]))			
		
	sys.stdout = orig_stdout
	f.close()
