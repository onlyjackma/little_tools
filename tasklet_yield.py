#!/usr/bin/env python
from collections import deque
def foo():
	for n in xrange(5):
		print("I am foo %d" % n)
		yield

def bar():
	for n in xrange(10):
		print("I am bar %d" % n)
		yield

def spam():
	for n in xrange(7):
		print("I am spam %d" % n)
		yield

taskqueue = deque()
taskqueue.append(foo())
taskqueue.append(bar())
taskqueue.append(spam())

while taskqueue:
	task = taskqueue.pop()
	try:
		next(task)
		taskqueue.appendleft(task)
	except StopIteration:
		pass
