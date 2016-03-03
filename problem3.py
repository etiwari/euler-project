#!/usr/bin/env python
#shitty code. can se the answer way before the thing is done executing. Put a delimiter to shorten the execution time.
import sys
import math

a = 600851475143
primelist = []
primelist.append(3)
b = 5
result = 1
prime = True

while b<math.sqrt(a):
	for i in primelist:
		if b%i == 0:
			prime = False
			break
	if prime:
		primelist.append(b)
		if (a%b == 0 and b>result):
			result = b
			print str(result) + "@@@@@@@@@@@@@@@@2"
	prime = True
	b += 2
print result
