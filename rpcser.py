#!/usr/bin/env python
from SimpleXMLRPCServer import SimpleXMLRPCServer
s = SimpleXMLRPCServer(("",9000))
def twice(x):
    return x*2
s.register_function(twice)
s.serve_forever()

