#!/usr/bin/env python
HOST = '127.0.0.1'      # Symbolic name meaning the local host
HOST = ''
PORT = 50008            # Arbitrary non-privileged port
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print "Listening on %s:%s" % (HOST, PORT)
while True:
    conn, addr = s.accept()
    print 'Connected by', addr,
    data = conn.recv(1024)
    print data
    conn.close()
