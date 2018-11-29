from select import select
from socket import *

#创建套接字作为关注的io

s = socket()

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(("0.0.0.0",8888))

s.listen(5)

#添加到关注列表
rlist=[s]
wlist=[]
xlist=[]

while 1:
    #循环监控io事件的发生
    rs,ws,xs = select(rlist,wlist,xlist)
    #处理发生的io事件
    for r in rs:
        if r is s: #遍历到s说明s就绪,有客户端连接
            c,addr = r.accept()
            print("Connect from ",addr)
            rlist.append(c)
        else:
            data = r.recv(1024)
            
            if not data:
                rlist.remove(r) #客户端退出,移除关注
                r.close()
                continue
            print("收到:",data.decode())
            # r.send(b"Receive msg")
            wlist.append(r) #判断ws有东西 直接返回
    for w in ws:
        w.send(b"Receive")
        wlist.remove(w)#发回之后立即删除,否则会一直发送
    
    for x in xs:
        pass



