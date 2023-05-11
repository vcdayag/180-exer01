import socket
import interpolation
import sys

host = '127.0.0.1'
# port = 5050

n = int(sys.argv[1]) + 1
port = int(sys.argv[2])
# number of threads
status = int(sys.argv[3])

s = socket.socket()
s.bind((host,port))
s.listen()
conn, addr = s.accept()

with conn:
    print("Connected by", addr)
    
    while True:
        data = conn.recv(64000)
        if not data:
            break
        print(data.decode())
        print("na send all")
        mat = interpolation.generateMatrix(n)
        
        conn.sendall(str(mat).encode())
        print(mat)