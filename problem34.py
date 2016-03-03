#!/usr/bin/env python
import time

start = time.time()
def factorial(var):
	product = 1
	while var>=1:
		product *= var
		var -= 1
	return product
def function(var):
	var_copy = var
	sum = 0
	while var_copy!=0:
		sum += factorial(var_copy%10)
		var_copy /= 10
	if var == sum:
		return var
	else:
		return 0
i=10
ans_sum=0
while i<50000:
	ans_sum += function(i)
	print "Answer: %s" %ans_sum
	i += 1
time_elapsed = time.time() - start
print "Time Elapsed: %s" %time_elapsed