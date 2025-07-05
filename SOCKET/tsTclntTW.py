#_*_ coding:'UTF-8'_*_
#网络编程(Twisted Reactor时间戳TCP客户端)
from twisted.internet import protocol,reactor
HOST = 'localhost'
PORT = 8080

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('>')
        if data:
            print('...senfing %s...'%data)
            self.transport.write(data.encode('utf-8'))
        else:
            self.transport.loseConnection()
    def connectionMade(self):
        self.sendData()
    def dataReceived(self, data):
        print(data.decode('utf-8'))
        self.sendData()
class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self,connector,reason:reactor.stop()
reactor.connectTCP(HOST,PORT,TSClntFactory())
reactor.run()