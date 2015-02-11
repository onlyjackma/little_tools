#!/usr/bin/env python
import threading
import time

def clock(interval):
	while True:
		print("The time is %s" % time.ctime())
		time.sleep(interval)

t1 = threading.Thread(target=clock,args=(5,))
t1.daemon = True
t1.start()
t1.join()
