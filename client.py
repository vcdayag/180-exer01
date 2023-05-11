import socket
import pickle
host = '127.0.0.1'
port = 5060

s = socket.socket()
s.connect((host,port))
s.sendall(b'Hello, world')
masterdata = bytearray()
buffsize = 4096
while True:
    data = s.recv(buffsize)
    masterdata.extend(data)
    if len(data) < buffsize:
        break

print(pickle.loads(masterdata))

