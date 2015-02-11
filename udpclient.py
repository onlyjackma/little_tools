#!/usr/bin/env python
import socket,traceback,sys
host = sys.argv[1]
port =12346
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
while 1:
	try:
		#message,address = s.recvfrom(8129)
		data="hello  man"
		s.sendto(data,("127.0.0.1",12345))
		#print "GOT data from ",address,message
		break
	except KeyboardInterrupt:
		exit()
	except :
		traceback.print_exc()
