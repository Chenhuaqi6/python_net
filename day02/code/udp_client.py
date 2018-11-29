# #创建套接字
# #消息收发
# #关闭套接字

# from socket import *
# import sys


# #从命令行获取 ip 和 port

# HOST = sys.argv[1]
# PORT = int(sys.argv[2])
# ADDR = (HOST,PORT)


# sockfd = socket(AF_INET,SOCK_DGRAM)


# #消息收发
# while True:
#     data = input("Msg: ")
#     if not data:
#         break
#     sockfd.sendto(data.encode(),ADDR)
#     msg,addr = sockfd.recvfrom(1024)
#     print("Sever msg:",msg.decode())

# sockfd.close()

from socket import *
import sys

host = sys.argv[1]
port = int(sys.argv[2])

addr = (host,port)

s = socket(AF_INET,SOCK_DGRAM)

while 1:
    data = input(">>")
    if not data:
        break
    s.sendto(data.encode(),addr)
    c,addr = s.recvfrom(1024)
    print("服务端消息:",c.decode(),addr)

s.close()