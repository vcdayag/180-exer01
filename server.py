import socket

host = '127.0.0.1'
port = 5050

s = socket.socket()
s.bind((host,port))
s.listen()
conn, addr = s.accept()

with conn:
    print("Connected by", addr)
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("na send all")
        conn.sendall(data)