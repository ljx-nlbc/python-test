#_*_ conding:UTF-8 _*_
#网络编程学习(TCP服务器)
#接受来自客户端的消息，然后将消息加上时间戳前缀并返回客户端
import socket
import os
from time import ctime
#创建套接字
Tcps = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定端口号
#host = socket.gethostname()#获取主机名
host = ''
port = 8080#端口号
ADDR = (host,port)
try:
    Tcps.bind(ADDR)
except OSError:
    print('服务器繁忙，请稍后再连...')
#监听
Tcps.listen(5)
#设置接收客户端数据的最大字节值
BUFSIZE = 2048
while(True):
    print('waiting for connection...')
    #与客户端建立连接
    tcpCliSock,addr = Tcps.accept()
    print('...connrcted from:',addr)
    #与客户端进行通信
    while(True):
        #接收客户端来信
        data = tcpCliSock.recv(BUFSIZE)
        data = data.decode('utf-8')
        if not data:
            break
        #将数据返回给客户端
        #tcpCliSock.send(bytes('[%s] %s'%(ctime(),data),'utf-8'))
        if data == 'time':
            sdata = [ctime()]
        elif data == 'name':
            sdata = [os.name]
        elif 'ls' in data:
            path = data.split(' ')
            if len(path) == 1:
                sdata = os.listdir()
            else:
                try:
                    sdata = os.listdir(path[1])
                except FileNotFoundError:
                    sdata = [('{0}:不存在，请重新输入...'.format(path[1]))]
        else:
            sdata = ['指令无效，请重新输入！']
        for i in range(len(sdata)):
            tcpCliSock.send((sdata[i] + ' ').encode('utf-8'))
            
    tcpCliSock.close()




