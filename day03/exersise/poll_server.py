# from socket import *
# from select import *

# #创建套接字作为关注io
# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(("0.0.0.0",8888))
# s.listen(2)

# #创建poll对象
# p = poll()

# #建立查找字典
# fdmap = {s.fileno():s}

# #注册io
# p.register(s,POLLIN|POLLERR)

# #循环监控
# while 1:
#     #等待io发生
#     events = p.poll()

#     for fd,event in events:
#         if fd == s.fileno():
#             c,addr = fdmap[fd].accept()
#             print("客户端信息:",addr)
#             #添加新的关注io
#             p.register(c,POLLIN|POLLHUP)
#             fdmap[c.fileno()] = c
#         elif event & POLLIN:
#             data = fdmap[fd].recv(1024)
#             if not data:
#                 p.unregister(fd)
#                 fdmap[fd].close()
#                 del fdmap[fd]
#             else:
#                 print("收到消息:",data.decode())
#                 fdmap[fd].send("收到消息".encode())



# from select import *
# from socket import *

# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(("0.0.0.0",8888))
# s.listen(5)

# #创建poll对象

# p = poll()

# #创建查找字典

# fdmap = {s.fileno():s}

# #注册io
# p.register(s,POLLIN|POLLERR)

# #循环监控
# while 1:
#     #等待io发生
#     events = p.poll()
#     for fd,event in events:
#         if fd == s.fileno():
#             c,addr = fdmap[fd].accept()
#             print("客户端信息:",addr)
#             #添加新的关注io
#             p.register(c,POLLIN|POLLHUP)
#             fdmap[c.fileno()] = c
#         elif event & POLLIN:
#             data = fdmap[fd].recv(1024)
#             if not data:
#                 p.unregister(fd)
#                 fdmap[fd].close()
#                 del fdmap[fd]
#             else:
#                 print("客户端消息:",data.decode())
#                 fdmap[fd].send("收到消息!!".encode())

from select import *
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(2)

#创建poll对象
p = poll()

#建立查找字典
f = {s.fileno():s}

#注册io
p.register(s,POLLIN|POLLHUP)


while 1:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = f[fd].accept()
            print("客户端信息为:",addr)
            #添加新的关注io
            p.register(c,POLLIN|POLLERR)
            f[c.fileno()]=c
        elif event & POLLIN:
            data = f[fd].recv(1024)
            if not data:
                p.unregister(fd)
                f[fd].close()
                del f[fd]
            else:
                print("收到客户端消息:",data.decode())
                f[fd].send("这里是服务端,收到消息".encode())