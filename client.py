import socket

host = '127.0.0.1'
port = 5050

s = socket.socket()
s.connect((host,port))
s.sendall(b'Hello, world')
data = s.recv(1024)

