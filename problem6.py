#!/usr/bin/env python
import sys

sum1 = 0
sum2 = 0
i = 1
while i<=100:
	sum1+= (i*i)
	sum2+= i
	i += 1
print (sum2*sum2)-sum1