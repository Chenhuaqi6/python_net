from select import select
from socket import *
import sys
s = socket()
s.bind(("0.0.0.0",8888))
s.listen(0)

#监控io
print("等待我监控的io....")
rs,ws,xs, = select([s,sys.stdin],[],[s])
print("终于发生了")
print(rs)
