# from socket import *

# #创建套接字
# sockfd = socket(AF_INET,SOCK_DGRAM)

# #绑定地址

# sockfd.bind(("0.0.0.0",8888))

# #消息收发

# while True:
#     data,addr = sockfd.recvfrom(5)
#     print("Receive from",addr,data.decode())
  
#     sockfd.sendto("Thanks for your message".encode(),addr)

# sockfd.close()


from socket import *

#创建套接字

s = socket(AF_INET,SOCK_DGRAM)

s.bind(("0.0.0.0",8888))

while 1:
    data , addr = s.recvfrom(1024)

    print("消息来自:",addr,data.decode())

    s.sendto("收到消息".encode(),addr)
s.close()