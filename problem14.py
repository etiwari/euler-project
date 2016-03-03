#!/usr/bin/env python
import time

start = time.time()
count = 0
def function(var):
	global count
	while var>1:
		count += 1
		if var%2 == 0:
			var = var/2
		else:
			var = 3*var + 1
def main():
	maxinfo = [0,0]
	i = 0
	while i<1000000:
		global count
		count = 0
		function(i)
		if count>maxinfo[0]:
			maxinfo[0] = count
			maxinfo[1] = i
		i+=1
	return maxinfo[1]
print "Answer: %s" %main()
time_elapsed = time.time() - start
print "Time Elapsed: %s" %time_elapsed