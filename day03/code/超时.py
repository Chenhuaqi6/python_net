from socket import *

from time import sleep,ctime

#创建tcp套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",8888))
sockfd.listen(5)

#设置超时时间
sockfd.settimeout(5)

while 1:
    print("waitng for connect...")
    try:
        connfd,addr = sockfd.accept()
    except BlockingIOError:
        sleep(2)
        print(ctime())
        continue
    except timeout:
        print("超时等待5秒...")
        continue
    else:
        data = connfd.recv(1024).decode()

        print(data)
        connfd.send(b"Receive message")
        break
sockfd.close()