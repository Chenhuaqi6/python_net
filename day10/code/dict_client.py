from socket import *
import pymysql
import sys
import getpass
#注册请求
def do_register(s):
    while 1:
        name = input("User:")
        passwd = getpass.getpass()
        passwd1 = getpass.getpass("Again:")

        if(" " in name) or (" " in passwd):
            print("用户名或密码不许有空格")
            continue
        if passwd != passwd1:
            print("俩次输入密码不一致")
            continue
        msg = "R %s %s"%(name,passwd)
        #发送请求
        s.send(msg.encode())
        #等待回复
        data = s.recv(128).decode()
        if data == "ok":
            print("注册成功")
            return
        elif data == "EXISTS":
            print("该用户已存在")
        else:
            print("注册失败")
        return
#登录请求
def do_login(s):
    name = input("User:")
    passwd = getpass.getpass()

    msg = "L %s %s"%(name,passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "ok":
        print("登录成功")
        login(s,name)
    else:
        print("登录失败")  

# 查询请求
# def do_find(s,name):
#     while 1:
#         danci = input("请输入查询单词:")
#         msg = "Q %s %s"%(name,danci)
#         s.send(msg.encode())

#         data = s.recv(1024).decode()

#         if data == "##":
#             print("未查询到结果")
#             login(s,name)
#         else:
#             print("单词解释:",data)

def do_find(s,name):
    while 1:
        word = input("单词")
        if word == "##":
            break
        msg = "Q %s %s"%(name,word)
        s.send(msg.encode())
        #接收服务端反馈结果
        data = s.recv(2048).decode()
        if data =="FALL":
            print("没有该单词")
        else:
            print(data) 
def do_history(s,name):
    msg = "H %s"%name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "ok":
        while 1:
            data = s.recv(1024).decode()
            if data == "##":
                break
            print(data)

    else:
        print("没有历史记录")


#二级界面
def login(s,name):
    while 1:
        print("""
        ==========查询界面============
        ---1.查词  2.历史记录  3.注销---
        ============================
        """)
        try:
            cmd = int(input("请输入选项>"))
        except Exception as e:
            print("命令错误")
            continue

        if cmd not in [1,2,3]:
            print("不存在该选项")
            continue
        elif cmd == 1:
            do_find(s,name)
        elif cmd == 2:
            do_history(s,name)
        elif cmd == 3:
            break
    

def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    s = socket()
    try:
        s.connect((HOST,PORT))
    except Exception as e:
        print(e)
        return
    while 1:
        print("""
        =========Welcome===========
        ---1.注册  2.登录   3.退出---
        ===========================
        """)
        try:
            cmd = int(input("请输入选项>"))
        except Exception as e:
            print("命令错误")
            continue
        except KeyboardInterrupt:
            s.send(b"E")
            s.close()
            sys.exit("客户端退出")
        if cmd not in [1,2,3]:
            print("不存在该选项")
            continue
        elif cmd == 1:
            do_register(s)
        elif cmd == 2:
            do_login(s)
        elif cmd == 3:
            s.send(b"E")
            sys.exit("谢谢使用")

main()