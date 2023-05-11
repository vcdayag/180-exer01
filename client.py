import socket
from array import array
import interpolation
import pickle
host = '127.0.0.1'
port = 5058

s = socket.socket()
s.connect((host,port))
s.sendall(b'Connected Client')
binaryinput = b''

matsize = int(s.recv(2).decode())
counter = 0
while counter < matsize:
    data = s.recv(4096)
    if not data:
        break
    counter += 4096
    print("resib")
    binaryinput += data
    data = b''

print("outside")
# mat = interpolation.generateCornersMatrix(binaryinput.decode())
cornermat = eval(binaryinput.decode())
print(cornermat)
n = len(cornermat[0])
# output = interpolation.buildMatrixFromCorners(cornermat)
# print(output)
print("n",n)

