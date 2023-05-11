import socket
import interpolation
import sys
import pickle

host = '127.0.0.1'
port = 5058

# size of matrix
n = int(sys.argv[1]) + 1
# input port
# port = int(sys.argv[2])
# number of threads
status = int(sys.argv[3])

s = socket.socket()
s.bind((host,port))
s.listen(5)
conn, addr = s.accept()

with conn:
    print("Connected by", addr)
    
    while True:
        data = conn.recv(4096)
        if not data:
            break
        print(data.decode())
        mat = interpolation.generateCornersMatrix(n)
        matbytes = str(mat)
        counter = 0
        
        print(matbytes)
        # conn.sendall(str(len(matbytes)).encode())
        # conn.sendall(matbytes)
        # conn.sendall(pickle.dumps(mat))