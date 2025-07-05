# _*_coding='utf-8'_*_
#网络编程学习(SocketServerTcp服务器)
from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

host = ''
port = 8080
ADDR = (host,port)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:',self.client_address)
        data = self.rfile.readline().decode('utf-8')
        self.wfile.write(bytes('[{0}] {1}'.format(ctime(),data),'utf-8'))
tcpServ = TCP(ADDR,MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()
