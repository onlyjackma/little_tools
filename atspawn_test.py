#!/usr/bin/env python
def spamrun(fn):
	def sayspam(*args):
		print "spam.spam,spam"
		print args
		return fn(*args)
	return sayspam

@spamrun
def useful(a,b):
	print a**2+b**2

useful(3,4)
