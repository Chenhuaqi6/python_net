from threading import Thread
from time import sleep,ctime

class Mythread(Thread):
    def __init__(self,target,args=(),kwargs={},name="Thread-1"):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.name = name
    
    def run(self):
        self.target(*self.args,**self.kwargs)
         

#测试函数
def player(sec,song):
    for i in range(2):
        print("playing %s:%s"%(song,ctime()))
        sleep(sec)

t = Mythread(target = player,args=(3,),kwargs={"song":"年少有为"},name = "Tedu")
t.start()

t.join()