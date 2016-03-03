#!/usr/bin/env python

def change(x):
	r = ''
	s = ''
	start = 0
	x = ' ' + x + ' '
	for i in range(len(x)):
		if i==0 :
			p = x.find(' ', start+1, len(x))
			if x[1] in 'aeiouAEIOU':
				s += x[start+1:p+1]# : replaced with ,
				r = x[start+1:p]
			word = r
			long = len(r)
			start = p
		else:
			if x[i] == ' ': # missing :
				p = x.find(' ', start+1, len(x))
				if p != -1:
					if x[i+1] in 'aeiouAEIOU':
						s += x[start+1:p+1]
						r = x[start+1:p]
					if long < len(r):
						long = len(r)
						word = r
					start = p
	return long, word, s

a = raw_input('Enter string: ')
print change(a)