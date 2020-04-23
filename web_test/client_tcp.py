import socket

HOST = '127.0.0.1'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
print("connecting to server")
data = s.recv(1024)
print("client get from server: %s" % (str(data)))
s.close
