import socket

#创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址

sockfd.bind(("0.0.0.0",8688))

#设置监听

sockfd.listen(5)

print("Writing for connect...")

#处理客户端连接

while 1:
    connfd,addr = sockfd.accept()

    print("Connect from",addr)

    #收发消息
    while 1:

        data = connfd.recv(5)
        if not data:
            break
        print("Receive:",data.decode())


        n = connfd.send("Hello Kitty".encode())
        print("Send %d bytes"%n)
    if not data:
        break
    # 关闭套接字
        connfd.close()
sockfd.close()



