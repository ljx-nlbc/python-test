#_*_ conding:UTF-8 _*_
#网络编程学习(TCP客户端)
#输入发送信息到服务端，并从服务端返回添加了时间戳的相同信息
import socket
print('如需使用默认服务器IP或者默认端口号请直接回车。')
#创建套接字
Tcps = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Tcps.settimeout(5)
timeout = Tcps.gettimeout()
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
    port = 8080#设置端口号
ADDR = (host,port)
try:
    Tcps.connect(ADDR)
except ConnectionRefusedError as e:
    print('Connection refused!')
except TimeoutError:
    print('timed out!')
else:
    #设置最大接收字节
    BUFSIZE = 1024
    while(True):
        data = input('>')
        if not data:
            break
        #向服务器发送信息
        Tcps.send(bytes(data,'utf-8'))
        #接收服务器的信息
        data = Tcps.recv(BUFSIZE)
        if not data:
            break
        print(data.decode('utf-8'))
    Tcps.close()

