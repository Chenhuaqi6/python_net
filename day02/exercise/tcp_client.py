# from socket import *

# s = socket()

# c = ("127.0.0.1",8888)
# s.connect(c)

# file = open("send.png","rb")
# while 1:
#     data = file.read(1024)
#     if not data:
#         break
#     s.send(data)
# file.close()
# s.close()


# from socket import *

# s = socket()

# c = ("127.0.0.1",8888)

# s.connect(c)

# file = open("send.png","rb")

# while 1:
#     data = file.read(1024)
#     if not data:
#         break
#     s.send(data)
# file.close()
# s.close()

from socket import *
s = socket()

c = ("127.0.0.1",6666)

s.connect(c)
while 1:
    data = input(">>")
    if not data:
        break
    s.send(data.encode())

    n = s.recv(1024)
    print("服务端消息:",n.decode())

s.close()
