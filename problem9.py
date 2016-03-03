#!/usr/bin/env python
import sys

for a in range(1,1000):
	for b in range(1,1000):
		if (a<b) and ((a*a)+(b*b)==(1000-(a+b))*(1000-(a+b))):
			print "Answer: %s" %(a*b*(1000-(a+b)))
			print "%s ,%s ,%s" %(a,b,(1000-(a+b)))