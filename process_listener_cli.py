#!/usr/bin/env python
from multiprocessing.connection import Client
conn = Client(("127.0.0.1",15000),authkey="12345")
conn.send((2,4))
r = conn.recv()
print(r)
conn.send(("Hello","World"))
r = conn.recv()
print(r)
conn.close()

