# from socket import *

# #创建套接字
# sockfd = socket()

# #发起连接
# sever_addr = ("127.0.0.1",9989)
# sockfd.connect(sever_addr)

# #服务端先收后发 客户端先发后收
# while 1:
#     data = input(">>")
#     sockfd.send(data.encode())
#     data = sockfd.recv(1024)
#     print("服务端返回:",data.decode())

# sockfd.close()


# from socket import * 


# ttfd = socket()

# sever_addr = ("127.0.0.1",8888)
# ttfd.connect(sever_addr)

# data = input(">>")
# ttfd.send(data.encode())

# data = ttfd.recv(1024)
# print("服务端返回:",data.decode())
# ttfd.close()


#创建套接字
#发送链接
#看服务端先发 客户端就先收

# from socket import *

# ttfd = socket()

# address = ("127.0.0.1",8888)
# ttfd.connect(address)

# data = input(">>")

# ttfd.send(data.encode())

# data = ttfd.recv(1024)
# print("服务端返回",data.decode())
# ttfd.close()


from socket import *

ttfd = socket()

address = ("127.0.0.1",8888)

ttfd.connect(address)
data = input(">>")
ttfd.send(data.encode())

data = ttfd.recv(1024)
print("服务端返回",data.decode())

ttfd.close()