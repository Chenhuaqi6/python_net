from socket import *

#创建tcp套接字

s = socket()

s.bind(("0.0.0.0",8898))

s.listen(8)

while True:
    c,addr = s.accept()
    print("connect from",addr)
    data = c.recv(4096)
    print(data)

    #返回http响应

    data = """HTTP/1.1 200 OK
    Content-Endoding: gizp
    Content-Type: text/html

    <h1>Welcome to tedu</h1>
    <p>Python test</p>
    <p>cao ni  ma</p>
    """

    c.send(data.encode())  #发送给浏览器
    c.close()
s.close()