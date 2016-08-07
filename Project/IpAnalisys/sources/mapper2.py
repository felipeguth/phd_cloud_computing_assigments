#!/usr/bin/python

import sys;
import re;

for line in sys.stdin:
	try:
		(ip, a,b,dateS,d,mtd,linkS,hstr, p, p2) = re.split("[ \t]+", line.strip())			
		print '%s\t%s' % (ip, "1") 				
	except ValueError:
		continue
		
	
	
	
	
