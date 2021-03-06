import gevent
from gevent import monkey
monkey.patch_socket() #执行脚本修改阻塞行为,在导入模块前执行
from socket import *

#创建套接字
def server():
    s = socket()
    s.bind(("0.0.0.0",8888))
    s.listen(6)
    while 1:
        c,addr = s.accept()
        print("Connect from",addr)
        # handle(c)
        gevent.spawn(handle,c)



#处理客户端
def handle(c):
    while 1:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"Receive")



server()