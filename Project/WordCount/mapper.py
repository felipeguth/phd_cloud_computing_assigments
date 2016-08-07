#!/usr/bin/env python
# mapper.py

import sys

#file_name_given = "/home/fgub/4300.txt"
#if file_name_given:
 #   inf = open(file_name_given)
  #  sys.stdin = inf
#else:
 #   inf = sys.stdin
  #  print "Else"


#get lines from stdin ---
for line in sys.stdin:
    #remove whitespace
    line = line.strip()
 
    #--- split the line into words ---
    words = line.split()
 
    #--- output tuples [word, 1] in tab-delimited format---
    for word in words:
        print '%s\t%s' % (word, "1")
