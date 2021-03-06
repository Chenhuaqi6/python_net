#coding = utf-8
"""
HTTP SERVER v2.0
解析具体request
使用多线程并发处理
能返回简单数据
使用类封装
"""
from socket import *
from threading import Thread
import sys

#封装 httpserver功能
class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        #对象属性
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        #创建套接字
        self.create_socket()
    
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)

    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen to the port %d"%self.port)
        while 1:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务器退出")
            except Exception as e:
                print(e)
                continue
            #创建新的线程处理客户端请求
            clientthread = Thread(target=self.handle,args=(connfd,))
            clientthread.setDaemon(True)
            clientthread.start()
    #处理客户端请求
    def handle(self,connfd):
        #接收request
        requst = connfd.recv(4096)
        if not requst:
            return
        #按行切割
        requstHeaders = requst.splitlines()
        print(connfd.getpeername(),":",requstHeaders[0])
        #获取具体的请求内容
        get_request = str(requstHeaders[0]).split(" ")[1]
        
        # 想获取网页
        if get_request == "/" or get_request[-5:] == ".html": #[-5:]最后五个字符
            self.get_html(connfd,get_request)
        #想获取数据
        else:
            self.get_data(connfd,get_request)
        connfd.close()

   
    #发送网页
    def get_html(self,connfd,get_request):
        if get_request == "/":
            filename = self.static_dir+"/index.html"
        else:
            filename = self.static_dir+get_request
        try:
            f = open(filename)
        except Exception:
            #没找到网页
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "\r\n"
            responseBody = "Sorry,not found the page"
        else:
            #返回网页
            responseHeaders = "HTTP/1.1 200 ok \r\n"
            responseHeaders += "\r\n"
            responseBody = ""
            while 1:
                data = f.read(1024)
                if not data:
                    break
                responseBody += data
        finally:
            response = responseHeaders+responseBody
            connfd.send(response.encode())
    
    def get_data(self,connfd,get_request):
        urls = ["/time","/web","/python"]

        if get_request in urls:
            if get_request == "/time":
                import time
                responseBody = time.ctime()
            elif get_request == "/web":
                responseBody = "Web Frame"
            
            elif get_request == "/python":
                responseBody = "Python"
            
            responseHeaders = "HTTP/1.1 200 ok\r\n"
            responseHeaders += "\r\n"
        else:
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "\r\n"
            responseBody = "<h1>None</h1>"
        response = responseHeaders + responseBody
        connfd.send(response.encode()) 




        
#提供服务器地址和静态文件路径
server_addr = ("0.0.0.0",8000)
static_dir = "/home/tarena/python_net/day09/http/static"


#创建服务器对象
httpd = HTTPServer(server_addr,static_dir)
#调用函数启动服务
httpd.server_forever()