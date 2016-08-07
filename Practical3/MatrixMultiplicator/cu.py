#!/usr/bin/python

#read and generate file 
import sys;
import re;
import random

n = int(raw_input("Enter the number of rows of A:"))
m = int(raw_input("Enter the number of columns of A and rows of B:"))
k = int(raw_input("Enter the number of columns of B:"))


a = [[0 for col in range(m)] for row in range(n)]
b = [[0 for col in range(k)] for row in range(m)]

for i in range(n):
	for j in range(m):
		a[i][j] = raw_input("A enter element %d %d " %(i,j))
		
	#save to file
	orig_stdout = sys.stdout
	f = file('A.txt', 'w')
	sys.stdout = f
	
	for i in range(n):
			for j in range(m):
				print("%s %d %d\t%s" %("a",i, j, a[i][j]))			
		
	sys.stdout = orig_stdout
	f.close()

for i in range(m):
	for j in range(k):
		b[i][j] = raw_input("B enter element %d %d " %(i,j))
	
	#save to file
	orig_stdout = sys.stdout
	f = file('B.txt', 'w')
	sys.stdout = f
	
	for i in range(m):
			for j in range(k):
				print("%s %d %d\t%s" %("b",i, j, b[i][j]))			
		
	sys.stdout = orig_stdout
	f.close()




