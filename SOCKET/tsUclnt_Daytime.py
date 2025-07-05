#_*_ coding:'UTF-8' _*_
#网络编程(UDP客户端)
#输入发送信息到服务端，并从服务端返回添加了时间戳的相同信息
from socket import *
#创建套接字
Udps = socket(AF_INET,SOCK_DGRAM)
Udps.settimeout(5)
timeout = Udps.gettimeout()
print('超时时间:',timeout)
#连接服务器,指定主机和端口
host = "127.0.0.1"
port = getservbyname("daytime")
ADDR = (host,port)
BUFSIZE = 1024
flag = 0
while(True):
    try:
        data = '请求回复...'
        Udps.sendto(data.encode('utf-8'),ADDR)
        data,addr = Udps.recvfrom(BUFSIZE)
        if not data:
            break
        print("the server's time is:",data.decode('utf-8'))
        flag = 0
        input()
    except TimeoutError:
        print('timed out!')   
        flag = 1 
Udps.close()