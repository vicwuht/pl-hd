import socket

HOST = '127.0.0.1'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = "udp data comming"


while True:
    s.sendto(data.encode('utf8'), (HOST, PORT))
    choise = input("print q to exit ,other going on")
    if choise == 'q':
        break

s.close()
