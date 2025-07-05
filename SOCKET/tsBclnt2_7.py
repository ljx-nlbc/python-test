#_*_ coding:'utf-8'_*_
#网络编程2-7练习:半双工聊天。
#半双工聊天客户端
from socket import *
PORT = '127.0.0.1'
HOST = 8080
ADDR = (PORT,HOST)
BUFSIZE = 1024
#创建套接字
tcpClisock = socket(AF_INET,SOCK_STREAM)
#尝试连接服务器
tcpClisock.connect(ADDR)
while(True):
    data = input('输入向服务器发送的消息 >').encode('utf-8')
    if not data:
        break
    tcpClisock.send(data)
    print('等待服务器回信息')
    data = tcpClisock.recv(BUFSIZE)
    data = data.decode('utf-8')
    if not data:
        break
    print('服务器回复的消息为:',data)
tcpClisock.close()

