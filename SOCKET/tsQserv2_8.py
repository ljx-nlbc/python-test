#_*_ coding:'utf-8'_*_
#网络编程2-7练习:全双工聊天。
#全双工聊天服务器(将用户A和用户B的通信通过服务器传输)
from socket import *
import threading
from time import ctime
import re
HOST = ''
PORT = 8080
ADDR = (HOST,PORT)
BUFSIZE = 1024

#记录连接的客户端的用户名和套接字对应的关系
clients = {}
#记录了通信双方的套接字对应
chatwith = {}
#创建服务器套接字
tcpSerSock = socket(AF_INET,SOCK_STREAM)
#绑定套接字
tcpSerSock.bind(ADDR)
#监听链接
tcpSerSock.listen(5)
 
#处理客户端确定用户名之后发送的文本
def messageTransfrom(sock,user):
    while(True):
        data = sock.recv(BUFSIZE).decode('utf-8')
        if not data:
            if sock in chatwith.keys():
                chatwith[sock].send(data)
                del chatwith[chatwith[sock]]
                del chatwith[sock]
            del clients[user]
            sock.close()
            break
        if data == 'Quit':
            sock.send(data)
            if chatwith.keys(sock):
                data = '%s.'%data
                chatwith[sock].send(data)
                del chatwith[chatwith[sock]]
                del chatwith[sock]
            del clients[user]
            sock.close()
            break
        elif re.match('To:.+',data) is not None:
            data = data[3:]
            if data in clients.keys():
                if data == user:
                    sock.send('请不要尝试与你自己对话'.encode('utf-8'))
                else:
                    chatwith[sock] = clients[data]
                    chatwith[clients[data]] = sock
            else:
                sock.send(('用户%s没有加入'%data).encode('utf-8'))
        else:
            if sock in chatwith.keys():
                chatwith[sock].send(('[%s] %s:(%s)'%(ctime(),user,data)).encode('utf-8'))
            else:
                sock.send('目前无人和你通信'.encode('utf-8'))
            
#每个客户连接之后，都会启动一个新线程
#连接成功之后需要输入用户名
def connectThread(sock,test):
    user = None
    while(True):
        username = sock.recv(BUFSIZE).decode('utf-8')
        if not username:
            print('客户端未输入用户名...')
            break
        if username in clients.keys():
            sock.send('Reuse'.encode('utf-8'))
        else:
            sock.send('ok'.encode('utf-8'))
            clients[username] = sock
            user = username
            break
    if not user:
        sock.close()
        return
    print('The username is: %s'%user)
    messageTransfrom(sock,user)

def main():
    #等待客户端连接
    print('waiting for connection...')
    tcpCliSock,addr = tcpSerSock.accept()
    print('...connected from:',addr)
    #创建线程并运行
    ts = threading.Thread(target=connectThread,args=(tcpCliSock,None,))
    ts.start()
if __name__=="__main__":
    main()
    