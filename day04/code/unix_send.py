# from socket import *

# #确保通信俩段用的是同一个套接字文件

# sock_file = "./sock_file"

# #创建本地套接字
# sockfd = socket(AF_UNIX,SOCK_STREAM)

# #连接另一端
# sockfd.connect(sock_file)

# #收发消息
# while 1:
#     msg = input(">>")
#     if msg:
#         sockfd.send(msg.encode())
#         print(sockfd.recv(1024).decode())
#     else:
#         break

# sockfd.close()

from socket import *

sk = "./myfile"

s = socket(AF_UNIX,SOCK_STREAM)

s.connect(sk)

while 1:
    msg = input(">>")
    if not msg:
        break
    else:
        s.send(msg.encode())
        print(s.recv(1024).decode())
s.close()