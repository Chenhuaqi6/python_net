from multiprocessing import Process
import os,sys
from socket import *

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

def handler(c):
    print("connect from:",c.getpeername())
    while 1:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send("收到".encode())
    c.close()
    sys.exit(0) #退出子进程


s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
print("等待客户端连接...")

while 1:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print("出现错误",e)
        continue
    
    #创建子进程处理客户端请求
    p = Process(target= handler,args = (c,))
    p.daemon = True  #主进程退出 子进程也推出
    p.start()
