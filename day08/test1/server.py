from socket import *
import os,sys
from threading import Thread
import time

#全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)
FILE_DIR = "/home/tarena/1809/"

def zombie():
    os.wait()

class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
    
    def do_list(self):
        file_list = os.listdir(FILE_DIR)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(0.1) #防止粘包
        for file in file_list:
            if file[0] != "." and os.path.isfile(FILE_DIR+file):
                self.connfd.send(file.encode())
                time.sleep(0.1)
        self.connfd.send(b"##")
    
    def do_get(self,filename):
        try:
            f = open(FILE_DIR+filename,"rb")
        except:
            self.connfd.send("没有该文件".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(0.1)
        while 1:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)
        f.close()
    def do_put(self,filename):
        try:
            f = open(filename,"wb")
        except Exception as e:
            self.connfd.send("上传失败".encode())
            return
        else:
            self.connfd.send(b"ok")
        while 1:
            data = self.connfd.recv(1024)
            if data == b"##":
                break
            f.write(data)
        f.close()
        


def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(4)

    print("listen to the port 8888...")

    while 1:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常",e)
            continue
        print("连接用户:",addr)

        #创建子进程,处理客户端请求
        pid = os.fork()
        if pid == 0:
            sockfd.close()
            ftp = FtpServer(connfd)

            while 1:
                data = connfd.recv(1024).decode()
                print(data)
                if not data or data[0] == "Q":
                    connfd.close()
                    sys.exit("客户端退出")
                elif data[0] == "L":
                    ftp.do_list()
                elif data[0] == "G":
                    filename = data.split(" ")[-1]
                    ftp.do_get(filename)
                elif data[0] == "P":
                    filename = data.split(" ")[-1]
                    ftp.do_put(filename)
                
        
            os._exit(0)
        
        else:
            connfd.close()
            #单独创建线程处理僵尸进程
            t = Thread(target=zombie)
            t.setDaemon(True)#主线程退出分支线程也退出
            t.start()
            continue
main()

            