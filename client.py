import socket
from array import array
import interpolation

host = '127.0.0.1'
port = 5050

s = socket.socket()
s.connect((host,port))
s.sendall(b'Hello, world')
data = s.recv(64000)
mat = eval(data)
n = len(mat[0])
output = interpolation.terrain_inter(mat,n,(0,n))
print(output)

