import sys
# parse command line
file_name_given = "/home/fgub/4300.txt"

if file_name_given:
    inf = open(file_name_given)
    sys.stdin = inf
else:
    inf = sys.stdin
    print "Else"
