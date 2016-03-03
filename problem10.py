#!/usr/bin/env python
#bad code. follows exponential order and hence taked too much time. Like way too much. Come up with a faster way of doing it.
import sys

primelist = [2]
for i in range(3,2000001,2):
	isprime = True
	for element in primelist:
		if (i%element==0):
			isprime = False
			break
	if isprime:
		primelist.append(i)
		print "%s is prime" %i
sum=0
for element in primelist:
	sum+=element
print primelist
print "Answer: %s" %sum