#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/20 17:05
  * @author: by Ysan

    epoll 通过单进程实现同时
'''


import socket, logging
import select, errno

logger = logging.getLogger("network-server")


def InitLog():
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("network-server.log")
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)


if __name__ == "__main__":
    InitLog()

    try:
        # 创建 TCP socket 作为监听 socket
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as msg:
        logger.error("create socket failed")

    try:
        # 设置 SO_REUSEADDR 选项
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        logger.error("setsocketopt SO_REUSEADDR failed")

    try:
        # 进行 bind -- 此处未指定 ip 地址，即 bind 了全部网卡 ip 上
        listen_fd.bind(('', 2003))
    except socket.error as msg:
        logger.error("bind failed")

    try:
        # 设置 listen 的 backlog 数
        listen_fd.listen(10)
    except socket.error as msg:
        logger.error(msg)

    try:
        # 创建 epoll 句柄
        epoll_fd = select.epoll()
        # 向 epoll 句柄中注册 监听 socket 的 可读 事件
        epoll_fd.register(listen_fd.fileno(), select.EPOLLIN)
    except select.error as msg:
        logger.error(msg)

    connections = {}
    addresses = {}
    datalist = {}
    while True:
        # epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
        epoll_list = epoll_fd.poll()

        for fd, events in epoll_list:
            # 若为监听 fd 被激活
            if fd == listen_fd.fileno():
                # 进行 accept -- 获得连接上来 client 的 ip 和 port，以及 socket 句柄
                conn, addr = listen_fd.accept()
                logger.debug("accept connection from %s, %d, fd = %d" % (addr[0], addr[1], conn.fileno()))
                # 将连接 socket 设置为 非阻塞
                conn.setblocking(0)
                # 向 epoll 句柄中注册 连接 socket 的 可读 事件
                epoll_fd.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)
                # 将 conn 和 addr 信息分别保存起来
                connections[conn.fileno()] = conn
                addresses[conn.fileno()] = addr
            elif select.EPOLLIN & events:
                # 有 可读 事件激活
                datas = ''
                while True:
                    try:
                        # 从激活 fd 上 recv 10 字节数据
                        data = connections[fd].recv(10)
                        # 若当前没有接收到数据，并且之前的累计数据也没有
                        if not data and not datas:
                            # 从 epoll 句柄中移除该 连接 fd
                            epoll_fd.unregister(fd)
                            # server 侧主动关闭该 连接 fd
                            connections[fd].close()
                            logger.debug("%s, %d closed" % (addresses[fd][0], addresses[fd][1]))
                            break
                        else:
                            # 将接收到的数据拼接保存在 datas 中
                            datas += data
                    except socket.error as  msg:
                        # 在 非阻塞 socket 上进行 recv 需要处理 读穿 的情况
                        # 这里实际上是利用 读穿 出 异常 的方式跳到这里进行后续处理
                        if msg.errno == errno.EAGAIN:
                            logger.debug("%s receive %s" % (fd, datas))
                            # 将已接收数据保存起来
                            datalist[fd] = datas
                            # 更新 epoll 句柄中连接d 注册事件为 可写
                            epoll_fd.modify(fd, select.EPOLLET | select.EPOLLOUT)
                            break
                        else:
                            # 出错处理
                            epoll_fd.unregister(fd)
                            connections[fd].close()
                            logger.error(msg)
                            break
            elif select.EPOLLHUP & events:
                # 有 HUP 事件激活
                epoll_fd.unregister(fd)
                connections[fd].close()
                logger.debug("%s, %d closed" % (addresses[fd][0], addresses[fd][1]))
            elif select.EPOLLOUT & events:
                # 有 可写 事件激活
                sendLen = 0
                # 通过 while 循环确保将 buf 中的数据全部发送出去
                while True:
                    # 将之前收到的数据发回 client -- 通过 sendLen 来控制发送位置
                    sendLen += connections[fd].send(datalist[fd][sendLen:])
                    # 在全部发送完毕后退出 while 循环
                    if sendLen == len(datalist[fd]):
                        break
                # 更新 epoll 句柄中连接 fd 注册事件为 可读
                epoll_fd.modify(fd, select.EPOLLIN | select.EPOLLET)
            else:
                # 其他 epoll 事件不进行处理
                continue

