from socket import *

from time import sleep,ctime

#创建tcp套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",8888))
sockfd.listen(5)

#设置非阻塞状态
sockfd.setblocking(False)
sleep(5)
while 1:
    print("waitng for connect...")
    try:
        connfd,addr = sockfd.accept()
        #设置recv的非阻塞
        connfd.setblocking(False)
    except BlockingIOError:
        sleep(2)
        print(ctime())
        continue
    else:
        data = connfd.recv(1024).decode()

        print(data)
        connfd.send(b"Receive message")
        break
sockfd.close()