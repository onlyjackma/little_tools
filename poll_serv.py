#!/usr/bin/env python
import socket,select
s = socket.socket()
host = ""
port = 1234

s.bind((host,port))

fdmap = {s.fileno():s}
s.listen(5)
p = select.poll()
p.register(s)
while True:
	events = p.poll()
	for fd,event in events:
		if fd == s.fileno():
			c,addr = s.accept()
			print "Got connection from",addr
			p.register(c)
			fdmap[c.fileno()] = c
		elif event & select.POLLIN:
			data = fdmap[fd].recv(1024)
			fdmap[fd].send(data)
			if not data:
				print fdmap[fd].getpeername(),'disconnected'
				p.unregister(fdmap[fd])
				del fdmap[fd]
			else:
				print data

