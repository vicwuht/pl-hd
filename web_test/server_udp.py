import socket

HOST = '0.0.0.0'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))

while True:
    data, address = s.recvfrom(1024)
    print(f"getting {str(data, encoding = 'utf8')} from {address}")

s.close()
