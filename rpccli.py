#!/usr/bin/env python
from xmlrpclib import ServerProxy
s = ServerProxy('http://127.0.0.1:9000')
print s.twice(2)
