from socket import *
import sys
import time

#具体功能实现
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd
    
    def do_list(self):
        self.sockfd.send("L".encode())#发送请求
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            while 1:
                file = self.sockfd.recv(1024).decode()
                if file == "##":
                    break
                print(file)
        else:
            print(data)
    
    def do_quit(self):
        self.sockfd.send("Q".encode())
        self.sockfd.close()
        sys.exit("谢谢使用")
    
    def do_get(self,filename):
        self.sockfd.send(("G "+filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            f = open(filename,"wb")
            while 1:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()
            print("%s下载完成"%filename)
        else:
            print(data)
    
    def do_put(self,filename):
        try:
            f = open(filename,"rb")
        except Exception as e:
            print("出现错误,没有该文件")
            return
        self.sockfd.send(("P "+filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            while 1:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            f.close()
            print("%s上传完成"%filename)
        else:
            print(data)
            
#网络连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    sockfd = socket()

    try:
        sockfd.connect(ADDR)
    

    except Exception as e:
        print("连接服务器失败",e)
        return
    
    #创建类对象
    ftp = FtpClient(sockfd)

    while 1:
        print("=======命令选项========")
        print("***     list        ***")
        print("***   get file      ***")
        print("***   put file      ***")
        print("***     quit        ***")
        print("======================\n")
        
        cmd = input("输入命令:")


        if cmd.strip() == "list":
            ftp.do_list()
        elif cmd.strip() == "quit":
            ftp.do_quit()
        elif cmd[:3] == "get":
            filename = cmd.split(" ")[-1]
            ftp.do_get(filename)
        elif cmd[:3] == "put":
            filename = cmd.split(" ")[-1]
            ftp.do_put(filename)
        
        else:
            print("请输入正确指令")
main()
