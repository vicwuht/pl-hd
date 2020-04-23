import socket
import datetime

HOST = '0.0.0.0'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn,addr = s.accept()
    print("client %s is connected" % str(addr))
    data = "server time is " + str(datetime.datetime.now())
    print("send current time to client")
    conn.send(data.encode('utf8'))
    conn.close()
