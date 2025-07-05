#_*_coding:'utf-8'_*_
#网络编程学习(使用广播模式实现：多用户、多房间、全双工聊天服务器)
import socket,select
import time

HOST = socket.gethostname()
PORT = 8080
ADDR = (HOST,PORT)
BUFSIZE = 1024

inputs = []#将连接加入到列表中
fd_name = {}#将socke与用户关系对应
roomidlist = []#房间号列表
fd_room = {}#socket与房间号的关联
roomidname = {}#房间号和用户名的关联

#创建服务器
def conn():
    print('等待连接...')
    tcpSersock = socket.socket()
    try:
        tcpSersock.bind(ADDR)
        tcpSersock.listen(5)
    except:
        print('套接字正在使用中，请稍等再连接')
        return 'tcperr'
    return tcpSersock

#与客户端进行连接
def new_coming(tcpSersock):
    tcpClisock,addr = tcpSersock.accept()
    print('欢迎用户:{0},{1}'.format(tcpClisock,addr))
    wel = '请输入你的用户名:'
    #try:
    tcpClisock.send(wel.encode('utf-8'))
    name = tcpClisock.recv(BUFSIZE)
    name = name.decode('utf-8')

    room = '请输入你要加入的房间号(目前存在的房间号:{0}):'.format(roomidlist)
    tcpClisock.send(room.encode('utf-8'))
    roomid = tcpClisock.recv(BUFSIZE)
    roomid = roomid.decode('utf-8')
    
    if roomid not in roomidlist:
        roomidlist.append(roomid)

    inputs.append(tcpClisock)
    fd_name[tcpClisock] = name
    fd_room[tcpClisock] = roomid

    if roomidname.get(roomid) != None:
        name1 = roomidname[roomid]
        roomidname[roomid] = name1 + ' ' + name
    else:
        roomidname[roomid] = name

    nameList = '房间{0}的用户有:{1}'.format(roomid,(roomidname[roomid]))
    tcpClisock.send(nameList.encode('utf-8'))
    #except:
    #    print('服务器意外关闭，请重新启动！')

#运行服务器
def server_run():
    tcpSersock = conn()
    if tcpSersock != 'tcperr':
        inputs.append(tcpSersock)
        while(True):
            try:
                r,w,e = select.select(inputs,[],[])
            except:
                print('服务器意外关闭，请重新启动!')
                break
            for temp in r:
                if temp is tcpSersock:
                    new_coming(tcpSersock)
                else:
                    disconnect = False
                    data = temp.recv(BUFSIZE).decode('utf-8')
                    if data == '':
                        data = fd_name[temp] + '离开了房间'
                        disconnect = True
                    else:
                        data = fd_name[temp] + '说:' + data
                    #说话的人的所属ID
                    roomid = fd_room[temp]                         
                    
                    if disconnect:
                        inputs.remove(temp)
                        fd_room.pop(temp)
                        print('房间'+roomid+'的'+data)
                        for other in inputs:
                            if other != tcpSersock and other != temp:
                                try:
                                    if fd_room[other] == roomid:
                                        other.send(data.encode('utf-8'))
                                except Exception as e:
                                    print(e)
                        del fd_name[temp]
                    else:
                        print('房间'+roomid+'的'+data)
                        for other in inputs:
                            if other != tcpSersock and other != temp:#加上判断不能将信息发送给自己
                                try:
                                    if fd_room[other] == roomid:
                                        other.send(data.encode('utf-8'))
                                except Exception as e:
                                    print(e)

if __name__=='__main__':
    server_run()
