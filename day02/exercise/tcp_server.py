# from socket import *

# s = socket()

# s.bind(("0.0.0.0",8888))

# s.listen(8)
# print("等待客户端连接..")

# c,addr = s.accept()
# file = open("recv.png","wb")
# while 1:

#     data = c.recv(1024)
#     if not data:
#         break
#     file.write(data)
    
# c.close()
# file.close()
# s.close()


# from socket import *

# s = socket()#空括号默认TCP

# s.bind(("0.0.0.0",8888))  #绑定地址

# s.listen(5) #设置监听
# print("等待客户端连接...")

# file = open("recv.png","wb")
# c,addr = s.accept()

# while 1:
#     data = c.recv(1024)
#     if not data:
#         break
#     file.write(data)
    
# c.close()
# file.close()
# s.close()

# from socket import *

# s = socket()

# s.bind(("0.0.0.0",6666))

# s.listen(2)
# print("等待客户端连接...")

# c,addr = s.accept()
# while 1:
#     data = c.recv(1024)
#     if not data:
#         break
#     print("收到的消息:",data.decode())
#     print("消息来自:",addr)

#     n = c.send("收到消息".encode())
#     print("发送总字节:",n)

# c.close()
# s.close()
