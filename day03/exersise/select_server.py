# from select import select
# from socket import *

# #创建套接字作为关注io
# s = socket()

# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# s.bind(("0.0.0.0",8888))

# s.listen(5)

# #添加关注列表
# rlist=[s]
# wlist=[]
# xlist=[]

# while 1:
#     #循环控制io事件的发生
#     rs,ws,xs = select(rlist,wlist,xlist)

#     #处理发生的io事件
#     for r in rs:
#         if r ==s:
#             c,addr = r.accept()
#             print("客户端信息:",addr)
#             rlist.append(c)
#         else:
#             data = r.recv(1024)

#             if not data:
#                 rlist.remove(r) #客户端退出 移除关注
#                 r.close()
#                 continue
#             print("收到:",data.decode())
#             wlist.append(r) #判断ws有东西 直接返回
#     for w in ws:
#         w.send(b"Receive")
#         wlist.remove(w) #发会之后立即删除,否则一直发送

# from select import select
# from socket import *

# #创建套接字关注io
# s = socket()

# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# s.bind(("0.0.0.0",8888))

# s.listen(5)

# #创建关注列表
# rlist = [s]
# wlist = []
# xlist = []

# #使用大循环来控制谁触发监控
# while 1:
#     rs,ws,xs = select(rlist,wlist,xlist)

#     #遍历rs若是s 说明是有新客户端连接,若是r则是有消息发送

#     for r in rs:
#         if r == s:
#             c,addr = r.accept()
#             print("消息来自:",addr)
#             rlist.append(c)
#         else:
#             data = r.recv(1024)
#             if not data:
#                 rlist.remove(c)
#                 r.close()
#             print("收到: ",data.decode())
#             wlist.append(r)
#     for w in wlist:
#         w.send("服务端收到消息".encode())
#         wlist.remove(w)


# from select import select
# from socket import *

# s = socket()

# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# s.bind(("0.0.0.0",8888))

# s.listen(5)

# #创建监听列表
# rlist = [s]
# wlist = []
# xlist = []

# #创建大循环判断是谁触发
# while 1:
#     rs,ws,xs = select(rlist,wlist,xlist)
    
#     for r in rs:
#         if r == s:
#             c,addr = r.accept()
#             print("消息来自:",addr)
#             rlist.append(c)
#             print(c)
#         else:
#             data = r.recv(1024)
#             if not data:
#                 rlist.remove(c)
#                 r.close()
#                 continue
#             print("客户端消息:",data.decode())
#             wlist.append(r)
#     for w in ws:
#         n = w.send("收到消息".encode())
#         print("发送%d字节"%n)
#         wlist.remove(w)
#     for x in xs:
#         pass



# from select import select
# from socket import *

# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(("0.0.0.0",8888))
# s.listen(5)

# rlist = [s]
# wlist = []
# xlist = []

# while 1:
#     rs,ws,xs = select(rlist,wlist,xlist)
#     for r in rs:
#         if r == s:
#             c,addr = r.accept()
#             print("客户端信息: ",addr)
#             rlist.append(c)
#         else:
#             data = r.recv(1024)
#             if not data:
#                 rlist.remove(r)
#                 r.close()
#                 continue
#             print("客户端消息:",data.decode())
#             wlist.append(r)
#     for w in ws:
#         w.send("这里是服务端,已收到消息!!".encode())
#         wlist.remove(w)


from select import select
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

rlist = [s]
wlist = []
xlist = []

while 1:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r == s:
            c,addr = r.accept()
            print("客户端地址:",addr)
            rlist.append(c)
        else:
            data = r.recv(1024)

            if not data:
                r.close()
                rlist.remove(r)
                continue
            print("收到消息:",data.decode())
            wlist.append(r)
    for w in ws:
        w.send("收到消息!!".encode())
        wlist.remove(w)