#_*_ coding:'utf-8'_*_
#网络编程2-7练习:半双工聊天。
#半双工聊天服务器
from socket import *
HOST = ''
PORT = 8080
ADDR = (HOST,PORT)
BUFSIZE = 1024
#创建服务器套接字
tcpSerSock = socket(AF_INET,SOCK_STREAM)
#绑定套接字
tcpSerSock.bind(ADDR)
#监听链接
tcpSerSock.listen(5)
while(True):
    #等待客户端连接
    print('waiting for connection...')
    tcpCliSock,addr = tcpSerSock.accept()
    print('...connected from:',addr)
    while(True):
        print('请等待客户端发来的消息...')
        data = tcpCliSock.recv(BUFSIZE)
        data = data.decode('utf-8')
        if not data:
            print(addr,'已关闭连接')
            break
        else:
            print('客户端发来的消息为:',data)    
            data = input('输入向客户端发送的消息 >').encode('utf-8')       
            while(True):               
                if not data:
                    tcpCliSock.close()
                    print(addr,'已关闭连接')
                    break
                else:
                    tcpCliSock.send(data)
                    break
            if not data:
                break
    tcpCliSock.close()