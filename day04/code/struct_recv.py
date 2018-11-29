# from socket import *
# import struct

# s = socket(AF_INET,SOCK_DGRAM)
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(("0.0.0.0",8888))

# while 1:
#     data,addr = s.recvfrom(128) #接收格式
#     fmt = data.decode()

#     data,addr = s.recvfrom(1024)     #接收数据
#     data = struct.unpack(fmt,data)   #按格式接收
#     print(data)
# s.close()


# from socket import *
# import struct

# s = socket(AF_INET,SOCK_DGRAM)

# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# s.bind(("0.0.0.0",8888))

# while 1:
#     data,addr = s.recvfrom(128) #接收格式
#     fmt = data.decode()

#     data,addr = s.recvfrom(1024) #接收数据
#     data = struct.unpack(fmt,data)
#     print(data)
# s.close()


from socket import *
import struct 

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(("0.0.0.0",8888))

while 1:
    data,addr = s.recvfrom(128)
    fmt = data.decode()

    data,addr = s.recvfrom(1024)
    data = struct.unpack(fmt,data)
    print(data)
s.close()