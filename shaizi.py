#!/usr/bin/env python
from random import randrange
num = input("How many dice? :")
sides = input("How many sides per dice? :")
sum = 0
for i in range(num):
	pnum = randrange(sides) + 1
	print pnum
	sum += pnum
	

print 'The result is ',sum
