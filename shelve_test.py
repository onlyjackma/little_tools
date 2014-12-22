#!/usr/bin/env python
import shelve
s = shelve.open('test.dat')
s['X'] = ['a','b','c']
s['X'].append('d')
print s['X']
