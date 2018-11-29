from socket import *

#创建tcp套接字
sockfd = socket()

#发起连接
server_addr = ("127.0.0.1",8688)
sockfd.connect(server_addr)

#消息收发 先发后收 (服务端先收后发)
while 1:
    data = input(">>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("From server:",data.decode())
    # if data == "q":
sockfd.close()
