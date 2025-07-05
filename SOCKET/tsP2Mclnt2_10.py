#_*_coding:utf-8_*_
#网络编程(使用广播模式实现：多用户、多房间、全双工聊天客户端)
import socket,select,threading
import time
HOST = socket.gethostname()
PORT = 8080
ADDR = (HOST,PORT)
BUFSIZE = 1024
FLAG = 1

#将服务器与客户端建立连接
def conn():
    tcpClisock = socket.socket()
    tcpClisock.connect(ADDR)
    return tcpClisock

#接收信息
def lis(tcpClisock):
    my = [tcpClisock]
    while(True):
        r,w,e = select.select(my,[],[])
        if tcpClisock in r:
            data = (tcpClisock.recv(BUFSIZE)).decode('utf-8')           
            n = 5
            while(data == ''):
                time.sleep(0.1)
                n = n-1    
            print(data)       
            if data == '':
                print('服务器被关闭,客户端自动退出!')
                global FLAG
                FLAG = 0
                break
            

#发送信息
def talk(tcpClisock):
    while(True):
        if FLAG == 1:
            info =input()
        else:
            break
        try:
            tcpClisock.send(info.encode('utf-8'))
        except Exception as e:
            print('服务器已被关闭')
            break

def main():
    tcpClisock = conn()
    t = threading.Thread(target=lis,args=(tcpClisock,))
    t.start()    
    t1 = threading.Thread(target=talk,args=(tcpClisock,))
    t1.start()

if __name__ == '__main__':
    main()



