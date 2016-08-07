#!/usr/bin/python

import sys;
import re;
from datetime import datetime

#Take date parameters
for line in sys.stdin:
		
	try:
		(date1,date2) = re.split("[ \t]+", line.strip())			
	 				
	except ValueError:
		date1 = 0
		continue
		
	break
	
try:
			
	if (int(date1) == 0): #No filter in date params
		f = 0
		for line in sys.stdin:
			try:
				(ip, a,b,dateS,d,mtd,linkS,hstr, p, p2) = re.split("[ \t]+", line.strip())			
				print '%s\t%s' % (ip, "1") 				
			except ValueError:
				continue
	else:
		f =1;	
except ValueError:
	f =1
	

if f ==1 : #filter
	
	dfrom = datetime.strptime(date1, "%d/%m/%Y")
	dto   = datetime.strptime(date2, "%d/%m/%Y")


	#read raw file and produce key, value output
	for line in sys.stdin:
		
		#Filter by date	
		try:
			(ip, a,b,dateS,d,mtd,linkS,hstr, p, p2) = re.split("[ \t]+", line.strip())
			
			dateS = dateS[1:12]
			dateS = datetime.strptime(dateS, "%d/%b/%Y")
			
			#print(dfrom,dto,dateS)
			if (dateS >= dfrom) and (dateS <= dto):
				print '%s\t%s' % (ip, "1") 				
		except ValueError:
			continue
		

	
	
