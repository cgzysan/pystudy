#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/22 16:57
  * @author: by Ysan

    Twisted 是一个事件驱动的网络框架，其中包含了：网络协议，线程，数据库管理，网络操作等诸多功能

    事件驱动模型，任务交错执行，但仍然在一个单独的线程控制中。当处理I/O或者其他昂贵的操作时，
    注册一个回调到事件循环中，然后当I/O操作完成时继续执行。回调描述了该如何处理某个事件。
    事件循环轮询所有的事件，当事件到来时将它们分配给等待处理事件的回调函数。这种方式让程序
    尽可能的得以执行而不需要用到额外的线程。事件驱动型程序比多线程程序更容易推断出行为，因为程序员不需要关心线程安全问题。

    Reactor模式
    Twisted实现了设计模式中的反应堆（reactor）模式，这种模式在单线程环境中调度多个事件源产生的事件到它们各自的事件处理例程中去。
    Twisted的核心就是reactor事件循环。Reactor可以感知网络、文件系统以及定时器事件。它等待然后处理这些事件，从特定于平台的行为中抽象出来。

    Protocols   描述了如何以异步的方式处理网络中的事件

    1. makeConnection               在transport对象和服务器之间建立一条连接
    2. connectionMade               连接建立起来后调用
    3. dataReceived                 接收数据时调用
    4. connectionLost               关闭连接时调用

    Transports  代表网络中两个通信节点之间的连接
    1. write                   以非阻塞的方式按顺序依次将数据写到物理连接上
    2. writeSequence           将一个字符串列表写到物理连接上
    3. getPeer                 取得连接中对端的地址信息
    4. getHost                 取得连接中本端的地址信息

    ECHO协议
'''

from twisted.internet import protocol
from twisted.internet import reactor


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print("client said ", data.decode())
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


def main():
    # factory = protocol.ServerFactory()
    # factory.protocol = Echo

    reactor.listenTCP(1234, EchoFactory())
    reactor.run()


if __name__ == '__main__':
    main()
