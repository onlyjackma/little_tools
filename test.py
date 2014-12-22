#!/usr/bin/env python
import sys
#print __name__

args = sys.argv[1:]
args.reverse()
print " ".join(args)
print ("%s %d" % (sys.argv[0],len(sys.argv)))

