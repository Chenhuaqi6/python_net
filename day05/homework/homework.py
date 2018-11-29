import os

filename = "./recv.png"

#获取大小

size = os.path.getsize(filename)

#上半部分

def copy1():
    f = open(filename,"rb")
    fw = open("1.png","wb")
    n = size // 2
    while 1:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -=1024
    f.close()
    fw.close()
#下半部分
def copy2():
    f = open("./recv.png","rb")
    fw = open("2.png","wb")
    f.seek(size // 2,0)
    while 1:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:
    copy1()
else:
    copy2()