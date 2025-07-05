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
#host = socket.gethostname()#获取本地主机名
host = input('请输入服务器IP: ')
port = input('请输入服务器端口号: ')
if port != '':
    port = int(port)
if host == '':
    host = '192.168.92.129'
if port == '':
    port = 8080
ADDR = (host,port)
BUFSIZE = 1024
flag = 0
while(True):
    if flag == 0:
        data = bytes(input('>'),'utf-8')
        if not data:
            break
    Udps.sendto(data,ADDR)
    try:
        data,addr = Udps.recvfrom(BUFSIZE)
        if not data:
            break
        print(data.decode('utf-8'))
        flag = 0
    except TimeoutError:
        print('timed out!')   
        flag = 1 
Udps.close()