#_*_ coding:'utf-8'_*_
#网络编程2-7练习:半双工聊天。
#半双工聊天客户端
from socket import *
import threading
import time
PORT = '127.0.0.1'
HOST = 8080
ADDR = (PORT,HOST)
BUFSIZE = 1024
#创建套接字
tcpClisock = socket(AF_INET,SOCK_STREAM)
#尝试连接服务器
tcpClisock.connect(ADDR)

#发送消息
def send_msg(sock):
    while(True):
        try:
            data = input('输入向服务器发送的消息 >').encode('utf-8')
            sock.send(data)
            if data == 'Quit':
                break
        except:
            print('Error!send')
#接收消息
def recv_msg(sock):
    while(True):
        try:
            data = sock.recv(BUFSIZE)
            data = data.decode('utf-8')
            if data == 'Quit.':
                print('他已退出聊天...')
                continue
            if data == 'Quit':
                break
            print('\n服务器回复的消息为:',data)
        except:
            print('Error!recv')

def main():
    print('连接成功！')
    while(True):
        username = input('你的账户名字(退出请直接输入quit):').encode('utf-8')
        tcpClisock.send(username)
        if not username:
            break
        response = tcpClisock.recv(BUFSIZE)
        if response == 'Reuse':
            print('该账户已经存在，请设置一个新账户')
            continue
        else:
            print('welcome!%s'%username.decode('utf-8'))
            break
    if not username:
        tcpClisock.close()
    ts = threading.Thread(target=send_msg,args=(tcpClisock,))
    tr = threading.Thread(target=recv_msg,args=(tcpClisock,))
    ts.start()
    tr.start()

if __name__ == "__main__":
    main()
    
    


