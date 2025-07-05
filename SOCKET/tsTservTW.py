#_*_coding:'utf-8'_*_
#网络编程(Twisted Reactor TCP服务器)
from twisted.internet import protocol,reactor
from time import ctime
PORT = 8080
class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:',clnt)
    def dataReceived(self, data):
        data = data.decode('utf-8')
        self.transport.write(('[%s] %s'%(ctime(),data)).encode('utf-8'))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT,factory)
reactor.run()