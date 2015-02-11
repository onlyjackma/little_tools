#!/usr/bin/env python
import time,ssl,socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',6000))
s.listen(5)

while True:
	client,addr = s.accept()
	print "Connection from ",addr
	client_ssl = ssl.wrap_socket(client,
									server_side=True,
									certfile="timecert.pem")
	client_ssl.sendall(b"HTTP/1.0 200 OK\r\n")
	client_ssl.sendall(b"Connection: Close\r\n")
	client_ssl.sendall(b"Content-type: text/plain\r\n\r\n")
	resp = time.ctime()+"\r\n";
	client_ssl.sendall(resp.encode('latin-1'))
	client_ssl.close()
	client.close()
