#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/22 17:06
  * @author: by Ysan
'''

from twisted.internet import reactor, protocol

# a client protocol
class EchoClient(protocol.Protocol):
    '''once connected, send a message, then print the result'''

    def makeConnection(self, transport):
        print("建立连接", transport)
        super(EchoClient, self).makeConnection(transport)

    def connectionMade(self):
        self.transport.write("hello An".encode('utf-8'))

    def dataReceived(self, data):
        # As soon as any data is received, write it back
        print("server said : ", data)
        self.transport.loseConnection()

    def connectionLost(self, reason):
        print("connection lost")


class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()


def main():
    f = EchoFactory()
    reactor.connectTCP('localhost', 1234, f)
    reactor.run()


if __name__ == '__main__':
    main()
