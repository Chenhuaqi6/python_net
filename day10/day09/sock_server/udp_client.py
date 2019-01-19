from socket import *
import sys
host = sys.argv[1]
port = int(sys.argv[2])

addr = (host,port)

s = socket(AF_INET,SOCK_DGRAM)

while 1:
    data = input(">>")
    if not data:
        break
    s.sendto(data.encode(),addr)
    c,addr = s.recvfrom(1024)
    print("服务端消息:",c.decode(),addr)

s.close()