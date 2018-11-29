# from socket import *


# #创建套接字
# sockfd = socket()

# #绑定地址
# sockfd.bind(("0.0.0.0",9989))

# #设置监听
# sockfd.listen(8)
# print("等待客户端连接...")

# #处理客户端
# while 1:
#     connfd,addr = sockfd.accept()
#     print("客户端信息:",addr)
#     while 1:
#     #收发消息
#         data = connfd.recv(1024)
#         print("收到的消息:",data.decode())

#         n = input(">>")
#         connfd.send(n.encode())


#     connfd.close()
# sockfd.close()




# from socket import *

#创建字节套
#绑定地址
#设置监听
#处理客户端
#收发消息
#关闭

# ttfd = socket()

# ttfd.bind(("0.0.0.0",8888))

# ttfd.listen(8)
# print("等待客户端连接...")

# connfd,addr = ttfd.accept()
# print("客户端详细信息: ",addr)

# data = connfd.recv(1024)
# print("客户端消息:",data.decode())

# n = connfd.send("我发给客户端".encode())
# print("发送%d字节"%n)

# connfd.close()
# ttfd.close()


from socket import *

ttfd = socket()

ttfd.bind(("0.0.0.0",8888))

ttfd.listen(8)
print("正在等待客户端....")

aa,bb = ttfd.accept()
print("客户端详细信息:",bb)

data = aa.recv(1024)
print("收到客户端消息:",data.decode())

n= aa.send("我是服务端".encode())
print("发送%d字节"%n)

bb.close()
ttfd.close()


