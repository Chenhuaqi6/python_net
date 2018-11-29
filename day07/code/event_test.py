from threading import Event

#创建事件对象
e = Event()

e.set() #设置e的状态
e.clear() #清除e的状态
print(e.is_set()) #打印e的状态
e.wait()


print("************************")