#!/usr/bin/env python
import sys

maximum = 0

def palindromecheck(var):
	result = 0
	while var != 0:
		c = var%10
		result = (result*10) + c
		var = var/10
	return result

def innerloop(var):
	global maximum
	b = 101
	while(b < 1000):
		c = var*b
		if (c == palindromecheck(c) and c > maximum):
			maximum = c
			print "%s x %s = %s = %s" % (var, b, c, palindromecheck(c))
		b += 1

a = 101
while(a < 1000):
	innerloop(a)
	a += 1
print maximum