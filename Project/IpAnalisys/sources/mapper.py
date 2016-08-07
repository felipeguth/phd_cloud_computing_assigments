#!/usr/bin/python

import sys;
import re;
from datetime import datetime

#filter data format dd/mm/yyyy 31/12/2014
#no filter data params should be passed as  0 0

date1 = sys.argv[1];
date2 = sys.argv[2];


if (int(date1) == 0): #No filter
	for line in sys.stdin:
		try:
			(ip, a,b,dateS,d,mtd,linkS,hstr, p, p2) = re.split("[ \t]+", line.strip())			
			print '%s\t%s' % (ip, "1") 				
		except ValueError:
			continue
else: #filter
	
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
		
	
	
	
	
	
