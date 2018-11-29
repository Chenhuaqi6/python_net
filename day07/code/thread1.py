import threading
from time import sleep
import os

a = 1

#线程函数
def music():
    global a
    print("a1 = ",a)
    a = 1000
    for i in range(3):
        sleep(4)
        print("播放盗将行",os.getpid())
        

#创建线程对象
t = threading.Thread(target = music)

t.start()
#主线程
print("a2",a)

for i in range(3):
    sleep(3)
    print("播放学猫叫",os.getpid())
print("a3",a)

t.join()

print("主函数",a)
print("主线程,分支线程共用")