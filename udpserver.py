#!/usr/bin/env python
import socket,traceback
host = ''
port =12345
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
while 1:
	try:
		message,address = s.recvfrom(8129)
		print "GOT data from ",address,message
	except KeyboardInterrupt:
		exit()
	except :
		traceback.print_exc()
