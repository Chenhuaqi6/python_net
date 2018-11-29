from socket import *
import os,sys
from threading import Thread

    

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

#客户端处理函数
def handler(c):
    print("connect from:",c.getpeername())
    while 1:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"receive")
    c.close()



#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
print("等待客户端连接...")

#接收客户端请求
while 1:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print("出现错误:",e)
        continue
    
    #创建线程处理客户端请求
    t = Thread(target=handler,args=(c,))
    t.setDaemon(True)
    t.start()
