#!/usr/bin/env python
from multiprocessing.connection import Listener
serv = Listener(('',15000),authkey='12345')
while True:
	conn = serv.accept()
	while True:
		try:
			x,y = conn.recv()
		except EOFError:
			break
		result = x + y
		conn.send(result)
	conn.close()
