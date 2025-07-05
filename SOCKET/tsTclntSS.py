#_*_conding:'utf-8'_*_
#网络编程(SocketServerTCP客户端)
from socket import *

host = '127.0.0.1'
port = 8080
BUFSIZE = 1024
ADDR = (host,port)

while(True):
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('>')
    if not data:
        break
    tcpCliSock.send(bytes('%s\r\n'%data,'utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8').strip())
    tcpCliSock.close()