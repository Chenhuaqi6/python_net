# from socket import *

# s = socket()

# s.bind(("0.0.0.0",8888))

# s.listen(5)

# file = open("test.html","rb")
# while 1:
#     c , addr = s.accept()
#     print("客户端来自:",addr)

#     data = c.recv(1024)
#     # print(data)

#     data = file.read()


#     c.send(data)
#     c.close()
# file.close()
# s.close()


from socket import *

#接收request 发送response

def handleClient(connfd):
    resquest = connfd.recv(4096)
    #将request按行分割
    resquest_lines = resquest.splitlines()
    #查看请求的每一行
    for line in resquest_lines:
        print(line)
    try:
        f = open("index.html")
    except Exception:
        response = "HTTP/1.1 404 NOT Found\r\n"
        response += "Content-Type: text/html\r\n"
        response +="\r\n"
        response += "<h1>Sorry the page not found!</h1>"
    else:
        response = "HTTP/1.1 200 Ok\r\n"
        response += "Content-Type: text/html\r\n"
        response +="\r\n"
        response += f.read()
    finally:
        #将结果给客户端
        connfd.send(response.encode())                                                                          
        



#创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(("0.0.0.0",8000))
    sockfd.listen(5)
    print("Listen the port 8000...")
    while 1:
        connfd,addr = sockfd.accept()
        #处理请求
        handleClient(connfd)
        connfd.close()
if __name__ == "__main__":
    main()