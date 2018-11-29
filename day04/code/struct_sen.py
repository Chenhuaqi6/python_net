# from socket import *
# import struct
# addr = ("127.0.0.1",8888)
# s = socket(AF_INET,SOCK_DGRAM)

# while 1:
#     id = input("id:")
#     name = input("name:")
#     n = len(name)
#     height = input("height:")
#     fmt = "i%dsf"%n
#     s.sendto(fmt.encode(),addr) #先发送格式
#     data = struct.pack(fmt,int(id),name.encode(),float(height))

#     s.sendto(data,addr)

# from socket import *
# import struct

# addr = ("127.0.0.1",8888)

# s = socket(AF_INET,SOCK_DGRAM)

# while 1:
#     id = input("id:")
#     name = input("name:")
#     n = len(name)
#     age = input("age:")
#     fmt = "i%dsf"%n

#     s.sendto(fmt.encode(),addr) #先发送格式
#     data = struct.pack(fmt,int(id),name.encode(),int(age))

#     s.sendto(data,addr)


from socket import *
import struct

addr = ("127.0.0.1",8888)

s = socket(AF_INET,SOCK_DGRAM)

while 1:
    id = input("id")
    name = input("name")
    n = len(name)
    height = input("身高")

    fmt = "i%dsf"%n

    s.sendto(fmt.encode(),addr)

    data = struct.pack(fmt,int(id),name.encode(),float(height))

    s.sendto(data,addr)
