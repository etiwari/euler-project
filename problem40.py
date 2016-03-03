#!/usr/bin/env python
import time

start = time.time()
def function(var):
	decimal = []
	while var!=0:
		decimal.append(var%10)
		var /= 10
	decimal.reverse()
	return decimal
def mainfunc():
	i=1
	final_list = []
	while i<100000:
		final_list += function(i)
		i += 1
	print "Answer: %s" %(final_list[0]*final_list[9]*final_list[99]*final_list[999]*final_list[9999]*final_list[99999])
mainfunc()
time_elapsed = time.time() - start
print "Time Elapsed: %s" %time_elapsed