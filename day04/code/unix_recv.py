# from socket import *
# import os

# #确定套接字文件
# sock_file = "./sock_file"

# #判断文件是否存在
# if os.path.exists(sock_file):
#     os.remove(sock_file)

# #创建本地套接字
# sockfd = socket(AF_UNIX,SOCK_STREAM)
# #绑定套接字文件
# sockfd.bind(sock_file)

# #监听
# sockfd.listen(5)

# #消息的收发
# while 1:
#     c,addr = sockfd.accept()
#     while 1:
#         data = c.recv(1024)
#         if not data:
#             break
#         else:   
#             print(data.decode())
#             c.send("收到".encode())

#     c.close()
# sockfd.close()

from socket import *
import os

sk = "./myfile"  #创建套接字文件
if os.path.exists(sk):
    os.remove(sk)
s = socket(AF_UNIX,SOCK_STREAM)
s.bind(sk)
s.listen(5)

while 1:
    c,addr = s.accept()
    while 1:
        data = c.recv(1024)
        if not data:
            break
        else:
            print(data.decode())
            c.send("收到".encode())
    c.close()
s.close()