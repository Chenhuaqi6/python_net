from select import *
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

#创建poll对象

p = epoll()

#创建查找字典

fdmap = {s.fileno():s}

#注册io
p.register(s,EPOLLIN|EPOLLERR)

#循环监控
while 1:
    #等待io发生
    events = p.poll()
    print("您有io需要处理")
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("客户端信息:",addr)
            #添加新的关注io
            p.register(c,EPOLLIN|EPOLLHUP|EPOLLET)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("客户端消息:",data.decode())
                fdmap[fd].send("收到消息!!".encode())