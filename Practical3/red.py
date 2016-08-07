#!/usr/bin/python

import sys;
import re;

if len(sys.argv) != 4:
	print("Syntax: %s " % (sys.argv[0]));
	exit(1);

n = int(sys.argv[1]);
for line in sys.stdin:
	(i, j, v) = re.split("[ \t]+", line.strip());
	for c in range(1, n + 1):
		print("%d %s %s\t%s R" % (c, i, j, v));
