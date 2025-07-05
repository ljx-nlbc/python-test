#_*_ coding:UTF-8 _*_
#网络编程学习(UDP服务器)
#接收来自客户端的消息，并将加了时间戳的消息返回给客户端
import socket
from time import ctime
#创建套接字
Udps = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口号
host = ''
port = 13
ADD = (host,port)
Udps.bind(ADD)
#设置接收客户端数据的最大字节
BUFSIZE = 1024
while(True):
    print('waiting for message...')
    data,addr = Udps.recvfrom(BUFSIZE)
    data = data.decode('utf-8')
    datalist = '[{0}] {1}'.format(ctime(),data)
    Udps.sendto(bytes(datalist,'utf-8'),addr)
    print('...received from and returned to:',addr)
