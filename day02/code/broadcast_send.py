from socket import *

from time import sleep

#设置广播地址

dest = ("192.168.43.255",6456)

#设置udp地址
s = socket(AF_INET,SOCK_DGRAM)

#设置可以发送广播 

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while 1:
    sleep(2)

    s.sendto("你认为做大哥,我教你梳中分".encode(),dest)

s.close()
