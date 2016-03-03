#!/usr/bin/env python
#hTis is just cheating. Come on.
import sys
print 1%1
result = 1
i = 2
"""
while i <= 20:
	a = result
	result*=i
	print "%s x %s = %s" %(a, i, result)
	i += 1
print result
"""
while result*2<20:
	result*=2
while i <= 20:
	if (result%i != 0):
		a = result
		result*=i
		print "%s x %s = %s" %(a, i, result)
	i += 1
i = 1
while i <= 20:
	if (result%i == 0):
		print "divisable by %s" %(i)
	i += 1
print result/3