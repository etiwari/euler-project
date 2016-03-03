#!/usr/bin/env python
import sys

primelist = []
primelist.append(2)
b = 3
prime = True
counter = 1
while counter<10002:
	for i in primelist:
		if b%i == 0:
			prime = False
			break
	if prime:
		primelist.append(b)
		counter += 1
	prime = True
	b += 2
print primelist[10000]